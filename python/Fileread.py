# Python program to read file word by word


with open('word.txt','r') as file:
    for line in file:
        for word in line.split():
            print(word)
