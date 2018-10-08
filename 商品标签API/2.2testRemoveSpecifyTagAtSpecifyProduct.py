# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging
"""
移除指定商品下指定标签
post:/api/entity/tenant/:tenantId/platformType/:platformType/goods/:goodsId/tagId/:tagId/removeTag
"""

logging.basicConfig(level=logging.INFO)

@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "goodid": "10211021",
    "tagid": "1",
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "goodid": "10221022",
    "tagid": "1",
    "code": "200"}
)
class AddRemoveSpecifyTagAtSpecifyProduct(unittest.TestCase):
    def setParameters(self, tenant, platformtype, goodid, tagid,code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.goodid = goodid
        self.tagid = tagid
        self.code = code

    def testAddTagToProduct(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/entity/tenant/:tenantId/platformType/:platformType/goods/:goodsId/tagId/:tagId/removeTag
        url = host + '/api/entity/tenant/' + self.tenant + '/platformType/' + self.platformtype + '/goods/' + self.goodid + '/tagId/' + self.tagid + 'removeTag'
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
        logging.info("return_code={return_code},return_msg={return_msg}".format(return_code=self.return_code,
                                                                                return_msg=self.return_msg))
        self.assertEqual(str(self.return_code), self.code)


if __name__ == "__main__":
    unittest.main()