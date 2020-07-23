# Food 4 All

This website is an open source project and is an entry for **[Code Camp](https://codecamphackathon.netlify.app)**

# About

Many charitable organizations are working to provide food to the needy. It is commonly observed that a lot of food gets wasted in functions, parties and on other occasions. Most of the hotels, also face the situation that at the end of the day, a lot of food remains unused and literally, gets wasted. This website is being created to provide a platform/place for all those who have the surplus and are willing to donate the food to ones who are in dire need of the same. Any individual, hotel, restaurant etc. (“Donor”) can register on this platform/website so that identity of the donor and the food item/s donated (item, quantity, etc.) is duly captured. List of beneficiary/recipient organizations will be prepared by taking the details from the office where non-governmental organizations (NGOs) get themselves registered (e.g., Registrar of Societies). To know the profile of beneficiary/recipient organizations and their interest in providing food to the needy as collected from donors, will be assessed. In this way, the final list of beneficiary/recipient organizations will be prepared. Beneficiary/recipient organizations will be notified about the donor organizations and food to be donated on continuous basis. Beneficiary/Recipient organizations can then contact the donor organizations and can make necessary arrangements to pick up the food parcels/items from the place of the donor. If Beneficiary/Recipient organizations work for people on the streets or for the people in the slums, then they can make those items available to those persons/people at their places. Donor organizations can identify specific beneficiary/recipient for serving them on continuous basis, based on their location. Alternatively, donor organizations can send a message to all the organizations through this platform/website. Beneficiary/Recipient organizations will get confirmation. This website will help those donor organizations who do not have the database/knowledge about people/NGOs to whom they can donate. This can be replicated across the country and can be customized for specific village/s, sub-urban areas, towns, and cities. In this way, it will deal with the issue of provision of the food from the organizations which have the surplus to those who need the same.

# Using this project

#### Setting up:

Note: This project was developed on a windows 10 pc.

1. First of all you have to clone this repository onto your computer. You can do this by:

   - ```shell
     git clone https://github.com/Nalin-2005/Food4All.git
     ```

     ###### 	OR

   - Download this repository as zip from above.

2. You should also have python installed. This repo was made using python version 3.7.3. If python is not installed then you can get it from **[here](https://www.python.org)**

3. Then you should install the required python packages using pip. This project **currently** requires only Flask. You can install Flask by:

   ```shell
   pip install flask
   ```

#### Starting:

Firstly, you can run the project by opening the *command prompt* (windows) or *terminal* (linux/macos) in the project directory and typing:

```shell
python main.py
```

Alternatively if you have visual studio code installed you can open the folder as project and there is already a configuration present by the name of **Flask: Food4All**

1.  Fire up a GUI-based browser and go to **localhost:5000** . If you already have a project running on the same port, then you would have to change the port of either the ```main.py``` file of this project or the python file of the project running on the same port.
2. To check the mobile version, you can either access it using a mobile device or you can even use chrome's mobile view *(I only know about chrome but there might be others too)* by:
   - Right clicking
   - Clicking on  Inspect
   - Clicking on *Toggle Device Toolbar* 
   - And reloading the webpage

#### Status:

Currently (as of 23rd July, 2020) only frontend is being focused on so there is no usage of form data being done and so you can only work with or test the user interface and the functionality of data transfer. Also, the phone number given in the footer of every page is actually fake (numbers 0-9 in decreasing order) so don't try to call on them! But if you wish to talk to me regarding this project, you can use that email (It's working..).