# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline

class CustomImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
    	# EX:- https://australianfintech.com.au/wp-content/uploads/sites/7/2020/08/Adatree-2021.png
    	# output :- Adatree-2021.png
    	# Image name extraction from url
        image_name = request.url.split('/')[-1]
        # Creating image directory from url name
        # output :- Adatree-2021
        image_dir_for_stg = request.url.split('/')[-1].split('.')[0]
        return f'{image_dir_for_stg}/{image_name}'