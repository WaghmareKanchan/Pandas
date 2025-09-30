import pandas as pd
import os

#sorting file 
df = pd.read_excel(r'C:\Users\hp\Desktop\Imperative\excel_files\Engineer_Salaries.xlsx')

df_sorted = df.sort_values(by =['Company','Salary'], ascending = [False, True])

output_file = r'C:\Users\hp\Desktop\Imperative\excel_files\Sorted.xlsx'
df_sorted.to_excel(output_file, index = False)

os.startfile(output_file)