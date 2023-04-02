import random
import time

import pymysql
# from exercises.Locust_demo.locust_tidb import TidbTaskSet

db = pymysql.connect(
    host='XXXX', port=5000, user='XXXX', password='XXXX', db='XXXX')
cursor = db.cursor()
sql = "SELECT c.`platenumber` FROM caroutpayment c LEFT JOIN parking_record p ON c.`platenumber` = p.`plate_number` WHERE c.`parkingid` = 6089 AND p.`area_id` AND p.`state` = 0 AND p.`status` < 3 GROUP BY c.`platenumber`;"                  # % (random.choice(TidbTaskSet.sql_parkingid), random.choice(TidbTaskSet.sql_state))
ret = time.time()
cursor.execute(sql)
tet = time.time()
print(tet-ret)

data = cursor.fetchall()
cet = time.time()
print(cet-tet)

print(data)
db.close()
