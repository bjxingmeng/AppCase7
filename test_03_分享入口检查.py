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


class 分享入口检查(unittest.TestCase, BasePage):
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
    def test_01_资讯新闻分享(self):
        a.return_back()
        a.click_T('首页')
        a.click_T('新闻')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('分享')
        a.cha_T('复制链接')
 
    @testcase
    def test_02_资讯视频分享(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/layout_item')
        a.click_T('分享')
        a.cha_T('复制链接')

    @testcase
    def test_03_资讯图片分享(self):
        a.return_back()
        a.click_T('图片')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('分享')
        a.click_T('复制链接')

    def test_04_资讯行情分享(self):
        a.return_back()
        a.click_T('行情')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('分享')
        a.click_T('复制链接')

    @testcase
    def test_05_资讯养车分享(self):
        a.return_back()
        a.click_T('养车')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('分享')
        a.cha_T('复制链接')

    @testcase
    def test_06_资讯评测分享(self):
        a.return_back()
        a.click_T('评测')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('分享')
        a.cha_T('复制链接')

    @testcase
    def test_07_资讯政策分享(self):
        a.return_back()
        a.click_T('政策')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('分享')
        a.cha_T('复制链接')

    @testcase
    def test_08_资讯物流分享(self):
        a.return_back()
        a.click_T('物流')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('分享')
        a.cha_T('复制链接')

    @testcase
    def test_09_论坛十大(self):
        a.return_back()
        a.click_T('论坛')
        a.click_T('十大热帖')
        a.click_R('com.truckhome.bbs:id/ten_hot_post_title_tv')
        a.click_T('分享')
        a.click_T('复制链接')

    @testcase
    def test_10_论坛牛人加入(self):
        a.return_back()
        a.click_T('牛人')
        a.click_R('com.truckhome.bbs:id/cattle_regiment_label_join_iv')
        a.click_R('com.truckhome.bbs:id/news_share')
        a.click_T('复制链接')

    @testcase
    def test_11_论坛推荐(self):
        a.return_back()
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/tv_forum_common_title')
        a.click_T('分享')
        a.click_T('复制链接')

    @testcase
    def test_12_论坛最新(self):
        a.return_back()
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/tv_forum_newest_title')
        a.click_T('分享')
        a.click_T('复制链接')

    @testcase
    def test_13_论坛视频(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('分享')
        a.click_T('复制链接')

    @testcase
    def test_14_卡友圈推荐列表(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('推荐')
        a.huaDongChaZhao()
        a.click_R('com.truckhome.bbs:id/lay_app_forward')
        a.click_T('复制链接')

    @testcase
    def test_15_卡友圈最新列表(self):
        a.return_back()
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/lay_app_forward')
        a.click_T('复制链接')

    @testcase
    def test_16_卡友圈视频列表(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/lay_app_forward')
        a.click_T('复制链接')

    @testcase
    def test_17_卡友圈附近列表(self):
        a.return_back()
        a.click_T('附近')
        a.click_R('com.truckhome.bbs:id/lay_app_forward')
        a.click_T('复制链接')

    def test_18_卡友圈推荐详情(self):
        a.return_back()
        a.click_T('推荐')
        a.huaDongChaZhao()
        a.click_R('com.truckhome.bbs:id/lay_item')
        a.click_R('com.truckhome.bbs:id/lay_app_forward')
        a.click_T('复制链接')

    @testcase
    def test_19_卡友圈最新详情(self):
        a.return_back()
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/iv_comment')       
        a.click_R('com.truckhome.bbs:id/lay_app_forward')
        a.click_T('复制链接')

    @testcase
    def test_20_卡友圈视频详情(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/tv_count_comment')
        a.click_R('com.truckhome.bbs:id/lay_app_forward')
        a.click_T('复制链接')

    @testcase
    def test_21_卡友圈附近详情(self):
        a.return_back()
        a.click_T('附近')
        a.click_R('com.truckhome.bbs:id/tv_count_comment')
        a.click_R('com.truckhome.bbs:id/lay_app_forward')
        a.click_T('复制链接')