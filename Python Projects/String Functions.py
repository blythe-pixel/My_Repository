import string
ken = "                 Kristian Roger Agdeppa     "


print(ken.strip())
""".strip is a type of statement that removes the unnecessary
    spaces before the first word and after the last word"""


print(ken.lower())
""".lower is a type of statement that turns all the words under
    the string into lower caps"""

print(ken.upper())
""".upper is a type of statement that turns all the words under
    the string into upper caps"""


print(ken.replace('K', 'C'))
print(ken.replace('Roger', 'VISOC'))
""".replace('', '') statement is a powerful command that is used
    to replace a character/string inside the string"""


alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
print(alphabet_list)