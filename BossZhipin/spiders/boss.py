# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from BossZhipin.items import BosszhipinItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from BossZhipin.loaders import BossZhipinLoader
import re
from time import sleep


class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com']
    # start_urls = ['https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page='+str(page)+'&ka=page-'+str(page) for page in list(range(1,11)) ]
    start_urls = ['https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page='+str(page)+'&ka=page-'+str(page) for page in range(1,11) ]
    rules = (
        Rule(LinkExtractor(allow="/c101010100/\?query=[^&]+&page=\d+&ka=page-\d+", restrict_xpaths ='//div[@class="info-primary"]/h3[@class="name"]/a'), callback='parse_item'),
        Rule(LinkExtractor(allow="/c101010100/\?query=[^&]+&page=\d+&ka=page-\d+", restrict_xpaths ="//div[@class='page']/a[@class='next']")),
    )

    def start_requests(self):
        for start_url in self.start_urls:
            yield Request(start_url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        if not re.search('\?query=', response.url):
            item = BosszhipinItem()
            item['role_description'] = response.xpath('//div[@class="detail-content"]/div[1]//text()').extract()
            yield item
            # loader = BossZhipinLoader(item=BosszhipinItem(), response=response)
            # # loader.add_xpath('role_description', '//div[@class="detail-content"]/div[1]//text()')
            # loader.add_xpath('role_description', '//body//text()')
            # yield loader.load_item()
