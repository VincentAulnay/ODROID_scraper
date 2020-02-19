import urllib.request


#code = 'https://raw.githubusercontent.com/VincentAulnay/test_private/master/BB_FROMWEB.py?token=AubUEoiuCQqSlrT4C6RQRvSjk2q_hy8bks5cj6TSwA%3D%3D'
code = 'https://raw.githubusercontent.com/VincentAulnay/ODROID_scraper/master/print.py'
response = urllib.request.urlopen(code)
data = response.read()

exec(data)
