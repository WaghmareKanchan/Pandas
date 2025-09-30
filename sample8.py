import pandas as pd
import os

#drop duplicates values in columns 
df = pd.read_excel(r'C:\Users\hp\Desktop\Imperative\excel_files\All_column.xlsx')

df_cleaned = df.drop_duplicates(subset = ['Country'])

output_file = r'C:\Users\hp\Desktop\Imperative\excel_files\All_column.xlsx'
df_cleaned.to_excel(output_file, index = False)

os.startfile(output_file)