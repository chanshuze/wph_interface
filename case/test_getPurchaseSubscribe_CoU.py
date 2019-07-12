#coding:utf-8
import requests
import unittest
class getPurchaseSubscribe(unittest.TestCase):
    #前置登录为了token
    def setUp(self):
        self.s=requests.session()
        loginheader = {
            "Authorization": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTU2MzUwNTI4MiwidHlwIjoiSldUIn0.eyJpZCI6MjY2ODQzNzUzNjAyMzUxNTM0LCJleHAiOjE1NjM1MDUyODJ9.WxIOz4-jyiYxyCtynZ1Cp04F-w41AMRDbTH8bdLR_b0",
            "Content-Type": "application/json; charset=UTF-8" }
        loginurl = 'http://api.88ba.com/user/login'
        loginbody = {"mobile": "15002020501",
                     "captcha": "1234"}
        self.loginr = self.s.post(loginurl, json=loginbody, headers=loginheader)
    def getPurchaseSubscribe (self,x):
        header = {"Authorization":self.loginr.json()["body"]["token"]}
        url = "http://api.88ba.com/order/subscribe/getPurchaseSubscribe"
        r =self.s.get(url, params=x, headers=header)
        return r.json()
    def test_01(self):
        u'''userId存在'''
        a={'userId':'314561849444008293'}
        self.getPurchaseSubscribe(a)
        self.assertEqual(self.getPurchaseSubscribe(a)["msg"], "success")
    def test_02(self):
        u'''userId不存在'''
        a={'userId':'12345678'}
        self.getPurchaseSubscribe(a)
        self.assertEqual(self.getPurchaseSubscribe(a)["msg"],"success")
    def test_03(self):
        u'''userID为空'''
        a={'userId':''}
        self.getPurchaseSubscribe(a)
        self.assertNotEqual(self.getPurchaseSubscribe(a)["msg"],"success")
    def tearDown(self):
        self.s.close()
