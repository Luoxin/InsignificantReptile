import urllib.request
from contextlib import closing
import requests
from tqdm import tqdm

class HtmlDownloader:
    '''
    和下载相关的类
    '''
    def download_html(self, url):
        '''
        下载碰面
        :param url: 需要下载的地址
        :return: 页面内容或None
        '''
        try:
            # url=url.encode("utf-8")
            print("准备下载页面"+url)
            user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
            headers = {'User-Agent': user_agent}
            req_timeout = 20
            request = urllib.request.Request(url, headers=headers)
            # print(request)
            response = urllib.request.urlopen(request, None, req_timeout)  # 这里会有一个返回值 是我们的响应
            # print(response.getcode())
            # 我们判断如果不是200就返回None 否则就返回数据就
            if response.getcode() != 200:
                return None

            # 从响应中读取页面数据并返回
            return response.read()
        except :
            return None

    def download_file(self,url, fileName):
        '''
        下载文件
        :param url: 下载地址
        :param fileName: 文件名
        :return:
        '''
        with closing(requests.get(url, stream=True)) as response:
            chunk_size = 1024  # 单次请求最大值
            content_size = int(response.headers['content-length'])  # 内容体总大小
            with open(fileName, "wb") as file:
                # 有进度条显示
                # for data in tqdm(response.iter_content(chunk_size=chunk_size),unit_scale=True,ncols=80,total=int(content_size/1024)+1,desc="{} downloading......".format(fileName),unit="b"):
                # 无进度条显示
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)

        print(f"{fileName}下载完成")
