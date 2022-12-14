import mysql.connector
from mysql.connector import Error
from st_aggrid import AgGrid
import pandas as pd
from pathlib import Path

import streamlit as st
#import pypyodbc

#import unicodecsv as csv
import csv
import speech_recognition as sr
import pyodbc

# Title
st.title("SR using streamlit !!!")

if st.button('SPEAK'):
    #current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    #st.write(current_dir)
    #path = Path(__file__).parent.absolute()
    #fp2=path('sahansha.accdb')
    #fp = Path(path,'dbfiles','sahansha1.accdb')
    #fp1="C:\Users\sahar\Desktop\srstreamlit\sahansha.accdb"
    #st.write(path)
    #st.write(fp)
    #filespec=r"fp"
    #DBQl =str(current_dir)+"/dbfiles/sahansha1.accdb"
    #st.write('how are u')
    #conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"+ r"DBQ=DBQ1;"+r"UID=root;"+r"PWD=saha;")
    #conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"+r"DBQ={};".format(fp))
    
    #conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"+ r"DBQ=C:\Users\sahar\Desktop\srstreamlit\dbfiles\sahansha1.accdb;"+r"UID=root;"+r"PWD=saha;")
    def init_connection():
        return mysql.connector.connect(**st.secrets["mysql"])

    conn = init_connection()
    #conn = mysql.connector.connect(host='localhost',database='sahanum',port='124',
    #                                   user='root',
    #                                   password='saha',charset="utf8mb4")
    cursor = conn.cursor()
    cursor.execute('select * from productdb')
   
    #for row in cursor.fetchall():
        #st.write(row)
        
    with open('Output.csv', 'w',encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['a','b','c','d','e','f','g','h'])
        for row in cursor.fetchall() :
            writer.writerow(row)

    st.write("done")
    df = pd.read_csv('Output.csv')
    AgGrid(df)





