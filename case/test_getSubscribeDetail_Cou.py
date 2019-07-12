#coding:utf-8
import requests
import unittest
class getSubscribeDetail(unittest.TestCase):
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
    def getSubscribeDetail (self,x):
        header = {"Authorization":self.loginr.json()["body"]["token"]}
        url = "http://api.88ba.com/order/subscribe/getSubscribeDetail"
        r =self.s.get(url, params=x, headers=header)
        return r.json()
    def test_01(self):
        u'''serviceId输入101，plan正常输入'''
        a={'serviceId':'101','plan':'333177429558296834'}
        self.getSubscribeDetail(a)
        self.assertEqual(self.getSubscribeDetail(a)["msg"],"success")
    def test_02(self):
        u'''serviceId输入空，plan正常输入'''
        a={'serviceId':'','plan':'333177429558296834'}
        self.getSubscribeDetail(a)
        self.assertNotEqual(self.getSubscribeDetail(a)["msg"],"success")
    def test_03(self):
        u'''serviceId输入不存在的id，plan正常输入'''
        a={'serviceId':'20000','plan':'333177429558296834'}
        self.getSubscribeDetail(a)
        self.assertNotEqual(self.getSubscribeDetail(a)["msg"],"success")
    def test_04(self):
        u'''serviceId输入101，plan输入空'''
        a = {'serviceId': '101', 'plan': ''}
        self.getSubscribeDetail(a)
        self.assertNotEqual(self.getSubscribeDetail(a)["msg"], "success")
    def test_05(self):
        u'''serviceId输入101，plan输入不存在的id'''
        a = {'serviceId': '101', 'plan': '123456789'}
        self.getSubscribeDetail(a)
        self.assertEqual(self.getSubscribeDetail(a)["msg"], "success")
    def tearDown(self):
        self.s.close()