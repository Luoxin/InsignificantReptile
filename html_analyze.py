# coding:utf-8
import json
from bs4 import BeautifulSoup
import re
from urllib import parse
from urllib.parse import urljoin
from lxml import etree
import traceback



class HtmlParser(object):
    '''
    和解析相关的类
    '''
    def paser_xpath(self, html_content, xpath_dict):  # 解析页面
        '''
        利用xpath解析
        :param html_content:页面内容
        :param xpath_dict: xpath的解析列表
            {
                '解析的key':{
                    'xpath' : '' ,  # xpath  必须
                    'base_url':'',  # 要拼接的基础的url
                    'reserved_keywords'：[''],  # 存在则保留，和removed_keywords只能存在一个
                    'removed_keywords': [''],   # 存在则删除，和reserved_keywords只能存在一个
                }
            }
        :return: 解析结果的字典
        '''
        try:
            soup = etree.HTML(html_content)
            result_dict={}
            for key,val in xpath_dict.items():
                result_dict[key]=self._paser_xpath_onekey(soup=soup, key=key, val=val)
            return result_dict
        except:
            return None

    def _paser_xpath_onekey(self, soup, key, val):
        result=[]
        try:
            if 'base_url' in val:  # url的
                '''
                如果是url则拼接
                ["xpath","url"]
                '''
                result_list = soup.xpath(val["xpath"])
                for __, url in enumerate(result_list):
                    result.append(urljoin(val["base_url"], url))
            else:  # 不需要处理的
                result = soup.xpath(val["xpath"])

            #  对关键字做处理
            if 'reserved_keywords' in val:
                if isinstance(val["reserved_keywords"], list):
                    self.__reserved_keywords(result, val["reserved_keywords"])
                pass
            elif 'removed_keywords' in val:
                if isinstance(val["removed_keywords"], list):
                    self.__reserved_keywords(result, val["removed_keywords"])
        except Exception:
            result = ["Error", str(traceback.format_exc()), str(Exception.with_traceback())]
        return result



    def __reserved_keywords(self,data,reserved_keywords):
        pass

    def __removed_keywords(self,data,removed_keywords):
        pass



