class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        # supplies_set = set(supplies)

        # for i, recipe in enumerate(recipes):
        #     can_make = True
        #     for ingre in ingredients[i]:
        #         if ingre not in supplies_set:
        #             can_make = False
        #             break
            
        #     if can_make:
        #         supplies_set.add(recipe)
        #         res.append(recipe)

        available = set(supplies)
        recipe_queue = deque([i for i in range(len(recipes))])
        last_size = -1

        while len(available) > last_size:
            last_size = len(available)
            queue_size = len(recipe_queue)
            while queue_size:
                queue_size -= 1
                recipe_idx = recipe_queue.popleft()
                if all(ingredient in available for ingredient in ingredients[recipe_idx]):
                    available.add(recipes[recipe_idx])
                    res.append(recipes[recipe_idx])
                else:
                    recipe_queue.append(recipe_idx)

        return res
