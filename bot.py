import json
import os
import re
import discord
from discord.ext import commands
import asyncio
import DiscordUtils


async def get_prefix(bot, message):
    p = re.search(bot.prefix + "\\s*", message.content, re.I)
    if p:
        return message.content[:len(p.group())].lstrip()

    return commands.when_mentioned(bot, message)


def attach_cogs(bot):
    cog_list = os.listdir("cogs/")
    for extension in cog_list:
        if ".py" not in extension:
            continue
        extension = extension[:-3]
        try:
            bot.load_extension(f"cogs.{extension}")
        except discord.ext.commands.errors.ExtensionAlreadyLoaded:
            return
        except Exception as e:
            print(f"\n[ERR] Failed to load extension {extension}. Reason: {e}")


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents = discord.Intents.all())
bot.prefix = "fun"
#bot.remove_command('help') <- you can use that if you want to make a custom command
attach_cogs(bot)





# EVENTS
@bot.event
async def on_ready():
    print("yey")
    game = discord.Game("fun help") #- you can change the bot activity here
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if type(error) is commands.CommandNotFound:
        return
    elif type(error) is commands.MissingRole:
        embed = discord.Embed(title="Nu ai rolul necesar pentru a utiliza aceasta comanda!", color=discord.Colour.red()) #translate (You do not have the required role to use this command!)
        msg=await ctx.send(embed=embed)
        await asyncio.sleep(6)
        await msg.delete()
    elif type(error) is commands.MissingPermissions:
        embed = discord.Embed(title="Nu ai permisiunile necesare pentru a utiliza comanda!", color=discord.Colour.red()) #translate (You do not have the necessary permissions to use the command! )
        msg=await ctx.send(embed=embed)
        await asyncio.sleep(6)
        await msg.delete()
    elif type(error) is commands.CommandOnCooldown:
        embed = discord.Embed(title="Esti in cooldown, încearcă să folosești din nou comanda peste {:.2f} secunde".format(error.retry_after), color=discord.Colour.red()) #translate(You are in the cooldown, try using the command again in {: .2f} seconds )
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(6)
        await msg.delete()
    else:
        print(error)


async def start():
    await bot.start("TOKEN", bot=True, reconnect=True) #change token text with your bot token 


if __name__ == "__main__":
    try:
        bot.loop.run_until_complete(start())
    except KeyboardInterrupt:
        bot.loop.run_until_complete(bot.close())
    except Exception as ex:
        print(f"[ERROR] {ex}")
    finally:
        print("Good Night!")
        bot.loop.close()
