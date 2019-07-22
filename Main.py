import urllib.request
from MyHTMLParsers import GameListHTMLParser

gameListUrl = 'https://www.oculus.com/experiences/quest/section/1888816384764129'
encoding = 'UTF-8'

parser = GameListHTMLParser(False)
contents = urllib.request.urlopen(gameListUrl).read().decode(encoding)
urls = parser.feed(contents)
print(urls)
