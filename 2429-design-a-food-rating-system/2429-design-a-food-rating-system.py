class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # self.ratings = ratings
        # self.foods = foods
        
        # self.foods_to_indices = {food: i for i, food in enumerate(foods)}
        # self.cuisines = cuisines

        # cuisines_to_ind = defaultdict(list)

        # for i, cuisine in enumerate(cuisines):
        #     cuisines_to_ind[cuisine].append(foods[i])
        
        # self.cuisines_to_ind = cuisines_to_ind

        self.food_to_rating = defaultdict(int)
        self.food_to_cuisine = defaultdict(str)

        from sortedcontainers import SortedSet
        self.cuisine_to_fr = defaultdict(SortedSet)

        for i, food in enumerate(foods):
            self.food_to_rating[food] = ratings[i]
            self.food_to_cuisine[food] = cuisines[i]

            self.cuisine_to_fr[cuisines[i]].add((-ratings[i], food))


    def changeRating(self, food: str, newRating: int) -> None:
        # ind = None
        # if food in self.foods_to_indices: ind = self.foods_to_indices[food]

        # if ind is not None:
        #     self.ratings[ind] = newRating

        prev = (-self.food_to_rating[food], food)

        self.cuisine_to_fr[self.food_to_cuisine[food]].remove(prev)
        self.food_to_rating[food] = newRating

        self.cuisine_to_fr[self.food_to_cuisine[food]].add((-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:

        fr = self.cuisine_to_fr[cuisine][0]

        return fr[1]
        # maxRating = 0
        # maxRatedFood = None

        # for i, c in enumerate(self.cuisines):
        #     if c != cuisine:
        #         continue
            
            # food = self.foods[i]

            # rating = self.ratings[i]

            # if rating > maxRating:
            #     maxRating = rating
            #     maxRatedFood = food
            
            # elif rating == maxRating and maxRatedFood > food:
            #     maxRatedFood = food
            

        # for food in self.cuisines_to_ind[cuisine]:
        #     food_idx = self.foods_to_indices[food]
        #     if self.ratings[food_idx] > maxRating:
        #         maxRating = self.ratings[food_idx]
        #         maxRatedFood = food
            
        #     elif self.ratings[food_idx] == maxRating and maxRatedFood > food:
        #         maxRatedFood = food
        
        # return maxRatedFood
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)