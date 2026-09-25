# module1: data pipeline
this module contain the zepto-capstone data pipeline

#work included 
-scrapping book data using             
requests and beautifulsoup
- cleaning and converting the scraped data
- converting GBP prices to INR using the required fixed rate
- storing the cleaned data in a normalized SGLite database
- running SQL queries on the database
- comparing SQL results with pandas dataframes
- 
- Workflow:
  
Web Scraping
     ↓
Data Cleaning
     ↓
GBP → INR Conversion
     ↓
SQLite Database
     ↓
SQL Queries
     ↓
Pandas Validation
- ## Data source
- books.tosrape.com
##Currency conversion
1 GBP = 105.50 INR
  Database Schema
categories
-----------
category_id (PK)
category_name

books
-----------
book_id (PK)
title
price_gbp
price_inr
rating
in_stock
category_id (FK)
Run
pip install -r requirements.txt
python scrape_and_load.py
python queries.py
Files
scrape_and_load.py – Scraping, cleaning and database creation
queries.py – SQL queries and Pandas validation
zepto_books.db – SQLite database
requirements.txt – Python dependencies
