file = open('fourletterwords.txt', 'r')
for line in file:
    word = line[:-1]
    print(word)