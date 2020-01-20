import requests
import pocket
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
access_token = os.getenv("ACCESS_TOKEN")

pocket_instance = pocket.Pocket(consumer_key, access_token)


def get_active_articles(pocket_instance):
    articles = pocket_instance.get()[0]["list"]
    return {
        articles[a]["resolved_title"]: (
            articles[a]["resolved_id"],
            articles[a]["resolved_url"],
        )
        for a in articles
    }


def get_archived_articles(pocket_instance):
    articles = pocket_instance.get(state="archive")[0]["list"]
    return {
        articles[a]["resolved_title"]: (
            articles[a]["resolved_id"],
            articles[a]["resolved_url"],
        )
        for a in articles
    }


@app.route("/")
@app.route("/list")
def base():
    return render_template("base.html", articles=get_active_articles(pocket_instance))


@app.route("/read")
def archive():
    return render_template("base.html", archives=get_archived_articles(pocket_instance))


@app.route("/markread", methods=["POST"])
def markread():
    if "articleID" not in request.form:
        return "no article id", 400
    pocket_instance.archive(request.form["articleID"], wait=False)
    return "success", 200


@app.route("/delete", methods=["POST"])
def delete():
    if "articleID" not in request.form:
        return "no article id", 400
    pocket_instance.delete(request.form["articleID"], wait=False)
    return "success", 200


@app.route("/readd", methods=["POST"])
def readd():
    if "articleID" not in request.form:
        return "no article id", 400
    pocket_instance.readd(request.form["articleID"], wait=False)
    return "success", 200
