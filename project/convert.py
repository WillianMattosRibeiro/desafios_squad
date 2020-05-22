import pandas as pd
import os


print("convertando arquivo ...")
df = pd.read_html('./data/raw/megasena/2020-05-21/d_mega.htm')[0]
'''
print('Removendo arquivo csv existente')
if os.path.exists('./data/swamp/megasena/d_mega.csv'):
   os.remove('./data/swamp/megasena/d_mega.csv')
'''
print('salvando arquivo csv')
df.to_csv('./data/swamp/megasena/d_mega.csv')
tabela = pd.read_csv('./data/swamp/megasena/d_mega.csv')
print(tabela)




