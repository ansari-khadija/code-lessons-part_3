import pandas as pd
print("=== 1. Create DataFrame using a Dictionary ===")
data = {
    'Name': ['Amit', 'Priya', 'Rahul'],
    'Age': [22, 25, 21],
    'Marks': [80, 90, 75]
}
d = pd.DataFrame(data)
print(d)

print("=== 2. Create DataFrame using a List ===")
data2 = [
    ['Amit', 22, 80],
    ['Priya', 25, 90],
    ['Rahul', 21, 75]
]
df = pd.DataFrame(
    data2,
    columns=['Name', 'Age', 'Marks']
)
print(d)
print(d.shape)
print(d.columns)
print(d.index)
print(d.dtypes)
print(d.size)