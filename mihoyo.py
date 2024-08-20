# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:41:08 2024

@author: HQmolin
"""

import requests
from lxml import etree

import time
import re
import csv

#这里是将爬取到的文件保存到该文件目录中mihoyo_comment.csv 也可以使用其他保存方式
fp = open('./mihoyo_comment.csv','wt', newline='',encoding='utf-8')


writer = csv.writer(fp)
#此处为只爬取floor_id uid comment 可以参照下面网址进行进一步修改
writer.writerow(('floor_id','uid','comment'))

#这里可以将请求头换为自己的
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

#这里是防删楼的编号 可以和起始楼保持一致
#起始楼可以进行自定义(该处示例为1469000)
#爬取楼层数可自定义 但是由于删楼爬取数必然小于指定数目
n = 1000
first_floor = 1469000
floor = first_floor - 1

def get_info(url):
    global floor
    wb_data = requests.get(url,headers = headers)
    try:
        floor_id = re.findall('"floor_id":(.*?),',wb_data.text,re.S)[0]
        uid = re.findall('"uid":"(.*?)",',wb_data.text,re.S)[0]
        comment = re.findall('"content":"(.*?)",',wb_data.text,re.S)[0]
        if floor != floor_id:
            writer.writerow((floor_id,uid,comment))
            print(floor_id)
            floor = floor_id
    except IndexError:
        pass
#此网址可以自定义 具体为最热/最早/最晚评论 最终楼层自定义在上面的first_floor 具体帖子也可以自定义（该处为最热的4.8版本活动帖）size固定为1 受前面代码限制
if __name__ == '__main__':
    urls=['https://bbs-api.miyoushe.com/post/wapi/getPostReplies?gids=2&is_hot=false&last_id={}&order_type=2&post_id=55221094&size=1'.format(str(first_floor-i)) for i in range(1,n)]
    for url in urls:
        get_info(url)
    fp.close()