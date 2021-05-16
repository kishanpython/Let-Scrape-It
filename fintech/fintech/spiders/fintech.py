
import scrapy
from urllib.parse import urljoin
from  ..items import FintechItem, ImageItem

class FinTech(scrapy.Spider):
    name = 'fintech'
    allowed_domains = ['australianfintech.com.au']
    start_urls = ['https://australianfintech.com.au/directory-all/']

    def parse(self, response):
        comp_url=response.css('.wpb_wrapper .row .item-thumbnail a::attr(href)').getall()
        cmp_url = comp_url
        for p in cmp_url:
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_info, meta={'url_items':p})

    # parse-info
    def parse_info(self, response):

        # Items-Instance
        items = FintechItem()

        # Image-Instance
        images = ImageItem()

        # sub-url-items
        sub_url = response.meta.get('url_items')

        # company-title-name
        comp_title_name = response.css('.project-title::text').extract_first()

        # company-image-downloader
        try:
            comp_image_url = response.css('div.content-image img::attr(src)').extract()[0]
            clean_img_url = [response.urljoin(comp_image_url)]
            images["image_urls"] = clean_img_url
            yield images

        except:
            comp_image_url = 'Not Found'

        # All-Details-Elements
        ele_meta_data = response.css('.project-meta-item')

        # company-found-date
        try:
            date_founded = ele_meta_data[1].css('div.item-meta-value::text').extract()
        except:
            date_founded = 'Not Found'  

        # company-description
        try:
            comp_des = response.css('div.single-post-content-text p::text').extract()
        except:
            comp_des = 'Not Found'

        # company-header-quarter data
        try:
            head_quarter = ele_meta_data[2].css('div.item-meta-value::text').extract()
        except:
            head_quarter = "Not Found" 

        # company_location_data
        try:
            location_data  = ele_meta_data[3].css('div.item-meta-value::text').extract() 
        except:
            location_data = 'Not Found'   

        # social-media-urls
        try:
            social_media_urls  = ele_meta_data.css('div.item-meta-value a').xpath('@href').extract()[1:]
        except:
            social_media_urls  = 'Not Found'

        # store data in the items
        items['sub_url'] = sub_url
        items['cmp_name'] = comp_title_name
        items['founded_date'] = date_founded
        items['comp_desc'] = comp_des
        items['head_quarter'] = head_quarter
        items['location_data'] = location_data
        items['social_media_urls'] = social_media_urls
        items['company_image_url'] = comp_image_url
        yield items