import pandas as pd
import numpy as np
import glob
import os


#akifffffffff
#sadsadadasd

#Bu program .csv uzantılı birden çok dosyayı birleştirmek için kullanılır



os.getcwd()
#Klasor uzantisini secin
path = u"/Users/muratcansinim/Desktop/ASELSAN/_yapilan_calismalar/_Lidar_Verileri_200330/26022020_Lidar_Veriler"
#liste = os.listdir(path)





# Selecting csv files
all_files = glob.glob(path + "/*.csv")

# Reading and concating all Csv files
all_csv = (pd.read_csv(f,encoding='UTF-16 LE') for f in all_files)
df_merged   = pd.concat(all_csv, ignore_index=True)

#Kayit adini belirleyin, bu dosyanin bulundugu klasorde olusacaktir.
df_merged.to_csv( "merged.csv")
