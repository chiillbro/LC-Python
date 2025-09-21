class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.shops = n
        from sortedcontainers import SortedSet
        self.movie_sp = defaultdict(SortedSet)
        self.ms_p = defaultdict(int)

        for shop, movie, price in entries:
            self.movie_sp[movie].add((price, shop))
            ms = str(movie) + str(shop)
            self.ms_p[ms] = price
        
        self.rented_movies = SortedSet()

    def search(self, movie: int) -> List[int]:
        shop_info = self.movie_sp[movie]

        shops = []
        for price, shop in shop_info:
            if len(shops) == 5:
                break
            
            if (price, shop, movie) in self.rented_movies:
                continue
            
            shops.append(shop)
        
        return shops
        

    def rent(self, shop: int, movie: int) -> None:
        price = self.ms_p[str(movie) + str(shop)]

        self.rented_movies.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.ms_p[str(movie) + str(shop)]

        self.rented_movies.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        reports = []

        for price, shop, movie in self.rented_movies:
            if len(reports) == 5:
                break
            
            reports.append((shop, movie))
        
        return reports


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()