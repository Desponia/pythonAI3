
class GraphProblem():
    def __init__(self, states, distances):
        self.states = states
        self.distances = distances

    def start_state(self):
        # BEGIN_YOUR_CODE
        # raise Exception("Not implemented yet")
        return 'S'
        # END_YOUR_CODE

    def is_end(self, state):
        # BEGIN_YOUR_CODE
        # raise Exception("Not implemented yet")
        return state == 'G'
        # END_YOUR_CODE

    def succ_and_cost(self, state):
        # BEGIN_YOUR_CODE
        # raise Exception("Not implemented yet")
        results = []

        # for edge in self.distances.keys():
        #     if state == edge[0]:
        #         results.append((edge[0] + '->' + edge[1], edge[1], self.distances[edge]))

        for(prev_state, next_state), cost in list(self.distances.items()):
            if state == prev_state:
                results.append((prev_state + '->' + next_state, next_state, cost))

        return results

        # END_YOUR_CODE
        
states = ['S', 'A', 'B', 'C', 'D', 'E', 'G']
distances = {
    ('S', 'A'): 1,
    ('A', 'B'): 3,
    ('A', 'C'): 1,
    ('B', 'D'): 3,
    ('C', 'D'): 1,
    ('C', 'G'): 2,
    ('D', 'G'): 3,
    ('D', 'E'): 4,
    ('S', 'G'): 12,
}

problem = GraphProblem(states, distances)

import backtracking_search
bts = backtracking_search.BacktrackingSearch(verbose=3)
# print(bts.solve(problem))

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
# dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
print(dps.solve(problem))

import uniform_cost_search
ucs = uniform_cost_search.UniformCostSearch(verbose=3)
# print(ucs.solve(problem))
