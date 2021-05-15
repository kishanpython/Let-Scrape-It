
import scrapy
from urllib.parse import urljoin
from  ..items import FintechItem, ImageItems

class FinTech(scrapy.Spider):
    name = 'fintech'
    allowed_domains = ['australianfintech.com.au']
    start_urls = ['https://australianfintech.com.au/directory-all/']


    def parse(self, response):
        comp_url=response.css('.wpb_wrapper .row .item-thumbnail a::attr(href)').getall()
        cmp_url = comp_url[:5]
        for p in cmp_url:
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_info, meta={'url_items':p})

    def parse_info(self, response):

        items = FintechItem()
        sub_url = response.meta.get('url_items')
        # company_title
        comp_title_name = response.css('.project-title::text').extract_first()

        # company_image_url
        try:
            comp_image_url = response.css('div.content-image img::attr(src)').extract()[0]
        except:
            comp_image_url = 'Not Found'

        # All Details elements
        ele_meta_data = response.css('.project-meta-item')

        try:
            date_founded = ele_meta_data[1].css('div.item-meta-value::text').extract()
        except:
            date_founded = 'Not Found'  

        try:
            comp_des = response.css('div.single-post-content-text p::text').extract()
        except:
            comp_des = 'Not Found'

        try:
            head_quarter = ele_meta_data[2].css('div.item-meta-value::text').extract()
        except:
            head_quarter = "Not Found" 

        try:
            location_data  = ele_meta_data[3].css('div.item-meta-value::text').extract() 
        except:
            location_data = 'Not Found'   

        try:
            social_media_urls  = ele_meta_data.css('div.item-meta-value a').xpath('@href').extract()[1:]
        except:
            social_media_urls  = 'Not Found'

        items['sub_url'] = sub_url
        items['cmp_name'] = comp_title_name
        items['founded_date'] = date_founded
        items['comp_desc'] = comp_des
        items['head_quarter'] = head_quarter
        items['location_data'] = location_data
        items['social_media_urls'] = social_media_urls
        items['company_image_url'] = comp_image_url

        yield items