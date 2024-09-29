import json
from csv import DictReader
from homework_3_files import JSON_FILE_PATH
from homework_3_files import CSV_FILE_PATH


def result():
    with open(JSON_FILE_PATH, 'r') as jfp:
        users = json.loads(jfp.read())
        user_mas = []
        for i in range(len(users)):
            user = {
                "name": users[i]["name"],
                "gender": users[i]["gender"],
                "address": users[i]["address"],
                "age": users[i]["age"],
                "books": [],
            }
            user_mas.append(user)
            del user

    with open(CSV_FILE_PATH, 'r') as cfp:
        reader = DictReader(cfp)
        book_mas = []
        for row in reader:
            book_mas.append(row)
        books = []
        for i in range(len(book_mas)):
            book = {
                "title": book_mas[i]["Title"],
                "author": book_mas[i]["Author"],
                "pages": book_mas[i]["Pages"],
                "genre": book_mas[i]["Genre"],
            }
            books.append(book)
            del book

        i, j = 0, 0
        while i < len(books):
            if j < len(user_mas):
                user_mas[j]["books"].append(books[i])
                j += 1
            else:
                j = 0
            i += 1

    with open("result.json", "w") as result_final:
        result_final.write(json.dumps(user_mas, indent=4))

result()





