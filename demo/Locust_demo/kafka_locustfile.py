from locust import task, User, TaskSet

from demo.Locust_demo.kafka_client import KafkaClient

class KafkaLocustUser(User):
    abstract = True

    def __init__(self, *args, **kwargs):
        super(KafkaLocustUser, self).__init__(*args, **kwargs)
        if not KafkaLocustUser.client:
            KafkaLocustUser.client = KafkaClient(KAFKA_BROKERS)

KAFKA_BROKERS = ['10.110.50.96:9092']

class KafkaBehavior(TaskSet):
    @task(100)
    def task1(self):
        self.client.send("test-topic",
                         message="{'phone_number': '13718415257','plate_number': '藏Q6QD177'}")

class KafkaUser(KafkaLocustUser):
    min_wait = 1
    max_wait = 1000
    tasks = [KafkaBehavior]