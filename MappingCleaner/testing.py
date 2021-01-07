import pandas as pd

workbook = pd.read_excel('enrich_file.xlsx', 'Rules', engine='openpyxl')
print(workbook)