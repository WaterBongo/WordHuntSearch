
with open('board.txt','r') as f:
    word_string = f.read().strip()
    word_square = [list(word_string[i:i+4]) for i in range(0, len(word_string), 4)]

with open('wordlist2.txt','r') as f:
    Inital_wordlist = set(f.read().split("\n"))
secondary_wordlist = set([])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_valid_extension(x, y, used):
    max_row = len(word_square)
    max_col = len(word_square[0])
    return 0 <= x < max_row and 0 <= y < max_col and (x, y) not in used


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

three_letter_dict = {}

for key in word_dict:
    for dx, dy in directions:
        new_x = word_dict[key]['used_cordinates'][-1][0] + dx
        new_y = word_dict[key]['used_cordinates'][-1][1] + dy
        if is_valid_extension(new_x, new_y, word_dict[key]['used_cordinates']):
            three_letter_dict[key + word_square[new_x][new_y]] = {"used_cordinates":word_dict[key]['used_cordinates'] + [(new_x, new_y)],
                                                                         "possible_words":[]}
            for word in word_dict[key]['possible_words']:
                if word.startswith(key + word_square[new_x][new_y]):
                    three_letter_dict[key + word_square[new_x][new_y]]['possible_words'].append(word)

delete_words(three_letter_dict)


four_letter_dict = {}

for key in three_letter_dict:
    for dx, dy in directions:
        new_x = three_letter_dict[key]['used_cordinates'][-1][0] + dx
        new_y = three_letter_dict[key]['used_cordinates'][-1][1] + dy
        if is_valid_extension(new_x, new_y, three_letter_dict[key]['used_cordinates']):
            four_letter_dict[key + word_square[new_x][new_y]] = {"used_cordinates":three_letter_dict[key]['used_cordinates'] + [(new_x, new_y)],
                                                                         "possible_words":[]}
            for word in three_letter_dict[key]['possible_words']:
                if word.startswith(key + word_square[new_x][new_y]):
                    four_letter_dict[key + word_square[new_x][new_y]]['possible_words'].append(word)

delete_words(four_letter_dict)
print(four_letter_dict)