<!--
.. title: scrapy爬取boss官网北京爬虫岗位招聘列表
.. slug: scrapy-pa-qu-bossguan-wang-bei-jing-pa-chong-gang-wei-zhao-pin-lie-biao
.. date: 2019-01-03 06:35:05 UTC+08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

## 前言
 + 因为开始找工作了，用scrapy简单爬取以下boos官网的爬虫岗位招聘情况吧
###### 项目地址: https://github.com/ivuex/BossZhipinScrapy
###### 安装
```
git clone https://github.com/ivuex/BossZhipinScrapy.git
cd BossZhipinScrapy
mkvirtualenv boss_zhipin_scrapy
pip3 install scrapy pymongo requests
``` 
###### 配置
```
PROXY_URL = 'http://{}:{}'.format(your_proxies_api_host, your_proxies_api_port)
MONGO_URI = 'your_mongodb_host'
MONGO_DB = 'your_mongodb_port'
```
###### 运行
```
# 在根目录中
scrapy crawl boss
```