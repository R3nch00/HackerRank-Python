from collections import OrderedDict

def word_occurrences(n, words):
    word_count = OrderedDict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_words_count = len(set(words))  # Count the number of distinct words

    # Output the number of distinct words
    print(distinct_words_count)

    # Output the number of occurrences for each distinct word
    print(" ".join(str(word_count[word]) for word in word_count))

if __name__ == "__main__":
    n = int(input())
    words = [input().strip() for _ in range(n)]

    word_occurrences(n, words)
