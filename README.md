# Book Scraper: Extract Book Data from "Books to Scrape"

This Python script automates the process of scraping book data from the "Books to Scrape" website (https://books.toscrape.com/). It efficiently extracts valuable information about various books, including:

1. Product Name
2. Image URL
3. Price
4. Rating
5. Description (from product page)
6. UPC Code (from product page)
7. Product Type (from product page)
8. Reviews (from product page)
9. Stock Count (from product page, cleaned to extract the actual integer value)

## Key Features:

**Comprehensive Data Extraction:** Gathers a wide range of informative book data points.
**Efficient Page Iteration:** Scrapes data from multiple website pages to collect information from a broader selection.
**Structured DataFrame Creation:** Organizes the scraped data in a well-formatted pandas DataFrame for ease of analysis and manipulation.
**CSV Export:** Saves the final dataset to a CSV file for convenient access and sharing.
**Clear Error Handling:** Includes mechanisms to gracefully handle potential scraping errors encountered during data collection.

## Benefits:

**Time Savings:** Automates the data collection process, eliminating the need for manual scraping.
**Organized Data:** Provides well-structured book data for further analysis or building applications.
**Ease of Use:** Simple setup and execution with clear instructions.

## Getting Started

1. **Install Dependencies:**
`Bash
pip install requests beautifulsoup4 pandas re`
2. **Clone the Repository:**
`Bash
git clone https://github.com/<your-username>/book-scraper.git`
3. **Run the Script:**
`Bash
python book_scraper.py  # Replace with your script name if different`


This will create a CSV file named `books_bookstoscrape.csv` containing the scraped data.

## Code Structure

The book_scraper.py script is the heart of this project. It handles the following processes:

Initialization: Imports necessary libraries and defines functions.
Main Scraping Loop: Iterates through product pages on the website.
Fetches the HTML content of each page using requests.
Parses the HTML content with BeautifulSoup.
Extracts book details from each product listing using relevant tags and attributes.
Handles potential errors during scraping.
Additional Details Retrieval: For each book, retrieves its product page to extract additional information like description, UPC, product type, reviews, and stock count.
Data Processing: Cleans the stock count data to extract the actual integer value.
DataFrame Creation: Creates two DataFrames:
One for initial scraped details (name, image URL, price, rating).
Another for additional details retrieved from product pages (description, UPC, product type, reviews, stock count).
DataFrame Concatenation: Merges the two DataFrames into a single comprehensive DataFrame.
CSV Export: Saves the final DataFrame as a CSV file named books_bookstoscrape.csv.

## Additional Notes:

1. Feel free to modify the script to customize the scraping behavior or data extraction logic as needed.
2. Remember to be respectful of the website's terms of use when scraping data.
