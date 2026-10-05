import pandas as pd

input_file = "./data/source_input/Online Retail.xlsx"
output_file = "./data/raw/online_retail.csv"

df = pd.read_excel(input_file)

df.to_csv(output_file, index = False)

print("تم تحويل الملف بنجاح")
print(f"عدد الصفوف :{len(df)}")
print(f"عدد الاعمدة :{len(df.columns)}")
