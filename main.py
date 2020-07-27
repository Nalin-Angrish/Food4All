"""
Main python file for Food4All Website.
This File should be run as it is the main server.
Running any file other than this will lead to not running the server.

Author:- Nalin Angrish
Jai Shri Ram!
"""


from flask import Flask, render_template, request, url_for, redirect        # Importing all flask dependencies

import myEmail, dbmanager                                                   # Import custom tools

import random                                                               # Import other library (ies)



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



@app.route("/donate/process", methods=["POST", "GET"])                      # Process data submitted through donate form
def donateprocessor():              
    if request.method == "POST":            
        name = request.form['name']                     # Get all data
        phone = request.form['number']
        address = request.form['address']
        state = request.form['state']
        food = request.form['food']
        typeOfFood = request.form['type']
        transport = request.form['trans']
        location = request.form['loc']


    index = str(dbmanager.addOrder(name, phone, address, food, typeOfFood, transport, location))  # Use dbmanager to add an order and get it's index number for further operations
    infoUrl = str(request.url_root)[:-1] + url_for('orders', num=index)         # Generate url for information about order (For NGOs)
    NGOList = dbmanager.getNGOs(state)
    
    
    for NGO in NGOList:                                     # Get list of NGOs and send each one of them an email to notify them about a new donor along with the information link
        NGOname , NGOemail = tuple(NGO)
        myEmail.send(NGOemail,
                subject="Food4All - A new donor {} in your region needs you...".format(name),
                text="We have recieved an order from {}, in {}. As we knew that your organisation {} operates here, we thought to inform you about it. You can visit the details about this order from {}".format(name, state, NGOname, infoUrl))

    
    
    if isMobile(request.user_agent.string):                 # Return user with an information webpage with a link to approve the order
        return render_template("mobile/donatesuccess.htm", number=index)
    else:
        return render_template("desktop/donatesuccess.htm", number=index)

@app.route("/orders/<num>")                                                 # Order Information page
def orders(num):
    myOrder = dbmanager.getOrder(num)

    name = myOrder.getName()
    phone = myOrder.getPhone()
    address = myOrder.getAddress()
    food = myOrder.getFood()
    tof = myOrder.getFoodType()
    trans = myOrder.getTransport()
    

    status = myOrder.isApproved()
    if(status == True):                 # Generate a simple string value based on approval
        status = "Approved"
    else:
        status = "Approval Pending"


    if("+91" not in phone):             # Rectify a phone number
        phone = "+91"+phone
    if (" " in phone):
        phone = phone.replace(" ", "")
    

    if isMobile(request.user_agent.string):
        return render_template('mobile/orders.htm', num=num, name=name, phone=phone, address=address, food=food, tof=tof, trans=trans, status=status)
    else:
        return render_template('desktop/orders.htm', num=num, name=name, phone=phone, address=address, food=food, tof=tof, trans=trans, status=status)

@app.route("/donate/approve/<number>")                                      # Page after order is approved
def approveDonation(number):
    dbmanager.approveOrder(number)
    return redirect(url_for('success'))

@app.route('/signup/process', methods=["POST", "GET"])                      # Process data submitted through sign-up form
def signupprocessor():
    if request.method == "POST":                    # Get all the data
        name = request.form['name']
        email = request.form['email']
        states = request.form.getlist('states')

    for state in states:                            # use dbmanager to add an NGO in all of the states
        dbmanager.addNGO(state, name, email)
    
    return redirect(url_for('success'))


@app.route('/success')                                                      # This will display the success message and redirect to the home page
def success():
    if isMobile(request.user_agent.string):
        return render_template('mobile/success.htm')
    else:
        return render_template('desktop/success.htm')

@app.route("/otpgen/<mailaddr>")                                            # Generate otp and send it to <mailaddr>
def otpgen(mailaddr):
    otp = random.randint(100000, 999999)        # Generate random number
    myEmail.send(mailaddr, subject="OTP from Food4All",
            text="Thank you for registering to Food4All. Use this OTP for completing the registration: "+str(otp))
    return str(otp)         # return the otp(as an ajax response) & Mail the otp to the given address ^^





if __name__ == "__main__":                                                  # Start the web server...
    app.run(debug = True, port = 5000)                  # Flask only supports 1 request at a time but this can be increased 
                                                        # by integrating it with a production deployment web server like apache or nginx