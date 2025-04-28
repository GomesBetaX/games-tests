numbers = [1, 2, 3]
# key items
# new_list = [NEW_ITEM_EXPRESSION for ITEM in LIST]
new_list = [n + 1 for n in numbers]

name = "Angela"
new_list = [letter for letter in name]

new_range = [n + 1 for n in range(1, 5)]
print(new_range)

# nova lista com conditional
# new_list = [NEW ITEM EXPRESSION for ITEM in LIST if CONDITION]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_names = [name for name in names if len(name) == 4]
print(new_names)

# to set a user name in git
# git config --global user.name "gomesbetax"
# git config --global user.email "diego.gomesazul@gmail.com"