#!/usr/bin/env python
# coding: utf-8

# In[1]:


#from pyunitreport import HTMLTestRunner
#from selenium import webdriver
#from time import sleep
from tqdm import tnrange, tqdm_notebook
import datetime
import unittest
import ftplib
import os


# In[2]:


class Download_Dail_Pisco():  
    def __init__(self):
        Direction = 'ftp.senamhi.gob.pe'
        User = 'publi_dgh2'
        Password = '123456'
        
        self.Tp = ftplib.FTP(Direction)
        self.Tp.login(User,Password)
        
        #Especifique El periodo de busqueda 
        self.Start_Date = datetime.date(2016, 1, 1)
        self.End_Date = datetime.date(2018, 7, 31)
        
        # Ubicacmos el Directorio
        path = "C:\\Users\\ASUS\\Desktop"
        path = "F:\\"
        os.chdir(path)
        os.mkdir("Download_Pisco")
        self.Path = os.chdir(path +"\\Download_Pisco")
        
        #Archivos 
        print(self.Tp.pwd())
        
        #Ubicacion de los archivos diarios de precipitacion
        self.Dir = self.Tp.cwd('PISCOp_V2.1_beta/Daily_Products/unstable/PISCOpd')
        #self.List = self.Tp.retrlines('LIST')
            
    def Download(self):
        Intervalo = datetime.timedelta(days=1)
        for i in tnrange((self.End_Date - self.Start_Date + datetime.timedelta(days=1)).days, desc = "!! Descargando !!"):
            Name_Precipitation = str(self.Start_Date + i*Intervalo)
            self.Tp.retrbinary("RETR "+'PISCOpd_V2.1.'+ Name_Precipitation +'.tif', open(Name_Precipitation+'.tif', 'wb').write)
        self.Tp.quit()
    

#if __name__ == "__main__":
#    unittest.main(
#        verbosity = 2,
#        testRunner= HTMLTestRunner(
#            output ='Download_Dail_Pisco',
#            report_name = 'reporte_Pisco',
#        )
#    )
f = Download_Dail_Pisco()    
f.Download()


# In[ ]:


#if __name__ == "__main__":
#    unittest.main(
#        verbosity = 2,
#        testRunner= HTMLTestRunner(
#            output ='Mercado libre',
#            report_name = 'reporte',
#        )
#    )
f = Download_Dail_Pisco()    
f.Download()
#f.teorDown


# In[ ]:


formato_fecha = "%d-%m-%Y"
day_delta = datetime.timedelta(days=1)
day_dos = datetime.timedelta(days=2)
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 3, 1)

for i in tqdm(range(0, (end_date-start_date  + day_dos).days)):
    print (i)


# In[ ]:




