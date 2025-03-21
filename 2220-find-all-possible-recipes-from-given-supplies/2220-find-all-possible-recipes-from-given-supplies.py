class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # res = []
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



        # ** Typical BFS Approach **

        # available = set(supplies)
        # recipe_queue = deque([i for i in range(len(recipes))])
        # last_size = -1

        # while len(available) > last_size:
        #     last_size = len(available)
        #     queue_size = len(recipe_queue)
        #     while queue_size:
        #         queue_size -= 1
        #         recipe_idx = recipe_queue.popleft()
        #         if all(ingredient in available for ingredient in ingredients[recipe_idx]):
        #             available.add(recipes[recipe_idx])
        #             res.append(recipes[recipe_idx])
        #         else:
        #             recipe_queue.append(recipe_idx)



        # ** Typical DFS Approach **

        # can_make = {supp : True for supp in supplies}
        # recipe_to_idx = {recipe : idx for idx, recipe in enumerate(recipes)}

        # def checkRecipe(recipe, visited):
        #     if can_make.get(recipe, False): return True
        #     if recipe in visited or recipe not in recipe_to_idx: return False

        #     visited.add(recipe)

        #     can_make[recipe] = all(checkRecipe(ingre, visited) for ingre in ingredients[recipe_to_idx[recipe]])

        #     return can_make[recipe]

        # return [recipe for recipe in recipes if checkRecipe(recipe, set())]

        

        # ** Optimal Solution : Using Topological Sort (Kahn's Algorithm)

        available_supplies = set(supplies)
        recipe_to_idx = defaultdict(int)
        dependency_graph = defaultdict(list)
        in_degree = [0] * len(recipes)

        for i, recipe in enumerate(recipes):
            recipe_to_idx[recipe] = i
            for ingre in ingredients[i]:
                if ingre not in available_supplies:
                    dependency_graph[ingre].append(recipe)
                    in_degree[i] += 1
        
        queue = deque([idx for idx, i in enumerate(in_degree) if not i])
        res = []

        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            res.append(recipe)
            if recipe not in dependency_graph: continue
            for dependent_recipe in dependency_graph[recipe]:
                dependent_recipe_idx = recipe_to_idx[dependent_recipe]
                in_degree[dependent_recipe_idx] -= 1
                if not in_degree[dependent_recipe_idx]:
                    queue.append(dependent_recipe_idx)
        
        return res




