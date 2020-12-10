from selenium import webdriver  # importing selenium library to automate Whatssapp

# In this we are making a driver agent which will be controlling the browser
agent = webdriver.Chrome("Your own chromedriver software address")

agent.get("Please use whatssapp web URL here")  # URL of Whatssapp web to open Whatssapp in browser
print("Please scan the QR code from your Whatssapp for further process: ")

agent.maximize_window()  # here making the browser window to full screen

name = input("Please enter the contact or the group name: ")

message = input("Please enter a message to send: ")


choice = input("Pleas Enter YES to Continue or NO to modify the message: ")

flag = 0  # using to check whether the message send or not

if choice.lower() == "no":
    message = input("Please reenter a new message to send: ")

try:
    # Finding the user to whom we want to send the message
    contact = agent.find_element_by_xpath("//span[@title='{}']".format(name))

    # Clicking to open the chat
    contact.click()

    # Finding the message box where we will be typing the message

    messsagebox = agent.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
   
    #this x path is given by inspecting the element in the browser

    # here we will be typing the message
    messsagebox.send_keys(message)

    # Finding the send button to send the message
    sendbtn = agent.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button") \
 \
    # finally clicking on the send button
    sendbtn.click()

except:
    flag = 1
    # Unsuccessful message
    print("Sorry, unable to send message. Please enter a valid contact or the group name")

if flag == 0:
    # Successful message
    print("Message send successfully")
