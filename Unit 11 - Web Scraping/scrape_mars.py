# Import Dependencies

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from sqlalchemy import create_engine
import psycopg2
from splinter import Browser
from selenium import webdriver


def init_browser():
    executable_path = {"executable_path": "C:/Users/Heather/Desktop/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
   
    # NASA Mars News

    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)
    
    news_html = browser.html
    news_soup = bs(news_html,'lxml')

    nasa_title = news_soup.find('div', class_='bottom_gradient').text
    nasa_article = news_soup.find('div', class_='article_teaser_body').text
    
    # JPL Mars Space Images

    jpl_url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    jpl_html = browser.html
    jpl_soup = bs(jpl_html,'lxml')

    url = jpl_soup.find('div',class_='carousel_container').article.footer.a['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov'+ url

    # Mars Facts

    mars_facts_df = pd.read_html('https://space-facts.com/mars/')[0]
    mars_facts_df.columns=['Description', 'Mars']
    mars_facts_df.set_index('Description', inplace=True)

    mars_table = mars_facts_df.to_html()

    # Hemispheres

    hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)  

    hem_html = browser.html
    hem_soup = bs(hem_html,"html.parser")

    results = hem_soup.find_all("div",class_='item')

    image_urls = []
    for result in results:
            product_dict = {}
            titles = result.find('h3').text
            end_link = result.find("a")["href"]
            image_link = "https://astrogeology.usgs.gov/" + end_link    
            browser.visit(image_link)
            html = browser.html
            soup= bs(html, "html.parser")
            downloads = soup.find("div", class_="downloads")
            image_url = downloads.find("a")["href"]
            product_dict['title']= titles
            product_dict['image_url']= image_url
            image_urls.append(product_dict)

    # Add output data into dictionary

    mars_data = {
                "nasa_title":nasa_title, 
                "nasa_article":nasa_article, 
                "featured_image_url":featured_image_url, 
                "mars_table":mars_table, 
                "image_urls":image_urls, 
                
                }
    

    # Close the browser
    browser.quit()

    return mars_data