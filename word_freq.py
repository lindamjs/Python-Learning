from collections import defaultdict
def word_freq_counter(text):
    word_freq = defaultdict(int)

    word = text.split()
    for word in word:
        word_freq[word] = word_freq[word]+1

    #Sort the dict by values
    word_freq = sorted(word_freq.items(),key = lambda x:x[1], reverse = True)

    top_three = word_freq[0:3]

    print(top_three)

word_freq_counter("hello world this is my first hello project world this is my second hello project")