# Line Chat Analyzer

This is the repository for my ongoing line chat analyzer. The goal of this project
is to find out a chat's basic stats. I made this project since LINE doesn't 
provide stats for your chats (to my knowledge) and I couldn't find anyone who 
already made an analyzer for line chats. It is written in Python making use of 
pandas and matplotlib for analysis and visualization. 

It works by analyzing the chat's history which is provided by LINE on its 
mobile app. Text data is first cleaned and then converted into a dataframe. From
there we can count a user's total number of chats, stickers, shares, etc. Since
chat history formats for personal chat and group chats are the same, this code
should work for both.

### Current Features
> - Frequency of chats per hour -> most active hours
> - Frequency of chat (including shares, stickers, photos) per user 
> - Frequency of post shares per user 
> - Frequency of sticker use per user
> - Frequency of photo adding per user
> - Frequency of chat (text only) per user
> - Avg of chat length by character per user 
> - Avg of chat length by word per user

### Specifications:
* Python 3.7
* Libraries: Pandas, Yaml, wordcloud,


### How To Use:

---

#### Retrieving Chat History
On how to check retrieve chat history check out (https://help.line.me/line/?contentId=20004537)
> 1. Tap the menu icon at the top of the chat screen > Other settings.
> 2. Tap Export chat history and choose how you want to send the file.

Before you transfer send the text file from your phone to your computer, create a
folder with same name as your group name separated by comma. This serves as a 
convention to help you in the future since you need to specify the name of the
folder as well as the name of the file in the config. Then create two folders
named 'cleaned' and 'original. Place the file on the original.
> Group_Number_1_chat_history.txt --> folder: Group_Number_1

---

### Analyzing Chat
1. Configure folder and filename on env.yaml
    - for group chats there are cases where authors possess multiple accounts. To
    count their chats as one, specify the duplicated name with the real names
    > Potato : "Richard Hendriks"
2. Run main.py


## TO DO:
1. Add test files
2. Config menu to choose which stat to retrieve
3. Refactor main.py module
3. Web implementation