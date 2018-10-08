#!/usr/local/bin python
# coding=utf-8
# @Time    : 2018/8/19 下午12:24
# @Author  : lifangyi
# @File    : pytest_allure_test.py
# @Software: PyCharm

import allure
import pytest

# Features定制
# Story定制
# 用例标题 == 方法名
# 用例描述 == 注释
# Severity 严重性
# Step描述
# Issue链接
# testcase管理地址


@allure.feature('test module')
class TestAllure(object):

    @allure.story('test_story_01_of_module')
    @allure.severity('blocker')
    @allure.issue('https://github.com/leefyi')
    @allure.testcase('http://www.testlink.com')
    def test_case_01(self):
        """
        用例描述：module01-case01
        """
        assert 0

    @allure.story('test_story_02_of_module')
    @allure.severity('normal')
    @allure.issue('https://github.com/leefyi')
    @allure.testcase('http://www.testlink.com')
    def test_case_02(self):
        """
        用例描述：module01-case02
        """
        assert isinstance('Jack', str)

    @allure.story('test_story_03_of_module')
    @allure.severity('minor')
    @allure.issue('https://github.com/leefyi')
    @allure.testcase('http://www.testlink.com')
    @pytest.mark.skip(reason='暂不执行')
    def test_case_03(self):
        """
        用例描述：module02-case01
        """
        assert 0 == 0

    @allure.story('test_story_04_of_module')
    @allure.severity('critical')
    @allure.issue('https://github.com/leefyi')
    @allure.testcase('http://www.testlink.com')
    def test_case_04(self):
        """
        用例描述：module02-case02
        """
        assert 1 == 1

    @allure.story('test_story_05_of_module')
    @allure.severity('critical')
    @allure.issue('https://github.com/leefyi')
    @allure.testcase('http://www.testlink.com')
    def test_str(self):
        str1 = 'hello'
        str2 = 'world'

        assert str_concat(str1, str2) == 'Hello World'

# Step 定制
# 测试步骤，若两个参数均为str,则拼接


@allure.step('字符串相加')
def str_concat(str1, str2):
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2

    return str1 + str2


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', '../xml'])
