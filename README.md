# discorddiary
A discord bot written using discord.py to make a diary on a discord server, with a streaks system

# How it works
Everyday, at midnight (gmt +8) , the bot will send the current date into the channel to help mark the start of a new day.
If it is a new month, the bot will create a new discord channel with the month and the year.
When a user sends a message for the first time that day, the bot will tell the user's current streak and thank them for mantaining their streak
If the user with a streak has not sent a message that day, the bot will remind them to send a message to mantain thier streak at 7pm (gmt +8)
