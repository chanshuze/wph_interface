#coding:utf-8
import requests
import unittest
class updateUserSubscribe(unittest.TestCase):
    #前置登录就是为了token
    def setUp(self):
        self.s=requests.session()
        loginheader = {
            "Authorization": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTU2MzUwNTI4MiwidHlwIjoiSldUIn0.eyJpZCI6MjY2ODQzNzUzNjAyMzUxNTM0LCJleHAiOjE1NjM1MDUyODJ9.WxIOz4-jyiYxyCtynZ1Cp04F-w41AMRDbTH8bdLR_b0",
            "Content-Type": "application/json; charset=UTF-8" }
        loginurl = 'http://api.88ba.com/user/login'
        loginbody = {"mobile": "15002020501",
                     "captcha": "1234"}

        self.loginr = self.s.post(loginurl, json=loginbody, headers=loginheader)

    #order/purchase/createOrUpdate
    def updateUserSubscribe (self,x):
        header = {"Authorization":self.loginr.json()["body"]["token"]}
        url = "http://api.88ba.com/order/subscribe/updateUserSubscribe"
        r =self.s.post(url, json=x, headers=header)
        return r.json()

    def test_01(self):
        u'''参数全对'''
        a={
            "areas": [110100, 120100],
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": 9,
                 "industryTypeId": 1,
                 "serviceTypeId": 2,
                 "attrValueId": 2,
                 "startValue": 0,
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_02(self):
        u'''没添加订阅地区areas'''
        a={
            "areas":'',
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": 9,
                 "industryTypeId": 1,
                 "serviceTypeId": 2,
                 "attrValueId": 2,
                 "startValue": 0,
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_03(self):
        u'''没添加计划plan'''
        a={
            "areas": [110100, 120100],
            "plan": "",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": 9,
                 "industryTypeId": 1,
                 "serviceTypeId": 2,
                 "attrValueId": 2,
                 "startValue": 0,
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_04(self):
        u'''没添加用户userid'''
        a={
            "areas": [110100, 120100],
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": '',
                 "orderType": 9,
                 "industryTypeId": 1,
                 "serviceTypeId": 2,
                 "attrValueId": 2,
                 "startValue": 0,
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_05(self):
        u'''没添加订单类型orderType'''
        a={
            "areas": [110100, 120100],
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": '',
                 "industryTypeId": 1,
                 "serviceTypeId": 2,
                 "attrValueId": 2,
                 "startValue": 0,
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_06(self):
        u'''没添加行业种类industryTypeId'''
        a={
            "areas": [110100, 120100],
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": 9,
                 "industryTypeId": '',
                 "serviceTypeId": 2,
                 "attrValueId": 2,
                 "startValue": 0,
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_07(self):
        u'''没有添加服务类型serviceTypeId'''
        a={
            "areas": [110100, 120100],
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": 9,
                 "industryTypeId": 1,
                 "serviceTypeId": '',
                 "attrValueId": 2,
                 "startValue": 0,
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_08(self):
        u'''没添加订阅推送时间段attrValueId'''
        a={
            "areas": [110100, 120100],
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": 9,
                 "industryTypeId": 1,
                 "serviceTypeId": 2,
                 "attrValueId": '',
                 "startValue": 0,
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_09(self):
        u'''没有添加起始值startValue'''
        a={
            "areas": [110100, 120100],
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": 9,
                 "industryTypeId": 1,
                 "serviceTypeId": 2,
                 "attrValueId": 2,
                 "startValue": '',
                 "endValue": 3}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")
    def test_10(self):
        u'''没有添加结束值endValue'''
        a={
            "areas": [110100, 120100],
            "plan": "333274184702492937",
            "subscribes":
            [
                {"userId": 333273904455877103,
                 "orderType": 9,
                 "industryTypeId": 1,
                 "serviceTypeId": 2,
                 "attrValueId": 2,
                 "startValue": 0,
                 "endValue": ''}
            ]
        }
        self.updateUserSubscribe(a)
        self.assertNotEqual(self.updateUserSubscribe(a)["msg"],"success")

    def tearDown(self):
        self.s.close()
