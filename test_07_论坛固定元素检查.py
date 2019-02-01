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


class 论坛固定元素检查(unittest.TestCase, BasePage):
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
    def test_01_论坛列表关注(self):
        a.click_T('论坛')
        a.click_T('推荐')
        a.cha_T('关注')

    @testcase
    def test_02_论坛列表推荐(self):
        a.cha_T('推荐')

    @testcase
    def test_03_论坛列表最新(self):
        a.cha_T('最新')

    @testcase
    def test_04_论坛列表求助(self):
        a.cha_T('求助')

    @testcase
    def test_05_论坛列表十大热帖(self):
        a.cha_T('十大热帖')

    @testcase
    def test_06_论坛列表牛人(self):
        a.cha_T('牛人')

    @testcase
    def test_07_论坛列表视频(self):
        a.cha_T('视频')

    @testcase
    def test_08_论坛推荐求助问答(self):
        a.return_back()
        a.click_T('论坛')
        a.click_T('推荐')
        a.cha_T('求助问答')

    @testcase
    def test_09_论坛推荐活动标题(self):
        a.cha_R('com.truckhome.bbs:id/forum_recommend_activity_title_tv') #活动标题

    @testcase
    def test_10_论坛推荐查看全部(self):
        a.cha_T('查看全部')

    @testcase
    def test_11_论坛推荐标题(self):
        a.cha_R('com.truckhome.bbs:id/tv_forum_common_title') #标题

    @testcase
    def test_12_论坛推荐发帖人昵称(self):
        a.cha_R('com.truckhome.bbs:id/tv_forum_common_author') #发帖人昵称

    @testcase
    def test_13_论坛推荐查看回帖数(self):
        a.cha_R('com.truckhome.bbs:id/tv_forum_common_count') #查看回帖数

    @testcase
    def test_14_论坛推荐发帖按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_forum_post') #查看回帖数

    @testcase
    def test_15_论坛推荐发帖按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_forum_post') #查看回帖数

    @testcase
    def test_16_论坛推荐发帖按钮(self):
        a.cha_R('com.truckhome.bbs:id/iv_forum_post') #发帖按钮

    @testcase
    def test_17_论坛推荐发帖子(self):
        a.click_R('com.truckhome.bbs:id/iv_forum_post')
        a.cha_T('发帖子') #发帖子按钮

    @testcase
    def test_18_论坛推荐发帖子(self):
        a.click_R('com.truckhome.bbs:id/iv_forum_post')
        a.cha_T('发求助') #发求助按钮

    @testcase
    def test_19_论坛最新标题(self):
        a.return_back()
        a.click_T('论坛')
        a.click_T('最新')
        a.cha_R('com.truckhome.bbs:id/tv_forum_newest_title') #标题

    @testcase
    def test_20_论坛最新昵称(self):
        a.cha_R('com.truckhome.bbs:id/tv_forum_newest_nickname') #昵称

    @testcase
    def test_21_论坛最新浏览观看数(self):
        a.cha_R('com.truckhome.bbs:id/tv_forum_newest_count') #浏览观看数

    @testcase
    def test_22_论坛求助标题(self):
        a.return_back()
        a.click_T('论坛')
        a.click_T('求助')
        a.cha_R('com.truckhome.bbs:id/tv_tribune_sos_content') #标题

    @testcase
    def test_23_论坛求助类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_tribune_sos_tag') #类型

    @testcase
    def test_24_论坛求助帮助数(self):
        a.cha_R('com.truckhome.bbs:id/tv_tribune_sos_help_num') #帮助数

    @testcase
    def test_25_论坛十大热帖日期(self):
        a.click_T('十大热帖')
        a.cha_R('com.truckhome.bbs:id/ten_hot_post_date_tv') #日期

    @testcase
    def test_26_论坛牛人我要加入(self):
        a.click_T('牛人')
        a.cha_R('com.truckhome.bbs:id/cattle_regiment_label_join_iv') #我要加入按钮

    @testcase
    def test_27_论坛视频标题(self):
        a.return_back()
        a.click_T('论坛')
        a.click_T('视频')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_28_论坛视频封面(self):
        a.cha_R('com.truckhome.bbs:id/iv_video') #封面

    @testcase
    def test_29_论坛视频发帖人昵称(self):
        a.cha_R('com.truckhome.bbs:id/tv_user_name') #发帖人昵称

    @testcase
    def test_30_论坛视频回帖数(self):
        a.cha_R('com.truckhome.bbs:id/tv_join_repaly') #回帖数