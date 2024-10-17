import requests
import socket
import uuid
import datetime
import time

# List of common websites to test connectivity
websites = [
    "http://www.google.com",
    "http://www.facebook.com",
    "http://www.amazon.com",
    "http://www.youtube.com",
    "http://www.reddit.com",
    "http://www.wikipedia.org",
    "http://www.twitter.com",
    "http://www.netflix.com",
    "http://www.microsoft.com",
    "http://www.apple.com"
]

# Function to get the MAC address of the wireless access point (works on Linux/macOS)
def get_mac_address():
    try:
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 8)][::-1])
        return mac_address
    except Exception as e:
        return f"Error retrieving MAC address: {e}"

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address

# Function to log the error when connection fails
def log_failure(website, log_file="network_log.txt"):
    with open(log_file, 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mac_address = get_mac_address()
        ip_address = get_local_ip()
        file.write(f"{timestamp}, Website: {website}, MAC: {mac_address}, IP: {ip_address}\n")

# Function to attempt connection to a website
def test_website(website):
    try:
        response = requests.get(website, timeout=5)
        if response.status_code == 200:
            print(f"Connection successful to {website}")
    except requests.RequestException:
        print(f"Connection failed to {website}. Logging...")
        log_failure(website)

# Main function to test all websites and repeat every 2 minutes
def main():
    while True:
        for website in websites:
            test_website(website)
        print("Waiting for 2 minutes before next check...")
        time.sleep(120)  # Wait for 120 seconds (2 minutes)

if __name__ == "__main__":
    main()
