# Food 4 All

This website is an open source project and is an entry for **[Code Camp](https://codecamphackathon.netlify.app)**

You can get information about my team **[here](https://codecamphackathon.netlify.app/TheJuniorDev)**

Note: all passwords in theis project have now been removed and changed. This website is now kept only as a template for others.
Also, this project has now been hosted at: **[food-4-all.herokuapp.com](https://food-4-all.herokuapp.com)**

# About

Many charitable organizations are working to provide food to the needy. It is commonly observed that a lot of food gets wasted in functions, parties and on other occasions. Most of the hotels, also face the situation that at the end of the day, a lot of food remains unused and literally, gets wasted. This website is being created to provide a platform/place for all those who have the surplus and are willing to donate the food to ones who are in dire need of the same. Any individual, hotel, restaurant etc. (“Donor”) can register on this platform/website so that identity of the donor and the food item/s donated (item, quantity, etc.) is duly captured. List of beneficiary/recipient organizations will be prepared by taking the details from the office where non-governmental organizations (NGOs) get themselves registered (e.g., Registrar of Societies). To know the profile of beneficiary/recipient organizations and their interest in providing food to the needy as collected from donors, will be assessed. In this way, the final list of beneficiary/recipient organizations will be prepared. Beneficiary/recipient organizations will be notified about the donor organizations and food to be donated on continuous basis. Beneficiary/Recipient organizations can then contact the donor organizations and can make necessary arrangements to pick up the food parcels/items from the place of the donor. If Beneficiary/Recipient organizations work for people on the streets or for the people in the slums, then they can make those items available to those persons/people at their places. Donor organizations can identify specific beneficiary/recipient for serving them on continuous basis, based on their location. Alternatively, donor organizations can send a message to all the organizations through this platform/website. Beneficiary/Recipient organizations will get confirmation. This website will help those donor organizations who do not have the database/knowledge about people/NGOs to whom they can donate. This can be replicated across the country and can be customized for specific village/s, sub-urban areas, towns, and cities. In this way, it will deal with the issue of provision of the food from the organizations which have the surplus to those who need the same.

# How it works

We have created a website to connect the people who want to donate food to the poor and the NGOs and other non-profit organisations who can take the food from these people and donate it to the people in the food-deficit areas. 

The people who want to donate food can submit their details like Name, Phone number, Food (and amount of food) they want to donate, their address, and the State / UT in which they live, type of food (cooked, semi-cooked, raw) and whether or not they need the transportation to send food to the NGO's office.

Based on their State / UT, our form processor will get the list of the NGOs which operate in those regions. These NGOs can be listed from the offices where they are registered, or they can themselves register on this website. For their registration, they would have to submit information like Name of organisation, Email address & states in which they operate. Their authenticity will be ensured by an OTP system.

When the donors send a donation request, these NGOs will be notified by that email with which they are registered on this website and can access all the information provided by the donor, including contact details, and can talk to them about the necessary arrangements required. After the donor has finalized the NGO to be helped, he can change the status of the order from "Pending" to "Approved" so that other NGOs can be told that the order has been finalized and not to contact the donor (in order to not disturb the person). 

We have created a fine looking and simple user interface so as not to overcomplicate things for the user.
For security purposes, all orders are logged so that if there is any misleading information provided, like wrong phone/address/etc. are given to blame another person, then appropriate actions can be taken.
Also, the registration of the NGOs is also done as safely as possible, by including One-Time-Password technology.


We support Open-source development so this project will be kept open even after Code Camp and others can use this project as a template for their own projects.

# Using This project 

### Setting Up

1. This project runs on Python so make sure you have Python installed. If it is not installed, then you can install it from [python.org](https://python.org/downloads). Note: This project was developed using python 3.7.3.

2. After you have python installed, you have to install [flask](https://flask.palletsprojects.com/). You can install flask by 

   ```pip install flask```

3. Then if you have not cloned this repository till now, then you can clone it using the git command or by going above and clicking **Code > Download as Zip** and extracting it.

### Starting

You will see a *main.py* file in the project directory. You can either directly run it by double clicking it or by opening a command prompt *(or terminal if you are using Linux/MacOS)* in the project directory and typing 

```python main.py```

### Using

After the *main.py* script is running, fire up your browser and go to localhost:5000.

You will see a webpage. For testing the working of this website, you should first sign up yourself as an NGO.	(Although not actually but you will need to, for testing purposes)

###### Signing up

You will have to enter some information about your *fake* NGO like :

- Name of Organisation
- Email Address (This email will be used to notify NGO about new donors)
- States in which your NGO Operates. (We will be using it to send information of only relevant donors)

Then after you submit this form, you will get an email (at the email address you mentioned) with the OTP. Now you can use this OTP to perform successful registration (You can check this by once entering wrong OTP - I have tried my best to keep it as safe as possible)

Enter the OTP and click on the submit button.

Then after your registration is successful, you can go on to the next step

###### Donate

Now go to the home page (Link will be given on that particular page) and click on the **Donate** Button.

There you will need to fill some information about your *fake* donation like:

- Your Location (Webpage will ask for it)

- Your Name
- Your Phone Number (For use by NGO to contact you)
- Your Address
- Your State/UT (To send notifications to relevant NGOs) 
- Food to be donated and it's quantity
- Type of food (whether you are giving cooked food, semi-cooked food, or raw ingredients)
- Whether or not you need transport help from NGO to deliver it to NGO's Office

After you submit the form, the server will send an email to the NGOs working in that region (I hope that you have registered). Also you will see a page which contains a link for approving (Do not press it now, it is to be pressed after you have decided which NGO will help you)

That email will contain a link for getting the order details (As the server is running on the localhost - the link will also be of localhost so use the same computer for checking the email [this will automatically work properly during deployment])

Now you can go to that link (Order details will not appear as that part is not completed as yet, but you will still see the order number.)

While testing you should see in the database/orders folder there will be a text file with the name as the order number. you can peek into that file and you will see the data inside it (It is recommended to not change the contents). For reading that data a class is present in the *dbmanager.py* file.

In the order's text file you will see some lines of text.

After you click on the Approval link, the text file would also contain some text =>  ```*Approved*```

This will be used by the server to check whether the order is approved or not. 



# Additional Notes

The email given in the footer can be used by you to inform me about anything related to this project.

Do not call on the number because it is just numbers 0-9 in descending order!

Also, while testing make sure that your internet connection is properly working

These webpages are a bit different for mobile phones, so you can test even mobile versions using chrome's (I don't know about others) inspect > toggle device toolbar (Mobile mode).

