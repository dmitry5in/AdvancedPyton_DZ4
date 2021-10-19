import hashlib


def get_hash(name_file):
    with open(name_file, 'r', encoding='UTF-8') as file:
        for line in file:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


for i in get_hash('countries.txt'):
    print(i)
