from urllib.parse import urlparse, parse_qs
url = "https://www.google.com/search?q=котики&uact=5"
parsed_url = urlparse(url)
pq = parse_qs(parsed_url.query)