# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging
"""
查询租户下的客户标签
get:/api/entity/tenant/:tenantId/tagEntityType/customerTag/tags
"""

logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "code": "200"
},
{
    "tenant": "sjyj",
    "code": "200"
}
)
class SearchCustomerTagInTenant(unittest.TestCase):
    def setParameters(self, tenant, code):
        self.tenant = tenant
        self.code = code

    def testSearchCustomerTagInTenant(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/entity/tenant/:tenantId/tagEntityType/customerTag/tags
        url = host + '/api/entity/tenant/' + self.tenant + '/tagEntityType/CustomerTag/tags'
        try:
            self.response = requests.get(url, headers=headers)
        except Exception:
            logging.error("请求出现异常,status={status},message={message} ".format(status=self.response.status_code,message= self.response.text))

        try:
            self.checkResult()
        except AssertionError:
            logging.error("测试数据是,tenant={tenant},code={code}".format(tenant=self.tenant, code=self.code))
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