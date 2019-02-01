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


class 首页固定元素检查(unittest.TestCase, BasePage):
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
    def test_01_推荐全部(self):
        a.cha_T('全部')

    @testcase
    def test_02_推荐轮播图(self):
        a.cha_R('com.truckhome.bbs:id/focus_map_ad_iv') #轮播图

    @testcase
    def test_03_推荐全部资讯(self):
        a.click_T('全部')
        a.cha_T('资讯')

    @testcase
    def test_04_推荐全部新闻专题(self):
        a.cha_T('新闻专题') #新闻专题

    @testcase
    def test_05_推荐全部专题(self):
        a.cha_T('专题') #专题

    @testcase
    def test_06_推荐全部商城询价(self):
        a.cha_T('商城询价') #商城询价

    @testcase
    def test_07_推荐全部优选尿素(self):
        a.cha_T('优选尿素') #优选尿素

    @testcase
    def test_08_推荐全部优惠购车(self):
        a.cha_T('优惠购车') #优惠购车

    @testcase
    def test_09_推荐全部挂车集市(self):
        a.cha_T('挂车集市') #挂车集市

    @testcase
    def test_10_推荐全部二手车(self):
        a.cha_T('二手车') #二手车

    @testcase
    def test_11_推荐全部挂车选购(self):
        a.cha_T('挂车选购') #挂车选购

    @testcase
    def test_12_推荐全部挂靠黄页(self):
        a.cha_T('挂靠黄页') #挂靠黄页

    @testcase
    def test_13_推荐全部看图选车(self):
        a.cha_T('看图选车') #看图选车

    @testcase
    def test_14_推荐全部卡友服务(self):
        a.cha_T('卡友服务') #卡友服务

    @testcase
    def test_15_推荐全部司机招聘(self):
        a.huaDongChaZhao()
        a.cha_T('司机招聘') #司机招聘

    @testcase
    def test_16_推荐全部求助(self):
        a.cha_T('求助') #求助

    @testcase
    def test_17_推荐全部附近商家(self):
        a.cha_T('附近商家') #附近商家

    @testcase
    def test_18_推荐全部安全随行(self):
        a.cha_T('安全随行') #安全随行

    @testcase
    def test_19_推荐全部附近卡友(self):
        a.cha_T('附近卡友') #附近卡友

    @testcase
    def test_20_推荐全部附近经销商(self):
        a.cha_T('附近经销商') #附近经销商

    @testcase
    def test_21_推荐全部附近服务站(self):
        a.cha_T('附近服务站') #附近服务站

    @testcase
    def test_22_推荐全部活动(self):
        a.cha_T('活动') #活动

    @testcase
    def test_23_推荐全部购车计算器(self):
        a.cha_T('购车计算器') #购车计算器

    @testcase
    def test_24_推荐全部快运贷(self):
        a.cha_T('快运贷') #快运贷

    @testcase
    def test_25_推荐全部1(self):
        a.cha_T('司机险') #司机险

    @testcase
    def test_26_资讯新闻标题(self):
        a.return_back()
        a.click_T('新闻')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_27_资讯新闻类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_28_资讯新闻评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_29_资讯新闻图片(self):
        a.cha_R('com.truckhome.bbs:id/iv_news') #图片

    @testcase
    def test_30_资讯视频标题(self):
        a.return_back()
        a.click_T('视频')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_31_资讯视频类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_32_资讯视频评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_33_资讯视频播放数(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_play') #播放数
        a.cha_R('com.truckhome.bbs:id/iv_image') #播放数

    @testcase
    def test_34_资讯图片标题(self):
        a.return_back()
        a.click_T('图片')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_35_资讯图片类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_36_资讯图片评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_37_资讯图片查看数(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_play') #查看数
        a.cha_R('com.truckhome.bbs:id/iv_image') #查看数

    @testcase
    def test_38_资讯行情地区(self):
        a.return_back()
        a.click_T('行情')
        a.cha_R('com.truckhome.bbs:id/ll_location') #地区

    @testcase
    def test_39_资讯行情标题(self):
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_40_资讯行情类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_41_资讯行情评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_42_资讯行情图片(self):
        a.cha_R('com.truckhome.bbs:id/iv_news') #图片

    @testcase
    def test_43_资讯导购类型筛选(self):
        a.return_back()
        a.click_T('导购')
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型筛选

    @testcase
    def test_44_资讯导购品牌筛选(self):
        a.cha_R('com.truckhome.bbs:id/tv_brand') #品牌筛选

    @testcase
    def test_45_资讯导购价格筛选(self):
        a.cha_R('com.truckhome.bbs:id/tv_price') #价格筛选      

    @testcase
    def test_46_资讯导购地区(self):
        a.cha_R('com.truckhome.bbs:id/tv_location_city') #地区

    @testcase
    def test_47_资讯导购标题(self):
        a.cha_R('com.truckhome.bbs:id/article_title_tv') #标题

    @testcase
    def test_48_资讯导购类型(self):
        a.cha_R('com.truckhome.bbs:id/article_tv_type') #类型
        
    @testcase
    def test_49_资讯导购价格(self):
        a.cha_R('com.truckhome.bbs:id/article_price') #价格

    @testcase
    def test_50_资讯导购图片(self):
        a.cha_R('com.truckhome.bbs:id/article_iv') #图片

    @testcase
    def test_51_资讯养车标题(self):
        a.return_back()
        a.click_T('养车')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_52_资讯养车类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_53_资讯养车评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_54_资讯养车图片(self):
        a.cha_R('com.truckhome.bbs:id/iv_news') #图片

    @testcase
    def test_55_资讯评测标题(self):
        a.return_back()
        a.click_T('评测')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_56_资讯评测类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_57_资讯评测评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_58_资讯评测图片(self):
        a.cha_R('com.truckhome.bbs:id/iv_news') #图片

    @testcase
    def test_59_资讯政策标题(self):
        a.return_back()
        a.click_T('政策')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_60_资讯政策类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_61_资讯政策评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_62_资讯政策图片(self):
        a.cha_R('com.truckhome.bbs:id/iv_news') #图片

    @testcase
    def test_63_资讯政策标题(self):
        a.return_back()
        a.click_T('政策')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_64_资讯政策类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_65_资讯政策评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_66_资讯政策图片(self):
        a.cha_R('com.truckhome.bbs:id/iv_news') #图片

    @testcase
    def test_67_资讯物流标题(self):
        a.return_back()
        a.click_T('物流')
        a.cha_R('com.truckhome.bbs:id/tv_title') #标题

    @testcase
    def test_68_资讯物流类型(self):
        a.cha_R('com.truckhome.bbs:id/tv_type') #类型

    @testcase
    def test_69_资讯物流评论(self):
        a.cha_R('com.truckhome.bbs:id/tv_count_comment') #评论

    @testcase
    def test_70_资讯物流图片(self):
        a.cha_R('com.truckhome.bbs:id/iv_news') #图片

    @testcase
    def test_71_资讯音频标题(self):
        a.return_back()
        a.click_T('音频')
        a.cha_R('com.truckhome.bbs:id/audio_title_tv') #标题 

    @testcase
    def test_72_资讯音频图片(self):
        a.cha_R('com.truckhome.bbs:id/audio_iv') #图片

    @testcase
    def test_73_资讯音频播放数(self):
        a.cha_R('com.truckhome.bbs:id/audio_play_count_tv') #播放数

    @testcase
    def test_74_资讯音频播放按钮(self):
        a.cha_R('com.truckhome.bbs:id/audio_play_iv') #播放按钮

