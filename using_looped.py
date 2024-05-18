import time
# with open('board.txt','r') as f:
#     word_string = f.read().strip()
word_string = input("Enter the word square: ")
word_square = [list(word_string[i:i+4]) for i in range(0, len(word_string), 4)]
with open('board.txt', 'w') as f:
    f.write(word_string)
with open('wordlist2.txt','r') as f:
    Inital_wordlist = set(f.read().split("\n"))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_valid_extension(x, y, used):
    max_row = len(word_square)
    max_col = len(word_square[0])
    if 0 <= x < max_row and 0 <= y < max_col and (x, y) not in used:
        return True
    return False    
def check_valid_words(word_dict):
    valid_words = []
    for letter_combo in word_dict:
        for word in word_dict[letter_combo]['possible_words']:
            if word == letter_combo:
                valid_words.append([word, word_dict[letter_combo]['used_cordinates']])
    return valid_words  


def remove_duplicates(words_list : list):
    new_list = []
    for words in words_list:
        if words not in new_list:
            new_list.append(words)
    return new_list

def get_touching_combinations(x, y):
    combinations = []
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if is_valid_extension(new_x, new_y, []):
            combinations.append([word_square[x][y] + word_square[new_x][new_y], (x, y), (new_x, new_y)])
    return combinations

def delete_words(word_dict):
    need_to_delete = []
    for key in word_dict:
        if len(word_dict[key]['possible_words']) == 0:
            need_to_delete.append(key)

    for key in need_to_delete:
        del word_dict[key]
    return word_dict

def looped_search_stacked(x, y, combo, word, used):
    new_used = used[:]
    found = False
    if word == combo:
        valid_wrds.append([word, new_used])
        found = True
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if is_valid_extension(new_x, new_y, used):
            new_str = combo + word_square[new_x][new_y]
            if word.startswith(new_str):
                new_used.append((new_x, new_y))
                found = looped_search_stacked(new_x, new_y, new_str, word, new_used) or found
                new_used.pop()
    return found


#finis the function
def looped_search_for_words(word_dict):
    for key in word_dict:
        for word in word_dict[key]['possible_words']:
            next_letter = word[len(key)]
            for dx,dy in directions:
                new_x = word_dict[key]['used_cordinates'][-1][0] + dx
                new_y = word_dict[key]['used_cordinates'][-1][1] + dy
                if is_valid_extension(new_x, new_y, word_dict[key]['used_cordinates']):
                    if next_letter == word_square[new_x][new_y]:
                        pass


def create_extra_letter_dict(word_dict):
    new_dict = {}
    for key in word_dict:
        for dx, dy in directions:
            new_x = word_dict[key]['used_cordinates'][-1][0] + dx
            new_y = word_dict[key]['used_cordinates'][-1][1] + dy
            if is_valid_extension(new_x, new_y, word_dict[key]['used_cordinates']):
                new_dict[key + word_square[new_x][new_y]] = {"used_cordinates":word_dict[key]['used_cordinates'] + [(new_x, new_y)],
                                                             "possible_words":[]}
                for word in word_dict[key]['possible_words']:
                    if word.startswith(key + word_square[new_x][new_y]):
                        new_dict[key + word_square[new_x][new_y]]['possible_words'].append(word)
    return new_dict


start_time = time.time()
all_combinations = []
for i in range(len(word_square)):
    for j in range(len(word_square[i])):
        combinations = get_touching_combinations(i, j)
        all_combinations.extend(combinations)

word_dict = {}
for words in all_combinations:
    word_dict[words[0]] = {"used_cordinates":[words[1], words[2]],
                           "possible_words":[]}

    
for words in all_combinations:
    for word in Inital_wordlist:
        if word.startswith(words[0]):
            word_dict[words[0]]['possible_words'].append(word)
delete_words(word_dict)

valid_wrds = []
#definitely could loop all of this lol.
three_letter_dict = create_extra_letter_dict(word_dict)
delete_words(three_letter_dict)
valid_wrds.extend(check_valid_words(three_letter_dict))

four_letter_dict = create_extra_letter_dict(three_letter_dict)
delete_words(four_letter_dict)
valid_wrds.extend(check_valid_words(four_letter_dict))



for four_Letter_combo in four_letter_dict:
    for words in four_letter_dict[four_Letter_combo]['possible_words']:
        looped_search_stacked(four_letter_dict[four_Letter_combo]['used_cordinates'][-1][0],
                             four_letter_dict[four_Letter_combo]['used_cordinates'][-1][1], 
                             four_Letter_combo, words, 
                             four_letter_dict[four_Letter_combo]['used_cordinates'])


valid_wrds.sort(key=lambda x: len(x[0]), reverse=True)
valid_wrds = remove_duplicates(valid_wrds)
filz = open('oute.txt','w')
for wrd in valid_wrds:
    filz.write(str(wrd) + "\n")
filz.close()
end_time = time.time()
print("Time taken: ", end_time - start_time)