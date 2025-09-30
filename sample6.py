import pandas as pd
import os

df = pd.read_excel(r'C:\Users\hp\Desktop\Imperative\excel_files\Date.xlsx')

#convert date into string format year
df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')

df['Transaction_Date'] = df['Date'].dt.strftime('%b - %Y')

output_file = r'C:\Users\hp\Desktop\Imperative\excel_files\Date_Convert.xlsx'
df.to_excel(output_file, index = False)

os.startfile(output_file)
