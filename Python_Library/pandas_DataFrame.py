import pandas as pd #IMPORTING PANDAS
import numpy as np  #IMPORTING NUMPY
from numpy.random import randn

data=randn(4,3)     #CREATING A MATRIX WITH RANDOM VALUES FROM randn FUNCTION IN NUMPY  (rows,coulmns)
rows=["A", "B", "C", "D"] #CREATING ROW INDEX FOR DATA FRAME(EQUAL TO NUMBER OF DEFINED ROWS IN data MATRIX)
coulmns=["January", "Febuary", "March"] #   CREATING COULMN INDEX FOR DATA FRAME(EQUAL TO NUMBER OF DEFINED COULMNS IN data MATRIX)


my_df= pd.DataFrame(data, rows, coulmns)        #DEFINING DATAFRAME WITH (DATA, ROW, COULMN)
print(my_df)            #PRINTING DATAFRAME







#DISPLAYING DATA FROM A CSV FILE

my_df2= pd.read_csv(r"C:\Users\RAMAW\OneDrive\Documents\Python Codes\Python_Library\dog_data.csv")
print(my_df2)


print(my_df2.loc[5])    #ACCESSING A SINGLE ELEMENT FROM THE DATASET
print(my_df2.loc[[0,1,2,3,4,5,6,7,8,9,10]])     #ACCESSING MULTIPLE ELEMENTS FROM THE DATASET

