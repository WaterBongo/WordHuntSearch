with open("./wordlist.txt",'r') as f:
    wordlist = f.readlines()
    wordlist = [word.strip() for word in wordlist]
for word in wordlist:
    if len(word) <= 2:
        wordlist.remove(word)
        print(f"Removed {word}")
    elif len(word) > 16:
        wordlist.remove(word)
        print(f"Removed {word}")
with open("./wordlist2.txt",'a+') as f:
    for word in wordlist:
        f.write(word + '\n')
print("Wordlist modified.")