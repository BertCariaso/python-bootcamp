examples =[
    "The quick brown fox jumps","I love programming in Python!",""
]


def longest_word(string):
    words=string.split()
    longest_word_found=""

    for word in words:
        if len(word) > len(longest_word_found):
                longest_word_found=word

    return longest_word_found

for example in examples:
    print(longest_word(example))





"""    

longest_word=[{
    "The quick brown fox jumps","I love programming in Python!",""
}]

for word in longest_word:
    if len(word > len(longest_word_found)

    print(word)

"""
