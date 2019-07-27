import json
from enum import Enum

URL = 'url'
NAME = 'name'
PRICE = 'price'
SIZE = 'size'
DESCRIPTION = 'description'

class DatabaseJSONFile:
    def __init__(self, file, verbose):
        self.verbose = verbose
        self.file = file

        f = open(self.file, 'a') # add if file empty/doesn't exist, add {}
        f.close()

        if self.verbose:
            print('Database initialized')

    def get_url_list(self):
        f = open(self.file, 'r')
        data = json.loads(f.read())
        f.close()
        ret_list = []
        for key in data:
            ret_list.append(data[key][URL])
        return ret_list

    def add_update_data(self, url, name, price, size, description):
        f = open(self.file, 'r')
        data = json.loads(f.read())
        f.close()
        if url not in data:
            data[url] = {URL: url, NAME: name, PRICE: price, SIZE: size, DESCRIPTION: description}
            result = AddUpdateResult.ADDED
        else:
            result = self.update(url, name, price, size, description, data)
            result = AddUpdateResult.UPDATED if result else AddUpdateResult.NOT_UPDATED
        f = open(self.file, 'w')
        f.write(json.dumps(data))
        f.close()
        return result

    def update(self, url, name, price, size, description, data):
        changed = False
        if name:
            if data[url][NAME] != name:
                data[url][NAME] = name
                changed = True
        if price:
            if data[url][PRICE] != price:
                data[url][PRICE]= price
                changed = True
        if size:
            if data[url][SIZE] != size:
                data[url][SIZE] = size
                changed = True
        if description:
            if data[url][DESCRIPTION] != description:
                data[url][DESCRIPTION] = description
                changed = True
        return changed


class AddUpdateResult(Enum):
    ADDED = 1
    UPDATED = 2
    NOT_UPDATED = 3

