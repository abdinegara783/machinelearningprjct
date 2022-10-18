#mengkopy data
dataku=dataku.copy()
#Melihat dimensi data
dataku.shape
#melihat variabel null(missing value)
# Mendeteksi kolom yang memiliki data NA
kolom_na = [kolom for kolom in dataku.columns if dataku[kolom].isnull().sum() > 0]
kolom_na
#Mereduksi Dimensi Data
dataku.drop(dataku.columns[[0,1,2,3,4,5]], axis=1, inplace=True)
#Melihat dimensi data
dataku.shape
#Melihat variabel unik di setiap kolom
dataku.nunique()
#Melihat data missing value
dataku.isna()
#Ringkasan Missing Value
dataku.isna().sum()
#banyak NaN pada Kode diagnosis ICD 10 adalah 1380241
#Mencari banyak peserta yang sehat (1422387)
dataku.groupby('Status Pulang Peserta').count()
#menghitung kode diagnosis ICD 10 yang tidak missing value (2676657)
dataku.count()
#melihat kode diagnosis ICD 10 yang memiliki status pulang peserta sehat
dataku[(dataku['Status Pulang Peserta'] == 'Sehat')]
