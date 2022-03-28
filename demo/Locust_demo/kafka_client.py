# https://github.com/TonyWu1995/kafka-locust

import time

from kafka import KafkaProducer
from locust import events


class KafkaClient:
    def __init__(self, kafka_brokers=None):
        print("creating message sender with params: " + str(locals()))
        if kafka_brokers is None:
            # kafka_brokers = ['10.110.50.96:9092', '10.110.50.104:9092', '10.110.50.119:9092']  # sit
            kafka_brokers = ['10.103.20.101:9092', '10.103.20.102:9092', '10.103.20.103:9092']  # prod
        self.producer = KafkaProducer(bootstrap_servers=kafka_brokers)

    def __handle_success(self, *arguments, **kwargs):
        end_time = time.time()
        elapsed_time = int((end_time - kwargs["start_time"]) * 1000)
        try:
            record_metadata = kwargs["future"].get(timeout=1)
            request_data = dict(request_type="ENQUEUE",
                                name=record_metadata.topic,
                                response_time=elapsed_time,
                                response_length=record_metadata.serialized_value_size)

            self.__fire_success(**request_data)
        except Exception as ex:
            print("Logging the exception: {0}".format(ex))
            raise

    def __handle_failure(self, *arguments, **kwargs):
        print("failure " + str(locals()))
        end_time = time.time()
        elapsed_time = int((end_time - kwargs["start_time"]) * 1000)

        request_data = dict(request_type="ENQUEUE", name=kwargs["topic"], response_time=elapsed_time,
                            exception=arguments[0])
        self.__fire_failure(**request_data)

    def __fire_failure(self, **kwargs):
        events.request_failure.fire(**kwargs)

    def __fire_success(self, **kwargs):
        events.request_success.fire(**kwargs)

    def send(self, topic, key=None, message=None):
        start_time = time.time()
        future = self.producer.send(topic, key=key.encode() if key else None,
                                    value=message.encode() if message else None)
        future.add_callback(self.__handle_success, start_time=start_time, future=future)
        future.add_errback(self.__handle_failure, start_time=start_time, topic=topic)

    def finalize(self):
        print("flushing the messages")
        self.producer.flush(timeout=5)
        print("flushing finished")
