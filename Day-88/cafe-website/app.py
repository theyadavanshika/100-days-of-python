from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    search = request.args.get("search", "")

    connection = sqlite3.connect("cafes_updated.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM cafe WHERE name LIKE ? OR location LIKE ?",
        (f"%{search}%", f"%{search}%"),
    )
    cafes = cursor.fetchall()

    connection.close()

    return render_template("index.html", cafes=cafes, search=search)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        map_url = request.form["map_url"]
        img_url = request.form["img_url"]
        coffee_price = request.form["coffee_price"]
        has_wifi = int(request.form["has_wifi"])
        has_sockets = int(request.form["has_sockets"])
        has_toilet = int(request.form["has_toilet"])
        can_take_calls = int(request.form["can_take_calls"])
        seats = request.form["seats"]

        connection = sqlite3.connect("cafes_updated.db")
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO cafe
            (name, location, map_url, img_url, coffee_price,
            has_sockets, has_toilet, has_wifi, can_take_calls, seats)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                name,
                location,
                map_url,
                img_url,
                coffee_price,
                has_sockets,
                has_toilet,
                has_wifi,
                can_take_calls,
                seats,
            ),
        )

        connection.commit()
        connection.close()

        return redirect(url_for("home"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
