'''
Now you gonna enter into a chatbot named "Agro_Bot".
It is built on the objective of helping farmers especially beginners.
Agro_bot can do two works. They are
1. If you give the corresponding number of your soil type it will give the perfect crops for your soil type.
2. If you give the corresponding number of your soil type it will give the characteristics of the soil that will
    help you to understand your soil.
'''

import random                 # random is a library, it will give some random thing from your collection
from datetime import datetime # datetime is a library to get the present time
def greet_and_introduce():    # function to start the conversation
    return "Hi there! I am an agro_bot. I can help you to select a right crop for your soil and properties of the soil. May I know your name ?"
    
def get_timeofday_greeting(): # function to wish the user accordingly..
    current_time = datetime.now()
    timeofday_greeting = "Good morning"
    if current_time.hour > 12 and current_time.hour<17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour > 17 and current_time.hour<22:
        timeofday_greeting = "Good evening"
    elif current_time.hour > 22:
        timeofday_greeting = "Hi, That's late"
    return timeofday_greeting

def welcome(name):          # function to welcome the user with his/her name
    messages = [
        "Nice to meet you!"+" "+name,
        "Good to see you."+" "+name,
        "Hey! what's up"+" "+name
    ]
    print(get_timeofday_greeting())
    print(random.choice(messages))
def show_menu(): # function to show the things that bot can do
    print("The things I can do are ..")
    print("1.Know the correct crops for your soil")
    print("2.Know the properties of your soil")
    print("3.End of this chat")
    print("====================================")
    try: 
        return int(input("Enter your choice"))
    except:
        print("Only enter choice")
        return int(input("Enter your choice:"))
def select_soil(): # function which gives the option to select the soil type
    print("1.Black soil")
    print("2.Red soil or Yellow soil")
    print("3.Aluvial soil")
    print("4.Laterite soil")
    print("5.Arid soil")
    print("6.Forest or mountain soil")
    print("7.Desert soil")
    print("8.Other soils")
    try:
        return int(input("Enter choice : "))
    except:
        print("please select corresponding number of your desired soil")
        return int(input("Enter your choice: "))
def correct_crop (your_soil): # function to suggest the correct crop
    if your_soil==1:
        return  "cotton,rice,sugarcane,wheat,jowar,sunflower,ceralcrops,citrus fruits,vegetables,tobacco,groundnut,oil seedcrops and millets"
    elif your_soil==2:
        return "rice,wheat,sugarcane,groundnut,maize/corn,ragi,potato,oil seeds,pulses,millets,fruits such as orange,mango,citrus"
    elif your_soil==3:
        return "Tobacco,cotton,rice,wheat,bajra,jowar,pea,pigeon pea,chick pea,black gram,green gram,mustard,linseed,sesam,barle,jute,maize,any oil seeds"
    elif your_soil==4:
        return "cotton,rice,wheat,tea,cofee,rubber,coconut,cashews,these are used to make bricks due to presence large amounts of iron"
    elif your_soil==5:
        return "wheat,cotton,corn,millets,pulses,barley"
    elif your_soil==6:
        return "tea,spices,wheat,barly,maize,coffee,tropical fruits and temperature fruits"
    elif your_soil==7:
        return "millet and barly"
    elif your_soil==8:
        return "not suitable for cultivation"
def characterstics_of_soil(your_soil): # function to give the characterstics of the particular soil
    if (your_soil==1):
        return "Rich in iron,lime,magnesium,aluminium. \n Poor in phosphorous,nitrogen and humus.Black soils become sticky when wet and develop cracks in any season."
    elif (your_soil==2):
        return "These soils are red in color due to presence of iron oxide.These are sandy and rich in potash. \n They are poor in lime,nitrogen,phosphorous,magnesium,iron-oxide."
    elif (your_soil==3):
        return "Aluvial soils are mixture of clay and sand.Rich in phosphoric acid and organic mattter \n Poor in nitrogen and potash."
    elif (your_soil==4):
        return "Rich in iron \n Poor in humus,phosphate,nitrogen and calcium."
    elif (your_soil==5):
        return "Rich in plant food.These soils are deficient of humus and moisture due to the fact that high evaporation in arid regions."
    elif(your_soil==6):
        return "Rich in organic matter. \n Poor in nutrients such as Potash, Phosphorous and Lime."
    elif(your_soil==7):
        return "These soils are sandy and dry and contains some amount of nitrogen."
    elif(your_soil==8):
        return "Not suitable for cultivation."
'''
Now we are at the main function, which is the back bone of the chatbot.
Agro_bot is the main function which regulate everything in the bot.
'''
def Agro_bot():
    print(greet_and_introduce())
    name = input("Your name: ") # To take the username
    welcome(name)
    choice = show_menu() # the duty of Agro_bot selected by a user is stored in choice.
    if (choice > 3 or choice <= 0): # if the choice is not available, it will ask the another time
        print("Please enter right number shown above ^")
        print("=================================")
        choice = show_menu()
    while (choice <= 3 and choice > 0) :
        if choice == 1:
            your_soil = select_soil() # soil type selected by a user is stored in your_soil
            print(correct_crop(your_soil))
            print("=================================")
            choice = show_menu()
        elif(choice == 2):
            your_soil = select_soil() # soil type selected by a user is stored in your_soil
            print(characterstics_of_soil(your_soil))
            print("=================================")
            choice = show_menu()
        else:
            print("Come back again !") # here you will end the chat with agro_bot
            break
Agro_bot()