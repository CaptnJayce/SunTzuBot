# main.py 
import random 
import os
import datetime
import nextcord
from nextcord.ext import commands, tasks
from dotenv import load_dotenv
from astral.sun import sun
from astral import LocationInfo
import datetime
from datetime import date

intents = nextcord.Intents.default()
intents.message_content = True

load_dotenv()
bot = commands.Bot(command_prefix="/", intents=intents)

quotes = [
    "The supreme art of war is to subdue the enemy without fighting.",
    "All warfare is based on deception.",
    "Appear weak when you are strong, and strong when you are weak.",
    "If you know the enemy and know yourself, you need not fear the result of a hundred battles.",
    "Opportunities multiply as they are seized.",
    "The greatest victory is that which requires no battle.",
    "The general who wins a battle makes many calculations in his temple before the battle is fought.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "To win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill.",
    "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.",
    "Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.",
    "The art of war teaches us to rely not on the likelihood of the enemy's not coming, but on our readiness to receive him; not on the chance of his not attacking, but rather on the fact that we have made our position unassailable.",
    "The quality of decision is like the well-timed swoop of a falcon which enables it to strike and destroy its victim.",
    "The opportunity of defeating the enemy is provided by the enemy himself.",
    "To fight and conquer in all your battles is not supreme excellence; supreme excellence consists in breaking the enemy's resistance without fighting.",
    "Hence to fight and conquer in all your battles is not supreme excellence; supreme excellence consists in breaking the enemy's resistance without fighting.",
    "What is essential in war is victory, not prolonged operations.",
    "The clever combatant imposes his will on the enemy, but does not allow the enemy's will to be imposed on him.",
    "The good fighters of old first put themselves beyond the possibility of defeat, and then waited for an opportunity of defeating the enemy.",
    "Move swift as the Wind and closely-formed as the Wood. Attack like the Fire and be still as the Mountain.",
    "The art of war is of vital importance to the State.",
    "There is no instance of a nation benefiting from prolonged warfare.",
    "Thus the highest form of generalship is to balk the enemy's plans.",
    "To know your Enemy, you must become your Enemy.",
    "The skilful employer of men will employ the wise man, the brave man, the covetous man, and the stupid man.",
    "The general who advances without coveting fame and retreats without fearing disgrace, whose only thought is to protect his country and do good service for his sovereign, is the jewel of the kingdom.",
    "He will win who knows when to fight and when not to fight.",
    "He who knows when he can fight and when he cannot will be victorious.",
    "He will win who knows how to handle both superior and inferior forces.",
    "If you know the enemy and know yourself, you need not fear the result of a hundred battles.",
    "To secure ourselves against defeat lies in our own hands, but the opportunity of defeating the enemy is provided by the enemy himself.",
    "Know yourself and you will win all battles.",
    "The victorious strategist only seeks battle after the victory has been won.",
    "The general who loses makes a point to look for the cause within himself.",
    "The wise warrior avoids the battle.",
    "Even the finest sword plunged into salt water will eventually rust.",
    "In the midst of chaos, there is also opportunity.",
    "If you wait by the river long enough, the bodies of your enemies will float by.",
    "There are not more than five musical notes, yet the combinations of these five give rise to more melodies than can ever be heard.",
    "When strong, avoid them. If of high morale, depress them. Seem humble to fill them with conceit. If at ease, exhaust them. If united, separate them. Attack their weaknesses. Emerge to their surprise.",
    "Rouse him, and learn the principle of his activity or inactivity. Force him to reveal himself, so as to find out his vulnerable spots.",
    "All men can see these tactics whereby I conquer, but what none can see is the strategy out of which victory is evolved.",
    "The skillful tactician may be likened to the shuai-jan. Now the shuai-jan is a snake that is found in the Ch'ang mountains. Strike at its head, and you will be attacked by its tail; strike at its tail, and you will be attacked by its head; strike at its middle, and you will be attacked by head and tail both.",
    "The energy developed by good fighting men is as the momentum of a round stone rolled down a mountain thousands of feet in height.",
    "He who is prudent and lies in wait for an enemy who is not, will be victorious.",
    "The clever combatant looks to the effect of combined energy, and does not require too much from individuals.",
    "If fighting is sure to result in victory, then you must fight, even though the ruler forbid it; if fighting will not result in victory, then you must not fight even at the ruler's bidding.",
    "Hence the saying: If you know the enemy and know yourself, you need not fear the result of a hundred battles.",
    "Thus, what is of supreme importance in war is to attack the enemy's strategy.",
    "Pretend inferiority and encourage his arrogance.",
    "So in war, the way is to avoid what is strong, and strike at what is weak.",
    "The greatest victory is that which requires no battle.",
    "The general who wins a battle makes many calculations in his temple before the battle is fought.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "To win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill.",
    "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.",
    "Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.",
    "The art of war teaches us to rely not on the likelihood of the enemy's not coming, but on our readiness to receive him; not on the chance of his not attacking, but rather on the fact that we have made our position unassailable.",
    "The quality of decision is like the well-timed swoop of a falcon which enables it to strike and destroy its victim.",
    "The opportunity of defeating the enemy is provided by the enemy himself.",
    "To fight and conquer in all your battles is not supreme excellence; supreme excellence consists in breaking the enemy's resistance without fighting.",
    "Hence to fight and conquer in all your battles is not supreme excellence; supreme excellence consists in breaking the enemy's resistance without fighting.",
    "What is essential in war is victory, not prolonged operations.",
    "The clever combatant imposes his will on the enemy, but does not allow the enemy's will to be imposed on him.",
    "The good fighters of old first put themselves beyond the possibility of defeat, and then waited for an opportunity of defeating the enemy.",
    "Move swift as the Wind and closely-formed as the Wood. Attack like the Fire and be still as the Mountain.",
    "The art of war is of vital importance to the State.",
    "There is no instance of a nation benefiting from prolonged warfare.",
    "Thus the highest form of generalship is to balk the enemy's plans.",
    "To know your Enemy, you must become your Enemy.",
    "The skilful employer of men will employ the wise man, the brave man, the covetous man, and the stupid man.",
    "The general who advances without coveting fame and retreats without fearing disgrace, whose only thought is to protect his country and do good service for his sovereign, is the jewel of the kingdom.",
    "He will win who knows when to fight and when not to fight.",
    "He who knows when he can fight and when he cannot will be victorious.",
    "He will win who knows how to handle both superior and inferior forces.",
    "If you know the enemy and know yourself, you need not fear the result of a hundred battles.",
    "To secure ourselves against defeat lies in our own hands, but the opportunity of defeating the enemy is provided by the enemy himself.",
    "Know yourself and you will win all battles.",
    "The victorious strategist only seeks battle after the victory has been won.",
    "The general who loses makes a point to look for the cause within himself.",
    "The wise warrior avoids the battle.",
    "Even the finest sword plunged into salt water will eventually rust.",
    "In the midst of chaos, there is also opportunity.",
    "If you wait by the river long enough, the bodies of your enemies will float by.",
    "There are not more than five musical notes, yet the combinations of these five give rise to more melodies than can ever be heard.",
    "When strong, avoid them. If of high morale, depress them. Seem humble to fill them with conceit. If at ease, exhaust them. If united, separate them. Attack their weaknesses. Emerge to their surprise.",
    "Rouse him, and learn the principle of his activity or inactivity. Force him to reveal himself, so as to find out his vulnerable spots.",
    "All men can see these tactics whereby I conquer, but what none can see is the strategy out of which victory is evolved."
]

date = date.today()
year = date.year
month = date.month
day = date.day

loc = LocationInfo(name='London', region='England', timezone='Europe/London', latitude=51.5072, longitude=0.1276)
s = sun(loc.observer, date=datetime.date(year, month, day), tzinfo=loc.timezone)

sunrise_time = s['sunrise'].strftime("%H:%M")
sunset_time = s['sunset'].strftime("%H:%M")

# Function to get current time
def get_current_time():
    return datetime.datetime.now().strftime("%H:%M")

print(f"Sunrise time: {sunrise_time}")
print(f"Sunset time: {sunset_time}")

i = 0

# used for the active developer badge
@bot.command(name="quoteme")
async def quote(ctx):
        channel = bot.get_channel(1178013378984296551)
        await channel.send("@everyone '" + quotes[i] + "'\n -Sun Tzu, The Art of War")

@tasks.loop(minutes=1)
async def schedule_message():
    now = get_current_time()
    print("Current time is: " + now)
    if(now == sunrise_time or now == sunset_time):
        print("It is time for a quote")    
        global i
        print(i)
        # id for sun-tzus-inspiration channel: 1177992967852675102
        # id for bot-testing channel: 1178013378984296551
        channel = bot.get_channel(1177992967852675102)
        await channel.send("@everyone '" + quotes[i] + "'\n -Sun Tzu, The Art of War")
        i += 1
    else:
        print("It isn't sunrise/sunset yet")
        
@bot.event
async def on_ready():
    print(f"Logged on")
    random.shuffle(quotes)
    await schedule_message.start()

if __name__ == '__main__':
    bot.run(os.getenv("BOT_TOKEN"))