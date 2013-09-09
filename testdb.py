
# using mysql odbc driver http://www.mysql.com/downloads/connector/odbc/
import pyodbc
#connect to localhost
cstr = "DRIVER={MySQL ODBC 3.51 Driver}; SERVER=localhost;DATABASE=test00; UID=root; PASSWORD=shesuper;"
cstr = "DRIVER={MySQL ODBC 3.51 Driver}; SERVER=localhost; PORT=3306;DATABASE=test00; UID=root; PASSWORD=shesuper;"
cstr = "Driver={MySQL ODBC 5.1 Driver};Server=127.0.0.1;Port=3306;Database=test00;User=root; Password=shesuper;Option=3;"
cstr = "DRIVER={FreeTDS};SERVER=127.0.0.1;DATABASE=test00;UID=0;PWD=shesuper"
cstr = "DRIVER={FreeTDS};SERVER=127.0.0.1;PORT=3306;DATABASE=test00;UID=root;PWD=shesuper"
cstr = "DRIVER={MySQL ODBC 5.1 Driver};SERVER=localhost;DATABASE=tester;USER=root;PASSWORD=shesuper;OPTION=3;"
cstr = "Driver={MySQL ODBC 5.1 Driver};Server=localhost;Port=3306;Database=tester;User=root;Password=shesuper;Socket=MySQL;Option=3;"
cnxn = pyodbc.connect(cstr)
cursor = cnxn.cursor()

#select all tables from all databases

cursor.execute("select t1.TABLE_SCHEMA field1,t1.TABLE_NAME field2  from `TABLES` t1;")
rows = cursor.fetchall()
for row in rows:
    print "%s.%s" % (row.field1,row.field2)


