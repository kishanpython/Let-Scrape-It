# Let-Scrape-It-with-Scrapy

This is a data scraping project to scrap the images and data from the Australia’s most comprehensive directory of FinTechs, have over 800 companies data. 

<p align="center" width="100%">
    <img width="45%" src="https://miro.medium.com/max/1100/0*hjn5ES8oTpqFYZ8W.png"> 

  
## The informations extracted are as follow:-
<ul>
  <li>Company Name</li>
  <li>Company Founder Data</li>
  <li>Company Description</li>
  <li>Company HeadQuarter</li>
  <li>Company Location</li>
  <li>Company Page Url</li>
  <li>Comapny Social Media Urls</li>
  <li>Company Image Url</li>
  <li>Company Image Data</li>
</ul>

## Sample Data 

Data stored in JSON format:- <a href="https://github.com/kishanpython/Let-Scrape-It/blob/main/fintech/items.json">Data Link</a>

```
{
"cmp_name": "BigFuture", 
"founder_data": ["Donald Hellyer, Michael Clancy & Chris Reay"], 
"comp_desc": [" Financial technology experts"], 
"head_quarter": ["Sydney, Australia"], 
"location_data": ["Australia"], 
"social_media_urls": ["https://linkedin.com/company/bigfuture-pty-ltd", "https://twitter.com/BigFuture14",    "https://facebook.com/aubigfuture","https://bigfuture.com.au/contact.html"], 
"sub_url": "https://australianfintech.com.au/company/bigfuture/",
"company_image_url": "https://australianfintech.com.au/wp-content/uploads/sites/7/2017/07/BigFuture-1.png"
}
```
## Image of all companies stored in the directory by the name of that particular company.
Link to Image data:- <a href="https://github.com/kishanpython/Let-Scrape-It/tree/main/fintech/images">Image Data</a>

## Tech :- 
<ul>
  <li>Python</li>
  <li>Scrapy</li>
</ul>  
