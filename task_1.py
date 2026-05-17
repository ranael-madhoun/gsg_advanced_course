import pandas as pd
csv_file='raw_data/student_coffee_crisis.csv'
json_file='raw_data/student_coffee_crisis.json'
lxs_file='raw_data/student_coffee_crisis.xlsx'
parquet_file='raw_data/student_coffee_crisis.parquet'

read_csv= pd.read_csv(csv_file)
print(read_csv.head(1))

read_js=pd.read_json(json_file)
print("last 3 items from json file\n",read_js.tail(3))

read_xlsx=pd.read_excel(lxs_file)
print(read_xlsx.head(1))

read_parquet = pd.read_parquet(parquet_file,engine="auto")
print(read_parquet.head(5))
