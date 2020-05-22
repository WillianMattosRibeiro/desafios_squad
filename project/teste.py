import requests
from datetime import datetime
import zipfile
import time
import pandas as pd
import os

url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
file = requests.get(url)
path = 'data\\raw\\megasena\\'
file_zip = 'temp\\D_megase.zip'
file_swamp = 'data\\swamp\\megasena\\'


data = datetime.now().strftime('%Y-%m-%d')
file_path = os.path.join(path,data)

file_html = os.path.join(file_path,'d_mega.htm')
file_csv = os.path.join(file_swamp,"d_mega.csv")

print('Salvando arquivo HTML local temporario...\n')
time.sleep(2)

open(file_zip, 'wb').write(file.content)

print("Extraindo arquivo para pasta de destino...\n")
time.sleep(2)

#descompactando arquivo e direcionando pra destino
zip_file = zipfile.ZipFile(file_zip, 'r')
for files in zip_file.namelist():
    zip_file.extract(files, file_path)
zip_file.close()



print("convertando arquivo ...\n")
df = pd.read_html(file_html)[0]
time.sleep(2)

print('salvando arquivo csv')
df.to_csv(file_swamp,"d_mega.csv")

tabela = pd.read_csv(file_csv)
print(tabela)
