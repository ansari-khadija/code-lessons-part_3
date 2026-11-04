import pandas as pd

# Storing Information
data ={
    "Name": ["Amit",'Priya',"Rahul","Riya","Sita"],
    "Marks": [80,90,75,85,95],
    "Subject": ["Python","Java","C++","JavaScript","Ruby"]
}

# creating dataframe
df = pd.DataFrame(data)
print(df)

# creating series and accessing elements
s = pd.Series(data["Subject"])
print(s)
m= pd.Series(data["Marks"],index=[1,2,3,4,5])
print(m)

