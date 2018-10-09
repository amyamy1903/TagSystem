# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging

"""
更新一个租户下的商品标签
post:/api/tenant/:tenantId/platformType/:platformType/goods/tagId/:tagId/updateTag
"""
logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "tagid": "1",
    "body_data": {
        "tagName": "商品标签1",
        "tagType": "String",
        "tag_default_value": "",
        "bak": "备注信息",
        "state":0,
        "tagGroup": "test_topic_group",
        "create_at": 1537182310166,
        "updater":"clive"
    },
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "tagid": "2",
    "body_data": {
        "tagName": "商品标签2",
        "tagType": "Int",
        "tag_default_value": "",
        "bak": "备注信息",
        "state":0,
        "tagGroup": "test_topic_group",
        "create_at": 1537182310166,
        "updater":"clive"
    },
    "code": "400"}
)
class UpdateProductTagInTenant(unittest.TestCase):
    def setParameters(self, tenant, platformtype, tagid, body_data,code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.tagid = tagid
        self.body_data = body_data
        self.code = code

    def testUpdateProductTagInTenant(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/tenant/:tenantId/platformType/:platformType/goods/tagId/:tagId/updateTag
        url = host + '/api/tenant/' + self.tenant + '/platformType/' + self.platformtype + '/goods/tagId/' + self.tagid + '/updateTag'
        data = self.body_data
        try:
            self.response = requests.post(url, headers=headers, data=json.dumps(data))
        except Exception:
            logging.error("请求出现异常,status={status},message={message} ".format(status=self.response.status_code,message= self.response.text))

        try:
            self.checkResult()
        except AssertionError:
            logging.error(
                "测试数据是,tenant={tenant},platform_type={platform_type},tag_id={tag_id},body_data={body_data},code={code}".format
                (tenant=self.tenant, platform_type=self.platformtype, tag_id=self.tagid, body_data=self.body_data,
                 code=self.code))
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