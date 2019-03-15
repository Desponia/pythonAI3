import util
import wordsegUtil

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start_state(self):
        # BEGIN_YOUR_CODE
        return (0, wordsegUtil.SENTENCE_BEGIN)
        # END_YOUR_CODE

    def is_end(self, state):
        # BEGIN_YOUR_CODE
        return state[0] == len(self.query)
        # END_YOUR_CODE

    def succ_and_cost(self, state):
        # BEGIN_YOUR_CODE
        results = []
        position, prev_word = state
        # 띄어쓰기 하나씩 넣어보는 for
        for length in range(1, len(self.query) - position + 1):
            cand_words = self.possibleFills(self.query[position:position+length])

            # possible 단어 찾는 for
            for word in cand_words:
                action = word
                new_state = (position + length, word)
                cost = self.bigramCost(prev_word, word)
                results.append((action, new_state, cost))

        return results

        # END_YOUR_CODE

unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
smoothCost = wordsegUtil.smoothUnigramAndBigram(unigramCost, bigramCost, 0.2)
possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')
problem = JointSegmentationInsertionProblem('mgnllthppl', smoothCost, possibleFills)

import dynamic_programming_search
dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=True, verbose=1)
print(dps.solve(problem))

import uniform_cost_search
ucs = uniform_cost_search.UniformCostSearch(verbose=0)
print(ucs.solve(problem))
