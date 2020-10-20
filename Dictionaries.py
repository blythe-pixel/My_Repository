# TODO CREATING A LIST
DATA1 = {1: 'persistent', 2: 'imbecile', 3: 'brave', 4: 'stupid'}

""" Dictionaries are like list but mostly you can call it by its given number """

DATA2 = ['Kristian', 'Mariblanca']

DATA3 = ['Roger', 'Agdeppa', 'J.R']

print(f'Mr. Agdeppa is {DATA1[1]} and {DATA1[3]}')

print()
"""The list under the dictionary is independent to the index value"""

print(f'His fullname is {dict(zip(DATA2, DATA3))}')

""" .get Operator is you can call a certain value if the value is -
not found the system will display a None instead of getting an error. """

print(DATA1.get(5, 'Error (NAME NOT FOUND)'))

del DATA3[2]
""" In order to delete one of the things inside the list 
    you can use "del ListName['Part of the list'] """

DATA2[1] = 'M.'
""" In order to add a particular thing inside a list
    you can use ListName[Index Value] = 'Additional' """
print()
print(dict(zip(DATA2, DATA3)))

# TODO CREATING A DICTIONARY
student_information = dict(Homeplaces=['Cagayan de Oro', 'Cebu City'], Age='18',
                           Schools=['SIBOL', 'KCS', 'MOGCHS', 'lICEO',
                                    'USTP'])

""" You can create a dictionary inside a dictionary which is called
    Multidimensional-Dictionary. """
print()
print(student_information['Homeplaces'])
print(student_information['Age'])
print(student_information['Schools'])
