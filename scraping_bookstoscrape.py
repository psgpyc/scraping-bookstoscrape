import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

# Function to extract details from each book article
def get_details(article):
  """
  This function parses a single book article from the HTML content and extracts details
  such as name, image source, price, rating, and product link.

  Args:
      article (BeautifulSoup object): A BeautifulSoup object representing a single book article.

  Returns:
      list: A list containing the extracted details of the book.
  """
  each_book = []
  base_url = "https://books.toscrape.com/catalogue/"
  name = article.find('img')['alt']
  img_source = f"https://books.toscrape.com/{article.find('img')['src']}"
  price = article.find('p', attrs={'class':'price_color'}).string[2:]
  rating = article.find('p', attrs={'class': 'star-rating'}).attrs['class'][-1]
  forwardurl = f"{base_url}{article.find('a')['href']}"
  each_book.append(name)
  each_book.append(img_source)
  each_book.append(price)
  each_book.append(rating)
  each_book.append(forwardurl)
  return each_book

# Main scraping loop
listOfBooks = []
for i in range(1,51):
  url = f"https://books.toscrape.com/catalogue/page-{i}.html"
  res = requests.get(url)
  res.encoding = 'UTF-8'

  if res.status_code == 200:
    content = res.text
    soup = BeautifulSoup(content, 'html.parser')
    ol = soup.body.find('ol', attrs={'class':'row'})
    article = ol.find_all('article')

    for eachVal in article:
      listOfBooks.append(get_details(eachVal))

  else:
    print(f"Error! Status Code: {res.status_code}")
    break

# Create pandas DataFrame from scraped data
df = pd.DataFrame(listOfBooks, columns=['Name', 'Link to Image', 'Price', 'Rating', 'Product Link'])
df

# Function to extract additional details from each book product page
def each_book_details(booklist):
  """
  This function takes a list of book product links and scrapes additional details from each product page.

  Args:
      booklist (list): A list containing product URLs for each book.

  Returns:
      list: A list of lists, where each inner list contains additional details for a corresponding book.
  """
  final_each_book_list = []

  for eachBookLink in booklist:
    book_details = []

    res = requests.get(url=eachBookLink)
    res.encoding = 'UTF-8'
    if res.status_code == 200:
      soup = BeautifulSoup(res.text, 'html.parser')
      article = soup.find('article', attrs={'class':'product_page'})
      if article.find('div', attrs={'id': 'product_description', 'class':'sub-header'}) is not None:
        desc = article.find('div', attrs={'id': 'product_description', 'class':'sub-header'}).find_next_sibling().get_text()
      else:
        desc = ''
      table_td = article.find_all('td')
      table_data = []
      for eachVal in table_td:
        table_data.append(eachVal.text)
      upc = table_data[0]
      product_type = table_data[1]
      reviews = table_data[-1]
      stock_count = re.findall(r"\d+", table_data[-2] )
      book_details.append(desc)
      book_details.append(upc)
      book_details.append(product_type)
      book_details.append(reviews)
      book_details.append(stock_count)

      final_each_book_list.append(book_details)


    else:
      return f"Error! Status Code{res.status_code}"
  return final_each_book_list

# Get additional details for each book
additional_details = each_book_details(df['Product Link'].to_list())

# Create a DataFrame from the additional details
dfx = pd.DataFrame(additional_details, columns=['Description', 'UPC', 'Product Type', 'Reviews', 'Stock Count'])
dfx

# Clean the 'Stock Count' column (assuming it's a list of strings with digits)
def get_stock_count(val):
  """
  This function extracts the actual stock count as an integer from the list of strings returned by the regex.

  Args:
      val (list): A list containing potentially multiple strings, where the first element should be the stock count.

  Returns:
      int: The extracted stock count as an integer.
  """
  return int(val[0])
dfx['Stock Count'] = dfx['Stock Count'].apply(get_stock_count)

dfx

# Combine the scraped data DataFrames
df = pd.concat([df,dfx], axis=1)

df

# Save the final DataFrame to a CSV file
df.to_csv('books_bookstoscrape.csv')

