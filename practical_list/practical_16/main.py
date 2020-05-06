import urllib.request, re

url = input('Enter an url: ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http://.*?)"', html)
print('\nLinks on given url:\n')
print([link for link in links])