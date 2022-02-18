# import main Flask class and request object
from flask import Flask,render_template, request,session
# create the Flask app
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


#It's a secret!
app.secret_key = 'the random string of secrets'

# Form Page
@app.route('/', methods = ["GET","POST"])
def index():
    return render_template('index.html')

# # Have the "/result" route display the information on a new HTML Page

@app.route("/result", methods=["GET","POST"])
def form_result():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["location"]=request.form["location"]
        session["language"]=request.form["language"]
        session["comments"]=request.form["comments"]

    return render_template("/result.html")

if __name__=="__main__":
    
    app.run(debug=True)
    

#Could not figure out session