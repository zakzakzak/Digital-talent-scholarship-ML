# artist: Name of the artist
# album: Name of the album
# released_year: Year the album was released
# length_min_sec: Length of the album (hours,minutes,seconds)
# genre: Genre of the album
# music_recording_sales_millions: Music recording sales (millions in USD) on [SONG://DATABASE]
# claimed_sales_millions: Album's claimed sales (millions in USD) on [SONG://DATABASE]
# date_released: Date on which the album was released
# soundtrack: Indicates if the album is the movie soundtrack (Y) or (N)
# rating_of_friends: Indicates the rating from your friends from 1 to 10


import pandas as pd

# read data from csv as data frame
df_csv = pd.read_csv('D:/boku no projecto/python/dts/Sesi3_file_tools/insurance.csv')
print("\n-------------------\n")

# print bagian teratas aja
print(df_csv.head())
print("\n-------------------\n")

# Mendapatkan data dari web
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df_exc = pd.read_excel(xlsx_path)
print(df_exc.head())
# print(df_exc)
print("\n-------------------\n")


# menampilkan kolom tertentu saja
x = df_csv[['age', 'sex']]
print(x.head())

# bisa 1D type series
x = df_exc['Length']
print(type(x))
print("\n-------------------\n")

# get column as dataframe type
x = type(df_exc[['Artist']])
print(x)
print("\n-------------------\n")

# df banyak kolom
y = df_exc[['Artist','Length','Genre']]
print(y)
print("\n-------------------\n")

# bisa juga dipakai dengan cara lokasi yaitu df.iloc[row,column] dengan mulai array 0
# df.iloc[row,column]
print(df_exc.iloc[0, 4])
print("\n-------------------\n")

# bisa juga dipanggil dengan df.loc[row, 'attribute']
# df.loc[row, 'attribute']
print(df_exc.loc[0, 'Artist'])
print(df_exc.loc[1, 'Artist'])
print(df_exc.loc[0, 'Released'])
print("\n-------------------\n")

# iloc[mulai:sebelum, mulai: sebelum]   *bukan jumlah panjang
# kecuali jika nama atribut 'mulai':'sampai'
# iloc untuk col angka, loc untuk col atribut
print(df_exc.iloc[0:2, 0:3])
df_exc.loc[0:2, 'Artist':'Released']
print("\n-------------------\n")


# excercise
# q <= rating column as dataframe
q = df_exc[["Rating"]]
print(type(q.head()))
print("\n-------------------\n")

# q <= released and artist column as dataframe
q = df_exc[["Released","Artist"]]
print(q.head())
print("\n-------------------\n")

# 2nd row 3rd column
q = df_exc.iloc[1,2]
print(q)
























# END
