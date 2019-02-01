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


class 点赞检查(unittest.TestCase, BasePage):
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
        cls.a.login('test1191','z123456z')

    @testcase
    def test_01_资讯新闻点赞(self):
        a.return_back()
        a.click_T('首页')
        a.click_T('新闻')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('点赞')
        a.cha_T('已赞')

    @testcase
    def test_02_资讯视频点赞(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/layout_item')
        a.click_T('点赞')
        a.cha_T('已赞')

    @testcase
    def test_03_资讯图片点赞(self):
        a.return_back()
        a.click_T('图片')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('点赞')
        a.cha_T('已赞')
        
    @testcase
    def test_04_资讯行情点赞(self):
        a.return_back()
        a.click_T('行情')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('点赞')
        a.cha_T('已赞')
        
    @testcase
    def test_05_资讯养车点赞(self):
        a.return_back()
        a.click_T('养车')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('点赞')
        a.cha_T('已赞')

    @testcase
    def test_06_资讯评测点赞(self):
        a.return_back()
        a.click_T('评测')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('点赞')
        a.cha_T('已赞')

    @testcase
    def test_07_资讯政策点赞(self):
        a.return_back()
        a.click_T('政策')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('点赞')
        a.cha_T('已赞')

    @testcase
    def test_08_资讯物流点赞(self):
        a.return_back()
        a.click_T('物流')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('点赞')
        a.cha_T('已赞')

    @testcase
    def test_09_论坛帖子点赞(self):
        a.return_back()
        a.click_T('论坛')
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/tv_forum_newest_title')
        a.click_T('点赞')
        a.cha_T('已赞')

    @testcase
    def test_10_卡友圈推荐点赞(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/tv_content')
        a.click_T('点赞')
        a.cha_T('已赞')

    @testcase
    def test_11_卡友圈最新点赞(self):
        a.return_back()
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/tv_count_comment')
        a.click_R('com.truckhome.bbs:id/tv_zan_state')
        a.cha_T('已赞')

    @testcase
    def test_12_卡友圈视频点赞(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/tv_count_comment')
        a.click_R('com.truckhome.bbs:id/tv_zan_state')
        a.cha_T('已赞')

    @testcase
    def test_13_卡友圈附近点赞(self):
        a.return_back()
        a.click_T('附近')
        a.click_R('com.truckhome.bbs:id/tv_count_comment')
        a.click_R('com.truckhome.bbs:id/tv_zan_state')
        a.cha_T('已赞')

    @testcase
    def test_14_卡友圈关注点赞(self):
        a.return_back()
        a.click_T('关注')
        a.click_R('com.truckhome.bbs:id/tv_count_comment')
        a.click_R('com.truckhome.bbs:id/tv_zan_state')
        a.cha_T('已赞')
