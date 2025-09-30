import pandas as pd

# Read the excel data
excel_file =r'C:\Users\hp\Desktop\Imperative\excel_files\sample.xlsx'

#Read the Excel specific columun
df = pd.read_excel(excel_file,usecols = ['Name','Age'])
print(df)