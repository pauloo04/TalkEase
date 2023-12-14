from flask import Blueprint, render_template, request, session, jsonify, send_file
from app.forms import *
from app.functions import *
from app.auth import login_required, logout

bp = Blueprint("home", __name__, url_prefix="/")

@bp.route("/", methods=["POST", "GET"])
def welcome():
    return render_template("home/welcome.html")

@bp.route("/home", methods=["POST", "GET"])
@login_required
def home():
    if request.method == "POST":
        print("Logout", flush= True)
        logout()
    return render_template("home/home.html")

@bp.route("/simplify", methods=["POST", "GET"])
@login_required
def simplify():
    if request.method == "POST":
        input_text = request.get_json()["input_text"]
        return jsonify({"simplified_text": simplifier(input_text)})
    return render_template("home/simplify.html")

@bp.route("/summerize", methods=["POST", "GET"])
@login_required
def summerize():
    if request.method == "POST":
        input_text = request.get_json()["input_text"]
        return jsonify({"summerized_text": summarizer(input_text)})
    return render_template("home/summerize.html")

@bp.route("/form", methods=["POST", "GET"])
@login_required
def form():
    if request.method == "POST":
        input_text = request.get_json()["input_text"]
        return jsonify({"formed_text": former(input_text)})
    return render_template("home/form.html")

@bp.route("/fix", methods=["POST", "GET"])
@login_required
def fix():
    if request.method == "POST":
        input_text = request.get_json()["input_text"]
        return jsonify({"fixed_text": former(input_text)})
    return render_template("home/fix.html")

@bp.route("/feedback", methods=["POST", "GET"])
@login_required
def feedback():
    if request.method == "POST":
        input_text = request.get_json()["input_text"]
        return jsonify({"feedbacked_text": feedbacker(input_text)})
    return render_template("home/feedback.html")

@bp.route("/audio", methods=["POST", "GET"])
def audio():
    if request.method == "POST":
        text = request.get_json()["text"]    
        text_to_wav("en-GB-Neural2-A", text)
        return send_file("./en-GB-Neural2-A.wav", mimetype="audio/wav", as_attachment=True)