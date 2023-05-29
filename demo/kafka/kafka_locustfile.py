from locust import task, User, TaskSet

from demo import KafkaClient

class KafkaLocustUser(User):
    abstract = True

    def __init__(self, *args, **kwargs):
        super(KafkaLocustUser, self).__init__(*args, **kwargs)
        if not KafkaLocustUser.client:
            KafkaLocustUser.client = KafkaClient(KAFKA_BROKERS)

# KAFKA_BROKERS = ['xxx.xxx.xxx.xxx:xxxx', 'xxx.xxx.xxx.xxx:xxxx', 'xxx.xxx.xxx.xxx:xxxx']  # sit
KAFKA_BROKERS = ['xxx.xxx.xxx.xxx:xxxx', 'xxx.xxx.xxx.xxx:xxxx', 'xxx.xxx.xxx.xxx:xxxx']  # prod

class KafkaBehavior(TaskSet):
    # @task(100)
    def task1(self):
        self.client.send("test-topic",
                         message="{'phone_number': '13718415257','plate_number': '藏Q6QD177'}")

   # @task(500)
    def task2(self):
        self.client.send("test-car-in", message="{'entranceTime': '1000','parkName': 'parkName','exitRoad': '0','onServerTime':'1',"
                                                "'entranceParkBoxId': 'box_id','exitCarPlateColor': '0','exitCarPlateColor': '0',"
                                                "'plateNumber': '藏Q6QD177','type': '1','exitParkBoxId': '0','parkId': 'park_id',"
                                                "'synId': 'syn_id','exitCarImageBelieve': '0','entranceCarImage': 'img',"
                                                "'parkingSecondRecord': '1','entranceCarImageBelieve': '100','exitTime': '-25200000',"
                                                "'entranceCarPlateColor': '1','entranceAreaId': 'area_id','entranceRoad': 'road_id'}")

    @task(400)
    def task3(self):
        self.client.send("test-car-out", message="'couponFee': '0','centerFee': '0','exitRoadName': 'road_out','receivableFee': 'receivable_fee',"
                                                 "'parkName': 'park_name','businessId': '0','entranceParkBoxId': 'box_id_in',"
                                                 "'integralsFee': '0','cpmFee': '0','onlineFee': '0','type': 'park_type',"
                                                 "'couponId': '0','useType': '0','exitParkBoxId': 'box_id_out','parkId': 'park_id',"
                                                 "'synId': 'syn_id','parkingSecondRecord': '1','entranceCarImageBelieve': '99',"
                                                 "'entranceCarPlateColor': 'plate_color_in','cartypeName': '小汽车','loseMoney': '0',"
                                                 "'cardFee': '0','cartypeId': '4556','adminId': '6128','buscardFee': '0','state': '0',"
                                                 "'actualFee': 'actual_fee','isFixed': 'park_type','useCouponParkingBoxid': '0',"
                                                 "'entranceTime': '1000','exitRoad': 'road_id_out','entranceRoadName': 'road_in',"
                                                 "'exitParkingBoxName': 'box_out','onServerTime': '1000','exitCarPlateColor': 'plate_color_out',"
                                                 "'plateNumber': 'plate_number','exitCarImageBelieve': '0','entranceCarImage': 'img_in',"
                                                 "'realName': '白老头','exitTime': '1000','exitCarImage': 'img_out','entranceAreaId': 'area_id_in',"
                                                 "'entranceRoad': 'road_id_in'")


class KafkaUser(KafkaLocustUser):
    min_wait = 1
    max_wait = 1000
    tasks = [KafkaBehavior]