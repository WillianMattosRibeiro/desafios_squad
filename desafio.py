import requests, csv, zipfile, os
from datetime import datetime
import pandas as pd


#getUrl And Save
url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
today = datetime.now().strftime('%Y-%m-%d')
filename = requests.get(url)
open ('C:/Atividade/D_megase.zip/', 'wb').write(filename.content)


#extraindo e salvando em pastas com data de ultima atualização

resulmega = zipfile.ZipFile('C:/Atividade/D_megase.zip')
resulmega.extractall ('C:/Atividade/data/raw/megasena' + datetime.now().strftime('%Y-%m-%d'))
resulmega.close()




#Convertendo pra CSV
df_mega = pd.read_html(html_file ,thousands='.',decimal='.')[0]
df_mega.to_csv('C:/Atividade/data/swamp/megasena',sep=';',encoding='latin1', index =False)


