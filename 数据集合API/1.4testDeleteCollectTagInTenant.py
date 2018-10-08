# !/usr/bin/python
# coding=utf-8

import requests
import unittest
import paramunittest
import time
import json
import logging

"""
删除一个租户下的数据集标签
get:/api/tenant/:tenantId/platformType/:platformType/collectType/:collectType/tagId/:tagId/removeTag
"""
logging.basicConfig(level=logging.INFO)


@paramunittest.parametrized(
{
    "tenantId": "qiushi6",
    "platformType": "top",
    "collectType":"customerRedList",
    "tagid": "1",
    "code": "200"},

)
class DeleteCollectTagInTenant(unittest.TestCase):
    def setParameters(self, tenant_id, platform_type, collect_type, tag_id, code):
        self.tenant_id = tenant_id
        self.platform_type = platform_type
        self.collect_type = collect_type
        self.tag_id = tag_id
        self.code = code

    def testDeleteCollectTagInTenant(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        headers = {
            'Content-Type': 'application/json'
        }
        host = "http://10.27.102.151:9000"
        #/api/tenant/:tenantId/platformType/:platformType/collectType/:collectType/tagId/:tagId/removeTag
        url = host + '/api/tenant/' + self.tenant_id + '/platformType/' + self.platform_type + 'collectType' \
              + self.collect_type + '/tagId/' + self.tag_id + '/removeTag'
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