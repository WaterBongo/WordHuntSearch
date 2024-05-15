import os
word_string = input("Enter the word square: ")
word_square = [list(word_string[i:i+4]) for i in range(0, len(word_string), 4)]
print(word_square)
for fourbyfour in word_square:
    for i in fourbyfour:
        f= open("/Users/edwardhe/Downloads/Word Game Solver/board.txt","a+")
        f.write(i)
    f.write('\n')
