# -*- coding: utf-8 -*-

BOT_NAME = 'BossZhipin'

SPIDER_MODULES = ['BossZhipin.spiders']
NEWSPIDER_MODULE = 'BossZhipin.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3

SPIDER_MIDDLEWARES = {
   'BossZhipin.middlewares.BosszhipinSpiderMiddleware': 543,
}

DOWNLOADER_MIDDLEWARES = {
   'BossZhipin.middlewares.BosszhipinDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
   'BossZhipin.pipelines.BosszhipinPipeline': 300,
}

PROXY_URL = 'http://127.0.0.1:5555'
MONGO_URI = 'localhost'
MONGO_DB = 'BossZhipin'



