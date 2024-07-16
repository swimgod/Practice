# Given a string of "Wait at the bus stop at Manhattan Beach for the bus to the mountains"
# Return the unique words
# Return the number of instances for each word
# Return the words with the highest count

def unique_words_count(sentence: str) -> dict:
    word_dict = {}
    for word in sentence.lower().split(' '):
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


def highest_count_words(word_dict: dict) -> []:
    max_count = max(word_dict.values())
    return [x for x in word_dict if word_dict[x] >= max_count]


if __name__ == "__main__":
    input_string = "Wait at the bus stop at Manhattan Beach for a bus to Mount Saint Helens"
    unique_words_dict = unique_words_count(input_string)
    print(sorted(list(unique_words_dict.keys())))
    print(unique_words_dict)
    print(highest_count_words(unique_words_dict))
