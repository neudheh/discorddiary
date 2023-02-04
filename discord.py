import discord, datetime, json
from discord.ext import tasks


discordToken = "token that i accidentally left here whoops"
discordIntents = discord.Intents(messages=True, guilds=True, members=True)
discordClient  = discord.Client(intents = discordIntents)
serverObject = None
catergoryObject = None

@discordClient.event
async def on_ready():
    print(f"Logged in as {discordClient.user}!")              #Prints message when client is ready to connect to the discord API

@discordClient.event
async def on_connect():
    eventLoop.start()

@tasks.loop(seconds = 1.0)                                    #Creates the event loop
async def eventLoop():
    global channelObject
    timezone = datetime.timezone(datetime.timedelta(hours=8))
    currentDate = datetime.datetime.now(timezone).strftime("%d/%m/%y")
    
    with open("date.json", "r") as file:
        pastDate = json.load(file)
    
    if pastDate == currentDate:                              #Checks if it is a new day, if it is not, the bot returns
        return
    monthDict = {
        1: "january",
        2: "febuary",
        3: "march",
        4: "april",
        5: "may",
        6: "june",
        7: "july",
        8: "august",
        9: "september",
        10: "october",
        11: "november", 
        12: "december"
    }
    channelName = f"{monthDict[datetime.datetime.now(timezone).month]}-{datetime.datetime.now(timezone).year}"
    channelObject = None
    
    for i in serverObject.channels:                          #Checks if there is a channel for the current month, if there is none, the bot makes one
        if i.name == channelName:
            channelObject == i
            break
            
    if not channelObject:
        channelObject = await serverObject.create_text_channel(
            name = channelName,
            category = catergoryObject
        )
    
    await channelObject.send(f"-{currentDate}-")             #Sends the current date in the channel

    dayAndMonth = datetime.datetime.now(timezone).strftime("%d/%m") #Checks if there is an event on that day
    with open("events.json", "r") as file:
        eventDict = json.load(file)
    if dayAndMonth in eventDict:                             #If there is, the bot sends a message to say what event it is
        await channelObject.send(f"It is {eventDict[dayAndMonth]} today!") 
            
    with open("date.json", "w") as file:
        json.dump(currentDate,file)        

    with open("streaks.json", "r") as file:                
        streaksDict = json.load(file)
    for i in streaksDict:
        userInfoDict = streaksDict[i]                        # goes through all user records in the database and checks if a user has an active streak, and if they have not chatted yet.
        if userInfoDict["sentMessage"] == False and userInfoDict["streak"] > 0:
            user = discordClient.get_user(userInfoDict)      # resets users streak and notifies user
            channelObject.send(f'{user.mention}, you broke your streak of {userInfoDict["streak"]}!')
            userInfoDict["streak"] = 0
        userInfoDict["sentMessage"] = False
        streaksDict[i] = userInfoDict

@discordClient.event                                          #Fires the event when a message is sent
async def on_message(message):
    if message.author.bot:
        return
    with open("streaks.json", "r") as file:
        streaksDict = json.load(file)
    
    if str(message.author.id) in streaksDict:                      #Finds the user in the data base and updates thier streak, if there is no record, it creates a default and sets the streak to 1
        userInfoDict = streaksDict[str(message.author.id)]
        userInfoDict["streak"] = userInfoDict["streak"] + 1
        userInfoDict["sentMessage"] = True
        streaksDict[message.author.id] = userInfoDict
    else:
        userInfoDict = {
            "streak" : 1,
            "sentMessage": True
        }
        streaksDict[message.author.id] = userInfoDict

    await message.channel.send(f'{message.author.mention}, you now have a streak of {userInfoDict["streak"]}!')

    with open("streaks.json", "w") as file:
        json.dump(streaksDict,file)
    

@eventLoop.before_loop                                        #Runs this function before starting the event loop
async def init():
    await discordClient.wait_until_ready()

    serverId = 1071286494624485466                            #Finds the diary server and creates the object of the server for the program to interact with it
    global serverObject
    for i in discordClient.guilds:
        if i.id == serverId:
            serverObject = i
            break

    catergoryId = 1071287384353816666                          #Finds the catergory to create the monthly channels in and creates an object for it
    global catergoryObject
    for i in serverObject.channels:
        if i.id == catergoryId:
            catergoryObject = i
            break

discordClient.run(discordToken)