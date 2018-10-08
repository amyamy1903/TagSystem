# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging

"""
根据条件查询一个租户下的数据集标签
post:/api/tag/tenant/:tenantId/tagEntityType/:tagEntityType/platformType/:platformType/tags?page&pageSize
"""
logging.basicConfig(level=logging.INFO)

#可选值：customerRedList, customerBlackList, telBlackList, mailBlackList
@paramunittest.parametrized(
{
    "tenantId": "qiushi6",
    "platformType": "top",
    "tagEntityType":"customerRedList",
    "page":"1",
    "pageSize":"20",
    "body_data": {
        "must": [{
            "type": "TagQuery",
            "name": "name",
            "operator": "like",
            "value": "birthd"
        }],
        "not": [],
        "should": []
},
    "code": "200"},

)
class SearchCollectTagInTenant(unittest.TestCase):
    def setParameters(self, tenant_id, platform_type, tag_entity_type,page,page_size, body_data, code):
        self.tenant_id = tenant_id
        self.platform_type = platform_type
        self.tag_entity_type = tag_entity_type
        self.page = page
        self.page_size = page_size
        self.body_data = body_data
        self.code = code

    def testSearchCollectTagInTenant(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/tag/tenant/:tenantId/tagEntityType/:tagEntityType/platformType/:platformType/tags?page&pageSize
        url = host + '/api/tenant/' + self.tenant_id + '/tagEntityType/' + self.tagEntityType + '/platformType/'\
              + self.platform_type + '/tags?page=' + self.page + '&pageSize=' + self.page_size
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
    unittest.main()