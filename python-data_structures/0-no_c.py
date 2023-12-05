def no_c(my_string):
    for c in my_string:
        if c in "Cc":
            no_c = my_string.remove(c)
    return no_c
        

#         def anti_vowel(text):
#     for c in text:
#         if c in "aeiouAEIOU":
#             no_vowel = text.replace(c, '')
#     return no_vowel
# print(anti_vowel('Hello World')