"""
Main python file for Food4All Website.
Author:- Nalin Angrish
"""


from flask import Flask, render_template, request, url_for, redirect, jsonify        # Importing all flask dependencies

app = Flask(__name__, static_folder="static", template_folder="pages")      # initialized a flask app



def isMobile(agent):                                                        # Method to check if the user is visiting the website using mobile/Tablet or not
    if("android" in agent.lower()):                 # User agent in Android devices contains 'android'
        return True
    elif("iphone" in agent.lower()):                # User agent in iPhones contains 'iphone'
        return True
    elif("ipad" in agent.lower()):                  # User agent in iPads contains 'ipad'
        return True
    else: return False




@app.route("/favicon.ico")                                                  # Favicon
def favicon():
    return redirect(url_for('static', filename="favicon.ico"))      # This favicon was generated using the online tool at favicon.io 


@app.route("/")                                                             # Home Page...
def home():
    if(isMobile(request.user_agent.string)):                        # Check if it is mobile user because pages need to be optimized for mobiles
        return render_template("mobile/home.htm")
    else:                                                           # If it is ot mobile user, then return desktop viewr
        return render_template("desktop/home.htm")


@app.route("/donate")                                                       # Donate Food
def donate():
    if(isMobile(request.user_agent.string)):
        return render_template("mobile/donate.htm")
    else:
        return render_template("desktop/donate.htm")


@app.route("/signup")                                                       # Sign up as an NGO
def signUp():
    if(isMobile(request.user_agent.string)):
        return render_template("mobile/signup.htm")
    else:
        return render_template("desktop/signup.htm")

@app.route("/donate/process", methods=["POST","GET"])
def donateprocessor():
    if request.method == "POST":
        name = request.form['name']
        print(name)
        phone = request.form['number']
        print(phone)
        address = request.form['address']
        print(address)
        city = request.form['state']
        print(city)
        food = request.form['food']
        print(food)
        typeOfFood = request.form['type']
        print(typeOfFood)
        transport = request.form['trans']
        print(transport)

    response = "name: "+name+"<br>phone: "+phone+"<br>address: "+address+"<br>city: "+city+"<br>food: "+food+"<br>type: "+typeOfFood+"<br>transport: "+transport
    return response







if __name__ == "__main__":                                                  # Start the web server...
    app.run(debug = True, port = 5000)                  # Flask only supports 1 request at a time but this can be increased 
                                                        # by interfacing it with a production web server like apache or nginx