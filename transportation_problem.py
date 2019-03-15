
class TransportationProblem():
    def __init__(self, end_state):
        self.end_state = end_state
        train = 1
        walk = 2

    def start_state(self):
        # BEGIN_YOUR_CODE
        return 1
        # END_YOUR_CODE

    def is_end(self, state):
        # BEGIN_YOUR_CODE
        # raise Exception("Not implemented yet")
        return state == self.end_state
        # END_YOUR_CODE

    def succ_and_cost(self, state):
        # BEGIN_YOUR_CODE
        results = []
        if state + 1 <= self.end_state:
            action = 'Walk'
            newState = state + 1
            cost = 1
            results.append((action, newState, cost))

        if state * 2 <= self.end_state:
            results.append(('Train', state * 2, 2))

        return results

        # END_YOUR_CODE

problem = TransportationProblem(7)

import backtracking_search
bts = backtracking_search.BacktrackingSearch(verbose=3)
print(bts.solve(problem))

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
# dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
print(dps.solve(problem))

import uniform_cost_search
ucs = uniform_cost_search.UniformCostSearch(verbose=3)
print(ucs.solve(problem))
