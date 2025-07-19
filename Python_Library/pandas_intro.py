import pandas as pd # IMPORTING PANDAS

var= pd.Series([1,2,3,4]) #CREATING A PANDAS SERIES  
print(var)

var1=pd.Series([1,2,3,4], index=["A", "B", "C", "D"]) #CREATING A PANDAS SERIES WITH UNIQUE INDEX VALUES
print(var1)


l1=[2,4,6,8,10]
indexof_2=["2*1", "2*2", "2*3", "2*4", "2*5"]

table_of2=pd.Series(l1,indexof_2) #ANOTHER WAY TO CREATE A PANDAS SERIES
print(table_of2)



my_dict={"phone": 2, "laptop": 10, "computer": 5}

new_series=pd.Series(my_dict)   #CREATING A PANDAS SERIES WITH A DICTIONARY
print(new_series)

print(new_series["laptop"])    #ACCESSING THE VALUE ASSOCIATED TO THE KEY "laptop"        

print(type(new_series))         #CHECKING TYPE OF new_series : "panda.series"

