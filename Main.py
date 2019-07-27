import urllib.request
from Database import DatabaseJSONFile
from MyHTMLParsers import GameListHTMLParser

gameListUrl = 'https://www.oculus.com/experiences/quest/section/1888816384764129'
encoding = 'UTF-8'

parser = GameListHTMLParser(False)
contents = urllib.request.urlopen(gameListUrl).read().decode(encoding)
urls = parser.feed(contents)
print(urls)

database = DatabaseJSONFile("test.json", True)
print(database.get_url_list())
database.add_update_data('https://www.oculus.com/experiences/quest/1794123900713108/','New game', '10.99£', '3.61 GB', "...")
print(database.get_url_list())