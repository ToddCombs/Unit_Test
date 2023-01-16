# Monograph-DB压测
from __future__ import absolute_import
from __future__ import print_function

import random
import time

from locust import User, between, TaskSet, task, events, constant
from sqlalchemy import create_engine, exc


def create_conn(conn_string):
    return create_engine("mysql+pymysql://" + conn_string).connect()


def engine(conn_string):
    return create_engine("mysql+pymysql://" + conn_string, pool_size=200, max_overflow=0)


def execute_query_(conn_string, query):
    _conn = create_conn(conn_string)
    rs = _conn.execute(query)
    return rs


def execute_query(conn_string, query):
    with engine(conn_string).begin() as conn:
        rs = conn.execute(query)
        return rs


class MySqlClient:
    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                res = execute_query(*args, **kwargs)
                events.request_success.fire(
                    request_type="MDB",
                    name=name,
                    response_time=int((time.time() - start_time) * 1000),
                    response_length=res.rowcount)
            except (Exception, exc.OperationalError) as e:
                events.request_failure.fire(
                    request_type="MDB",
                    name=name,
                    response_time=int((time.time() - start_time) * 1000),
                    exception=e)

        return wrapper


class CustomTaskSet(TaskSet):
    conn_string = "XX:XX@XXX.XXX.XXX.XXX:XXXX/XXXX"  # qa
    sql_plateNumber = ["XX", "XX"]

    sql_synid = ["XX", "XX"]

    sql_parkingid = ["XXX", "XX"]

    sql_state = ["XXX"]

    @task(50)
    def execute_query1(self):
        """普通索引查询"""
        self.client.execute_query1(
            self.conn_string,
            "SELECT id, plate_number, entrance_time, exit_time, receivable_fee FROM parking_record WHERE " \
            "plate_number = '%s';" % str(random.choice(CustomTaskSet.sql_plateNumber)))

    @task(1)
    def execute_query2(self):
        """普通索引查询"""
        self.client.execute_query2(
            self.conn_string,
            "SELECT COUNT(1) FROM parking_record WHERE plate_number = '%s';" % str(random.choice(CustomTaskSet.sql_plateNumber)))

    @task(50)
    def execute_query3(self):
        """普通索引查询降序100条"""
        self.client.execute_query3(
            self.conn_string,
            "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, update_time FROM parking_record " \
            "WHERE plate_number = '%s' ORDER BY entrance_time DESC LIMIT 100;" % str(random.choice(CustomTaskSet.sql_plateNumber)))

    @task(50)
    def execute_query4(self):
        """普通索引多条件查询"""
        self.client.execute_query4(
            self.conn_string,
            "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, update_time, is_finish FROM " \
            "parking_record WHERE entrance_time = '2021-01-01' AND is_finish = 1 AND plate_number = '%s';" \
            % str(random.choice(CustomTaskSet.sql_plateNumber)))

    @task(50)
    def execute_query5(self):
        """普通索引多条件查询"""
        self.client.execute_query5(
            self.conn_string,
            "SELECT is_finish, SUM(receivable_fee) AS receivable_fee FROM parking_record WHERE synid = '%s'" \
            " AND `status` = 1;" % str(random.choice(CustomTaskSet.sql_synid)))

    @task(50)
    def execute_query6(self):
        """唯一索引查询"""
        self.client.execute_query6(
            self.conn_string,
            "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, actual_fee, online_fee, " \
            "update_time, is_finish, `status` FROM parking_record WHERE synid = '%s';" \
            % str(random.choice(CustomTaskSet.sql_synid)))

    @task(1)
    def execute_query7(self):
        """唯一索引多条件查询"""
        self.client.execute_query7(
            self.conn_string,
            "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, actual_fee, online_fee, " \
            "update_time, is_finish, `status` FROM parking_record WHERE synid = '%s' AND is_finish = 0 AND " \
            "entrance_time > '2020-01-01';" % str(random.choice(CustomTaskSet.sql_synid)))

    @task(1)
    def execute_query8(self):
        """唯一索引查询"""
        self.client.execute_query8(
            self.conn_string,
            "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, actual_fee, online_fee, " \
            "update_time, is_finish, `status` FROM parking_record WHERE plate_number = '%s' AND synid = '%s';" \
            % (str(random.choice(CustomTaskSet.sql_plateNumber)), str(random.choice(CustomTaskSet.sql_synid))))

    @task(1)
    def execute_query9(self):
        """普通索引查询"""
        self.client.execute_query9(
            self.conn_string,
            "SELECT SUM(receivable_fee) AS total_receivable_fee, SUM(actual_fee) AS total_actual_fee, " \
            "SUM(online_fee) AS total_online_fee FROM parking_record WHERE plate_number = '%s' AND `status` = 1;" \
            % str(random.choice(CustomTaskSet.sql_plateNumber)))

    @task(1)
    def execute_query10(self):
        """普通索引查询"""
        self.client.execute_query10(
            self.conn_string,
            "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, actual_fee, online_fee, " \
            "update_time, is_finish, `status` FROM parking_record WHERE plate_number = '%s' AND " \
            "entrance_car_plate_color = 1 AND entrance_time > '2019-01-01';" \
            % str(random.choice(CustomTaskSet.sql_plateNumber)))

    @task(1)
    def execute_query11(self):
        """唯一索引联表查询"""
        self.client.execute_query11(
            self.conn_string,
            "SELECT parkingid, platenumber, exitparkingboxid, entrancetime, exittime, updatetime, receivablefee, " \
            "actualfee, onlinefee, pam2 FROM carout_payment c LEFT JOIN parking_record p ON c.`synid` = p.`synid` " \
            "WHERE updatetime > '2021-01-01' AND receivablefee = 0.00 AND actualfee = 0.00 AND c.`synid` = '%s';" \
            % str(random.choice(CustomTaskSet.sql_synid)))

    @task(10)
    def execute_query12(self):
        """普通索引内联查询"""
        self.client.execute_query12(
            self.conn_string,
            "SELECT row_number() over (ORDER BY plate_number DESC) row_num, parkingid, platenumber, " \
            "exitparkingboxid, entrancetime, exittime, updatetime, receivablefee, actualfee, onlinefee, pam2 " \
            "FROM carout_payment c INNER JOIN parking_record p ON c.`platenumber` = p.`plate_number` WHERE " \
            "entrancetime > '2019-01-01' AND receivablefee != 0.00 AND actualfee = 0.01 AND c.`platenumber` " \
            "= '%s';" % str(random.choice(CustomTaskSet.sql_plateNumber)))

    @task(50)
    def execute_query13(self):
        """唯一索引联表查询"""
        self.client.execute_query13(
            self.conn_string,
            "SELECT parkingid, platenumber, entrancetime, exittime, updatetime, receivablefee, actualfee, " \
            "onlinefee, couponfee, centerfee, cardfee, buscardfee, pam2, entranceroadname, exitroadname, realname," \
            " cartypename, exitparkingboxname FROM carout_payment c LEFT JOIN parking_record p ON c.`synid` " \
            "= p.synid WHERE entrancetime > '2019-01-01' AND receivablefee != 0.00 AND actualfee = 0.01 " \
            "AND c.`synid` = '%s';" % str(random.choice(CustomTaskSet.sql_synid)))

    @task(1)
    def execute_query14(self):
        """分页普通索引联表查询"""
        self.client.execute_query14(
            self.conn_string,
            "SELECT row_number() over (ORDER BY plate_number DESC) row_num, platenumber FROM carout_payment c " \
            "LEFT JOIN parking_record p ON c.`platenumber` = p.`plate_number` WHERE entrancetime > '2019-01-01' " \
            "AND receivablefee != 0.00 AND actualfee = 0.01 AND c.platenumber = '%s';" % str(
            random.choice(CustomTaskSet.sql_plateNumber)))

    @task(1)
    def execute_query15(self):
        """查询parking_id普通索引联表查询"""
        self.client.execute_query15(
            self.conn_string,
            "SELECT c.`platenumber` FROM carout_payment c LEFT JOIN parking_record p ON c.`platenumber` = p.`plate_number` " \
            "WHERE c.`parkingid` = %s AND p.`area_id` AND p.`state` = 0 AND p.`status` < 3 AND p.entrance_time = '2022-08-04' GROUP BY c.`platenumber`;" \
            % (random.choice(CustomTaskSet.sql_parkingid)))

    @task(1)
    def execute_query16(self):
        """select 查询in parking_id / plate_number order by entrance_time"""
        self.client.execute_query16(
            self.conn_string,
            "SELECT parking_id, plate_number FROM parking_record ORDER BY entrance_time LIMIT 0, 10;")

    def on_stop(self):
        print("------ Test over ------")


class MySqlLocust(User):
    min_wait = 0
    max_wait = 0
    tasks = [CustomTaskSet]
    wait_time = constant(0.5)
    # wait_time = between(min_wait, max_wait)

    def __init__(self, env):
        super().__init__(env)
        self.client = MySqlClient()