# -*- coding: utf-8 -*-
import re
from BossZhipin.items import BosszhipinItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from time import sleep

class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=%E7%88%AC%E8%99%AB&page='+str(page)+'&ka=page-'+str(page) for page in list(range(1,11)) ]
    rules = (
        Rule(LinkExtractor(allow="/c101010100/\?query=[^&]+&page=\d+&ka=page-\d+", restrict_xpaths ='//div[@class="info-primary"]/h3[@class="name"]/a'), callback='parse_item'),
        Rule(LinkExtractor(allow="/c101010100/\?query=[^&]+&page=\d+&ka=page-\d+", restrict_xpaths ="//div[@class='page']/a[@class='next']")),
    )

    def parse_item(self, response):
        if not re.search('\?query=', response.url):
            item = BosszhipinItem()
            company_name = response.xpath('/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[5]/div[1]//text()')
            item['company_name'] = company_name and company_name.extract_first() or ''
            publish_time = response.xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]//text()')
            item['publish_time'] = publish_time and publish_time.extract_first()[:3] or ''
            position_tags = response.xpath('/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/span//text()')
            item['position_tags'] = position_tags and position_tags.extract() or []
            working_location = response.xpath('//div[@class="location-address"]//text()')
            item['working_location'] = working_location and working_location.extract_first() or ''
            role_descriptions = response.xpath('//div[@class="detail-content"]/div[1]//text()')
            item['role_description'] =  role_descriptions and '\n'.join([item for item in role_descriptions.extract() if item.strip()]) or ''
            yield item
