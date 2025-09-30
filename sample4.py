import pandas as pd
import os

dataset = pd.read_excel(r"C:\Users\hp\Desktop\Imperative\excel_files\sample4.xlsx")

#Open excel file 
output_file = r"C:\Users\hp\Desktop\Imperative\excel_files\sample4.xlsx"
dataset.to_excel(output_file)

os.startfile(output_file)