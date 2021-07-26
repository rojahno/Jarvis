# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='create-channel', help="creates a new text channel")
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.command(name='delete-channel', help='delete a channel with the specified name')
@commands.has_role("admin")
async def delete_channel(ctx, channel_name):
    # check if the channel exists
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)

    # if the channel exists
    if existing_channel is not None:
        await existing_channel.delete()
    # if the channel does not exist, inform the user
    else:
        await ctx.send(f'No channel named, "{channel_name}", was found')


@bot.command(name="d6", help="Rolls a six sided dice")
async def roll_d6(ctx):
    dice = str(random.choice(range(1, 7)))
    await ctx.send(dice)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


if __name__ == "__main__":
    print("running")
    bot.run(TOKEN)
