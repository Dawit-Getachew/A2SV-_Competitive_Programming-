class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies, recipies = set(supplies), set(recipes)
        indegree = {elem:0 for elem in recipies}
        graph = defaultdict(list)
        for i, recipie in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    indegree[recipie] += 1
                    graph[ingredient].append(recipie)    
        queues = deque()
        for key, value in indegree.items():
            if value == 0:
                queues.append(key)
        result = []
        while queues:
            element = queues.popleft()
            result.append(element)
            for elem in graph[element]:
                indegree[elem] -= 1
                if indegree[elem] == 0:
                    queues.append(elem)
        return result
                    
            
            
        