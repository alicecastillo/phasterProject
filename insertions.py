#contains all necessary insertions

import mysql.connector
from userful_functions import runMySQLOperation


def insertRow(row):
    query = ("""INSERT INTO summary(`Accession`, `Region`, `Region Length`, `Completeness`, `Score`, 
            `# Total Proteins`, `Region Position`, `Most Common Phage`, `GC Percentage`, `Details`) 
            VALUES (%s)""" %(row))
    cursor = runMySQLOperation(query)


def getAccesses():
    query = ("SELECT accessions FROM accessionNumbers")
    accs = []
    cursor = runMySQLOperation(query)
    for acc in cursor:
        accs.append(acc)
    return accs

