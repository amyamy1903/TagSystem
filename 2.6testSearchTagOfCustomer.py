# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging
"""
查询某一客户具有的标签
get:/api/entity/tenant/:tenantId/platformType/:platformType/customers/:customerId
"""

logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformType": "top",
    "customerId":"zhangsan",
    "code": "200"
},
{
    "tenant": "sjyj",
    "platformType": "jd",
    "customerId":"lisi",
    "code": "200"
}
)
class SearchTagOfCustomer(unittest.TestCase):
    def setParameters(self, tenant, platformType, customerId, code):
        self.tenant = tenant
        self.platformType = platformType
        self.customerId = customerId
        self.code = code

    def testSearchTagOfCustomer(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/entity/tenant/:tenantId/platformType/:platformType/customers/:customerId
        url = host + '/api/entity/tenant/' + self.tenant + '/platformType/' + self.platformType + '/customers/' + self.customerId
        try:
            self.response = requests.get(url, headers=headers)
        except Exception:
            logging.error("请求出现异常,status={status},message={message} ".format(status=self.response.status_code,message= self.response.text))

        try:
            self.checkResult()
        except AssertionError:
            logging.error("测试数据是,tenant={tenant},platform_type={platform_type},customer_id={customer_id},code={code}".format
                (tenant=self.tenant, platform_type=self.platformType, customer_id=self.customerId, code=self.code))
            logging.error("结果对比不一致,status={status},message={message}"
                          .format(status=self.response.status_code, message=self.response.text))
            raise

    def checkResult(self):
        self.return_code = self.response.status_code
        self.return_msg = self.response.text
        logging.info("return_code={return_code},return_msg={return_msg}".format(return_code=self.return_code,
                                                                                return_msg=self.return_msg))
        self.assertEqual(str(self.return_code), self.code)
        #self.assertEqual(self.return_msg, self.text)


if __name__ == "__main__":
    unittest.main()