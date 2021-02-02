#!/usr/bin/env python
# coding: utf-8

# ***
# ## <center> DESCARGA DEL PRODUCTO GRILLADO PISCO</center>
# ### <center>CÓDIGO      :     PYTHON </center>
# ### <center>LIBRERIAS   :     FTPLIB - RISE </center>
# ### <center>POR         :     VICTOR B. VELÁSQUEZ HUAMÁN </center>
# ### <center>NOMBRE      :     PYPISCO </center>
# ### <center>FECHA       :     MARCH 23, 2019</center>
# ***
# >TEMA: Descarga de Precipitación del Producto  Grillado **PISCO-SENAMHI**

# ***Intalación de Librerias***

# In[ ]:


#!pip install tqdm
#!pip install rise


# ***Importación de Librerias***

# In[1]:


from tqdm import tnrange, tqdm_notebook
import datetime
#import unittest
import ftplib
import os


# ### 1.0  PRODUCTO GRILLADO PISCO 
# <p style="text-align: justify;"> Se denomina PISCO por sus siglas a <b>Peruvian Interpolation data of the SENAMHIs Climatological and Hidrological Observations</b>. Las cuales se encuentra en todo el territorio Peruano, las que
# son estimaciones por sensoramiento remoto es una fuente alterna de
# información siendo calibradas y validadas debido a la naturaleza indirecta de la
# medición. Climate Hazards Group Infrared Precipitation with Stations (CHIRPS)
# y Peruvian Interpolation data of the SENAMHI’s Climatological and Hidrological
# Observations (PISCO).</p>
# 
# 
# <figure>
# <img src = "./Imagenes/Pisco.PNG" alt = "Sol" style="width:500px"> </img>
#     <figcaption> Fuente :Adaptado desde "Generación de datos grillados de precipitación diaria y su utilidad para el monitoreo de inundaciones", Lavado et al.</figcaption> 
# </figure>
# 

# ### 2.0  DISTRIBUCIÓN ESPACIAL Y TEMPORAL
# 
#  #### 2.1  DISTRIBUCIÓN ESPACIAL
# Actualmente brindan esta información en una resolución
# espacial de 0.1 grados latitud y longitud. Funk et al. (2015, p. 10), menciona
# que CHIRPS valida las precipitaciones para el Perú con 403 estaciones que le
# brinda la Autoridad Nacional del Agua (ANA) Perú
# 
#  #### 2.2  DISTRIBUCIÓN TEMPORAL
# En la Plataforma FTP, se disponen de diferentes versiones y se localizan 02 archivos de con variaciones temporales las que se  describe a continuacion:
# 
# <ul>
# 
#   <li>Cuenta con una representación temporal desde el 01/01/1981 hasta la 31/07/2018,a escala diaria,</li>
# 
#   <li>Cuenta con una representación temporal desde el 01/01/1981 hasta la 31/12/2016,a escala diaria.</li>
# 
# </ul>
# 
# 
# |Data|ID| Datos   | Desde |Hasta|
# |---------|--|------|------|--------------|
# |Stable|N°1|01|01/01/1981|31/12/2016|
# |Unstable|N°2|13726|01/01/1981|31/07/2018|
# 

# ### 3.0 DIRECCIÓNES DE DESCARGA  
# El producto Pisco se encuentra con una resolución espacial de 0.1° y temporal
# desde el año 1981 hasta los años de 2016 y 2018, se puede descargar de varios sitios Web
# entre ellos tenemos los siguientes:
# <ul>
#  <li>International Research Institute for Climate Society</li> 
#     
# [IRI](http://iridl.ldeo.columbia.edu/SOURCES/.SENAMHI/.HSR/.PISCO/).
# 
#  <li>Desde el servidor Senamhi - ftp://ftp.senamhi.gob.pe/PISCOp_V2.1_beta</li>
# 
# [SENAMHI](https://www.senamhi.gob.pe/?p=observacion-de-inundaciones).
#     
# </ul>
# 
# 
# *
#     
# <figure>
# <img src = "./Imagenes/Pisco_.PNG" alt = "Sol" style="width:350px"> </img>
# <figcaption>Fuente :Elaboracion Propia - Desarrollado en software Qgis</figcaption> 
# </figure>

# ### 4.0 DESCARGA DESDE PYTHON
# 

# In[10]:


class Download_Dail_Pisco():  
    def __init__(self):
        Direction = 'ftp.senamhi.gob.pe'
        User = 'publi_dgh2'
        Password = '123456'
        
        self.Tp = ftplib.FTP(Direction)
        self.Tp.login(User,Password)
        
        #Especifique El periodo de busqueda 
        self.Start_Date = datetime.date(2011, 4, 2)
        self.End_Date = datetime.date(2011, 4, 10)
        
        # Ubicacmos el Directorio
        path = "C:\\Users\\ASUS\\Desktop"
        #path = "F:\\"
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


# In[ ]:


if __name__ == "__main__": 
    t =Download_Dail_Pisco()
    t.Download()


# ### 5.0 REFERENCIAS
# <ul>
#  <li> Senamhi </li>
#     
# [SENAMHI](https://www.senamhi.gob.pe/?p=observacion-de-inundaciones).
#    
#   <li> Libreria FtpLib </li>
#     
# [Ftplib](https://www.it-swarm-es.com/es/python/python-descargue-un-archivo-traves-de-un-servidor-ftp/1067995286/).   
#     
# <li> GitHub </li>
#     
# [Ftplib](https://github.com/bryan142857/Python).
#     
# </ul>
# 

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

