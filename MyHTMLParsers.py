from html.parser import HTMLParser
import json


class GameListHTMLParser(HTMLParser):
    def __init__(self, verbose):
        self.reading = False
        self.verbose = verbose
        self.returnElements = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            if len(attrs) == 1 and attrs[0][0] == 'type' and attrs[0][1] == 'application/ld+json':
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
        super().feed(contents)
        return self.returnElements

    def error(self, message):
        if self.verbose:
            print('Error:', message)
