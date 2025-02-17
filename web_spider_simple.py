import requests  # Library for making HTTP requests
from bs4 import BeautifulSoup  # Library for parsing HTML

def get_hrefs(url):
    """
    Fetches all href links from a given URL.
    
    Args:
        url (str): The target webpage URL to scrape links from.
        
    Returns:
        list: A list of href links found on the page.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url, timeout=10)
        
        # Raise an exception if the request was not successful
        response.raise_for_status()
        
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all anchor (<a>) tags
        anchor_tags = soup.find_all('a')
        
        # Extract href attributes from anchor tags and filter out None values
        hrefs = [a.get('href') for a in anchor_tags if a.get('href') is not None]
        
        return hrefs
    
    except requests.exceptions.RequestException as e:
        # Handle HTTP and network errors
        print(f"Error fetching URL {url}: {e}")
        return []

if __name__ == "__main__":
    # Example usage: specify the target URL
    target_url = "https://www.nyt.com"
    
    # Fetch hrefs from the webpage
    links = get_hrefs(target_url)
    
    # Print the extracted links
    for link in links:
        print(link)
