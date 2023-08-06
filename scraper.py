import json
import re
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Function to scrape text contents from HTML
def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()  # Extract text from HTML

    # Remove any remaining HTML tags and extra whitespaces
    cleaned_text = re.sub(r'<.*?>', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text

