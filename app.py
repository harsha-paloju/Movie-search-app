from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route("/")
def home():
    
    return render_template("home.html")

@app.route("/result",methods=["GET","POST"])
def result():
    api_key="c30b3ecd"
    Movie=request.form.get("search")

    url=f"https://www.omdbapi.com/?apikey={api_key}&t={Movie}"

    response=requests.get(url)

    data=response.json()
    
    if data["Response"] == "False":
        return render_template(
            "result2.html",
            error="Movie not found"
        )

    

    movie=data["Title"]
    rating=data["Ratings"][0]["Value"]
    release=data["Released"]
    actors=data["Actors"].split(",")
    actor1=actors[0]
    actor2=actors[1]
    actor3=actors[2]
    genre=data["Genre"]
    plot=data["Plot"]
    poster=data["Poster"]
    
    data = response.json()

    
    
    return render_template("result.html",movie=movie,rating=rating,release=release,actor1=actor1,actor2=actor2,actor3=actor3,genre=genre,plot=plot,image=poster)

if __name__ == "__main__":
    app.run(debug=True)
