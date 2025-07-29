from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Darboviete, Darbuotojas

routes = Blueprint("routes", __name__)

##################### PAGRINDINIS #####################

@routes.route("/")
def home():
    return render_template("home.html")

##################### DARBOVIETES #####################

###### SARASAS ######

@routes.route("/darbovietes/sarasas")
def darbovietes():
    visos = Darboviete.query.all()
    return render_template("darbovietes/sarasas.html", darbovietes=visos)

###### PRIDETI ######

@routes.route("/darbovietes/prideti", methods=["GET", "POST"])
def prideti_darboviete():
    if request.method == "POST":
        pavadinimas = request.form["pavadinimas"]
        miestas = request.form["miestas"]
        darbuotoju_skaicius = request.form.get("darbuotoju_skaicius")

        nauja = Darboviete(
            pavadinimas=pavadinimas,
            miestas=miestas,
            darbuotoju_skaicius=int(darbuotoju_skaicius)
        )
        db.session.add(nauja)
        db.session.commit()
        return redirect(url_for("routes.darbovietes"))

    return render_template("darbovietes/prideti_nauja.html")

###### REDAGUOTI ######

@routes.route("/darbovietes/redaguoti/<int:id>", methods=["GET", "POST"])
def redaguoti_darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)

    if request.method == "POST":
        darboviete.pavadinimas = request.form["pavadinimas"]
        darboviete.miestas = request.form["miestas"]
        darbuotoju_skaicius = request.form.get("darbuotoju_skaicius")
        darboviete.darbuotoju_skaicius = int(darbuotoju_skaicius)

        db.session.commit()
        return redirect(url_for("routes.darbovietes"))

    return render_template("darbovietes/redaguoti.html", darboviete=darboviete)

###### TRINTI ######

@routes.route("/darbovietes/trinti/<int:id>", methods=["GET", "POST"])
def trinti_darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)

    if len(darboviete.darbuotojai) > 0:
        klaida = "Negalima ištrinti darbovietės, nes joje dirba darbuotojų."
        return render_template("darbovietes/trinti.html", klaida=klaida, darboviete=darboviete)

    if request.method == "POST":
        db.session.delete(darboviete)
        db.session.commit()
        return redirect(url_for("routes.darbovietes"))

    return render_template("darbovietes/trinti.html", darboviete=darboviete)

###### INFORMACIJA ######

@routes.route("/darbovietes/sarasas/<int:id>")
def darboviete_detale(id):
    darboviete = Darboviete.query.get_or_404(id)
    return render_template("darbovietes/informacija.html", darboviete=darboviete)

######################################################################################################################

##################### DARBUOTOJAI #####################

###### SARASAS ######

@routes.route("/darbuotojai/sarasas")
def darbuotojai():
    visi = Darbuotojas.query.all()
    return render_template("darbuotojai/sarasas.html", darbuotojai=visi)

###### PRIDETI ######

@routes.route("/darbuotojai/prideti", methods=["GET", "POST"])
def prideti_darbuotoja():
    darbovietes = Darboviete.query.all()

    if request.method == "POST":
        vardas = request.form["vardas"]
        pavarde = request.form["pavarde"]
        pareigos = request.form["pareigos"]
        darboviete_id = request.form["darboviete_id"]

        naujas = Darbuotojas(
            vardas=vardas,
            pavarde=pavarde,
            pareigos=pareigos,
            darboviete_id=int(darboviete_id)
        )
        db.session.add(naujas)
        db.session.commit()
        return redirect(url_for("routes.darbuotojai"))

    return render_template("darbuotojai/prideti_nauja.html", darbovietes=darbovietes)

###### REDAGUOTI ######

@routes.route("/darbuotojai/redaguoti/<int:id>", methods=["GET", "POST"])
def redaguoti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)
    darbovietes = Darboviete.query.all()

    if request.method == "POST":
        darbuotojas.vardas = request.form["vardas"]
        darbuotojas.pavarde = request.form["pavarde"]
        darbuotojas.pareigos = request.form["pareigos"]
        darbuotojas.darboviete_id = int(request.form["darboviete_id"])

        db.session.commit()
        return redirect(url_for("routes.darbuotojai"))

    return render_template("darbuotojai/redaguoti.html", darbuotojas=darbuotojas, darbovietes=darbovietes)

###### TRINTI ######

@routes.route("/darbuotojai/trinti/<int:id>", methods=["GET", "POST"])
def trinti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)

    if request.method == "POST":
        db.session.delete(darbuotojas)
        db.session.commit()
        return redirect(url_for("routes.darbuotojai"))

    return render_template("darbuotojai/trinti.html", darbuotojas=darbuotojas)

###### INFORMACIJA ######

@routes.route("/darbuotojai/sarasas/<int:id>")
def darbuotojas_informacija(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)
    return render_template("darbuotojai/informacija.html", darbuotojas=darbuotojas)


######################################################################################################################
