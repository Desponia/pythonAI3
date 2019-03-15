import util

class DynamicProgrammingSearch(util.SearchAlgorithm):
    def __init__(self, memory_use=True, verbose=0):
        self.memory_use = memory_use
        if memory_use:
            self.future_dict = {}
        self.verbose = verbose
        
    def future(self, state):
        # BEGIN_YOUR_CODE
        # self.num_visited += 1
        num_visited = 1


        if self.memory_use and state in self.future_dict:
            min_actions, min_cost, num_visited = self.future_dict[state]
            return min_actions, min_cost, 1

        if self.problem.is_end(state):

            min_cost = 0
            min_actions = []
            # return [], 0, num_visited
        else:
            succ_and_cost = self.problem.succ_and_cost(state)
            min_cost = float('inf')  # 무한대
            min_actions = []

            for action, new_state, cost in succ_and_cost:

                future_actions, future_cost, future_num_visited = self.future(new_state)
                num_visited += future_num_visited
                if future_cost + cost < min_cost:
                    min_cost = future_cost + cost
                    min_actions = [action] + future_actions

            if self.memory_use:
                self.future_dict[state] = min_actions, min_cost, num_visited

        return min_actions, min_cost, num_visited

        # END_YOUR_CODE

    def solve(self, problem):
        self.problem = problem
        actions, cost, num_visited = self.future(problem.start_state())
        if self.verbose >= 1:
            print("numStatesVisited = {}".format(num_visited))
            print("totalCost = {}".format(cost))
            print("actions = {}".format(actions))
        return actions, cost, num_visited

