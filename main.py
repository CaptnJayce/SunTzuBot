# main.py 
import discord
import random 
import os
import datetime
import time 
import asyncio
import nextcord
from nextcord.ext import commands, tasks
from dotenv import load_dotenv
from astral.sun import sun
from astral import LocationInfo

intents = nextcord.Intents.default()
intents.message_content = True

load_dotenv()
bot = commands.Bot(command_prefix="!", intents=intents)

quotes = [
    "The supreme art of war is to subdue the enemy without fighting.",
    "Appear weak when you are strong, and strong when you are weak.",
    "If you know the enemy and know yourself, you need not fear the result of a hundred battles.",
    "Opportunities multiply as they are seized.",
    "The greatest victory is that which requires no battle.",
    "All warfare is based on deception.",
    "The art of war teaches us to rely not on the likelihood of the enemy's not coming, but on our own readiness to receive him.",
    "The general who wins the battle makes many calculations in his temple before the battle is fought.",
    "There is no instance of a nation benefitting from prolonged warfare.",
    "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.",
    "The good fighters of old first put themselves beyond the possibility of defeat, and then waited for an opportunity of defeating the enemy.",
    "Treat your men as you would your own beloved sons. And they will follow you into the deepest valley.",
    "To know your Enemy, you must become your Enemy.",
    "Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.",
    "The opportunity to secure ourselves against defeat lies in our own hands, but the opportunity of defeating the enemy is provided by the enemy himself.",
    "In the midst of chaos, there is also opportunity.",
    "The clever combatant imposes his will on the enemy, but does not allow the enemy's will to be imposed on him.",
    "Even the finest sword plunged into salt water will eventually rust.",
    "Engage people with what they expect; it is what they are able to discern and confirms their projections. It settles them into predictable patterns of response, occupying their minds while you wait for the extraordinary moment — that which they cannot anticipate.",
    "There is no instance of a country having benefited from prolonged warfare.",
    "He who is prudent and lies in wait for an enemy who is not, will be victorious.",
    "To win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill.",
    "The greatest victory is that which requires no battle.",
    "Be extremely subtle, even to the point of formlessness. Be extremely mysterious, even to the point of soundlessness. Thereby you can be the director of the opponent's fate.",
    "All men can see these tactics whereby I conquer, but what none can see is the strategy out of which victory is evolved.",
    "The quality of decision is like the well-timed swoop of a falcon which enables it to strike and destroy its victim.",
    "When strong, avoid them. If of high morale, depress them. Seem humble to fill them with conceit. If at ease, exhaust them. If united, separate them. Attack their weaknesses. Emerge to their surprise.",
    "Move swift as the Wind and closely-formed as the Wood. Attack like the Fire and be still as the Mountain.",
    "Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.",
    "To fight and conquer in all your battles is not supreme excellence; supreme excellence consists in breaking the enemy's resistance without fighting.",
    "The greatest victory is that which requires no battle."
]

'''
@bot.command(name="quote")
async def quote(ctx):
    await ctx.send("@everyone '" + quotes[0] + "'\n -Sun Tzu, The Art of War")
'''

loc = LocationInfo(name='London', region='England', timezone='Europe/London', latitude=51.5072, longitude=0.1276)
s = sun(loc.observer, date=datetime.date(2023, 11, 26), tzinfo=loc.timezone)

sunrise_time = s['sunrise'].strftime("%H:%M")
sunset_time = s['sunset'].strftime("%H:%M")

now = datetime.datetime.now().strftime("%H:%M")

'''
print(now)
print(f"Sunrise time: {sunrise_time}")
print(f"Sunset time: {sunset_time}")
'''

i = 0

@tasks.loop(minutes=1)
async def schedule_message():
    print("checking time...")
    if(now == sunrise_time or now == sunset_time):    
        global i
        print(i)
        # id for sun-tzus-inspiration channel: 1177992967852675102
        # id for bot-testing channel: 1178013378984296551
        channel = bot.get_channel(1177992967852675102)
        await channel.send("@everyone '" + quotes[i] + "'\n -Sun Tzu, The Art of War")
        i += 1
    else:
        print("it isn't sunrise/sunset yet")
        
@bot.event
async def on_ready():
    print(f"Logged on motherfuckers")
    random.shuffle(quotes)
    await schedule_message.start()

if __name__ == '__main__':
    bot.run(os.getenv("BOT_TOKEN"))