from MyHTMLParsers import GameListHTMLParser, GamePageHTMLParser
import urllib.request


class DataGetter:
    @staticmethod
    def get_game_urls(game_list_url, html_encoding):
        parser = GameListHTMLParser(False)
        contents = urllib.request.urlopen(game_list_url).read().decode(html_encoding)
        urls = parser.feed(contents)
        return urls

    @staticmethod
    def get_game_data(game_url, html_encoding):
        parser = GamePageHTMLParser(False, game_url)
        contents = urllib.request.urlopen(game_url).read().decode(html_encoding)
        game_data = parser.feed(contents)
        return game_data
