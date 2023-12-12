import pandas as pd 

fichier_source = pd.ExcelFile("source\FichierSource.xlsx")
fichier_destination = pd.ExcelFile("destination\Fichier_destination.xlsx")

fichier_source_spec = pd.read_excel(fichier_source,"")