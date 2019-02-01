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


class 登陆入口检查(unittest.TestCase, BasePage):
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
    def test_01_新闻(self):
        a.return_back()
        a.click_T('首页')
        a.click_T('新闻')
        a.click_R('com.truckhome.bbs:id/tv_title') #第一条内容
        a.click_T('发表我的看法...')
        a.cha_T('去绑定微信')

    @testcase
    def test_02_视频(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/layout_item') #第一条内容
        a.click_T('发表我的看法...')
        a.cha_T('去绑定微信')

    @testcase
    def test_03_图片(self):
        a.return_back()
        a.click_T('图片')
        a.click_R('com.truckhome.bbs:id/tv_title') #第一条内容
        a.click_T('发表我的看法...')
        a.cha_T('去绑定微信')

    @testcase
    def test_04_行情(self):
        a.return_back()
        a.click_T('行情')
        a.click_R('com.truckhome.bbs:id/tv_title') #第一条内容
        a.click_R('com.truckhome.bbs:id/comment_tv')
        a.cha_T('去绑定微信')

    @testcase
    def test_05_养车(self):
        a.return_back()
        a.click_T('养车')
        a.click_R('com.truckhome.bbs:id/tv_title') #第一条内容
        a.click_R('com.truckhome.bbs:id/comment_tv')
        a.cha_T('去绑定微信')

    @testcase
    def test_06_评测(self):
        a.return_back()
        a.click_T('评测')
        a.click_R('com.truckhome.bbs:id/tv_title') #第一条内容
        a.click_R('com.truckhome.bbs:id/comment_tv')
        a.cha_T('去绑定微信')

    @testcase
    def test_07_政策(self):
        a.return_back()
        a.click_T('政策')
        a.click_R('com.truckhome.bbs:id/tv_title') #第一条内容
        a.click_R('com.truckhome.bbs:id/comment_tv')
        a.cha_T('去绑定微信')

    @testcase
    def test_08_物流(self):
        a.return_back()
        a.click_T('物流')
        a.click_R('com.truckhome.bbs:id/tv_title') #第一条内容
        a.click_T('发表我的看法...')
        a.cha_T('去绑定微信')


    @testcase
    def test_09_论坛发帖(self):
        a.return_back()
        a.click_T('论坛')
        a.click_R('com.truckhome.bbs:id/iv_forum_post')#发布按钮
        a.click_T('发帖子')
        a.cha_T('去绑定微信')
        
    @testcase
    def test_10_论坛求助(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_forum_post')#发布按钮
        a.click_T('发求助')
        a.cha_T('去绑定微信')
      
    @testcase
    def test_11_卡友圈推荐详情评论(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')#卡友圈tab按钮
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/lay_item')
        a.click_T('写评论')
        a.cha_T('去绑定微信')

    @testcase
    def test_12_卡友圈最新详情评论(self):
        a.return_back()
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/iv_comment')
        a.click_T('写评论')
        a.cha_T('去绑定微信')

    @testcase
    def test_13_卡友圈视频详情评论(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/tv_content')
        a.click_T('写评论')
        a.cha_T('去绑定微信')

    @testcase
    def test_14_卡友圈附近详情评论(self):
        a.return_back()
        a.click_T('附近')
        a.click_R('com.truckhome.bbs:id/iv_comment')
        a.click_T('写评论')
        a.cha_T('去绑定微信')

    @testcase
    def test_15_发布卡友圈(self):
        a.return_back()
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/iv_ciriv_circle_postcle_post')
        a.cha_T('去绑定微信')
