import pandas as pd
import pdfkit as pdf
import sqlite3
import pandas as pd
from tqdm import tqdm
def insertar_datos():
    df = pd.read_excel("/home/marco/Downloads/Separador/DIVIDIR.xlsx",sheet_name="Hoja1",header=0)
    for i,valor in enumerate(tqdm(df['DIVIDIR'])):
        cursor.execute("INSERT INTO DIV VALUES ('"
             +str(df.at[df.index[i],'DIVIDIR'])+
        "','"+str(df.at[df.index[i],'SECCION DOMICILIO'])+
        "','"+str(df.at[df.index[i],'LOCALIDAD'])+
        "','"+str(df.at[df.index[i],'MZA'])+
        "','"+str(df.at[df.index[i],'NOMBRE'])+
        "','"+str(df.at[df.index[i],'CALLE'])+
        "','"+str(df.at[df.index[i],'EXT'])+
        "','"+str(df.at[df.index[i],'INT'])+
        "','"+str(df.at[df.index[i],'TELEFONO'])+
        "','"+str(df.at[df.index[i],'SECCION VOTA'])+
        "','"+str(df.at[df.index[i],'CASILLA'])+
        "','"+str(df.at[df.index[i],'CONSECUTIVO'])+"')")

connection = sqlite3.connect('BASEDivicion.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS DIV
              (DIVIDIR TEXT, 
              SECCION_DOMICILIO TEXT, 
              LOCALIDAD TEXT,
              MZA TEXT,
              NOMBRE TEXT,
              CALLE TEXT,
              EXT TEXT,
              INT TEXT,
              TELEFONO TEXT,
              SECCION_VOTA TEXT,
              CASILLA TEXT,
              CONSECUTIVO TEXT)''')
insertar_datos()
connection.commit()
connection.close()