import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')

# menapilkan head
print(df_can.head())
print("------------/n")

# menapilkan tail
print(df_can.tail())
print("------------/n")

# informasi
print(df_can.info())
print("------------/n")
