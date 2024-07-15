# Given a string of "Wait at the bus stop at Manhattan Beach for the bus to the mountains"
# Return the unique words
# Return the number of instances for each word
# Return the words with the highest count

def unique_words(sentence: str) -> [str]:
    words = set()
    sentence = sentence.lower().split(' ')
    for word in sentence:
        if word not in words:
            words.add(word)

    return list(words)


def unique_words_count(sentence: str) -> dict:
    word_dict = {}
    for word in sentence.lower().split(' '):
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


if __name__ == "__main__":
    input_string = "Wait at the bus stop at Manhattan Beach for a bus to Mount Saint Helens"
    print(unique_words(input_string))
    print(unique_words_count(input_string))
