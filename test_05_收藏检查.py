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


class 收藏检查(unittest.TestCase, BasePage):
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
    def test_01_资讯新闻收藏(self):
        a.return_back()
        a.click_T('首页')
        a.click_T('新闻')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('收藏')

    @testcase
    def test_02_资讯取消新闻收藏(self):   
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('取消收藏')

    @testcase
    def test_03_资讯视频收藏(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/layout_item')
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('收藏')

    @testcase
    def test_04_资讯取消视频收藏(self):
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('取消收藏')

    @testcase
    def test_05_资讯图片收藏(self):
        a.return_back()
        a.click_T('图片')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('收藏')

    @testcase
    def test_06_资讯取消图片收藏(self):
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('取消收藏')
        
    @testcase
    def test_07_资讯行情收藏(self):
        a.return_back()
        a.click_T('行情')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('收藏')
        
    @testcase
    def test_08_资讯取消行情收藏(self):
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('取消收藏')
        
    @testcase
    def test_09_资讯养车收藏(self):
        a.return_back()
        a.click_T('养车')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('收藏')
        
    @testcase
    def test_10_资讯取消养车收藏(self):
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('取消收藏')

    @testcase
    def test_11_资讯评测收藏(self):
        a.return_back()
        a.click_T('评测')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('收藏')

    @testcase
    def test_12_资讯取消评测收藏(self):
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('取消收藏')

    @testcase
    def test_13_资讯政策收藏(self):
        a.return_back()
        a.click_T('政策')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('收藏')

    @testcase
    def test_14_资讯取消政策收藏(self):
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('取消收藏')

    @testcase
    def test_15_资讯物流收藏(self):
        a.return_back()
        a.click_T('物流')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('收藏')

    @testcase
    def test_16_资讯取消物流收藏(self):
        a.click_R('com.truckhome.bbs:id/iv_more')
        a.click_T('取消收藏')

    @testcase
    def test_17_卡友圈动态收藏(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/tv_count_comment')
        a.click_R('com.truckhome.bbs:id/toolBar_iv_set')
        a.click_T('添加收藏')

    @testcase
    def test_18_卡友圈取消动态收藏(self):
        a.click_R('com.truckhome.bbs:id/toolBar_iv_set')
        a.click_T('取消收藏')












