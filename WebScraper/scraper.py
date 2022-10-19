from turtle import title
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/aphrodite'

page = urlopen(url)
print(page)

# extracting HTML from the page using HTTPResponse objects .read() method
html_bytes = page.read()

# decode the sequence of bytes to string using utf-8
html = html_bytes.decode('utf-8')

# print the HTML to see the contents of the web page
print(html)


# Extracting text from HTML with String Methods
title_index = html.find('<title>')
print(title_index)

start_index = title_index + len('<title>')
print(start_index)

end_index = html.find('</title>')
print(end_index)

title = html[start_index:end_index]
print(title)

#########################

url = 'http://olympus.realpython.org/profiles/poseidon'
page = urlopen(url)
