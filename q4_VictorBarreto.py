import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"
)

crs = mydb.cursor()

exec_sql_cmd = lambda cmd, crs : crs.execute(cmd)

create_database = lambda db, crs : exec_sql_cmd("CREATE DATABASE IF NOT EXISTS " + db + ";\n", crs)
use_database = lambda db, crs: exec_sql_cmd("USE " + db + ";\n", crs)

create_table = lambda table, attrs, crs : exec_sql_cmd("CREATE TABLE IF NOT EXISTS " + table + "(" + attrs + ");\n", crs)

select = lambda cols, table, where, crs : exec_sql_cmd("SELECT " + cols + " FROM " + table + " WHERE " + where + ";\n", crs)
                                                           
insert = lambda table, cols, values, crs : exec_sql_cmd("INSERT INTO " + table + "(" + cols + ") VALUES (" + values + ");\n", crs)

delete = lambda table, where, crs : exec_sql_cmd("DELETE FROM " + table + " WHERE " + where + ";\n", crs)

create_database("pythondb", crs)
use_database("pythondb", crs)
create_table("USUARIOS", "id INT NOT NULL, nome VARCHAR(45) NOT NULL, console VARCHAR(45) NOT NULL, PRIMARY KEY(id)", crs)
create_table("JOGOS", "id INT NOT NULL, nome VARCHAR(45) NOT NULL, data_lancamento DATE NOT NULL, PRIMARY KEY(id)", crs)
# insert("USUARIOS", "id, nome, console", "1, \"Jorge\", \"XBox\"", crs)
# insert("USUARIOS", "id, nome, console", "2, \"Paulo\", \"Playstation\"", crs)
# insert("JOGOS", "id, nome, data_lancamento", "1, \"Halo 3\", '2007-09-25'", crs)
# insert("JOGOS", "id, nome, data_lancamento", "2, \"God of War Ragnarok\", '2022-11-09'", crs)
select("*", "USUARIOS", "true", crs)

res = crs.fetchall()
print_result = lambda crs : [print (x) for x in res]

print_result(crs)