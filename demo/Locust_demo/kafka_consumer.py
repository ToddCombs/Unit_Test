from kafka import KafkaConsumer
from kafka.structs import TopicPartition
# 创建一个消费者，指定topic, groupid，bootstrap_servers
# groupid 多个拥有想通groupid的消费者被判定为一组，一条数据记录只会被同一个族中的一个消费者消费。
# bootstrap_servers:kafka的节点，多个节点使用逗号分隔。
# 这种方式只会获取新产生的数据

# consumer = KafkaConsumer('test-topic')
consumer = KafkaConsumer(bootstrap_servers=['xxx.xxx.xxx.xxx:xxxx', 'xxx.xxx.xxx.xxx:xxxx', 'xxx.xxx.xxx.xxx:xxxx']) # kafka集群地址
consumer.subscribe(topics=['test-topic', 'test-car-in', 'test-car-out'])  # 订阅要消费的主题
print(consumer.topics())
print(consumer.position(TopicPartition(topic=u'test-car-in', partition=0)))  # 获取当前主题的最新偏移量
for msg in consumer:
    print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))
