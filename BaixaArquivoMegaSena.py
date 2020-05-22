import io
import requests
#from zipfile import ZipFile
from datetime import datetime
from CopiaCVSparaSWAMP import copiaCSV

import zipfile

now = datetime.now().strftime("%Y%m%d-%H%M%S")
path = 'C:/Documentos/Projeto-Lucky/projeto_lucky/output/data/raw/megasena/' + now

# Função baixar o arquivo zipado -  resultados loterias caixa
# def baixarResultadosMegasena():
#     url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
#     req = requests.get(url)

#     fileName = path+'/mega.zip'
#     file = open(fileName, 'wb') # ATENCAO: ABRINDO UM ARQUIVO QUE AINDA NAO EXISTE
#     for chunk in req.iter_content(100000):
#         file.write(chunk)
#     file.close()

def baixarResultadosMegasena():
    url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'
    req_file = requests.get(url)
    return req_file

# Função descompactar o arquivo zipado criando as pastas por data/hora -  resultados loterias caixa
# def descompactarResultadosMegasena():
#     file_name = "C:/temp/mega.zip" # ATENCAO: o arquivo ainda esta em memoria, tem como utilizalo para criar o path direto
#     with ZipFile(file_name, 'r') as zip:
#         zip.printdir()
#         zip.extractall(path)

# def descompactarResultadosMegasena(req_file, path):
#     with ZipFile(req_file, 'r') as zip: # NAO TEM COMO DESCOMPACTAR POIS AINDA E UMA REQUISICAO
#         zip.extractall(path)

def descompactarResultadosMegasena(req_file, path):
    arquivo_zip = zipfile.ZipFile(io.BytesIO(req_file.content)) # https://stackoverflow.com/questions/11914472/stringio-in-python3
    arquivo_zip.extractall(path)
    nome_arq = arquivo_zip.namelist()[0]
    print(nome_arq)
    return nome_arq

obj_req = baixarResultadosMegasena()
descompactarResultadosMegasena(obj_req, path)
copiaCSV(path+"/"+nome_arq, now)