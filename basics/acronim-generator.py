#acronim generator
acronim = input("Please enter the words you need acronim:\n")
acronim = acronim.upper()
list_of_words = acronim.split()
for word in list_of_words:
    print(word[0], end="")
print()
