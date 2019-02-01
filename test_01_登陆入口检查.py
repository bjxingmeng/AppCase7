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

    @testcase
    def test_01_新闻(self):
        a.click_T('首页')
        a.click_T('新闻')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('发表我的看法...')
        a.cha_T('立即注册')

    @testcase
    def test_02_视频(self):
        a.return_back()
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/layout_item')
        a.click_T('发表我的看法...')
        a.cha_T('立即注册')

    @testcase
    def test_03_图片(self):
        a.return_back()
        a.click_T('图片')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('发表我的看法...')
        a.cha_T('立即注册')

    @testcase
    def test_04_行情(self):
        a.return_back()
        a.click_T('行情')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/comment_tv')
        a.cha_T('立即注册')

    @testcase
    def test_05_养车(self):
        a.return_back()
        a.click_T('养车')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/comment_tv')
        a.cha_T('立即注册')

    @testcase
    def test_06_评测(self):
        a.return_back()
        a.click_T('评测')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/comment_tv')
        a.cha_T('立即注册')

    @testcase
    def test_07_政策(self):
        a.return_back()
        a.click_T('政策')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_R('com.truckhome.bbs:id/comment_tv')
        a.cha_T('立即注册')

    @testcase
    def test_08_物流(self):
        a.return_back()
        a.click_T('物流')
        a.click_R('com.truckhome.bbs:id/tv_title')
        a.click_T('发表我的看法...')
        a.cha_T('立即注册')
        
    @testcase
    def test_09_论坛推荐(self):
        a.return_back()
        a.click_T('论坛')
        a.click_T('推荐')
        a.click_T('添加圈子')
        a.cha_T('立即注册')
        
    @testcase
    def test_10_论坛我的消息系统通知(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/layout_forum_msg')
        a.click_T('系统通知')
        a.cha_T('立即注册')

    @testcase
    def test_11_论坛我的消息私信消息(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/layout_forum_msg')
        a.click_T('私信消息')
        a.cha_T('立即注册')


    @testcase
    def test_12_论坛我的消息赞我的(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/layout_forum_msg')
        a.click_T('赞我的')
        a.cha_T('立即注册')

    @testcase
    def test_13_论坛我的消息关注我的(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/layout_forum_msg')
        a.click_T('关注我的')
        a.cha_T('立即注册')


    @testcase
    def test_14_论坛关注(self):
        a.return_back()
        a.click_T('关注')
        a.click_R('com.truckhome.bbs:id/touxiang')
        a.cha_T('立即注册')
        
    @testcase
    def test_15_论坛发帖(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_forum_post')
        a.click_T('发帖子')
        a.cha_T('立即注册')
        
    @testcase
    def test_16_论坛求助(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_forum_post')
        a.click_T('发求助')
        a.cha_T('立即注册')
        
    @testcase
    def test_17_论坛牛人(self):
        a.return_back()
        a.click_T('牛人')
        a.click_R('com.truckhome.bbs:id/forum_user_info_layout')
        a.cha_T('立即注册')

    @testcase
    def test_18_卡友圈关注(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('关注')
        a.click_T('立即登录')
        a.cha_T('立即注册')

    @testcase
    def test_19_卡友圈推荐关注(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/truck_friends_circle_admin_setting_iv')
        a.cha_T('立即注册')

    @testcase
    def test_20_卡友圈视频关注(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/truck_friends_circle_admin_setting_iv')
        a.cha_T('立即注册')

    @testcase
    def test_21_卡友圈附近关注(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('附近')
        a.click_R('com.truckhome.bbs:id/truck_friends_circle_admin_setting_iv')
        a.cha_T('立即注册')

    @testcase
    def test_22_卡友圈集赞达人(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_R('com.truckhome.bbs:id/iv_recommend')
        a.click_R('com.truckhome.bbs:id/iv_liked_header1')
        a.cha_T('立即注册')

    @testcase
    def test_23_卡友圈头像(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_R('com.truckhome.bbs:id/iv_header')
        a.cha_T('立即注册')

    @testcase
    def test_24_卡友圈推荐详情关注(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/lay_item')
        a.click_R('com.truckhome.bbs:id/truck_friends_circle_img_guanzhu')
        a.cha_T('立即注册')

    @testcase
    def test_25_卡友圈最新详情关注(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/iv_comment')
        a.click_R('com.truckhome.bbs:id/truck_friends_circle_img_guanzhu')
        a.cha_T('立即注册')

    @testcase
    def test_26_卡友圈视频详情关注(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/tv_content')
        a.click_R('com.truckhome.bbs:id/truck_friends_circle_img_guanzhu')
        a.cha_T('立即注册')

    @testcase
    def test_27_卡友圈附近详情关注(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('附近')
        a.click_R('com.truckhome.bbs:id/iv_comment')
        a.click_R('com.truckhome.bbs:id/truck_friends_circle_img_guanzhu')
        a.cha_T('立即注册')

    @testcase
    def test_28_卡友圈推荐详情评论(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/lay_item')
        a.click_T('写评论')
        a.cha_T('立即注册')

    @testcase
    def test_29_卡友圈最新详情评论(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/iv_comment')
        a.click_T('写评论')
        a.cha_T('立即注册')

    @testcase
    def test_30_卡友圈视频详情评论(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/tv_content')
        a.click_T('写评论')
        a.cha_T('立即注册')

    @testcase
    def test_31_卡友圈附近详情评论(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('附近')
        a.click_R('com.truckhome.bbs:id/iv_comment')
        a.click_T('写评论')
        a.cha_T('立即注册')

    @testcase
    def test_32_卡友圈推荐详情点赞(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/lay_item')
        a.click_R('com.truckhome.bbs:id/lay_like')
        a.cha_T('立即注册')

    @testcase
    def test_33_卡友圈最新详情点赞(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('最新')
        a.click_R('com.truckhome.bbs:id/iv_comment')
        a.click_R('com.truckhome.bbs:id/lay_like')
        a.cha_T('立即注册')

    @testcase
    def test_34_卡友圈视频详情点赞(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('视频')
        a.click_R('com.truckhome.bbs:id/tv_content')
        a.click_R('com.truckhome.bbs:id/lay_like')
        a.cha_T('立即注册')

    @testcase
    def test_35_卡友圈附近详情点赞(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('附近')
        a.click_R('com.truckhome.bbs:id/iv_comment')
        a.click_R('com.truckhome.bbs:id/lay_like')
        a.cha_T('立即注册')

    @testcase
    def test_36_发布卡友圈(self):
        a.return_back()
        a.click_R('com.truckhome.bbs:id/iv_friends_circle')
        a.click_T('推荐')
        a.click_R('com.truckhome.bbs:id/iv_ciriv_circle_postcle_post')
        a.cha_T('立即注册')