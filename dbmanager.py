# This file will contain all the methods to interact with the local database

import os                       # Import all dependencies
import re
import random

def getOrderCount():                                # count the number of orders done till now and add 1 to get the current order number
    return str(len(os.listdir("./database/orders")) + 1)
    
def getTransport(trans):                            # Get description of mode of transport from abbrevation 'self'/'ngo'
    if(trans == "self"):
        return "Already has transport, will deliver to you."
    else:
        return "Needs Transport Assistance."

def addOrder(name, phone, address, food, tof, trans, location):           # Add order in the orders list
    count = getOrderCount()
    with open("database/orders/"+count+".txt", 'a+') as order:
        order.write(name)
        order.write("\n"+phone)
        order.write("\n"+address)
        order.write("\n"+food)
        order.write("\n"+tof)
        order.write("\n"+getTransport(trans))
        order.write("\n"+location)
    return count

def getOrder(number):                               # Get 'Order' object for the given order number
    return Order(str(number))

def approveOrder(number):                           # To add the approved tag to an order
    with open('database/orders/'+str(number)+'.txt', 'r+') as order:
        if("*Approved*" not in order.read()):
            order.write("\n*Approved*")



class Order(object):            # A class that can be used by our main python file for easily getting details of any order
    def __init__(self, name):
        self.data = open("database/orders/"+name+".txt", 'r').read().splitlines()

    def getName(self):                  # To get Name 
        return self.data[0]
    
    def getPhone(self):                 # To get Phone Number
        return self.data[1]

    def getAddress(self):               # To get Address
        return self.data[2]

    def getFood(self):                  # To get food
        return self.data[3]

    def getFoodType(self):              # To get food type
        return self.data[4]

    def getTransport(self):             # To get avalability of transport
        return self.data[5]

    def isApproved(self):               # To check if the order is approved or not
        return ("*Approved*" in self.data)  # data should contain *Approved* if it is approved
    
    # Here we are not adding Location because we do not need it to be accessible to any NGO by default.
    # The location would be used only to track fake orders or on other times when it is needed.




def addNGO(state, name, email):                 # To add an NGO's credentials in the given state
    with open("database/ngos/"+state+".txt", 'a+') as myFile:
        myFile.write(str("{},{}\n".format(name, email)))

def getNGOs(state):                                             # This function will return a list of tuples from a state,                                                                 
    with open("database/ngos/"+state+".txt", "r") as myFile:    # where each tuple would contain the name and email of one NGO and 
        data = list(myFile.read().split("\n"))                  # multiple tuples will hence contain for multiple NGOs

    final = []
    for eachObject in data:
        final.append(tuple(eachObject.split(",")))
    
    final.pop()                 # Because of the '\n' after each line, there will remain an empty tuple in the end. 
                                # So, to prevent any error, we will remove the last blank item from the list by using final.pop()
    
    return final