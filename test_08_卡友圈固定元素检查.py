#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from Public.BasePage import BasePage
from Public.Decorator import *
from PageObject import login
import unittest
from Public.AppAtxLibrary import AppatxLibrary
from Public.ReadConfig import ReadConfig
apk_url = ReadConfig().get_apk_url()
pkg_name = ReadConfig().get_pkg_name()
apk_path = ReadConfig().get_apk_path()


class 卡友圈固定元素检查(unittest.TestCase, BasePage):
    #本用例包含安装App、启动、初始app、检查正常登陆、退出功能
    global a
    a = AppatxLibrary()
    
    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.a = AppatxLibrary()
        cls.a.clear_app()
        cls.a.open_app()
        cls.a.chu_shi()

    @testcase
    def test_01_卡友圈推荐热议话题(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('推荐')
        a.cha_T('热议话题')   

    @testcase
    def test_02_卡友圈推荐热议话题一(self):
        a.cha_R('com.truckhome.bbs:id/img_one')

    @testcase
    def test_03_卡友圈推荐热议话题二(self):
        a.cha_R('com.truckhome.bbs:id/img_two')

    @testcase
    def test_04_卡友圈推荐热议话题三(self):
        a.cha_R('com.truckhome.bbs:id/img_three')

    @testcase
    def test_05_卡友圈推荐热议话题四(self):
        a.cha_R('com.truckhome.bbs:id/img_four')

    @testcase
    def test_06_卡友圈推荐热议话题一(self):
        a.cha_R('com.truckhome.bbs:id/img_one')

    @testcase
    def test_07_卡友圈推荐热议全部(self):
        a.cha_T('全部')

    @testcase
    def test_08_卡友圈推荐添加好友按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_recommend')#添加好友按钮

    @testcase
    def test_09_卡友圈最新关注按钮(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('最新')
        a.cha_R('com.truckhome.bbs:id/truck_friends_circle_admin_setting_iv') #关注按钮   

    @testcase
    def test_10_卡友圈最新昵称(self):
        a.cha_R('com.truckhome.bbs:id/tv_name') #昵称

    @testcase
    def test_11_卡友圈最新等级(self):
        a.cha_R('com.truckhome.bbs:id/img_level') #等级

    @testcase
    def test_12_卡友圈最新关注粉丝数(self):
        a.cha_R('com.truckhome.bbs:id/tv_time') #关注粉丝数

    @testcase
    def test_13_卡友圈最新头像(self):
        a.cha_R('com.truckhome.bbs:id/iv_header') #头像

    @testcase
    def test_14_卡友圈最新转发按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_app_forward') #转发按钮

    @testcase
    def test_15_卡友圈最新评论按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_comment') #评论按钮

    @testcase
    def test_16_卡友圈最新赞按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_like_nor') #赞按钮

    @testcase
    def test_17_卡友圈视频关注按钮(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('视频')
        a.cha_R('com.truckhome.bbs:id/truck_friends_circle_admin_setting_iv') #关注按钮

    @testcase
    def test_18_卡友圈视频昵称(self):
        a.cha_R('com.truckhome.bbs:id/tv_name') #昵称

    @testcase
    def test_19_卡友圈视频等级(self):
        a.cha_R('com.truckhome.bbs:id/img_level') #等级

    @testcase
    def test_20_卡友圈视频关注粉丝数(self):
        a.cha_R('com.truckhome.bbs:id/tv_time') #关注粉丝数

    @testcase
    def test_21_卡友圈视频头像(self):
        a.cha_R('com.truckhome.bbs:id/iv_header') #头像

    @testcase
    def test_22_卡友圈视频转发按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_app_forward') #转发按钮

    @testcase
    def test_23_卡友圈视频评论按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_comment') #评论按钮

    @testcase
    def test_24_卡友圈视频赞按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_like_nor') #赞按钮

    @testcase
    def test_25_卡友圈视频视频封面(self):
        a.cha_R('com.truckhome.bbs:id/surface_container') #视频封面        

    @testcase
    def test_26_卡友圈附近关注按钮(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('最新')
        a.cha_R('com.truckhome.bbs:id/truck_friends_circle_admin_setting_iv') #关注按钮        

    @testcase
    def test_27_卡友圈附近昵称(self):
        a.cha_R('com.truckhome.bbs:id/tv_name') #昵称

    @testcase
    def test_28_卡友圈附近等级(self):
        a.cha_R('com.truckhome.bbs:id/img_level') #等级

    @testcase
    def test_29_卡友圈附近关注粉丝数(self):
        a.cha_R('com.truckhome.bbs:id/tv_time') #关注粉丝数

    @testcase
    def test_30_卡友圈附近头像(self):
        a.cha_R('com.truckhome.bbs:id/iv_header') #头像

    @testcase
    def test_31_卡友圈附近转发按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_app_forward') #转发按钮
        a.cha_R('com.truckhome.bbs:id/iv_comment') #评论按钮
        a.cha_R('com.truckhome.bbs:id/iv_like_nor') #赞按钮
