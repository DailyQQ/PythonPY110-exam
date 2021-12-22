import random
from faker import Faker
import json
import os


def model_():
    from conf import MODEL
    return MODEL


def count_in_pk_():
    counter = 1
    while True:
        yield counter
        counter += 1


pk_ = count_in_pk_()


def title_():
    def all_books():
        # import books from books
        books_ = {
            "Текстовая Книга №1": [1, 2, 3, 4, 5],
            "Текстовая Книга №2": [1, 2, 3, 4, 5],
            "Текстовая Книга №3": [1, 2, 3, 4, 5],
            "Текстовая Книга №4": [1, 2, 3, 4, 5],
            "Текстовая Книга №5": [1, 2, 3, 4, 5]
        }
        return random.choice([i for i in books_ for x in books_[i]])

    random_times = random.randint(1, 5)
    for i in range(random_times):
        all_books()
    return all_books()


def years_():
    years = random.randint(0, 2022)
    return years


def pages_():
    pages = random.randint(0, 999)
    return pages


def isbn13_():
    fake = Faker()
    Faker.seed(0)
    for _ in range(random.randint(1, 100)):
        isbn13 = fake.isbn13()
    yield isbn13


def rating_():
    rating = random.uniform(0, 5)
    return rating


def price_():
    price = random.randint(0, 9999)
    return price


def authors_():
    authors_list = []
    fake = Faker()
    Faker.seed(0)
    for _ in range(random.randint(1, 3)):
        authors_list.append(fake.name())
    yield authors_list


def func_():
    a = {
        'model': model_(),
        'pk': next(pk_),
        'fields': {
            'title': title_(),
            'year': years_(),
            'pages': pages_(),
            'isbn13': next(isbn13_()),
            'rating': rating_(),
            'price': price_(),
            'author': next(authors_())
        }
    }

    filename = 'exam.txt'
    if os.path.exists('exam.txt'):
        with open(filename, "a", encoding='utf8') as f:
            json.dump(a, f, ensure_ascii=False, separators=(', ', ': '), indent=4)
    else:
        with open(filename, "x", encoding='utf8') as f:
            json.dump(a, f, ensure_ascii=False, separators=(', ', ': '), indent=4)


def main():
    counter_ = 1
    while counter_ <= 100:
        func_()
        counter_ += 1


if __name__ == "__main__":
    main()
