from sqlalchemy import create_engine
import pandas as pd
import os

engine_string = os.environ.get('DATABASE_URL', '')

datos = pd.DataFrame({
    "tipo": "super",
    "desc": "leche"
}, index=[0])

engine = create_engine(engine_string)
datos.to_sql("todo", if_exists="append", index=False, con=engine)
engine.dispose()
