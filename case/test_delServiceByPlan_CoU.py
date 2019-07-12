#coding:utf-8
import requests
import unittest
class delServiceByPlan(unittest.TestCase):
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
    def delServiceByPlan (self,x):
        header = {"Authorization":self.loginr.json()["body"]["token"]}
        url = "http://api.88ba.com/order/subscribe/delServiceByPlan"
        r =self.s.delete(url, params=x, headers=header)
        return r.json()
    def test_01(self):
        u'''isEnterprise输入1，plan正常输入'''
        a={'plan':'333164705449246978','isEnterprise':'1'}
        self.delServiceByPlan(a)
        self.assertEqual(self.delServiceByPlan(a)["msg"],"success")
    def test_02(self):
        u'''isEnterprise输入2，plan正常输入'''
        a={'plan':'333164705449246978','isEnterprise':'2'}
        self.delServiceByPlan(a)
        self.assertEqual(self.delServiceByPlan(a)["msg"],"success")
    def test_03(self):
        u'''isEnterprise输入3，plan正常输入'''
        a={'plan':'333164705449246978','isEnterprise':'3'}
        self.delServiceByPlan(a)
        self.assertEqual(self.delServiceByPlan(a)["msg"],"success")
    def test_04(self):
        u'''isEnterprise输入空，plan正常输入'''
        a={'plan':'333164705449246978','isEnterprise':''}
        self.delServiceByPlan(a)
        self.assertNotEqual(self.delServiceByPlan(a)["msg"],"success")
    def test_05(self):
        u'''isEnterprise输入1，plan输入空'''
        a={'plan':'','isEnterprise':'1'}
        self.delServiceByPlan(a)
        self.assertNotEqual(self.delServiceByPlan(a)["msg"],"success")
    def test_06(self):
        u'''isEnterprise输入1，plan输入不存在的id'''
        a={'plan':'123456','isEnterprise':'1'}
        self.delServiceByPlan(a)
        self.assertEqual(self.delServiceByPlan(a)["msg"],"success")
    def tearDown(self):
        self.s.close()
