rand_string = " to jest lista wyrazow  "

rand_string = rand_string.lstrip()
print(rand_string.rstrip())
print(rand_string.capitalize())
print(rand_string.upper())

strings_list = ['to', 'jest', 'lista', 'wyrazow.']
print(" ".join(strings_list))
strings_list_split = rand_string.split()
print(strings_list_split)
for i in strings_list_split:
    print(i)
print("Gdzie jest :", rand_string.count('jest'))
print("Gdzie jest :", rand_string.find('lista'))
print("Gdzie sa :", rand_string.replace("lista", "ciag"))


