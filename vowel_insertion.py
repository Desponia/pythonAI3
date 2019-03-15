import util
import wordsegUtil

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start_state(self):
        # BEGIN_YOUR_CODE
        return (0, wordsegUtil.SENTENCE_BEGIN)
        # END_YOUR_CODE

    def is_end(self, state):
        # BEGIN_YOUR_CODE
        return state[0] == len(self.queryWords)
        # END_YOUR_CODE

    def succ_and_cost(self, state):
        # BEGIN_YOUR_CODE

        results = []
        idx, prev_word = state
        # 이 state 에서 취할 수 있는 모든 엑션은 candidate_words에 있다.
        candidate_words = self.possibleFills(self.queryWords[idx])
        candidate_words.add(self.queryWords[idx])
        for word in candidate_words:
            action = word
            next_state = (idx+1, word)
            cost = self.bigramCost(prev_word, word)

            results.append((action, next_state, cost))

        return results

        # END_YOUR_CODE
    
unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')
problem = VowelInsertionProblem('thts m n th crnr'.split(), bigramCost, possibleFills)

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
# dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
# print dps.solve(problem)

import uniform_cost_search
ucs = uniform_cost_search.UniformCostSearch(verbose=0)
print(ucs.solve(problem))
