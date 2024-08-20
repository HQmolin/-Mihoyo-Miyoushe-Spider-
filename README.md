#米游社评论区爬虫 

该爬虫主要用于爬取米游社帖子下的评论 
所需包为requests lxml time re csv

目前支持爬取楼层id 用户id 评论内容（floor_id uid comment）
内容将被保存在同目录下的mihoyo_comment.csv中

目前可以自定义的内容为
n 爬取楼层数
first_floor 爬取起始楼层
order_type/is_hot 正序/倒序/热门
post_id 爬取的帖子编号
