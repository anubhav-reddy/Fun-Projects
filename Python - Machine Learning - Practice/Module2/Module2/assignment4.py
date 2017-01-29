import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
df = pd.read_html('http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2', header = 1) [0]


# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
df.columns = ['RK','PLAYER','TEAM','Games Played','Goals','Assists','Points','Plus/Minus Rating','Penalty Minutes','Points Per Game','Shots on Goal','Shooting Percentage','Game-Winning Goals','Power-Play Goals','Power-Play Assists','Short-Handed Goals','Short-Handed Assists']
print(df)


# TODO: Get rid of any row that has at least 4 NANs in it
#
df = df.dropna(axis=0,thresh = 4)
print(df)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?

print(df.Goals == 'G')
df = df[df.Goals != 'G']



# TODO: Get rid of the 'RK' column
#
df = df.drop(labels = 'RK', axis = 1)


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
df = df.reset_index(drop=True)
print(df)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
print(df.dtypes)
df[['Games Played','Goals','Assists','Points','Plus/Minus Rating','Penalty Minutes','Points Per Game','Shots on Goal','Shooting Percentage','Game-Winning Goals','Power-Play Goals','Power-Play Assists','Short-Handed Goals','Short-Handed Assists']] = df[['Games Played','Goals','Assists','Points','Plus/Minus Rating','Penalty Minutes','Points Per Game','Shots on Goal','Shooting Percentage','Game-Winning Goals','Power-Play Goals','Power-Play Assists','Short-Handed Goals','Short-Handed Assists']].apply(lambda x: pd.to_numeric(x, errors = 'coerce'))
print(df.dtypes)
# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print(len(df))
a = df['Shooting Percentage'].unique()
print(len(a))
a =  df.loc[15,'Games Played']
b = df.loc[16,'Games Played']
c = a + b
print(a, b, c)
