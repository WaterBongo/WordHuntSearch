import ast

# Open the file for reading
with open('oute.txt', 'r') as file:
    # Read each line and convert it into a list
    lines = [ast.literal_eval(line) for line in file]

# Now you can interact with the lines as a list
for line in lines:
    print(line)