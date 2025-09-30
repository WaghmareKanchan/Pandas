import pandas as pd
import os

#merge two excel files
df = pd.read_excel(r"C:\Users\hp\Desktop\Imperative\excel_files\sample3.xlsx")
df1 = pd.read_excel(r"C:\Users\hp\Desktop\Imperative\excel_files\sample4.xlsx")

merged_df = pd.concat([df,df1], axis = 1)

output_file = r'C:\Users\hp\Desktop\Imperative\excel_files\merged_output.xlsx'

merged_df.to_excel(output_file, index = False)

os.startfile(output_file)
