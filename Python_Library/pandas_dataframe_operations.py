import pandas as pd 
import numpy as np
import sys
import os



#DISPLAYING DATA FROM A CSV FILE
my_df2= pd.read_csv(r"C:\Users\RAMAW\OneDrive\Documents\Python Codes\Python_Library\dog_data.csv")
print(my_df2)



print(my_df2.head()) #PRINTING THE FIRST 5 ELEMENTS OF THE DATASET
print(my_df2.head(10)) #PRINTING THE FIRST n ELEMENTS OF THE DATASET



print(my_df2.tail()) #PRINTING THE LAST FIVE ELEMENTS OF THE DATASET
print(my_df2.tail(10)) #PRINTING THE LAST n ELEMENTS OF THE DATASET


print(my_df2.shape) #PRINTING SHAPE OF A DATASET
print(my_df2.ndim)  #PRINTING THE Dimensions of the dataset
print(my_df2.info()) #GET INFORMATION ABOUT THE DATASET
print(my_df2.dtypes) #GET THE DATATYPE OF THE DATASET


print("\n\n\n\n\n\n",my_df2["Breed"].describe()) #GETS DETAILS ABOUT A SPECIFIC COULMN  
print("\n\n\n\n\n\n",my_df2["DogName"].describe()) #GETS DETAILS ABOUT A SPECIFIC COULMN  
print("\n\n\n\n\n\n",my_df2["Color"].describe()) #GETS DETAILS ABOUT A SPECIFIC COULMN  
print("\n\n\n\n\n\n",my_df2["OwnerZip"].describe()) #GETS DETAILS ABOUT A SPECIFIC COULMN  


print(my_df2.Breed) #GETS DETAILS ABOUT A SPECIFIC COULMN       METHOD 2


print(my_df2.iloc[:, 1]) #GET A SPECIFIC COULMN BY THEIR INDEX