import  pandas as pd
from    sqlalchemy import create_engine


def cargaDatos(usuario, clave, servidor, db, table):
    engine = create_engine('mysql+pymysql://{usuario}:{clave}@{servidor}/{db}')
    # Consulta SQL para seleccionar los datos que deseas extraer
    query = "SELECT * FROM {table}"

    # Conecta a la base de datos
    connection = engine.raw_connection()
    cursor = connection.cursor()

    # Ejecuta la consulta y carga los resultados en un DataFrame
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    # Cierra el cursor y la conexión
    cursor.close()
    connection.close()

    return df

