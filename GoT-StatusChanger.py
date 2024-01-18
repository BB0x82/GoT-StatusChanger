# Nemt, Simpelt
# GUD BEVAR DANMARK
# LÆNGE LEVE 0x.82

import discord
import asyncio
import os
import ctypes
from colorama import Fore


ctypes.windll.kernel32.SetConsoleTitleW("GoT-StatusChanger          |          Credit: 0x.82")
user_token = ''
client = discord.Client()

async def change_status(status_type, status_text, image_url=None, url=None):
    activity = None
    if status_type.lower() == "watching":
        activity = discord.Activity(type=discord.ActivityType.watching, name=status_text)
    elif status_type.lower() == "listening":
        activity = discord.Activity(type=discord.ActivityType.listening, name=status_text)
    elif status_type.lower() == "streaming":
        activity = discord.Streaming(name=status_text, url=url, twitch_name="")
    elif status_type.lower() == "playing":
        activity = discord.Game(name=status_text)

    await client.change_presence(activity=activity)

@client.event
async def on_ready():
    print(f"Tak for din token JIMMY!  ==  {client.user}")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("")
        logo = '''
                     ██████╗  ██████╗ ████████╗    ███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ 
                    ██╔════╝ ██╔═══██╗╚══██╔══╝    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗
                    ██║  ███╗██║   ██║   ██║       ███████╗██║   ██║██║   ██║███████║██║  ██║
                    ██║   ██║██║   ██║   ██║       ╚════██║██║▄▄ ██║██║   ██║██╔══██║██║  ██║
                    ╚██████╔╝╚██████╔╝   ██║       ███████║╚██████╔╝╚██████╔╝██║  ██║██████╔╝
                     ╚═════╝  ╚═════╝    ╚═╝       ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝                                                                      
        '''
        moving_text = "                              Vil du joine GoT Squad så ansøg forhelved: cXjbUrGS4W"

        print(f'{Fore.RED}{logo}')
        print(f'{Fore.RED}{moving_text}{Fore.LIGHTRED_EX}')
        print("")
        print("  1. SOLID Changer")
        print("  2. AUTO Changer")
        print("  3. Quit")

        choice = input("  Vælg: ")

        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')

            status_text = input("  Skriv din Status Title: ")
            status_type = input("  (watching/playing/listening/streaming): ")

            await change_status(status_type, status_text)

        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')

            status_messages = []
            while True:
                status_text = input("  Skriv din Status Titler (Tryk ENTER og skriv 'done' for at færdiggøre): ")
                if status_text.lower() == "done":
                    break
                status_messages.append(status_text)

            status_type = input("  (watching/playing/listening/streaming): ")
            time_interval = 2

            while True:
                for status_text in status_messages:
                    await change_status(status_type, status_text)
                    await asyncio.sleep(time_interval)

        elif choice == "3":
            break

        else:
            print("  Er du født i en bus? Skriv nu forhelved et tal som du kan se på skærmen!")

    await client.close()

client.run(user_token, bot=False)

#CREDIT      GoT 0x.82
#CREDIT      GoT 0x.82
#CREDIT      GoT 0x.82