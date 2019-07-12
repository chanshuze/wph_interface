#coding:utf-8
import requests
import unittest
class getSubscribeList(unittest.TestCase):
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
    def getSubscribeList (self):
        header = {"Authorization":self.loginr.json()["body"]["token"]}
        url = "http://api.88ba.com/order/subscribe/getSubscribeList"
        r =self.s.get(url, headers=header)
        return r.json()
    def test_01(self):
        u'''正常请求'''
        self.getSubscribeList()
        self.assertEqual(self.getSubscribeList()["msg"],"success")
    def tearDown(self):
        self.s.close()
