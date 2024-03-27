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

**Comprehensive Data Extraction:** Gathers a wide range of informative book data points. <br>
**Efficient Page Iteration:** Scrapes data from multiple website pages to collect information from a broader selection. <br>
**Structured DataFrame Creation:** Organizes the scraped data in a well-formatted pandas DataFrame for ease of analysis and manipulation. <br>
**CSV Export:** Saves the final dataset to a CSV file for convenient access and sharing. <br>
**Clear Error Handling:** Includes mechanisms to gracefully handle potential scraping errors encountered during data collection.<br>
<br><br>

## Benefits:

**Time Savings:** Automates the data collection process, eliminating the need for manual scraping. <br>
**Organized Data:** Provides well-structured book data for further analysis or building applications. <br>
**Ease of Use:** Simple setup and execution with clear instructions. <br>

## Getting Started

1. **Install Dependencies:** <br>
`Bash <br>
pip install requests beautifulsoup4 pandas re`
2. **Clone the Repository:** <br>
`Bash <br>
git clone https://github.com/<your-username>/book-scraper.git`
3. **Run the Script:** <br>
`Bash <br>
python book_scraper.py  # Replace with your script name if different`
<br>

This will create a CSV file named `books_bookstoscrape.csv` containing the scraped data.
<br>
## Code Structure
<br>
The book_scraper.py script is the heart of this project. It handles the following processes:
<br>
Initialization: Imports necessary libraries and defines functions. <br>
Main Scraping Loop: Iterates through product pages on the website.<br>
Fetches the HTML content of each page using requests.<br>
Parses the HTML content with BeautifulSoup.<br>
Extracts book details from each product listing using relevant tags and attributes.<br>
Handles potential errors during scraping.<br>
Additional Details Retrieval: For each book, retrieves its product page to extract additional information like description, UPC, product type, reviews, and stock count.<br>
Data Processing: Cleans the stock count data to extract the actual integer value.<br>
DataFrame Creation: Creates two DataFrames:<br>
One for initial scraped details (name, image URL, price, rating).<br>
Another for additional details retrieved from product pages (description, UPC, product type, reviews, stock count).<br>
DataFrame Concatenation: Merges the two DataFrames into a single comprehensive DataFrame.<br>
CSV Export: Saves the final DataFrame as a CSV file named books_bookstoscrape.csv.<br>

## Additional Notes:
<br>
1. Feel free to modify the script to customize the scraping behavior or data extraction logic as needed.<br>
2. Remember to be respectful of the website's terms of use when scraping data.
