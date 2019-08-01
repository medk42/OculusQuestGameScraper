import json
from enum import Enum
from json import JSONDecodeError

URL = 'url'
NAME = 'name'
PRICE = 'price'
SIZE = 'size'
DESCRIPTION = 'description'

class DatabaseJSONFile:
    def __init__(self, file, verbose):
        self.verbose = verbose
        self.file = file
        self.data = {}

        if self.verbose:
            print('Database initialized')

    def get_url_list(self):
        if not self.read_file():
            return AddUpdateResult.FAILED
        ret_list = []
        for key in self.data:
            ret_list.append(self.data[key][URL])
        return ret_list

    def add_update_data(self, url, name, price, size, description):
        if not self.read_file():
            return AddUpdateResult.FAILED
        if url not in self.data:
            self.data[url] = {URL: url, NAME: name, PRICE: price, SIZE: size, DESCRIPTION: description}
            if not self.write_file():
                return AddUpdateResult.FAILED
            result = AddUpdateResult.ADDED
        else:
            result = self.update(url, name, price, size, description)
        return result

    def update(self, url, name, price, size, description):
        if not self.read_file():
            return AddUpdateResult.FAILED
        result = AddUpdateResult.NOT_UPDATED
        if url in self.data:
            if name:
                if self.data[url][NAME] != name:
                    self.data[url][NAME] = name
                    result = AddUpdateResult.UPDATED
            if price:
                if self.data[url][PRICE] != price:
                    self.data[url][PRICE] = price
                    result = AddUpdateResult.UPDATED
            if size:
                if self.data[url][SIZE] != size:
                    self.data[url][SIZE] = size
                    result = AddUpdateResult.UPDATED
            if description:
                if self.data[url][DESCRIPTION] != description:
                    self.data[url][DESCRIPTION] = description
                    result = AddUpdateResult.UPDATED
        if not self.write_file():
            return AddUpdateResult.FAILED
        return result

    def read_file(self):
        try:
            f = open(self.file, 'r')
        except OSError:
            if self.verbose:
                print('Database file', self.file, 'failed to open!')
            return False
        try:
            self.data = json.loads(f.read())
        except JSONDecodeError:
            if self.verbose:
                print('Database file', self.file, 'is not a valid JSON document.')
            return False
        f.close()
        return True

    def write_file(self):
        try:
            f = open(self.file, 'w')
        except OSError:
            if self.verbose:
                print('Database file', self.file, 'failed to open!')
            return False
        f.write(json.dumps(self.data))
        f.close()
        return True

    def drop(self):
        self.data = {}
        self.write_file()



class AddUpdateResult(Enum):
    ADDED = 1
    UPDATED = 2
    NOT_UPDATED = 3
    FAILED = 4

