# teste de abrir files da maneira clássica
# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# to open a file in read mode, you can use the 'with' statement
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# to open a file in write mode, you can use the 'with' statement
# with open("my_file(2).txt", "w") as file:
#     content = file.write("AAAAAA222")
#     print(content)

# to open a file in append mode, you can use the 'with' statement
# /Users/diego/OneDrive/Área de Trabalho/p_tests/testing/read, write, open
with open("../../../my_file.txt", "a") as file:
    content = file.write("\nFound ya!!")
    print(content)

