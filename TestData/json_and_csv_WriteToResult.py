import json
from files import JSON_FILE_PATH
from files import CSV_FILE_PATH
from csv import DictReader
import os


def get_path (path_ending):
    base_path = os.getcwd()
    full_path = os.path.join(base_path, path_ending)
    return full_path


def get_users():

    with open(JSON_FILE_PATH, 'r') as jfp:
        users = json.loads(jfp.read())
        data = []
        for user in users:
            data.append({
            "name": user["name"],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": []})


def get_books():

    with open(CSV_FILE_PATH, "r", newline='') as cfp:
        reader = DictReader(cfp)
        books = list(reader)
        result = [
            {
                'title': book['Title'],
                'author': book['Author'],
                'genre': book['Genre'],
                'pages': book['Pages']
            } for book in books
        ]
        return result


def add_books_for_users(users, books):
        index = 0
        users_count = len(users)

        for book in books:
            user = users[index]
            user['books'].append(book)
            index = (index + 1) % users_count

        return users

def write_json(users_with_books, path_ending):
    file_path = get_path(path_ending)
    with open(file_path, "w") as rj:
        json.dump(users_with_books, rj, indent=4)





