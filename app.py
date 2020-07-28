# import pandas as pd
# from sqlalchemy import create_engine
# datos = pd.DataFrame({
#     "tipo":["super","tarea"],
#     "desc":["leche","estudiar"]
# })
# # datos = pd.read_csv("archivo.csv")
# engine = create_engine("postgresql+psycopg2://postgres:gs@/todo_list")
# datos.to_sql("todo", if_exists="append", index=False, con=engine)
# engine.dispose()
from flask import Flask, render_template, request
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

@app.route("/")
def main():
#    return "hola mundo desde flask"
    return render_template("index.html")

@app.route("/api/consultar/<buscarTipo>")
def consultar(buscarTipo):

    if buscarTipo=="0":
        query = "select * from todo"
    elif buscarTipo=="1":
        query = "select * from todo where tipo='super'"
    else:
        query = "select * from todo where tipo='tarea'"

    engine = create_engine("postgresql+psycopg2://postgres:gs@/todo_list")
    datos = pd.read_sql(query, engine)
    engine.dispose()

    return datos.to_json(orient="records")


@app.route("/api/insert", methods=["POST"])
def insert():
    miJSON = request.json

    datos = pd.DataFrame({
        "tipo": "super" if miJSON["tipo"]==1 else "tarea",
        "desc": miJSON["texto"]
    }, index=[0])

    engine = create_engine("postgresql+psycopg2://postgres:gs@/todo_list")
    datos.to_sql("todo", if_exists="append", index=False, con=engine)
    engine.dispose()

    return datos.to_json(orient="records")

if __name__ == "__main__":
    app.run()


