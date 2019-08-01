class GameData:
    def __init__(self, url, name, price, rating, description):
        self.url = url
        self.name = name
        self.price = price
        self.rating = rating
        self.description = description

    def __str__(self) -> str:
        return 'URL: ' + self.url + ' Name: ' + self.name + ' Price: ' + str(self.price) + ' Rating: ' + \
               str(self.rating) + ' Description: ' + self.description
