samp_string = " This is a very important string "
samp_string = samp_string.strip()
mem_string = samp_string
samp_string = samp_string.upper()
print("Uppercase : ", samp_string)
samp_string = samp_string.lower()
print("Lowercase : ", samp_string)
words = mem_string.split()
print("Words")
for i in words:
    print(i)
print("How many ts? ", mem_string.count("s"))
print("String index : ", mem_string.index("string"))
print("Replace very : ", mem_string.replace("very", "kind of"))
letter_z = "z"
print("Is \"z\" a number or letter : ", letter_z.isalnum())
print("Is \"z\" a letter :", letter_z.isalpha())
print("Is \"z\" a number :", letter_z.isdigit())
print("Is \"z\" a space :", letter_z.isspace())