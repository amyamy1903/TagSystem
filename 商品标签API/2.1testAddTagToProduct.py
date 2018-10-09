# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging
"""
给商品增加标签
post:/api/entity/tenant/:tenantId/platformType/:platformType/goods/:goodsId/addGoodsTag
"""

logging.basicConfig(level=logging.INFO)

@paramunittest.parametrized(
{
    "tenant": "qiushi6",
    "platformtype": "top",
    "goodid": "10211021",
    "body_data": {
        "tagId": "1",
        "tagValue": "商品_tagid1_value"
    },
    "code": "200"},
{
    "tenant": "qiushi6",
    "platformtype": "jd",
    "goodid": "10221022",
    "body_data": {
        "tagId": "2",
        "tagValue": "商品_tag2_value"
    },
    "code": "400"}
)
class AddTagToProduct(unittest.TestCase):
    def setParameters(self, tenant, platformtype, goodid, body_data,code):
        self.tenant = tenant
        self.platformtype = platformtype
        self.goodid = goodid
        self.body_data = body_data
        self.code = code

    def testAddTagToProduct(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/entity/tenant/:tenantId/platformType/:platformType/goods/:goodsId/addGoodsTag
        url = host + '/api/entity/tenant/' + self.tenant + '/platformType/' + self.platformtype + '/goods/' + self.goodid + '/addGoodsTag'
        data = self.body_data
        try:
            self.response = requests.post(url, headers=headers, data=json.dumps(data))
        except Exception:
            logging.error("请求出现异常,status={status},message={message} ".format(status=self.response.status_code,message= self.response.text))

        try:
            self.checkResult()
        except AssertionError:
            logging.error(
                "测试数据是,tenant={tenant},platform_type={platform_type},good_id={good_id},body_data={body_data},code={code}".format
                (tenant=self.tenant, platform_type=self.platformtype, good_id=self.goodid, body_data=self.body_data,
                 code=self.code))
            logging.error("结果对比不一致,status={status},message={message}"
                          .format(status=self.response.status_code, message=self.response.text.encode('utf-8')))
            raise

    def checkResult(self):
        self.return_code = self.response.status_code
        self.return_msg = self.response.text.encode('utf-8')
        logging.info("return_code={return_code},return_msg={return_msg}".format(return_code=self.return_code,
                                                                                return_msg=self.return_msg))
        self.assertEqual(str(self.return_code), self.code)


if __name__ == "__main__":
    unittest.main()