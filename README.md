# 米游社评论区爬虫 

该爬虫主要用于爬取米游社帖子下的评论 

所需包为requests lxml time re csv

目前支持爬取楼层id 用户id 评论内容（floor_id uid comment）

内容将被保存在同目录下的mihoyo_comment.csv中

## 目前可以自定义的内容为

n 爬取楼层数

first_floor 爬取起始楼层

order_type/is_hot 正序/倒序/热门

（order_type==1时为从最早评论开始，反之则为从最新评论开始）

post_id 爬取的帖子编号

gids 对应的游戏社区

(原神为2 崩坏星穹铁道为6 绝区零为8)

## 若打开mihoyo_comment.csv为乱码 

可新建一个csv 

在数据栏目中导入mihoyo_comment.csv并保存 

则能够正常使用
