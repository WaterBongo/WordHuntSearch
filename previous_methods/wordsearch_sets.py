

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_valid_extension(x, y, used):
    max_row = len(word_square)
    max_col = len(word_square[0])
    return 0 <= x < max_row and 0 <= y < max_col and (x, y) not in used

possible_words = []
word_square = [
    ['i','a','g','b'],
    ['i','o','l','n'],
    ['t','y','b','n'],
    ['t','e','c','p']
]
used_spots = []
temp = []
new_list = set([])
elimated_words = set([])
second_elimated_words = set([])
third_eliminated_words = set([])
extended_new_new_list = set([])
with open('./wordlist2.txt','r') as f:
    wordlist = set(f.read().split("\n"))
for row in word_square:
    for letter in row:
        # Generate all 2-letter combinations
        for row in range(len(word_square)):
            for col in range(len(word_square[row])):
                # Traverse up
                # Traverse up
                # {}
                if row >= 1:
                    combo = word_square[row][col] + word_square[row-1][col]
                    temp.append((combo, (row, col), (row-1, col)))
                # Traverse down
                if row < len(word_square) - 1:
                    combo = word_square[row][col] + word_square[row+1][col]
                    temp.append((combo, (row, col), (row+1, col)))
                # Traverse left
                if col >= 1:
                    combo = word_square[row][col] + word_square[row][col-1]
                    temp.append((combo, (row, col), (row, col-1)))
                # Traverse right
                if col < len(word_square[row]) - 1:
                    combo = word_square[row][col] + word_square[row][col+1]
                    temp.append((combo, (row, col), (row, col+1)))
                # Traverse diagonally up-left
                if row >= 1 and col >= 1:
                    combo = word_square[row][col] + word_square[row-1][col-1]
                    temp.append((combo, (row, col), (row-1, col-1)))
                # Traverse diagonally up-right
                if row >= 1 and col < len(word_square[row]) - 1:
                    combo = word_square[row][col] + word_square[row-1][col+1]
                    temp.append((combo, (row, col), (row-1, col+1)))
                # Traverse diagonally down-left
                if row < len(word_square) - 1 and col >= 1:
                    combo = word_square[row][col] + word_square[row+1][col-1]
                    temp.append((combo, (row, col), (row+1, col-1)))
                # Traverse diagonally down-right
                if row < len(word_square) - 1 and col < len(word_square[row]) - 1:
                    combo = word_square[row][col] + word_square[row+1][col+1]
                    temp.append((combo, (row, col), (row+1, col+1)))
temp = set(temp)
input(":D")
import time
start_time = time.time()
for part_words in temp:
    for words in wordlist:
        if words.startswith(part_words[0].lower()):
            new_list.add(part_words)
            elimated_words.add(words)
end_time = time.time()
for combo in new_list:
    print(combo[0], combo[1], combo[2])

input(f"Time taken: {end_time - start_time} seconds")



extended_new_list = set()

# Helper function to handle coordinate bounds and used spot

# Directions vectors (dx, dy) for movements: up, down, left, right, diagonally (NW, NE, SW, SE)


# Iterate over the valid 2-letter combinations
for combo, p1, p2 in new_list:
    used_positions = {p1, p2}  # positions already used by this combo
    last_position = p2  # last letter's position
    last_x, last_y = last_position

    # Try each direction
    for dx, dy in directions:
        new_x, new_y = last_x + dx, last_y + dy
        
        if is_valid_extension(new_x, new_y, used_positions):
            new_letter = word_square[new_x][new_y]
            three_letter_combo = combo + new_letter
            new_positions = used_positions.union({(new_x, new_y)})
            
            # Check against word list (Assuming words are newline stripped in wordlist)

            for words in elimated_words:
                if words.startswith(three_letter_combo.lower()):
                    if   len(words) == 3:
                        possible_words.append((three_letter_combo, p1,p2, (new_x, new_y)))
                    extended_new_list.add((three_letter_combo, p1,p2, (new_x, new_y)))
                    second_elimated_words.add(words)

            # if any(word.startswith(three_letter_combo.lower()) for word in elimated_words):

            #     extended_new_list.add((three_letter_combo, p1, (new_x, new_y)))
            #     second_elimated_words.add(word)

# print(len(extended_new_list))
# for combo in extended_new_list:
#     print(combo[0], combo[1], combo[2])
print(len(second_elimated_words))
for wl in extended_new_list:
    print(wl)
input("4rth words")
for combo, p1,p2,p3 in extended_new_list:
    used_positions = {p1, p2, p3}
    last_position = p3
    last_x, last_y = last_position
    for dx, dy in directions:
        new_x, new_y = last_x + dx, last_y + dy
        if is_valid_extension(new_x, new_y, used_positions):
            new_letter = word_square[new_x][new_y]
            four_letter_combo = combo + new_letter
            new_positions = used_positions.union({(new_x, new_y)})
            for words in second_elimated_words:
                if words.startswith(four_letter_combo.lower()):
                    if len(words) == 4:
                        possible_words.append((four_letter_combo, p1, p2, p3, (new_x, new_y)))
                        extended_new_new_list.add((four_letter_combo, p1, p2, p3, (new_x, new_y)))
                        continue
                    third_eliminated_words.add(words)
                    extended_new_new_list.add((four_letter_combo, p1, p2, p3, (new_x, new_y)))


#maybe a new datatype where i can uses lists 
def search_letter(x,y,combo,used,want_word,num_letters):
    letter_to_find = want_word[num_letters-1]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_extension(new_x, new_y, used):
            new_letter = word_square[new_x][new_y].lower()
            if new_letter == letter_to_find:
                new_combo = combo + new_letter
                print(new_combo, want_word)

                if new_combo == want_word:
                    print("Found word | " + new_combo + " | " + str(used.union({(new_x, new_y)})))
                    return True
                    input()
                search_letter(new_x,new_y,new_combo,used.add({(new_x, new_y)}),want_word,num_letters+1)

            
                
            # new_used = used.union({(new_x, new_y)})
            # for words in third_eliminated_words:
            #     if words.startswith(new_combo.lower()):
            #         if len(words) == 5:
            #             possible_words.append((new_combo, p1, p2, p3, p4, (new_x, new_y)))
            #             extended_new_new_list.add((new_combo, p1, p2, p3, p4, (new_x, new_y)))
            #             continue
            #         third_eliminated_words.add(words)
            #         extended_new_new_list.add((new_combo, p1, p2, p3, p4, (new_x, new_y)))
            # search_letter(new_x, new_y, letter+1, new_combo, new_used)


for wl in extended_new_new_list:
    print(wl)
print(len(third_eliminated_words))
input("5th words")
for word in third_eliminated_words:
    for combo, p1, p2, p3, p4 in extended_new_new_list:
        used_positions = {p1, p2, p3, p4}
        last_position = p4
        last_x, last_y = last_position
        if word.startswith(combo.lower()):
            fifth_letter = word[4]
            search_letter(last_x, last_y, combo, used_positions ,word, num_letters=5)