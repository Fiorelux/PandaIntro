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
print(MyDataframe)