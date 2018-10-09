# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging
"""
根据条件查询一个租户下的客户标签
post:/api/tag/tenant/:tenantId/tagEntityType/customerTag/platformType/:platformType/tags?page&pageSize
"""

logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "tagid": "1",
    "body_data":{
        "must": [{
            "type": "TagQuery",
            "name": "name",
            "operator": "like",
            "value": "amyTag1"
        }],
        "not": [],
        "should": []
    },
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "tagid": "2",
    "body_data":{
        "must": [{
            "type": "TagQuery",
            "name": "name",
            "operator": "like",
            "value": "amyTag2"
        }],
        "not": [],
        "should": []
    },
    "code": "200"}
)
class SearchCustomerTag(unittest.TestCase):
    def setParameters(self, tenant, platformtype, tagid, body_data,code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.tagid = tagid
        self.body_data = body_data
        self.code = code

    def testSearchCustomerTag(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/ api / tag / tenant /:tenantId / tagEntityType / customerTag / platformType /:platformType / tags?page & pageSize
        #http://qiushi6-ccms.shuyun.com/datamanage/producttag/page/?page=1&pagesize=20&sortname=id&sortorder=desc&query=&qtype=&_=1538132551698
        url = host + '/api/tag/tenant/' + self.tenant + '/tagEntityType/customerTag/platformType/' + self.platformtype + '/tags?page=1&pageSize=20'
        data = self.body_data
        try:
            self.response = requests.post(url, headers=headers, data=json.dumps(data))
        except Exception:
            logging.error("请求出现异常,status={status},message={message} ".format(status=self.response.status_code,message= self.response.text))

        try:
            self.checkResult()
        except AssertionError:
            logging.error("测试数据是,tenant={tenant},platform_type={platform_type},tag_id={tag_id},body_data={body_data},code={code}".format
                          (tenant=self.tenant, platform_type=self.platformtype, tag_id=self.tagid, body_data=self.body_data, code=self.code))
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