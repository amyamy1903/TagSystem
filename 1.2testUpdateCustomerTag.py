# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging

"""
更新一个租户下的客户标签
/api/tenant/:tenantId/platformType/:platformType/customer/tagId/:tagId/updateTag
"""
logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "tagid": "1",
    "body_data":{
        "tagName" : "test",
        "tagType":"String",
        "tag_default_value":"",
        "bak":"",
        "state":1,
        "tagGroup":"test_topic_group2",
        "create_at":1537182310166,
        "updater":"clive"
    },
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "tagid": "2",
    "body_data":{
        "tagName" : "test",
        "tagType":"String",
        "tag_default_value":"",
        "bak":"",
        "state":1,
        "tagGroup":"test_topic_group2",
        "create_at":1537182310166,
        "updater":"clive"
    },
    "code": "200"}
)
class UpdateCustomerTag(unittest.TestCase):
    def setParameters(self, tenant, platformtype, tagid, body_data,code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.tagid = tagid
        self.body_data = body_data
        self.code = code

    def testUpdateCustomerTag(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        url = host + '/api/tenant/' + self.tenant + '/platformType/' + self.platformtype + '/customer/tagId/' + self.tagid + '/updateTag'
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
    unittest.main(verbosity=2)