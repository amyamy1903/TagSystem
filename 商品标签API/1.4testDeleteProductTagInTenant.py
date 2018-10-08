# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import logging

"""
删除一个租户下的商品标签
post:/api/tenant/:tenantId/platformType/:platformType/goods/tagId/:tagId/removeTag
"""
logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "tagid": "1",
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "tagid": "2",
    "code": "200"}
)
class DeleteProductTagInTenant(unittest.TestCase):
    def setParameters(self, tenant, platformtype, tagid, code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.tagid = tagid
        self.code = code

    def testDeleteProductTagInTenant(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/tenant/:tenantId/platformType/:platformType/goods/tagId/:tagId/removeTag
        url = host + '/api/tenant/' + self.tenant + '/platformType/' + self.platformtype + '/goods/tagId/' + self.tagid + '/removeTag'
        try:
            self.response = requests.get(url, headers=headers)
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
        logging.info("return_code={return_code},return_msg={return_msg}".format(return_code=self.return_code,return_msg=self.return_msg))
        self.assertEqual(str(self.return_code), self.code)


if __name__ == "__main__":
    unittest.main()