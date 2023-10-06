import pandas as pd
from numpy.random import randint

df =['lib', 'qty1', 'qty2'],['l2', 'q2', 'q2'],['l3', 'q3', 'q3'],['lib', 'qty1', 'qty2'],['lib', 'qty1', 'qty2']
d1 =pd.DataFrame(df,columns=['a','b','c'])
print(d1)
print("\nitertuples()")
for x1 in d1.itertuples():
    print(x1)
print("\niterrows()")
for x1 in d1.iterrows():
    print(x1)
print("\nitems()")
for x1 in d1.items():
    print(x1)
