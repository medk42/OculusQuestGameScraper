from Database import DatabaseJSONFile, AddUpdateResult
from DataGetter import DataGetter
from joblib import Parallel, delayed


gameListUrl = 'https://www.oculus.com/experiences/quest/section/1888816384764129'
encoding = 'UTF-8'
database_file = 'test.json'


def get_data_parallelized(url):
    return DataGetter.get_game_data(url, encoding)


print('[INFO] Getting game URLs')
urls = DataGetter.get_game_urls(gameListUrl, encoding)
print('[INFO] Loading database')
database = DatabaseJSONFile(database_file, False)
print('[INFO] Getting all game data (might take a while!)')
games = Parallel(n_jobs=32)(delayed(get_data_parallelized)(url) for url in urls)
print('[INFO] Got all data, checking database')
for game in games:
    info = database.add_update_data(game.url, game.name, game.price, game.rating, game.description)
    if info == AddUpdateResult.ADDED:
        print('NEW GAME: ' + game.name + ' (price: ' + str(game.price) + ' rating: ' + str(game.rating) + ' url: ' + game.url + ')')
    elif info == AddUpdateResult.UPDATED:
        print ('CHECK GAME (price change?): ' + game.name + ' (price: ' + str(game.price) + ' rating: ' + str(game.rating) + ' url: ' + game.url + ')')
    elif info == AddUpdateResult.FAILED:
        print('[ERROR] Adding game ' + game.name + ' failed!')
