import util
import wordsegUtil

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def start_state(self):
       return 0
        # END_YOUR_CODE
        
    def is_end(self, state):
        # BEGIN_YOUR_CODE
        return state == len(self.query)
        # END_YOUR_CODE
        
    def succ_and_cost(self, state):
        # BEGIN_YOUR_CODE
        results = []
        sentence = ''
        # cost = self.unigramCost(self.query)

        for i in range(1, len(self.query) - state + 1):
            target_word = self.query[state:state+i]
            results.append((target_word, state + i, self.unigramCost(target_word)))

        return results
        # END_YOUR_CODE

unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
problem = SegmentationProblem('thisisnotmybeautifulhouse', unigramCost)

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
# dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
# print dps.solve(problem)

import uniform_cost_search
ucs = uniform_cost_search.UniformCostSearch(verbose=0)
print(ucs.solve(problem))
