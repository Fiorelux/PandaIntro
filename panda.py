import pandas as pd
import numpy as np

col1 = [i for i in range(4)]
col2 = [float(i**2) for i in range(4) ]
col3 = ['cat1', 'cat2', 'cat3', 'cat1']



MyDataframe = pd.DataFrame({'INDEX':col1,
                              'DATE':pd.Timestamp('20130102'),
                              'SQUARED':col2,
                              'THREE':np.array([3]*4, dtype='int32'),
                              'SET':pd.Categorical(["test", "train", "test", "train"]),
                              'CAT':col3})
# print(MyDataframe)
# print(MyDataframe.head(2))
# print(MyDataframe.tail(3))
# print(MyDataframe.dtypes)
# print(MyDataframe.columns)
# print(MyDataframe['Date']) # column of a dataframe are also proprerty of an object so you can write print(MyDataframe.Data)

# print(MyDataframe.ix[3,'SQUARED'])

#print(MyDataframe[(MyDataframe['CAT'] == 'cat1') | (MyDataframe['SET'] != 'test')])

#MyDataframe['VALUES'] =[2,5,1]  this istruction doesn't work becouse there are only 3 elements

#MyDataframe.pop('THREE')


# # add a column
MyDataframe['VALUES'] = [2,5,1,0.1]
MyDataframe['NUM_CAT'] = [1,1,2,3]
# # vectorised operations on columns
# MyDataframe['DIVIDED'] = MyDataframe['VALUES']/MyDataframe['SQUARED']
#
# # column wide calcutions
# print(MyDataframe['VALUES'].median())
# print(MyDataframe['VALUES'].max())
# # get unique values
# print(MyDataframe['SET'].unique())
#
# print(MyDataframe.apply(max))


# def addset(string):
#     return string + 'set'
# MyDataframe['SET'] = MyDataframe['SET'].map(addset)



# MyDataframe['SET'] = MyDataframe['SET'].astype(str)
# MyDataframe['SET'] = MyDataframe['SET'].map(lambda x: x.upper()) #lambda are use to create temporary function sintax= lambra parameters



# # sorting on a column
# MyDataframe= MyDataframe.sort_values(by='VALUES')
# print(MyDataframe)
# # sorting on multiple columns
# MyDataframe= MyDataframe.sort_values(['NUM_CAT', 'VALUES'], ascending=[True, False])
# print(MyDataframe)

# # ## merging with other data frames
# MyDataframe2 = pd.DataFrame({'INDEX':[2,3,1,0],
#                               'VALUE2':[11,22,33,44]})
# # print(MyDataframe2)
# #
# # # other options for how are 'inner', 'outer', 'right'
# MyDataframe3 = pd.merge(MyDataframe, MyDataframe2,
#                          how='left', on='INDEX')
# # print(MyDataframe3)
#
# Trainset = MyDataframe3[MyDataframe3['SET'] != 'TRAINSET']
# print(Trainset)
# # resetting rownumbers
# Trainset = Trainset.reset_index()
# print(Trainset)
# # notice the index has now become a column
# #  not to be confused with INDEX
# #  so columns in pandas case sensitive
# #  we can drop it
# Trainset.pop("index")
# print(Trainset)
#
# # setting a generic path
# import os
# outpath = os.path.abspath('./Results/export.csv')
# print(outpath)
# if not os.path.exists(os.path.abspath("./Results")):
#     os.makedirs("./Results")
# # exporting to csv file (without row numbers)
# Trainset.to_csv(outpath, sep=';', index_label=False)
#
# Trainset_2 = pd.read_csv(os.path.abspath("./Results/export2.csv"), sep=";")
# print(Trainset_2)

import matplotlib.pyplot as plt
import matplotlib

#optional style
matplotlib.style.use('ggplot')
# draw 2000 random points and plot the sum
df_rand = pd.Series(np.random.randn(2000))
df_rand_sum = df_rand.cumsum()
df_rand_sum.plot()
plt.show()