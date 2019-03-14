import pyodbc

server = 'tcp:jacobemorycfserver.database.windows.net,1433'
database = 'AddressBook'
username = 'Falconier'
password = '9483dae1-8b8e-4959-9919-6b8bab5c035c'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};Server='+server+';Database='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# select
cursor.execute('select * from ' + database+ '.dbo.EmailBook')
for row in cursor:
    print(row)

## todo:fix insertion
##region insertion
FN = input("enter first name: ")
LN = input("enter last name: ")
E = input("enter email address:")
# insert
cursor.execute("insert into "+database+".dbo.EmailBook (FirstName, LastName, Email) values (?,?,?)", FN,LN,E)
# save
cnxn.commit()
# update
# update EmailBook set Email = 'bullinj1714@forsythtech.edu' where FirstName = 'Jacob' and LastName = 'Bullin'
cursor.execute('select * from ' + database+ '.dbo.EmailBook')
for row in cursor:
    print(row)
##endregion

cursor.close()
del cursor
cnxn.close()