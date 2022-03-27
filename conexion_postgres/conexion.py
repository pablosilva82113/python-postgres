#conectar postgres
import psycopg2
import csv

 
#conectar a la base de datos

conn = psycopg2.connect("dbname='actividades_esenciales' user='local_user' host='localhost' password='pablo821'")
cur = conn.cursor()
sql = "TRUNCATE TABLE establecimientos"
cur.execute(sql)
conn.commit()
with open('actividades_no_esenciales.csv',newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        clave = row[0]
        nombre = row[1]
        razon = row[2]
        sql = "INSERT INTO  establecimientos (clave, nombre, razon_social) VALUES ('"+clave+"', '"+nombre+"', '"+razon+"')"
        cur.execute(sql)
        conn.commit()

base = conn.cursor()
consulta="SELECT * FROM establecimientos"
base.execute(consulta)
resultado=base.fetchall()
print(resultado)
print(base.rowcount)


      
