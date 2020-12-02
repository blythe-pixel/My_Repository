# TODO PRINTING DATA FROM CVS FILE
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
# df = df.head(722)
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
# df = read_excel('Students_DataFrame.xlsx')
#
# print(df.sort_values(by=['Name'], ascending=[True]).to_string())

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



