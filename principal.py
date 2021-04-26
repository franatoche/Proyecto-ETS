import sqlite3
from sqlite3 import Error

# Función de conexión
def sql_conexion(nombrebd):
    try:
        conectado = sqlite3.connect(nombrebd)
        return conectado
    except Error:
        print(Error)

def sql_ejecutar(cursor, sentencia):
    try:
        resultado = cursor.execute(sentencia)

        return resultado
    except Error:
        print(Error)


# Establecimiento de conexión
empleado = sql_conexion('empleado.db')
# Creación del cursor para ejecutar sentencias SQL
cursoremp = empleado.cursor()
#sql_ejecutar(cursoremp, "CREATE TABLE IF NOT EXISTS Usuario (codigo_c	INTEGER, nombre VARCHAR(30), PRIMARY KEY(codigo_c))")
#sql_ejecutar(cursoremp, "INSERT INTO Usuario VALUES (2, 'Fernando González')")
# Instalar DB Browser for SQLite
empleado.commit()
resultado = sql_ejecutar(cursoremp, "SELECT * FROM Empleado")

tablaemp = cursoremp.fetchall()
print("*******************************")
print("EMPLEADO")
print("*******************************")
print("CODIGO\t\tNOMBRE", end="")
for i in range(len(tablaemp)):
    print(" ")
    for j in range(len(tablaemp[i])):
        print(tablaemp[i][j], end="\t\t")
print("\n*******************************")

# Cerrar conexión

empleado.close()









