import socket
# Sample data (IP to URL mapping)
ip_url_mapping = {
 '192.0.2.1': 'www.example.com',
 '192.0.2.2': 'www.openai.com',
 '192.0.2.3': 'www.google.com',
 '192.0.2.4': 'www.github.com'
}
# Function for IP to URL lookup
def ip_to_url(ip):
 return ip_url_mapping.get(ip, 'No URL found for this IP.')
# Function for URL to IP lookup
def url_to_ip(url):
 for ip, u in ip_url_mapping.items():
 if u == url:
 return ip
 return 'No IP found for this URL.'
# Sample usage
while True:
 user_input = input("Enter an IP address or URL (type 'exit' to quit): ")
 if user_input.lower() == 'exit':
 break
if user_input.replace('.', '').isdigit():
 ip_address = user_input
 print(f"URL for {ip_address} is {ip_to_url(ip_address)}")
 else:
 url = user_input
 print(f"IP for {url} is {url_to_ip(url)}")