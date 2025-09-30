import pandas as pd

# Read Excel data At a time 2 Excel Files
df = pd.read_excel(r"C:\Users\hp\Desktop\Imperative\excel_files\sample.xlsx")
print(df)

df1 = pd.read_excel(r"C:\Users\hp\Desktop\Imperative\excel_files\sample2.xlsx")
print(df1)