#coding:utf-8
# import requests
# import unittest
# class createOrupdate(unittest.TestCase):
#     #前置登录为了token
#     def setUp(self):
#         self.s=requests.session()
#         loginheader = {
#             "Authorization": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTU2MzUwNTI4MiwidHlwIjoiSldUIn0.eyJpZCI6MjY2ODQzNzUzNjAyMzUxNTM0LCJleHAiOjE1NjM1MDUyODJ9.WxIOz4-jyiYxyCtynZ1Cp04F-w41AMRDbTH8bdLR_b0",
#             "Content-Type": "application/json; charset=UTF-8" }
#         loginurl = 'http://api.88ba.com/user/login'
#         loginbody = {"mobile": "15002020501",
#                      "captcha": "1234"}
#
#         self.loginr = self.s.post(loginurl, json=loginbody, headers=loginheader)
#
#     #order/purchase/createOrUpdate
#     def purchase (self,x):
#         header = {"Authorization":self.loginr.json()["body"]["token"]}
#         url = "http://api.88ba.com/order/purchase/createOrUpdate"
#         r =self.s.post(url, json=x, headers=header)
#         return r.json()
#
#     def test_01(self):
#         u'''参数全对'''
#         a={"tOrderEngineeringOrder": {"businessType": 1,
#                                 "serviceType": 4,
#                                 "orderType": 1,
#                                 "customerRemark": "",
#                                 "publishRemark": "测试",
#                                 "provinceId": "",
#                                 "cityId": "",
#                                 "budget": "10000"},
#             "tOrderEngineeringOrderItem": [{"TemplateId": 5,
#                                      "AttrId": 1037,
#                                      "AttrName": "watt",
#                                      "AttrDisplay": "最大负载/W",
#                                      "AttrValue": "200",
#                                      "AttrDisplayValue": "200"},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1038,
#                                      "AttrName": "brand",
#                                      "AttrDisplay": "品牌",
#                                      "AttrValue": "1039",
#                                      "AttrDisplayValue": "品牌不限"},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1050,
#                                      "AttrName": "number",
#                                      "AttrDisplay": "数量(PCS)",
#                                      "AttrValue": "2000",
#                                      "AttrDisplayValue": "2000"},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1051,
#                                      "AttrName": "expirationDate",
#                                      "AttrDisplay": "采购截止日期",
#                                      "AttrValue": "2019-06-30",
#                                      "AttrDisplayValue": "2019-06-30"}],
#              "tUserDeliveryInfo": {"contactName": "兔子",
#                            "contactNo": "18682314873",
#                            "provinceId": "210000",
#                            "provinceName": "辽宁省",
#                            "cityId": "210100",
#                            "cityName": "沈阳市",
#                            "areaId": "210102",
#                            "areaName": "和平区",
#                            "address": "详细地址"}}
#         self.purchase(a)
#         self.assertEqual(self.purchase(a)["msg"],"success")
#     def test_02(self):
#         u'''没有添加最大负载'''
#         a={"tOrderEngineeringOrder": {"businessType": 1,
#                                 "serviceType": 4,
#                                 "orderType": 1,
#                                 "customerRemark": "",
#                                 "publishRemark": "测试",
#                                 "provinceId": "",
#                                 "cityId": "",
#                                 "budget": "10000"},
#             "tOrderEngineeringOrderItem": [{"TemplateId": 5,
#                                      "AttrId": 1037,
#                                      "AttrName": "watt",
#                                      "AttrDisplay": "最大负载/W",
#                                      "AttrValue": "",
#                                      "AttrDisplayValue": ""},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1038,
#                                      "AttrName": "brand",
#                                      "AttrDisplay": "品牌",
#                                      "AttrValue": "1039",
#                                      "AttrDisplayValue": "品牌不限"},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1050,
#                                      "AttrName": "number",
#                                      "AttrDisplay": "数量(PCS)",
#                                      "AttrValue": "2000",
#                                      "AttrDisplayValue": "2000"},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1051,
#                                      "AttrName": "expirationDate",
#                                      "AttrDisplay": "采购截止日期",
#                                      "AttrValue": "2019-06-30",
#                                      "AttrDisplayValue": "2019-06-30"}],
#              "tUserDeliveryInfo": {"contactName": "兔子",
#                            "contactNo": "18682314873",
#                            "provinceId": "210000",
#                            "provinceName": "辽宁省",
#                            "cityId": "210100",
#                            "cityName": "沈阳市",
#                            "areaId": "210102",
#                            "areaName": "和平区",
#                            "address": "详细地址"}}
#         self.purchase(a)
#         self.assertNotEqual(self.purchase(a)["msg"],"success")
#     def test_03(self):
#         u'''没有添加数量'''
#         a={"tOrderEngineeringOrder": {"businessType": 1,
#                                 "serviceType": 4,
#                                 "orderType": 1,
#                                 "customerRemark": "",
#                                 "publishRemark": "测试",
#                                 "provinceId": "",
#                                 "cityId": "",
#                                 "budget": "10000"},
#             "tOrderEngineeringOrderItem": [{"TemplateId": 5,
#                                      "AttrId": 1037,
#                                      "AttrName": "watt",
#                                      "AttrDisplay": "最大负载/W",
#                                      "AttrValue": "300",
#                                      "AttrDisplayValue": "300"},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1038,
#                                      "AttrName": "brand",
#                                      "AttrDisplay": "品牌",
#                                      "AttrValue": "1039",
#                                      "AttrDisplayValue": "品牌不限"},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1050,
#                                      "AttrName": "number",
#                                      "AttrDisplay": "数量(PCS)",
#                                      "AttrValue": "",
#                                      "AttrDisplayValue": ""},
#                                     {"TemplateId": 5,
#                                      "AttrId": 1051,
#                                      "AttrName": "expirationDate",
#                                      "AttrDisplay": "采购截止日期",
#                                      "AttrValue": "2019-06-30",
#                                      "AttrDisplayValue": "2019-06-30"}],
#              "tUserDeliveryInfo": {"contactName": "兔子",
#                            "contactNo": "18682314873",
#                            "provinceId": "210000",
#                            "provinceName": "辽宁省",
#                            "cityId": "210100",
#                            "cityName": "沈阳市",
#                            "areaId": "210102",
#                            "areaName": "和平区",
#                            "address": "详细地址"}}
#         self.purchase(a)
#         self.assertNotEqual(self.purchase(a)["msg"],"success")
#     def tearDown(self):
#         self.s.close()
