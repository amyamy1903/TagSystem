# !/usr/bin/python
# coding=utf-8


from locust import HttpLocust, TaskSet, task
import json
import Queue
from enum import Enum


class PlatformType(Enum):
    top = "top"
    jd = "jd"
    dd = "dd"
    full_platform = "full_platform"


class TagType(Enum):
    Type_String = "String"
    Type_Int = "Int"
    Type_Double = "Double"
    Type_LocalDate = "LocalDate"
    Type_DateTime = "DateTime"
    Type_Boolean = "Boolean"


class State(Enum):
    Enable = "0"
    Disable = "1"


class TestCustomerTag(TaskSet):

    def get_headers(self):
        base_headers = {
            'Content-Type': 'application/json'
        }
        return base_headers

    def get_body(self):
        data = self.locust.queueData.get()
        tmp_tag_id = str(data)
        return tmp_tag_id

    def get_url_data(self):
        tenant_id = "sjyj"
        platform_type = PlatformType.top
        creator = "yh"
        return tenant_id, platform_type, creator

    @task(1)
    def test_create_customer_tag(self):
        print "###test_create_customer_tag start:###"
        """/api/tenant/:tenantId/platformType/:platformType/customer/tagId/:tagId/createTag"""
        headers = self.get_headers()
        tag_id = self.get_body()
        url_data = self.get_url_data()
        tag_type = TagType.Type_String

        base_data = {"tagName" : "test" + tag_id,
                     "tagType":tag_type,
                     "tag_default_value":"",
                     "bak":"备注信息",
                     "tagGroup":"test_topic_group" + tag_id,
                     "creator":url_data[2]
                     }
        url = '/api/tenant/' + url_data[0] +'/platformType/' + url_data[1] + '/customer/tagId/' + tag_id + '/createTag'
        r = self.client.post(url, data=json.dumps(base_data), headers=headers)
        code = r.status_code
        #{"name":"BadRequest","detail":"TagEntity has already existed!"}
        #"tagEntityId":"customerTag-1000","tagEntityType":"customerTag","tenantId":"sjyj","tagName":"test1000","tagType":"String","create_at":1538032039923}
        msg = json.loads(r.text)
        if code != 200:
            print "test_create_customer_tag error msg:", code, r.text
            exit(0)

    # @task(1)
    # def test_update_customer_tag(self):
    #     print "###test_update_customer_tag start###"
    #     headers = self.get_headers()
    #     tag_id = self.get_body()
    #     url_data = self.get_url_data()
    #     base_data = {"tagName": "test" + tag_id,
    #                  "tagType": TagType.Type_String.value,
    #                  "tag_default_value": "",
    #                  "bak": "备注信息",
    #                  "state":State.Enable.value,
    #                  "tagGroup": "test_topic_group" + tag_id,
    #                  "create_at":
    #                  "updater": url_data[2]
    #                  }
    #     url = '/api/tenant/' + url_data[0] + '/platformType/' + url_data[1] + '/customer/tagId/' + tag_id + '/createTag'
    #     r = self.client.post(url, data=json.dumps(base_data), headers=headers)
    #     msg = json.loads(r.text)
    #     code = msg['code']
    #     if code != 10000:
    #         print "test_create_customer_tag error msg:", code, r.text
    #         exit(0)



class websiteUser(HttpLocust):
    host = "http://10.27.102.151:9000"
    task_set = TestCustomerTag
    queueData = Queue.Queue()
    for i in range(1, 2):
        queueData.put(i)
    # min_wait = 3000
    # max_wait = 6000


