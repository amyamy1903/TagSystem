# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging

"""
创建一个租户下的客户标签
/api/tenant/:tenantId/platformType/:platformType/customer/tagId/:tagId/createTag
"""
logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "tagid": "1",
    "body_data": {
        "tagName": "amytest1",
        "tagType": "String",
        "tag_default_value": "",
        "bak": "备注信息",
        "tagGroup": "test_topic_group",
        "creator": "yh"
    },
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "tagid": "2",
    "body_data": {
        "tagName": "amytest2",
        "tagType": "Int",
        "tag_default_value": "",
        "bak": "备注信息",
        "tagGroup": "test_topic_group",
        "creator": "yh"
    },
    "code": "200"}
)
class CreateCustomerTag(unittest.TestCase):
    def setParameters(self, tenant, platformtype, tagid, body_data,code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.tagid = tagid
        self.body_data = body_data
        self.code = code

    def testCreateCustomerTag(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        url = host + '/api/tenant/' + self.tenant + '/platformType/' + self.platformtype + '/customer/tagId/' + self.tagid + '/createTag'
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
        #self.assertEqual(self.return_msg, self.text)
        # message = {"tagId": "2", "tagEntityType": "customerTag", "tenantId": "qiushi6", "tagName": "test",
        #            "tagType": "String", "tag_default_value": "", "bak": "", "state": 1, "tagGroup": "test_topic_group2",
        #            "updater": "clive", "updated_at": 1538114715185}


if __name__ == "__main__":
    unittest.main(verbosity=2)