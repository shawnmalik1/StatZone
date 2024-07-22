import discord
from discord import app_commands
from discord.ext import commands
import responses
import commands_json
import json
from thefuzz import process

with open("2024 NBA League.json", "r") as file:
    data = json.load(file)

players = data["players"]
full_names = [f"{p['firstName']} {p['lastName']}" for p in players]
async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)



def run_discord_bot():
    with open(".env", "r") as file:
        TOKEN = file.readline()
    client = commands.Bot(command_prefix= "!", intents = discord.Intents.all())
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        try:
            synced = await client.tree.sync()
            print(f'Synced {len(synced)} command(s)')
        except Exception as e:
            print(e)
    @client.tree.command(name="ping", description="Check if the bot is online")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

    # @client.tree.command(name="allstars")
    # async def all_stars(interaction: discord.Interaction):
    #     #await interaction.response.send_message("Done")
    #     allstars = commands_json.allStars()
    #     embed = discord.Embed(title="Current All-Stars: ", description=allstars)
    #     await interaction.response.send_message(embeds=[embed])

    @client.tree.command(name="playerstats", description="Get the season stats for a given player")
    @app_commands.describe(player="Returns the season stats for a given player")
    async def player_stats(interaction: discord.Interaction, player: str):
        player = process.extract(player, full_names, limit=1)[0][0]
        player_stats = commands_json.playerStats(player)
        embed = discord.Embed(title=f"Player Stats for {player}: ", description=player_stats)
        await interaction.response.send_message(embeds=[embed])

    @client.tree.command(name="allstars", description="Get the current all stars")
    async def allstars(interaction: discord.Interaction):
        allStars = commands_json.allStars()
        embed = discord.Embed(title=f"Current All Stars: ", description=allStars)
        await interaction.response.send_message(embeds=[embed])
    @client.tree.command(name="player_strengths_weaknesses", description="Find players strengths and weaknesses")
    async def player_strengths_weakness(interaction: discord.Interaction, player: str):
        player = process.extract(player, full_names, limit=1)[0][0]
        playerInfo = commands_json.player_strength_and_weakness(player)
        embed = discord.Embed(title=f"Player Strengths and Weaknesses for {player}: ", description=playerInfo)
        await interaction.response.send_message(embeds=[embed])

    @client.tree.command(name="filterbystat", description="Find players with a stat above a certain threshold")
    @app_commands.describe(stat="Choose the stat you want to filter by", threshold="Choose the min threshold")
    @app_commands.choices(stat=[
        app_commands.Choice(name="Height", value="hgt"),
        app_commands.Choice(name="Strength", value="stre"),
        app_commands.Choice(name="Speed", value="spd"),
        app_commands.Choice(name="Jump", value="jmp"),
        app_commands.Choice(name="Inside Scoring", value="ins"),
        app_commands.Choice(name="Dunking", value="dnk"),
        app_commands.Choice(name="Free Throw", value="ft"),
        app_commands.Choice(name="Mid Range", value="fg"),
        app_commands.Choice(name="3PT", value="tp"),
        app_commands.Choice(name="Defensive IQ", value="diq"),
        app_commands.Choice(name="Offensive IQ", value="oiq"),
        app_commands.Choice(name="Dribbling", value="drb"),
        app_commands.Choice(name="Passing", value="pss"),
        app_commands.Choice(name="Rebounding", value="reb"),
    ])
    async def filter_by_stat(interaction: discord.Interaction, stat: discord.app_commands.Choice[str], threshold: int):
        statInfo = commands_json.filter_by_stat(stat.value, threshold)
        embed = discord.Embed(title=f"Players with {stat.name} above {threshold}: ", description=statInfo)
        await interaction.response.send_message(embeds=[embed])

    @client.tree.command(name="roster", description="Get the roster for a specific NBA team")
    async def roster(interaction: discord.Interaction, team_name: str):
        team_roster = commands_json.roster(team_name)
        embed = discord.Embed(title=f"2024 NBA Roster for the {team_name}: ", description=team_roster)
        await interaction.response.send_message(embeds=[embed])
    client.run(TOKEN)