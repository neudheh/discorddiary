# discorddiary
A discord bot written using discord.py to make a diary on a discord server, with a streaks system

# How it works
Everyday, at midnight (gmt +8) , the bot will send the current date into the channel to help mark the start of a new day.

https://user-images.githubusercontent.com/39615611/216775797-e2015438-a0c9-4996-9ec2-3085906e1ec5.mp4

If it is a new month, the bot will create a new discord channel with the month and the year.

https://user-images.githubusercontent.com/39615611/216775709-35d30f50-829f-4f65-92e0-1a94292e3ab9.mp4

When a user sends a message for the first time that day, the bot will tell the user's current streak and thank them for mantaining their streak.
**New user that has never used the bot before*:

https://user-images.githubusercontent.com/39615611/216775930-afdfdcf2-da65-4951-8a93-5a2df114308f.mp4

**Existing user that already has a streak in the database**:

https://user-images.githubusercontent.com/39615611/216776132-80b02b0c-dab8-4c75-90f2-ed56decd5082.mp4

If a user with an active streak has not chatted for the whole day, they lose thier streak.

https://user-images.githubusercontent.com/39615611/216776147-99d114a9-b21f-4a37-9351-e4200fccbac9.mp4

# Features
- Tells users what special celebrations are on that day, such as birthdays or christmas 

https://user-images.githubusercontent.com/39615611/216776433-5d8b89b1-3a70-41d8-98ca-7f34d3f8aee7.mp4

- Streaks system to prompt users to write everyday
- Different discord channels for each month to help organise
- Sends the date to help users remeber what happened on that day when they look back at their diary

# Improvements to be made
- Allow users to change timezones, in the event that they are overseas or not in gmt +8
- Allow users to create their own events
- Allow users to configure and set up the program within discord and not have to edit the code
