# coding:utf-8
import json
from bs4 import BeautifulSoup
import re
from urllib import parse
from lxml import etree
import traceback



class HtmlParser(object):
    '''
    和解析相关的类
    '''
    def paser_xpath(self,html_content,xpath_dict):  # 解析页面
        '''
        利用xpath解析
        :param html_content:页面内容
        :param xpath_dict: xpath的解析列表
        :return: 解析结果的字典
        '''
        try:
            soup = etree.HTML(html_content)
            result_dict={}
            for key,val in xpath_dict.items():
                try:
                    result_dict[key]=soup.xpath(val)
                except Exception:
                    result_dict[key]=["Error",str(traceback.format_exc()),str(Exception.with_traceback())]
            return result_dict
        except:
            return None



