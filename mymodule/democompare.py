import pandas as pd
sheet1=pd.read_excel("c://mydataset//Arrival_Dates.xlsx")
sheet2=pd.read_excel("c://mydataset//Arrival_Dates_Final.xlsx")
df_sheet = sheet1.compare(sheet2,keep_equal=False,align_axis=1)
df_sheet.to_excel("c://exceldata//diff1.xlsx")
print(df_sheet)