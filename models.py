from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref

db = SQLAlchemy()

class Darboviete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String(100), nullable=False)
    miestas = db.Column(db.String(50), nullable=False)
    darbuotoju_skaicius = db.Column(db.Integer, nullable=True)
    darbuotojai = db.relationship("Darbuotojas", backref="darboviete", cascade="all, delete")

class Darbuotojas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(50), nullable=False)
    pavarde = db.Column(db.String(50), nullable=False)
    pareigos = db.Column(db.String(100), nullable=False)
    darboviete_id = db.Column(db.Integer, db.ForeignKey('darboviete.id'), nullable=False)
