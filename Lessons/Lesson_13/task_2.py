class CountPagesException(Exception):
    def __init__(self, message='CountPagesException'):
        super().__init__(message)


class YearException(Exception):
    def __init__(self, message='YearException'):
        super().__init__(message)


class AuthorException(Exception):
    def __init__(self, message='AuthorException'):
        super().__init__(message)


class PriceException(Exception):
    def __init__(self, message='PriceException'):
        super().__init__(message)


class Book:
    count_pages: int
    year: int
    author: str
    price: int

    def __init__(self, count_pages: int, year: int, author: str, price: int):
        if count_pages is not int:
            raise CountPagesException
        elif year is not int:
            raise YearException
        elif author is not str:
            raise AuthorException
        elif price is not int:
            raise PriceException
        self.count_pages = count_pages
        self.year = year
        self.author = author
        self.price = price


book = Book(3, '3rrfew', 'sdfds', 3)