import PyQt6
#from PyQt6 import QMainWindow
import pyodbc
import sqlite3
from sqlalchemy import create_engine, select
import random
#from sqlachemy.orm import Session
#from PyQt6.QtSql import QSqlDatabase
#from tables import Base, User,

user = password = db = "wsrprbj-04"
driver = "ODBC+Driver+17+for+SQL+Server"
server = "SERV-PRB/MSSQL"
engine = create_engine(f"mssql://@{server}/{db}?driver={driver}&trusted_connection=yes")
#Base.metadata.create_all(engine)
con = sqlite3.connect("dbo.pacient")
cur = con.cursor()
eng = 'as5rtg'
for i in range(100):
    result = cur.execute("UPDATE pacient" +
                        "\nSET surname = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET fathername = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET num&ser = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET birthday = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET sex(male, female) = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET adress = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET phone = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET mail = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET medcard = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET medcard start = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET last visit = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET next visit = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET strax polis = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET lose strax polis = " + eng +
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET diagnoz = """ + eng + 
                        "\nWHERE id = " + str(i) +
                        "\nUPDATE pacient" +
                        "\nSET history ill = " + eng +
                        "\nWHERE id = " + str(i) + "")
    con.commit()
con.close()
#"print("Hello world")
#cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                      "Server=serv-prb/mssql;"
#                      "Database=wsrprbj-04;"
#                      "Trusted_Connection=no;"
##                      "UID=wsrprbj-04;"
#                     "PWD=wsrprbj-04;")
#"
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex = MyWidget()
#    ex.show()
#    sys.exit(app.exec())