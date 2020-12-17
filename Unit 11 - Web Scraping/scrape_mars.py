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

    mars_data = {
                "nasa_title":nasa_title, 
                "nasa_article":nasa_article, 
                "featured_image_url":featured_image_url, 
                "mars_table":mars_table
                }

    # Close the browser
    browser.quit()

    return mars_data