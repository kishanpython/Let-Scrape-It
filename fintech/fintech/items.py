# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FintechItem(scrapy.Item):
    # define the fields for your item here like:
    cmp_name = scrapy.Field()
    founded_date = scrapy.Field()
    comp_desc = scrapy.Field()
    head_quarter = scrapy.Field()
    location_data = scrapy.Field()
    social_media_urls = scrapy.Field()
    company_image_url = scrapy.Field()
    sub_url = scrapy.Field()


class ImageItems(scrapy.Item):
	image_urls = scrapy.Field()
    images = scrapy.Field()