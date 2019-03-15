import math, collections

SENTENCE_BEGIN = '-BEGIN-'

corpus = [
    'I am Sam',
    'Sam I am',
    'I do not like green'
]
    
# Counting
unigram_counts = collections.defaultdict(int)
# BEGIN_YOUR_CODE
for sentence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    for word in words:
        unigram_counts[word] += 1;
# END_YOUR_CODE

bigram_counts = collections.defaultdict(int)
# BEGIN_YOUR_CODE
for setence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    for i in range(len(words[:-1])):
        bigram_counts[(words[i], words[i+1])] += 1

print(bigram_counts)
# END_YOUR_CODE
        
# Bigram function
def bigram(prev_word, curr_word):
    # BEGIN_YOUR_CODE
    return bigram_counts[(prev_word, curr_word)] / unigram_counts[prev_word]
    # END_YOUR_CODE

# Printing results
print('\n- Bigram probabilities - ')
print(('P(-BEGIN-, I) = %f'%bigram(SENTENCE_BEGIN, 'I')))    
print(('P(-BEGIN-, Sam) = %f'%bigram(SENTENCE_BEGIN, 'Sam')))    
print(('P(I, do) = %f'%bigram('I', 'do')))
print(('P(like, green) = %f'%bigram('like', 'green')))
