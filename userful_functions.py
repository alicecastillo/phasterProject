#useful functions used in different subfiles

import mysql.connector

#universal connection to db
def runMySQLOperation(op):
    scheduledb = mysql.connector.connect(
        user="lab_admin",
        password="Phaster2020!",
        database="bradley",
        host = "localhost"
    )
    cursor = scheduledb.cursor(buffered=True)
    cursor.execute(op)
    scheduledb.commit()
    cursor.close()
    scheduledb.close()
    return cursor