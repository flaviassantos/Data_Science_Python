# create dummy variables for ‘column_x’ and exclude first dummy column
column_x_dummies = pd.get_dummies(df.column_x).iloc[:, 1:]
# concatenate two DataFrames (axis=0 for rows, axis=1 for columns)
df = pd.concat([df, column_x_dummies], axis=1)
‘’’
Less Frequently Used Features
‘’’
# create a DataFrame from a dictionary
pd.DataFrame({‘column_x’:[‘value_x1’, ‘value_x2’, ‘value_x3’], ‘column_y’:[‘value_y1’, ‘value_y2’, ‘value_y3’]})
# create a DataFrame from a list of lists
pd.DataFrame([[‘value_x1’, ‘value_y1’], [‘value_x2’, ‘value_y2’], [‘value_x3’, ‘value_y3’]], columns=[‘column_x’, ‘column_y’])
# detecting duplicate rows
df.duplicated()       # True if a row is identical to a previous row
df.duplicated().sum() # count of duplicates
df[df.duplicated()]   # only show duplicates
df.drop_duplicates()  # drop duplicate rows
df.column_z.duplicated()   # check a single column for duplicates
df.duplicated([‘column_x’, ‘column_y’, ‘column_z’]).sum()  # specify columns for finding duplicates
# Clean up missing values in multiple DataFrame columns
df = df.fillna({
 ‘col1’: ‘missing’,
 ‘col2’: ‘99.999’,
 ‘col3’: ‘999’,
 ‘col4’: ‘missing’,
 ‘col5’: ‘missing’,
 ‘col6’: ‘99’
})
# Concatenate two DataFrame columns into a new, single column - (useful when dealing with composite keys, for example)
df[‘newcol’] = df[‘col1’].map(str) + df[‘col2’].map(str)
# Doing calculations with DataFrame columns that have missing values
# In example below, swap in 0 for df[‘col1’] cells that contain null
df[‘new_col’] = np.where(pd.isnull(df[‘col1’]),0,df[‘col1’]) + df[‘col2’]
 
# display a cross-tabulation of two Series
pd.crosstab(df.column_x, df.column_y)
# alternative syntax for boolean filtering (noted as “experimental” in the documentation)
df.query(‘column_z < 20’) # df[df.column_z < 20]
df.query(“column_z < 20 and column_y==’string’”)  # df[(df.column_z < 20) & (df.column_y==’string’)]
df.query(‘column_z < 20 or column_z > 60’)        # df[(df.column_z < 20) | (df.column_z > 60)]
# Loop through rows in a DataFrame
for index, row in df.iterrows():
 print index, row[‘column_x’]
# Much faster way to loop through DataFrame rows if you can work with tuples
for row in df.itertuples():
 print(row)
# Get rid of non-numeric values throughout a DataFrame:
for col in df.columns.values:
 df[col] = df[col].replace(‘[⁰-9]+.-’, ‘’, regex=True)
# Change all NaNs to None (useful before loading to a db)
df = df.where((pd.notnull(df)), None)
# Split delimited values in a DataFrame column into two new columns
df[‘new_col1’], df[‘new_col2’] = zip(*df[‘original_col’].apply(lambda x: x.split(‘: ‘, 1)))
# Collapse hierarchical column indexes
df.columns = df.columns.get_level_values(0)
# display the memory usage of a DataFrame
df.info()         # total usage
df.memory_usage() # usage by column
# change a Series to the ‘category’ data type (reduces memory usage and increases performance)
df[‘column_y’] = df.column_y.astype(‘category’)
# temporarily define a new column as a function of existing columns
df.assign(new_column = df.column_x + df.spirit + df.column_y)
# limit which rows are read when reading in a file
pd.read_csv(‘df.csv’, nrows=10)        # only read first 10 rows
pd.read_csv(‘df.csv’, skiprows=[1, 2]) # skip the first two rows of data
# randomly sample a DataFrame
train = df.sample(frac=0.75, random_column_y=1) # will contain 75% of the rows
test = df[~df.index.isin(train.index)] # will contain the other 25%
# change the maximum number of rows and columns printed (‘None’ means unlimited)
pd.set_option(‘max_rows’, None) # default is 60 rows
pd.set_option(‘max_columns’, None) # default is 20 columns
print df
# reset options to defaults
pd.reset_option(‘max_rows’)
pd.reset_option(‘max_columns’)
# change the options temporarily (settings are restored when you exit the ‘with’ block)
with pd.option_context(‘max_rows’, None, ‘max_columns’, None):
 print df