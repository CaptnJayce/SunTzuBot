# suntzubot
A simple python discord bot that sends 'Sun Tzu, The Art of War' quotes to my server at (roughly) the time of sunset and sunrise.\
Disclaimer: 
- due to the api this bot is typically a few minutes earlier than iftar
- you can't update datetime during runtime so restarting each day is needed for accurate timing 

**Necessary:**\
✔️ Time should synchronize with actual sunrise and sunset\
✔️ Quotes should be random\
✔️ The same quote cannot be said twice in a row\
~~❌ Quotes can't be reused within 48 hours~~ This isn't even possible due to linear iteration over the array

**Optional:**\
✔️ Have 100 quotes in total\
❌ Comment code\
❌ Themed quotes during seasons and holidays such as Ramadan, Christmas, Winter, Autumn, etc\
❌ Quotes can be listed, removed and added via my personal discord server
