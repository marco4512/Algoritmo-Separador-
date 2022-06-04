import pandas as pd
import pdfkit as pdf
import sqlite3
import pandas as pd
from tqdm import tqdm
import os
from typing import Literal
dfx =pd.read_excel("./DIVIDIR.xlsx",sheet_name="Hoja1",header=0)
Solo_Encargados=[]
for valor in tqdm(dfx['DIVIDIR']):
    if valor not in Solo_Encargados:
        Solo_Encargados.append(valor)
connection = sqlite3.connect('BASEDivicion.db')
cursor = connection.cursor()
for i,val in enumerate(tqdm(Solo_Encargados)):
    df=pd.read_sql_query("SELECT * FROM DIV WHERE DIVIDIR ='"+str(val)+"'", connection)
    df.iloc[:, 1:11].to_html('./JUNTAR/HTMLS/'+str(i)+'.html')
    nazivFajla='./JUNTAR/PDF/'+str(i)+'.pdf'
    pdf.from_file('./JUNTAR/HTMLS/'+str(i)+'.html', nazivFajla)
connection.close()