# ==========================================================
# DATA SCIENCE - PROGRAM 8
# TOPIC: WEB SCRAPING USING BEAUTIFUL SOUP
# ==========================================================

# ----------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES
# ----------------------------------------------------------

# requests library is used to send HTTP requests
# and download the web page content.
import requests

# BeautifulSoup is used to parse HTML/XML documents
# and extract useful information from web pages.
from bs4 import BeautifulSoup


# ----------------------------------------------------------
# STEP 2: DEFINE REQUEST HEADERS
# ----------------------------------------------------------

# Many websites block requests coming from bots.
# To make our request look like it is coming from
# a real browser, we provide a User-Agent header.
#
# User-Agent identifies the browser and operating system.
headers = {
    "User-Agent": "Mozilla/5.0"
}


# ----------------------------------------------------------
# STEP 3: DEFINE THE TARGET URL
# ----------------------------------------------------------

# Amazon review page URL.
# This page contains customer reviews for a product.
url = "https://www.amazon.in/product-reviews/B09G9BL5CP/"


# ----------------------------------------------------------
# STEP 4: SEND HTTP GET REQUEST
# ----------------------------------------------------------

# Send a GET request to the website.
# The server returns the HTML source code.
r = requests.get(url, headers=headers)


# ----------------------------------------------------------
# STEP 5: CHECK REQUEST STATUS
# ----------------------------------------------------------

# Print the HTTP status code.
# 200 = Success
# 404 = Not Found
# 500 = Server Error
print("Status Code:", r.status_code)


# ----------------------------------------------------------
# STEP 6: PARSE HTML USING BEAUTIFULSOUP
# ----------------------------------------------------------

# Convert downloaded HTML content into a BeautifulSoup object.
# html.parser is Python's built-in HTML parser.
soup = BeautifulSoup(r.content, 'html.parser')


# ----------------------------------------------------------
# STEP 7: FIND ALL REVIEW SECTIONS
# ----------------------------------------------------------

# Amazon stores review text inside span tags
# with the attribute:
# data-hook="review-body"
#
# find_all() returns a list of matching elements.
reviews = soup.find_all(
    'span',
    {'data-hook': 'review-body'}
)


# ----------------------------------------------------------
# STEP 8: DISPLAY NUMBER OF REVIEWS FOUND
# ----------------------------------------------------------

# Print total reviews found on the page.
print("Number of Reviews Found:", len(reviews))


# ----------------------------------------------------------
# STEP 9: PRINT FIRST FIVE REVIEWS
# ----------------------------------------------------------

# reviews[:5] selects the first 5 reviews.
for review in reviews[:5]:

    # Extract only the review text.
    # strip() removes extra spaces and new lines.
    review_text = review.text.strip()

    # Print review text.
    print("\nReview:")
    print(review_text)


# ----------------------------------------------------------
# PROGRAM COMPLETED
# ----------------------------------------------------------

print("\nScraping Completed Successfully")