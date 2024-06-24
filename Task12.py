import re
from urllib.parse import urlparse

def get_url_from_user():
    """ Function to get a single URL from user input """
    url = input("Enter a URL: ")
    return url

def is_phishing(url):
    """ Function to determine if a URL is potentially a phishing link """
    # Example: Check if domain is in a suspicious list (you should maintain this list)
    suspicious_domains = ['example-phishing-domain.com', 'another-phishing-domain.org']
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    if domain in suspicious_domains:
        return True
    
    # Example: Check if URL uses HTTP instead of HTTPS
    if parsed_url.scheme.lower() == 'http':
        return True
    
    # Example: Check for URL shorteners
    if 'bit.ly' in domain or 'shorturl.at' in domain:
        return True
    
    # You can add more checks based on your knowledge of phishing characteristics
    
    return False

if __name__ == "__main__":
    user_url = get_url_from_user()
    if is_phishing(user_url):
        print(f"Phishing link detected: {user_url}")
    else:
        print(f"{user_url} is not a phishing link.")