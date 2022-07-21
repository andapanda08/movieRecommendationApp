from flask import Flask, jsonify, request
import csv
all_movies=[]
with open("movies.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

liked_movies=[]
notLiked_movies=[]
didNotWatch=[]

app=Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie=all_movies=[]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def notLiked_movie():
    movie=all_movies=[]
    all_movies=all_movies[1:]
    notLiked_movies.append(movie)
    return jsonify({
        "status":"success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def didNotWatch():
    movie=all_movies=[]
    all_movies=all_movies[1:]
    didNotWatch.append(movie)
    return jsonify({
        "status":"success"
    }), 201

if __name__=="__main__":
    app.run()



