"""
Pandas Cheatsheet

"""
import pandas as pd

"""
A DataFrame is an object that stores data as rows and columns.
You can think of a DataFrame as a spreadsheet or as a SQL table.

DataFrames have rows and columns.
Each column has a name, which is a string.
Each row has an index, which is an integer.
DataFrames can contain many different
data types: strings, ints, floats, tuples, etc.
"""
## creating dataframe
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name':['t-shirt','t-shirt','skirt','skirt'],
  'Color': ['blue','green','red','black']
})


# loading and inspecting csv files
import pandas as pd
#load the CSV below:
df =pd.read_csv('imdb.csv')
print(df.head())
print(df.info())


## selecting one column
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north

##selecting multiple columns
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north_south = df[['clinic_north', 'clinic_south']]

# selecting rows
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])

march = df.iloc[2]
january = df.iloc[0]

#selecting rows with logic
df[df.MyColumnName == desired_column_value]
df[df.MyColumnName > desired_column_value]
df[df.MyColumnName < desired_column_value]

df[(df.age < 30) | (df.name == 'Martha Jones')]
##selecting with isin function
january_february_march = df[df.month.isin(['January','February','March'])]
print(january_february_march)

# adding columnns to data DataFrame
df['Sold in Bulk?']= ['Yes', 'Yes', 'No', 'No']

# adding columns to df with diference of cloumn values
df['Margin'] = df['Price'] - df['Cost to Manufacture']

# adding columns with string operations ( takes df column name and applies string operation on Name column)
df['Lowercase Name']= df.Name.apply(str.lower)

# Renaming the columns in df
df.columns = ['ID','Title','Category','Year Released','Rating']
# Renaming the columns in df
df.rename(columns={'name':'movie_title'}, inplace=True)

#lambda function to read first and last char of the strings
mylambda = lambda x: x[0] + x[-1]

#lambda function with if else
mylambda = lambda x: 'Welcome to BattleCity!' \
  if x >= 13 \
  else 'You must be 13 or older'

# lambda function adding email provide from emial field
df['Email Provider'] = df.Email.apply(
    lambda x: x.split('@')[-1]
    )

#lambda function to split name and last name where in column name both are written
get_last_name = lambda x: x.split(' ')[-1]
df['last_name'] = df.name.apply(get_last_name)

#max value in the column price from dataframe orders
most_expensive = orders['price'].max()

#number of unique values in column shoe_color from dataframe orders
num_colors = orders['shoe_color'].nunique()

#df.groupby('column1').column2.measurement()
pricey_shoes = orders.groupby('shoe_type').price.max()
