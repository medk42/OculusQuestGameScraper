from Database import DatabaseJSONFile
from DataGetter import DataGetter


gameListUrl = 'https://www.oculus.com/experiences/quest/section/1888816384764129'
encoding = 'UTF-8'
database_file = 'test.json'

print(DataGetter.get_game_urls(gameListUrl, encoding))
database = DatabaseJSONFile(database_file, False)
print(DataGetter.get_game_data('https://www.oculus.com/experiences/quest/1794123900713107/', encoding))
