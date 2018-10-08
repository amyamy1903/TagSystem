# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging
"""
修改客户的标签值
post:/api/entity/tenant/:tenantId/platformType/:platformType/customers/:customerId/addCustomerTagVal
"""

logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "customerid": "zhangsan",
    "body_data": {
        "tagId": "1",
        "tagValue": "zhangsan_1_value_modify"
    },
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "customerid": "lisi",
    "body_data": {
        "tagId": "1",
        "tagValue": "lisi_1_value_modify"
    },
    "code": "200"}
)
class ModifyTagToCustomer(unittest.TestCase):
    def setParameters(self, tenant, platformtype, customerid, body_data,code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.customerid = customerid
        self.body_data = body_data
        self.code = code

    def testModifyTagToCustomer(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/entity/tenant/:tenantId/platformType/:platformType/customers/:customerId/updateCustomerTagVal
        url = host + '/api/entity/tenant/' + self.tenant + '/platformType/' + self.platformtype + '/customers/' + self.customerid + '/updateCustomerTagVal'
        data = self.body_data
        try:
            self.response = requests.post(url, headers=headers, data=json.dumps(data))
        except Exception:
            logging.error("请求出现异常,status={status},message={message} ".format(status=self.response.status_code,message= self.response.text))

        try:
            self.checkResult()
        except AssertionError:
            logging.error("结果对比不一致,status={status},message={message}"
                          .format(status=self.response.status_code, message=self.response.text))
            raise

    def checkResult(self):
        self.return_code = self.response.status_code
        self.return_msg = self.response.text
        self.return_msg = self.response.text
        logging.info("return_code={return_code},return_msg={return_msg}".format(return_code=self.return_code,
                                                                                return_msg=self.return_msg))
        self.assertEqual(str(self.return_code), self.code)


if __name__ == "__main__":
    unittest.main(verbosity=2)