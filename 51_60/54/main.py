import ssl

# Set default context sử dụng trong HTTP requests
## _create_unverified_context: giúp bypass SSL verification (k khuyến khích)
ssl._create_default_https_context = ssl._create_unverified_context