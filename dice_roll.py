from flask import Flask, render_template, request, redirect
import psycopg2
import random 

app = Flask (__name__)
dice_roll = []
POSTGRESQL_URI = "postgres://llnueiav:4b41FBBKPhnJrv75U0z4yW1_tehDMfqR@tuffi.db.elephantsql.com:5432/llnueiav"

connection = psycopg2.connect(POSTGRESQL_URI)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        results = []
        for dice in range(0, int(request.form.get("number_of_dices"))):
            results.append(random.randint(0, int(request.form.get("dice_type"))))
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