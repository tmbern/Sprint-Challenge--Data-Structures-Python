import time
from binary_search_tree import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# our Binary Search Tree from this week has a module contains...
# this allows us to search whether a value or input is in the bst
# if we move all the names from one list to their own search trees
# we should be able to traverse thru using contains method. 
BST_names_1 = BSTNode('')

for i in names_1:
    BST_names_1.insert(i)

# now that we have the names from names_1 in a bst we will itterate
# over the names in names_2, and if the bst of names_1 contains that 
# name then we will move it to the duplicates list.
for i in names_2:
    if BST_names_1.contains(i) is True:
        duplicates.append(i)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
