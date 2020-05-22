import os
from datetime import datetime
from zipfile import ZipFile
import pandas as pd
import requests

today = datetime.now().strftime('%Y-%m-%d')

## criando as pastas recursivamente ( caso as pastas já existam, elas não são criadas novamente)

os.makedirs('C:/Users/BlueShift/Desktop/data/raw/megasena', exist_ok=True)
os.makedirs('C:/Users/BlueShift/Desktop/data/swamp/megasena/' + today, exist_ok=True)
os.makedirs('C:/Users/BlueShift/Desktop/data/lake/megasena/' + today, exist_ok=True)
os.makedirs('C:/Users/BlueShift/Desktop/data/teste', exist_ok=True)

# Extraindo o resultados da mega-sena do site e salvando na pasta teste

url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
myfile = requests.get(url)
open('C:/Users/BlueShift/Desktop/data/teste/D_megase.zip', 'wb').write(myfile.content)

## descompactando o arquivo da pasta 'teste'  e salvando em uma pasta nomeada com a data de hoje

file = "C:/Users/BlueShift/Desktop/data/teste/D_megase.zip"

with ZipFile(file, 'r') as zip:
    zip.extractall('C:/Users/BlueShift/Desktop/data/raw/megasena/' + today)

#### Criação das variáveis para a busca do caminho correto dos arquivos

html_path = os.path.join('C:/Users/BlueShift/Desktop/data/raw/megasena/', today)
html_file = os.path.join(html_path, "d_mega.htm")
csv_path = os.path.join('C:/Users/BlueShift/Desktop/data/swamp/megasena/', today)
csv_file = os.path.join(csv_path, "d_mega.csv")
adjusted_csv_path = os.path.join('C:/Users/BlueShift/Desktop/data/lake/megasena/', today)
adjusted_csv_file = os.path.join(adjusted_csv_path, "d_mega.csv")

#### Transformando o html em csv e salvando no diretório nomeado com a data de hoje

df = pd.read_html(html_file, thousands='.', decimal='.')[0]
df.to_csv(csv_file, sep=';', encoding='latin1', index=False)

##### Executando a limpeza do arquivo csv e salvando um novo csv na camada lake

read_csv = pd.read_csv(csv_file, sep=';', encoding='latin1')
clean_csv = read_csv.apply(lambda x: x.replace('&nbsp', ''))
clean_csv.to_csv(adjusted_csv_file, sep=';', encoding='latin1', index=False)