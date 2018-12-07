# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item
from scrapy.utils.project import get_project_settings


class BosszhipinItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = table = get_project_settings().get('BOT_NAME')
    role_description = Field()
