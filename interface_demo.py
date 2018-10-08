# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging


logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "tagid": "1",
    "body_data": {
        "tagName": "test",
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
        "tagName": "test",
        "tagType": "Int",
        "tag_default_value": "",
        "bak": "备注信息",
        "tagGroup": "test_topic_group",
        "creator": "yh"
    },
    "code": "200"}
)
class TestCustomerTag(unittest.TestCase):
    def setParameters(self, tenant, platformtype, tagid, body_data,code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.tagid = tagid
        self.body_data = body_data
        self.code = code

    def testCustomerTag(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        # print("输入tenant：%s" % self.tenant)
        # print("输入platformtype：%s" % self.platformtype)
        # print("输入tagid:%s" % self.tagid)
        # print("期望结果：%s " % self.code)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        url = host + '/api/tenant/' + self.tenant + '/platformType/' + self.platformtype+ '/customer/tagId/' + self.tagid + '/createTag'
        print "url is:", url
        print "body_data is:", self.body_data
        # data = {"tagName" : "test" + self.tagid,
        #         "tagType":"String",
        #         "tag_default_value":"",
        #         "bak":"备注信息",
        #         "tagGroup":"test_topic_group" + self.tagid,
        #         "creator":"yh"
        #         }
        data = self.body_data
        try:
            self.response = requests.post(url, headers=headers, data=json.dumps(data))
            #logging.info("结果:status={status},message={message} ".format(status=self.response.status_code,message= self.response.text))
        except Exception:
            logging.error("结果失败,status={status},message={message} ".format(status=self.response.status_code,message= self.response.text))

        self.checkResult()

    def checkResult(self):
        self.return_code = self.response.status_code
        self.return_msg = self.response.text
        self.assertEqual(self.return_code, self.code)
        #self.assertEqual(self.return_msg, self.msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)