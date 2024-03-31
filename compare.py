import pandas
import pyarrow
import openpyxl
from pandas import Series
import numpy

f1 = pandas.read_excel('data/file1.xlsx', index_col=0) 
f2 = pandas.read_excel('data/file2.xlsx', index_col=0) 

m = f1.merge(f2, left_on="iban", right_on="iban")

print(m)