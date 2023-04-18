# 接口测试demo
import logging
import requests

logging.basicConfig(filename='api_test.log', level=logging.INFO,
                    format='%(asctime)s - %(levename)s - %(message)s')

def sendGETrequest():
    """
    根据名称模糊查询公司列表
    :return:
    """
    response = requests.get('http://base-service-client.intra.sit.etcp.net/base/company/v1/getCompanyList?name=北京')
    logging.info(f'Send GET request to http://base-service-client.intra.sit.etcp.net/base/company/v1/getCompanyList?name=北京, response status code: {response.status_code}')
    assert response.status_code == 200  # 断言检查响应状态码
    assert len(response.json()) > 0  # 检查响应长度是否大于0

def editGoods():
    """
    修改商品位置post请求
    :return:
    """
    data = {
      "activityId": 0,
      "goodsId": 0,
      "locationId": 0,
      "locationName": "string"
    }
    response = requests.post('http://goods.c.sit.etcp.net:80/activity/v1/goods/update', json=data)
    logging.info(f'Send POST request to http://goods.c.sit.etcp.net:80/activity/v1/goods/update, response status code: {response.status_code}')
    assert response.status_code == 200  # 断言检查响应状态码

def main():
    sendGETrequest()
    editGoods()

if __name__ == '__main__':
    main()