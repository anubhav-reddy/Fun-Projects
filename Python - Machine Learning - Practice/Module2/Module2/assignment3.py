import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
df = pd.read_csv('D:\Online COurses\Python\Data\Module2\Module2\Datasets\\servo.data', header = -1)
df.columns = ['motor','screw','pgain','vgain','class']
print(df)


# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
print(df[df.vgain == 5])
print(len(df[df.vgain == 5]))
print(pd.value_counts(df.vgain[df.vgain == 5]))

#Note to self: Value_counts can only ount data series and not data frame unlike len 

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
print(df[(df.motor == 'E') & (df.screw == 'E')])
print(len(df[(df.motor == 'E') & (df.screw == 'E')]))



# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
print(df[df.pgain == 4])
print(df.vgain[df.pgain == 4])
print(df.vgain[df.pgain == 4].mean())
#Note::below code is to cross check the mean value form above code

a = len(df.vgain[df.pgain == 4])
b = sum(df.vgain[df.pgain == 4])
print("count: "+ str(a),"sum: "+ str(b),"mean: "+str(b/a))
print(df.vgain.mean())


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print(df.dtypes)



