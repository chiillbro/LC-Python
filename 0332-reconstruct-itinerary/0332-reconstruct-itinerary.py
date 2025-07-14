class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        tickets.sort(reverse=True)

        for departure, arrival in tickets:
            adj_list[departure].append(arrival)
        

        stack = ["JFK"]
        itinerary = []

        while stack:
            if adj_list[stack[-1]]:
                stack.append(adj_list[stack[-1]].pop())

            else:
                itinerary.append(stack.pop())

        itinerary.reverse()
        return itinerary