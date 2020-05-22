import requests
from datetime import datetime
import zipfile
import time
import pandas as pd
import os

#valores
url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
file = requests.get(url)
data = datetime.now().strftime('%Y-%m-%d')
path = 'data\\raw\\megasena\\'
path_temp = '.\\temp\\D_megase.zip'
path_swamp ='data\\swamp\\megasena\\'


#variaveis
path_raw = os.path.join(path,data)
path_html= os.path.join(path_raw,'d_mega.htm')
path_csv = os.path.join(path_swamp,'d_mega.csv')

#criando arquivo temp
print('Salvando arquivo HTML local temporario...\n')
time.sleep(2)
open(path_temp, 'wb').write(file.content)

#descompactando arquivo e direcionando pra destino
print("Extraindo arquivo para pasta de destino...\n")
time.sleep(2)
zip_file = zipfile.ZipFile(path_temp, 'r')
for files in zip_file.namelist():
    zip_file.extract(files, path_raw)
zip_file.close()


#conversão de arquivo
print("convertando arquivo ...\n")
df = pd.read_html(path_html,thousands='.',decimal='.')[0]
time.sleep(2)

#destinando arqui ao path
print('salvando arquivo csv')
df.to_csv(path_csv,sep=';',index=False)

#printando arquivo
tabela = pd.read_csv(path_csv)
print(tabela)


#valores

#data = datetime.now().strftime('%Y-%m-%d')
lake = 'data\\lake\\megasena\\'

#variaveis
path_lake = os.path.join(lake,data)
csv_lake = os.path.join(path_lake,'tratado.csv')

print('lendo csv')
read_csv = pd.read_csv(path_csv, sep=';', encoding='utf-8')
print('limpando csv')

clean_csv = read_csv.apply(lambda x: x.replace('&nbsp', ''))


print('salvando arquivo')
clean_csv.to_csv('tratado.csv', sep=';', index=False)