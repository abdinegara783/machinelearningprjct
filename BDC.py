#mengkopy data
dataku=dataku.copy()
#Melihat dimensi data
dataku.shape
#melihat variabel null(missing value)
# Mendeteksi kolom yang memiliki data NA
kolom_na = [kolom for kolom in dataku.columns if dataku[kolom].isnull().sum() > 0]
kolom_na
