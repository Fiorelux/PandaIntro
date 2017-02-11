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

print(MyDataframe[(MyDataframe['CAT'] == 'cat1') | (MyDataframe['SET'] != 'test')])

#MyDataframe['VALUES'] =[2,5,1]  this istruction doesn't work becouse there are only 3 elements

MyDataframe.pop('THREE')
