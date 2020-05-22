from datetime import datetime
import pandas as pd
import os
import csv

#valores

data = datetime.now().strftime('%Y-%m-%d')
path_lk = 'data\\lake\\megasena\\'
path_swamp ='data\\swamp\\megasena\\'

#variaveis
path_csv = os.path.join(path_swamp,'d_mega.csv')
path_lake = os.path.join(path_lk, data)
path_csv_lake = os.path.join(path_lake,'tratado.csv')

print('lendo csv')
read_csv = pd.read_csv(path_csv, sep=';', encoding='utf-8')
print('limpando csv')

clean_csv = read_csv.apply(lambda x: x.replace('&nbsp', ''))


print('salvando arquivo')
clean_csv.to_csv(path_lake, sep=';', encoding='utf-8', index=False)

