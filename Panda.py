# TODO PRINTING DATA FROM CSV FILE
# from pandas import *
#
# df = read_csv(r'C:\Users\User\PycharmProjects\My_Repository\Pokemon Data Frame\pokemon_data.csv')
# df = df.head(10)
#
# print(df.to_string())
#
#
# """ printing pokemon name and its equivalent health points and
#     to_string() is a type of function that allows the system to print
#     all the data regardless of the number of rows and columns"""

# TODO LOCATING ITEMS FROM THE DATAFRAME
# from pandas import *
#
# df = read_csv(r'C:\Users\User\PycharmProjects\My_Repository\Pokemon Data Frame\pokemon_data.csv')
# print(df.to_string())
#
# """ printing columns by name"""
# print(f"Pokemon Name and Health Points")
# print(df[['Name', 'HP']])
#
#
# """ using the iloc[] you can retrieve data using the specific rows first int is the
#     starting point and second is the ending point"""
# print(df.iloc[:4].to_string())
#
#
# """ you can use the number of columns and rows to specify location of the desired data,
#     it is separated by an oxford comma"""
# print(df.iloc[721, 1])
#
# """ you can use this type of function to filter data from the Data Frame and set some
#     particular conditions"""
# print(df.loc[df['Legendary'] == True].to_string())

# TODO DATA SORTING
# from pandas import *
#
# df = read_excel('Students_DataFrame(Modified).xlsx')
#
# print(df.sort_values(by=['Name'], ascending=[True]).to_string())
#
# """ it sorts the values inside the file, you can use this by df.sort_values()
#     by= means the name of the column you want to sort, and you can specify
#     in the ascending= if it is sorted in reverse or not. Note: it can only filter
#     one column per function. """

# TODO MAKE CHANGES AND UPDATING THE DATAFRAME
# from pandas import *
# import datetime
# x = datetime.datetime.now()
# df = read_excel('Students_DataFrame.xlsx')
#
# df['GPA'] = df['Programming 101'] + df['Introduction to Computer Science']
# df['GPA'] = df['GPA'] / 2
#
# df['Date Modified'] = x
# df.to_excel(f'Students_DataFrame(Modified).xlsx', index=False)
#
# """ In order to update the current DataFrame, you need to use the function
#     df.to_excel() which the takes the first argument as the name of the file
#     and the second argument which is index=False implies that no index value
#     will be placed in the current file that will be created"""
#
# """ if you intend to create a txt file from a cvs (comma separated values) file
#     you can put an argument which is sep="\t" which indicates that the file
#     is separated by tabs after it is created"""

# TODO DATA FILTRATION (based on multiple conditions)
# from pandas import *
#
# df = read_excel(r'C:\Users\User\PycharmProjects\My_Repository\Pokemon Data Frame\pokemon_data.xlsx')
# print("Legendary Pokemon (Phychic)")
# print(df.loc[(df['Legendary'] == True) & (df['Type 1'] == 'Psychic')].to_string())
# print()
# print("Legendary Pokemon (Grass)")
# print(df.loc[(df['Legendary'] == True) & (df['Type 1'] == 'Grass')].to_string())
# print()
# print("Legendary Pokemon (Ice)")
# print(df.loc[(df['Legendary'] == True) & (df['Type 1'] == 'Ice')].to_string())
# print()
# print("Legendary Pokemon (Dragon)")
# print(df.loc[(df['Legendary'] == True) & (df['Type 1'] == 'Dragon') & (df['Attack'] >= 100)
#              & (df['Defense'] >= 100)].to_string())
#
# """ you can use || to that represents as 'or' and & to represent as 'and' """
#
# """ Data filtering is one of the useful things in Pandas, you can use this by
#     by the use of df.loc[], and the name of the column you want to filter and
#     it will automatically ask for an argument. Note: if the word you want to
#     filter is named "True", don't put a string quotation. """
#
# filtered_data = df.loc[(df['Legendary'] == True) & (df['Type 1'] == 'Dragon') & (df['Attack'] >= 100)
#                        & (df['Defense'] >= 100)]
#
# filtered_data.to_excel("filtered_data.xlsx", index=False)
# """ You can also save your filtered data into any file you want (xlsx, csv, txt, etc.) """
