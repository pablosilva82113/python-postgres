import psycopg2
import csv

conn = psycopg2.connect("dbname='actividades_esenciales' user='local_user' host='localhost' password='123456789'")
cur = conn.cursor()
sql = "TRUNCATE TABLE establecimientos"
cur.execute(sql)
conn.commit()
sql = "TRUNCATE TABLE actividades"
cur.execute(sql)
conn.commit()
sql = "TRUNCATE TABLE vialidades"
cur.execute(sql)
conn.commit()
with open('actividades_no_esenciales.csv',newline='',encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        clave = row[0]
        nombre = row[1]
        razon = row[2]
        consulta = "SELECT * FROM establecimientos WHERE clave = '"+clave+"'"
        cur.execute(consulta)
        if cur.rowcount == 0:
            cur.execute("INSERT INTO  establecimientos (clave, nombre, razon_social) VALUES ('"+clave+"', '"+nombre+"', '"+razon+"')")
            conn.commit()
        else:
            print("Actividad ya existe")
        codigo_actividad = row[3]
        nombre = row[4]
        per_ocu = row[5]

        consulta = "SELECT * FROM actividades WHERE codigo_act = '"+codigo_actividad+"'"
        cur.execute(consulta)
        if cur.rowcount == 0:
            cur.execute("INSERT INTO  actividades (codigo_act, nombre_act, per_ocu) VALUES ('"+codigo_actividad+"', '"+nombre+"', '"+per_ocu+"')")
            conn.commit()
        else:
            print("Actividad ya existe")
        tipo_vialidad= row[6]
        nombre_vial= row[7]
        tp_v_e_1= row[8]
        nombre_v_e_1= row[9]
        tp_v_e_2= row[10]
        nombre_v_e_2 = row[11]
        tp_v_e_3= row[12]
        nombre_v_e_3 = row[13]
      
        consulta = "SELECT * FROM vialidades WHERE tipo_vialidad = '"+tipo_vialidad+"'"
        cur.execute(consulta)
        if cur.rowcount == 0:
            cur.execute("INSERT INTO  vialidades (tipo_vialidad, nombre_vialidad, tipo_v_e_1, nom_v_e_1, tipo_v_e_2, nom_v_e_2, tipo_v_e_3, nom_v_e_3) VALUES ('"+tipo_vialidad+"', '"+nombre_vial+"', '"+tp_v_e_1+"', '"+nombre_v_e_1+"', '"+tp_v_e_2+"', '"+ nombre_v_e_2+"', '"+tp_v_e_3+"', '"+nombre_v_e_3+"');")
            conn.commit()
        else:
            print("Vialidad ya existe")

        
