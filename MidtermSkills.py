def longest_word_length(s):
    s = list(map(lambda x: len(x), s.split()))
    return max(s)

def word_freq(s):
    freq = dict()
    for i in s.split():
        if i not in freq.keys():
            freq[i] = 1
        else:
            freq[i] += 1
    return freq
print(word_freq('it is what it is and only what it is'))

