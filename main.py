# bot.py
from keep_alive import keep_alive
import os
import random
import discord
import json
import requests
import mechanicalsoup
import arg
import random
import sys
import requests
from dotenv import load_dotenv
import random
from random import choice

load_dotenv()
from discord.ext import commands
from dotenv import load_dotenv

keep_alive()
TOKEN = os.environ['arvid']

bot = commands.Bot(command_prefix='$')
####
#Endless-Online Change Update ###
#Json - Post Info? Testing
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.command(name='bot', help='posts current bots exp and lvl')
@commands.cooldown(1, 50, commands.BucketType.user)
async def exp(ctx):
    r = requests.get('https://game.eoserv.net/api/get_character?name=kodyt')
    json_data = json.loads(r.text)
    status_bot = json_data['level']
    status_exp = json_data['exp']
    status_guild = json_data['guild']
    await ctx.send('Bot Level is: **{}**'.format(status_bot) +
                   '       Current EXP is: **{}**'.format(status_exp) +
                   '       http://bbis.us/~blo/eosig/?user=kodyt&type=4')


# CHAR LOOK UP
@bot.command(
    name='player',
    help=
    '$player posts player stats.'
)
@commands.cooldown(1, 5, commands.BucketType.user)
async def exp(ctx, charName):
    r = requests.get('https://game.eoserv.net/api/get_character?name=' +
                     charName)
    json_data = json.loads(r.text)
    status_bot = json_data['level']
    status_exp = json_data['exp']
    status_guild = json_data['guild']
    status_usage = json_data['usage']
    status_home = json_data['home']
    status_title = json_data['title']
    
    await ctx.send('```\n Player Level: {}'.format(status_bot) +                                                                                          
                   '      \n EXP: {}'.format(status_exp) +                    
                   
                   '      \n Guild: {}'.format(status_guild) +                                                                                            
                   
                   '      \n Current Usage: {}'.format(status_usage) +             
                   
                   '     \n Title is: {}```'.format(status_title))
####
##item look up
# CHAR LOOK UP
@bot.command(
    name='sitem',
    help=
    'Look up and Item via eoserv.net using the Items ID number.'
)
@commands.cooldown(1, 10, commands.BucketType.user)
async def exp(ctx, itemID):
  
    r = requests.get('https://game.eoserv.net/item?item=' +
                     itemID)

    await ctx.send('https://game.eoserv.net/item?item=' +
                     itemID) 


###DOWNLOAD EO
@bot.command(name="servers", help='Endless Online Downloads')
@commands.cooldown(1, 10, commands.BucketType.user)
async def displayembed(ctx):
    embed = discord.Embed(title="**EO Clone**",
                          description="https://game.eoserv.net/")
    embed.add_field(name="**Fallen Evolution**",
                    value="https://fallen-evolution.com/",
                    inline=False)
    embed.add_field(name="**Bones Underground**",
                    value="http://game.bones-underground.org",
                    inline=False)
    embed.add_field(name="**EO2**",
                    value="http://www.endlessonline2.com/",
                    inline=False)
    embed.add_field(name="**EO Plus**",
                    value="http://eo-plus.com/",
                    inline=False)
    embed.add_field(name="**Server List**",
                    value="http://www.apollo-games.com/SLN/sln.php",
                    inline=False)

    embed.set_footer(
        text='\u200b',
        icon_url="https://cdn-icons-png.flaticon.com/512/183/183580.png")
    await ctx.send(embed=embed)


#Embed Commands


@bot.command(name="arvid", help='Arvid lists his commands.')
@commands.cooldown(1, 5, commands.BucketType.user)
async def displayembed(ctx):
    embed = discord.Embed(title="Hi, I'm Arvid.",
                          description="I'm a bot, I like to wall people.")
    embed.add_field(name="**$player <name>**",
                    value="This will post the players level and exp.",
                    inline=False)
    embed.add_field(name="**$eosig <name>**",
                    value="This will post a random eosig of the player.",
                    inline=False)
    embed.add_field(name="**$eo**",
                    value="This will post a random Endless Online Fact.",
                    inline=False)
    embed.add_field(name="**$servers**",
                    value="This will post the best known EO Servers.",
                    inline=False)

    embed.set_footer(
        text='\u200b',
        icon_url="https://cdn-icons-png.flaticon.com/512/183/183580.png")
    await ctx.send(embed=embed)


#EOSERV LOGIN and LOC
import mechanicalsoup


@bot.command(name="loc", help='bot cords')
@commands.cooldown(1, 50, commands.BucketType.user)
async def displayembed(ctx):

    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://game.eoserv.net/character?name=kodyt")
    browser.select_form()
    browser["username"] = my_secret = os.environ['username']
    browser["password"] = my_secret = os.environ['password']


    browser.submit_selected()

    page = browser.page

    startIndex = page.text.find("nMap") + 1
    endIndex = page.text.find("Stats")
    newStringArray = page.text[startIndex:endIndex].split(
    )  # ['Map143', 'X3', 'Y28']

    mapOutput = newStringArray[0]  # 'Map143'
    coordsOutput = newStringArray[1] + "\n" + newStringArray[
        2]  # 'X3 <newline> Y28'

    embed = discord.Embed(
        title="Location",
        description=
        "Current character location information, if character is on map 76 bot has been jailed. Botting On Twitch at https://www.twitch.tv/kodytron "
    )
    embed.add_field(name="Map", value=mapOutput, inline=False)
    embed.add_field(name="Coords", value=coordsOutput, inline=False)

    await ctx.send(embed=embed)


#######


#Endless Online Facts
@bot.command(name='eo', help='Posts a random *fact* about Endless Online.')
@commands.cooldown(1,20, commands.BucketType.user)
async def eo_history(ctx):
    eo_history = [
        'The server was destroyed.',
        'Is this eo discord or hello kitty online?',
        ('2022 - New Client: http://endless-online.com/downloads.html'),
        ('26th November 2009 - Servers are back online'),
      ('Sordie had us all with the kelogs!'),
        ('Eoserv.net - lets make a private server!'),
        ('2022 - VULT CAME HOME,'
         ' but will he be qwiddled again?'),
        ('21st March 2011 - Character reset'),
        ('July 2015 - BUYVM.NET aka frantech gave away the server'
         ' ..they got qwiddled'),
        ('Auguest 2015 - To the community'
         ' Its still unbelievable for me knowing that this critical access was just handed over by BUYVM.NET to people with bad intentions. EO will be down for now.'
         ),
        ('v16 released Jan 15th,'
         ' but on the 18th the server went down due to a heartless datacentre.'
         ),
        ('21st September 2005  Update Now that we have a magic/skill system working the next step should be a new NPC type to train learn new spells.'
         ),
        ('9th Febuary 2004 - OMG! we are back -Yep, we are back and meanwhile we have been working quite hard on the mmrpg project. (see version history) Things can only get better from this point since there is a dedicated server available.'
         ),
    ]

    response = random.choice(eo_history)
    await ctx.send(response)


#RANDOM IMAGE EOSIG LOOK UP
@bot.command(name='eosig', help='Look Up Char Info Via EoSig')
@commands.cooldown(1, 10, commands.BucketType.user)
async def eosig(ctx, charName):
    eosig = [
        'http://bbis.us/~blo/eosig/?user=' + charName + '&type=2',
        'http://bbis.us/~blo/eosig/?user=' + charName + '&type=3',
        ('http://bbis.us/~blo/eosig/?user=' + charName + '&type=1 '),
    ]

    response = random.choice(eosig)
    await ctx.send(response)


#
@bot.command(name='funfact')
async def fun_fact(ctx):
    global terminal_quotes
    terminal_quotes = [
        '** Fun fact: in 2208 Elon Musk\'s corpse was recovered for reproductive purposes.**',
        '** Popular architect Andres Gil was murdered by a swimmer whose name has been scrubbed from history. Only his spine was found.**',
        '** In 2033, Forest Ranger Taylor Brown found the first evidence of extraterrestrial life. It was a small meteor embed with a message.**',
        '** Spaceforce General OkieDokie flew the first glass pipe into their mouth and return in 2085.**',
        '** Famous artist LilPeace painted the first image of the Aliues, the First Contacts.**',
        '** ToxicGenocide is responsible for the COVID-29 vaccine. He would also go on to create several other vaccines.**',
        '** Doctor Ian Torrence invented the first artifical skin replacement. This would lead to a breakthrough in cosmetic surgeries on mens penis replacements.**',
        '** twitch.tv/rtlove was cool until he got banned on sea of thieves. He was sent on a solo colonization mission after micrsoft ended his streaming carrier. He was leading LDS church members to their death in an attempt to walk the Pacific Ocean.**',
        '** Doctor Alyssa McAdams is responsible for the leading CPR technique still used to date. She discovered this by accident while trying to save her partner, Blake.**',
        '** Mrcook was the first ever player of grand theft auto online. SQUEEEZE.**',
        '** RTloVe, prestigious esport streamer, beat the world record for time spent streaming continuously at 168 hours.**',

        (
            '**Mrcook hacked the CIA with his hands, '
            'leaving approximately 2.7 million civillians in danger of being accused of his crimes.**'
        ),
        (
            '**There was a decorated Sea Of Theives Player and esport professional who, in 2031, was finally unbanned from SoT.'
            ' Unfortunately, he would later go on to miss the game winning Insec at the League of Legends World Championship (season 2033)'
            ', resulting in a 2-3 loss for the first ever North American team to reach the final bracket. North America would never'
            ' reach another finals up until the esport ended in 2040. League of Legends was the United State\'s primary esport.**'
        ),
    ]
    response = random.choice(terminal_quotes)
    await ctx.send(response)
###

@bot.command(name='rps',help="Play with $rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await bot.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")
###arvid


@bot.command(name='hey')
async def randomroman(ctx, member: discord.Member=None):
    member = member or ctx.author

    variable=[
        f'{member.mention} Im about to wall you.',
        f'{member.mention} DO U SEE THAT THATS A LIGHT BULB ACTAVIST!',
        f'{member.mention} Lets all go play GTA ONLINE!'
       f'{member.mention} On Hood <:55th:912358713057235014>',
        f'{member.mention} I dont have time for your shit son.',
        f'{member.mention} Im not having any of your shit today son.',
       f'{member.mention} WEeeeWeeeeee eat meeeee eeeehhhhh'
        f'{member.mention} Elon Muscles beat the rock for the heavey weight UFC title in 2030 bet u didnt kno daaaaat catch me outside',
        f'{member.mention} Do you like it? ||I bet u do fae boy||',
        f'{member.mention} Have you heard the joke about the dumb ass with the phone? Look in the mirror dumb ass.'
       f'{member.mention} Im about to trout slap the shit out of u <:55th:912358713057235014>',
        f'{member.mention} When you die I bet mom will have a party. The Banner will read: The abortion Finally Took',
        f'{member.mention} So let me ask you this, why do you suck? -smile-',
        f'{member.mention} Did you know Steve The Crocodile dinkler from Down Undaaah died how he lived?'
    ]
    await ctx.send(random.choice(variable))
###Cook Pics ##
@bot.command(name='media')
async def randomroman(ctx, member: discord.Member=None):
    member = member or ctx.author

    variable=[
        f'{member.mention} want some pizza losers? https://cdn.discordapp.com/attachments/788233185199783976/794797510447202344/12_inch_pizza.mp4',
        f'{member.mention} Mr effin Cook is going to be walled https://cdn.discordapp.com/attachments/788233185199783976/846137559751196712/unknown.png',
        f'{member.mention} Haha yeah cool man https://cdn.discordapp.com/attachments/788233185199783976/894085103125426176/1633236803754.png'
       f'{member.mention} y u liek dis? https://cdn.discordapp.com/attachments/788233185199783976/917636425346842674/IMG_1538.png',
        f'{member.mention} what happened?! https://cdn.discordapp.com/attachments/788233185199783976/917636442224721950/1638849451373.png',
        f'{member.mention} suck my titties. https://cdn.discordapp.com/attachments/788233185199783976/788285823111790631/Suck_My_Tittie.mp4',
        f'{member.mention} https://cdn.discordapp.com/attachments/788233185199783976/788285909308145684/feet_1.png'
    ]
    await ctx.send(random.choice(variable))
#New 

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if "mrscook" in message.content.lower():
        await message.channel.send("Mrscook got tributed on 4chan - thanks belac.")
    if "mrcook" in message.content.lower():
        await message.channel.send("Mrcook is the best streamer ever. When he yells at his mom I cant help but gasp and spit my milk out.")
    if "mscook" in message.content.lower():
        await message.channel.send("Mscook get's tested for STI's weekly.")
def on_message(self, message):
    if (message.author.bot):
        return

      #RANDOM PHOTO


bot.run(TOKEN)
