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


class 选车固定元素检查(unittest.TestCase, BasePage):
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
    def test_01_选车筛选找车(self):
        a.click_T('选车')
        a.cha_T('筛选找车')

    @testcase
    def test_02_选车按工况找车(self):
        a.cha_T('按工况找车')

    @testcase
    def test_03_选车排行榜(self):
        a.cha_T('排行榜')

    @testcase
    def test_04_选车最近浏览(self):
        a.cha_T('最近浏览')

    @testcase
    def test_05_选车推荐品牌(self):
        a.cha_T('推荐品牌')

    @testcase
    def test_06_选车热销排行(self):
        a.cha_T('热销排行')

    @testcase
    def test_07_选车新能源选车(self):
        a.cha_T('新能源选车')

    @testcase
    def test_08_选车推荐配件(self):
        a.cha_T('推荐配件')










































