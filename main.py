# main.py 
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

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

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!quoteme"):
        random.shuffle(quotes)
        await message.channel.send("@everyone '" + quotes[0] + "'\n - Sun Tzu, The Art of War")

client.run("MTE3NzY4MjQ1MDUxNjgxMTg1Nw.GVj5ng.QdoTpnu_eGaGPGtjqmpyb7_oYOpjwmrx3AjNWg")