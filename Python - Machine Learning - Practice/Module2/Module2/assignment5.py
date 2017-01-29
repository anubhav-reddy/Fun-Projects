import pandas as pd
import numpy as np


# TODO:
# Load up the dataset, setting correct header labels
# Use basic pandas commands to look through the dataset...
# get a feel for it before proceeding!
# Find out what value the dataset creators used to
# represent "nan" and ensure it's properly encoded as np.nan
#
df = pd.read_csv('D:\Online COurses\Python\Data\Module2\Module2\Datasets\\census.data', header = -1)
df = df.drop(labels = 0, axis = 1)
df.columns = ['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']
print(df.head(10))


# TODO:
# Figure out which features should be continuous + numeric
# Conert these to the appropriate data type as needed,
# that is, float64 or int64
#
print(df.dtypes)
df[['age','capital-gain','capital-loss','hours-per-week']] = df[['age','capital-gain','capital-loss','hours-per-week']].apply(lambda x: pd.to_numeric(x, errors = 'coerce'))
print(df.dtypes)
print(df)

# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal types using
# the method discussed in the chapter.
#
print(df.education.unique())
ordered_education = ['Preschool','1st-4th','5th-6th','7th-8th','9th','10th','11th','12th','HS-grad','Some-college','Bachelors','Masters','Doctorate']
df.education = df.education.astype("category", ordered = True, categories = ordered_education).cat.codes

# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any nominal types by
# exploding them out to new, separate, boolean fatures.
#

df = pd.get_dummies(df,columns = ['race','sex','classification'])


# TODO:
# Print out your dataframe
print(df.dtypes)