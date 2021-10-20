import json


class CountriesIterator:

    def __init__(self):
        self.data = {}
        self.count = 0
        self.url = 'https://ru.wikipedia.org/wiki/'
        with open('countries.json', "r") as file:
            self.data = json.load(file)


    def __iter__(self):
        return self


    def __next__(self):
        if self.count < len(self.data):
            name = self.data[self.count]['translations']['rus']['common']
            link = name.replace(" ", "_")
            href = self.url + link
            with open("countries.txt", "a", encoding='UTF-8') as file:
                file.write(f"{name}, {href}\n")
            self.count += 1
            return name
        else:
            raise StopIteration


for item in CountriesIterator():
    print(item)



