from html.parser import HTMLParser
from GameData import GameData
import json


class GameListHTMLParser(HTMLParser):
    def __init__(self, verbose):
        self.reading = False
        self.verbose = verbose
        self.returnElements = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            if len(attrs) == 2 and attrs[0][0] == 'type' and attrs[0][1] == 'application/ld+json':
                if self.verbose:
                    print("Start reading:", tag)
                self.reading = True

    def handle_data(self, data):
        if self.reading:
            self.decode_json(data)

    def handle_endtag(self, tag):
        if tag == 'script' and self.reading:
            self.reading = False
            if self.verbose:
                print('Stop reading:', tag)

    def decode_json(self, text):
        item_list_elements = json.loads(text)['itemListElement']
        for element in item_list_elements:
            self.returnElements.append(element['url'])

    def feed(self, contents):
        """
        :param contents: HTML file
        :return: List of available game URLs
        """
        super().feed(contents)
        return self.returnElements

    def error(self, message):
        if self.verbose:
            print('Error:', message)


class GamePageHTMLParser(GameListHTMLParser):
    def __init__(self, verbose, game_url):
        self.game_url = game_url
        super().__init__(verbose)

    def handle_data(self, data):
        if self.reading:
            self.decode_json(data)

    def decode_json(self, text):
        data = json.loads(text)
        name = data['name']
        description = data['description']
        price = data['offers']['price']
        rating = data['aggregateRating']['ratingValue']
        url = self.game_url
        self.returnElements = GameData(url, name, price, rating, description)

    def feed(self, contents):
        """
        :param contents: HTML file
        :return: GameData object containing data parsed from a given HTML
        """
        super().feed(contents)
        return self.returnElements
