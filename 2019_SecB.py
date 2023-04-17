# Solution to CS AQA Paper 1 Section B

word1 = input("Enter word 1:")
word2 = input("Enter word 2:")
possible = True
for char in word1:
    if word2.find(char) == -1:
        possible = False
        break
    else:
        word2 = word2[:word2.find(char)] + word2[word2.find(char)+1:]
if possible:
    print("word 1 can be made from word 2")
else:
    print("it is not possible to make word 1 from word 2")
