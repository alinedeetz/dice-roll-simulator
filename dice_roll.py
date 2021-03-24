from flask import Flask, render_template, request, redirect
import psycopg2
import random
import os

print(os.environ)

app = Flask (__name__)
dice_roll = []
DB_USERNAME = os.environ["DICE_ROLL_DB_USERNAME"]
DB_PASSWORD = os.environ["DICE_ROLL_DB_PASSWORD"]
DB_HOSTNAME = os.environ["DICE_ROLL_DB_HOSTNAME"]
DB_PORT = os.environ["DICE_ROLL_DB_PORT"]
DB_NAME = os.environ["DICE_ROLL_DB_NAME"]
POSTGRESQL_URI = "postgres://{}:{}@{}:{}/{}".format(
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOSTNAME,
    DB_PORT,
    DB_NAME
)

connection = psycopg2.connect(POSTGRESQL_URI)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        results = []
        for dice in range(0, int(request.form.get("number_of_dices"))):
            results.append(random.randint(1, int(request.form.get("dice_type"))))
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO simulations VALUES (%s, %s, %s, %s);", 
                    (
                        request.form.get("username"),
                        request.form.get("number_of_dices"),
                        request.form.get("dice_type"),
                        ",".join(str(x) for x in results)
                    )
                )
        return redirect("/results")
    return render_template("dice_roll.j2")

@app.route("/results")
def results():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM simulations;")
            data = cursor.fetchall()
    return render_template("table.j2", data=data)

@app.route("/simulations")
def simulations():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM simulations;")
            transactions = cursor.fetchall()
    return render_template("table.j2", data=transactions)