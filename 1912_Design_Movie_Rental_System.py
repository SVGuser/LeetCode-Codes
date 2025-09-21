from collections import defaultdict
from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.shop_movie_price = {}  # (shop, movie) → price
        self.unrented = defaultdict(SortedList)  # movie → SortedList of (price, shop)
        self.rented = SortedList()  # SortedList of (price, shop, movie)

        for shop, movie, price in entries:
            self.shop_movie_price[(shop, movie)] = price
            self.unrented[movie].add((price, shop))

    def search(self, movie: int) -> list[int]:
        return [shop for price, shop in self.unrented[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.unrented[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]
