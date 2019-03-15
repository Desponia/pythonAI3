import util

class BacktrackingSearch(util.SearchAlgorithm):
    def __init__(self, verbose=0):
        self.verbose = verbose

    def recurrence(self, state, path, path_cost):
        if self.verbose >= 2:
            print('state %s with path %s [%d]'%(state, path, path_cost))
        self.num_visited += 1
        if self.problem.is_end(state):
            if self.best_path is None or path_cost < self.best_path_cost:
                self.best_path = path
                self.best_path_cost = path_cost

        else:
            succ_and_cost = self.problem.succ_and_cost(state)
            for action, new_state, cost in succ_and_cost:
                self.recurrence(new_state, path + [action], path_cost + cost)


    def solve(self, problem):
        # Not thread-safe
        self.problem = problem
        self.num_visited = 0
        self.best_path, self.best_path_cost = None, None
        
        initial_state = problem.start_state()
        empty_path = []
        self.recurrence(initial_state, empty_path, 0)
        
        return self.best_path, self.best_path_cost, self.num_visited
