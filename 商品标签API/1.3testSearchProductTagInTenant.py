# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging
"""
根据条件查询一个租户下的商品标签
post:/api/tag/tenant/:tenantId/tagEntityType/goodsTag/platformType/:platformType/tags?page&pageSize
"""

logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "page": "1",
    "pageSize":"20",
    "body_data":{
        "must": [{
            "type": "TagQuery",
            "name": "name",
            "operator": "like",
            "value": "商品标签1"
        }],
        "not": [],
        "should": []
    },
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "page": "1",
    "pageSize":"20",
    "body_data":{
        "must": [{
            "type": "TagQuery",
            "name": "name",
            "operator": "like",
            "value": "商品标签2"
        }],
        "not": [],
        "should": []
    },
    "code": "200"}
)
class SearchProductTagInTenant(unittest.TestCase):
    def setParameters(self, tenant, platformtype, page, pageSize, body_data, code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.page = page
        self.pageSize = pageSize
        self.body_data = body_data
        self.code = code

    def testSearchProductTagInTenant(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/tag/tenant/:tenantId/tagEntityType/goodsTag/platformType/:platformType/tags?page&pageSize
        url = host + '/api/tag/tenant/' + self.tenant + '/tagEntityType/goodsTag/platformType/' + self.platformtype + '/tags?page=' + self.page + '&pageSize=' + self.pageSize
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
        logging.info("return_code={return_code},return_msg={return_msg}".format(return_code=self.return_code,
                                                                                return_msg=self.return_msg))
        self.assertEqual(str(self.return_code), self.code)
        #self.assertEqual(self.return_msg, self.text)


if __name__ == "__main__":
    unittest.main()