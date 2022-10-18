from flask import Flask, jsonify, request
import csv

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_article = []
not_liked_article = []

app = Flask(__name__)

@app.route("/get-article")
def get_movie():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
    })

@app.route("/liked-article", methods = ["POST"])
def liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_article.append(article)
    return jsonify({
        "status" : "success"
    }), 201

@app.route("/unliked-article", methods = ["POST"])
def not_liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_article.append(article)
    return jsonify({
        "status" : "success"
    }), 201

if __name__ == "__main__":
    app.run()