class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")
        
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        book.add_contract(contract)
        return contract

    def contracts(self):
        return self._contracts.copy()

    def books(self):
        return list({contract.book for contract in self._contracts})

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise TypeError("contract must be an instance of Contract")
        self._contracts.append(contract)

    def contracts(self):
        return self._contracts.copy()

    def authors(self):
        return list({contract.author for contract in self._contracts})


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

        
        self.author._contracts.append(self)
        self.book.add_contract(self)

    @staticmethod
    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]
