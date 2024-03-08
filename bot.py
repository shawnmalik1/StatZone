import discord
from discord import app_commands
from discord.ext import commands
import responses
import JSON

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)



def run_discord_bot():
    TOKEN = "MTEzNjEzMDkwNzk0MjY5NDkxMg.G-gBZr.E2zUxgMw5TBMuowTFcgN6QdoOu2Mkn5OFDWNyk"
    client = commands.Bot(command_prefix= "!", intents = discord.Intents.all())
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        try:
            synced = await client.tree.sync()
            print(f'Synced {len(synced)} command(s)')
        except Exception as e:
            print(e)

    @client.tree.command(name="ping")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

    @client.tree.command(name="all_stars")
    async def all_stars(interaction: discord.Interaction):
        #await interaction.response.send_message("Done")
        allstars = JSON.allStars()
        embed = discord.Embed(title="Current All-Stars: ", description=allstars)
        await interaction.response.send_message(embeds=[embed])

    @client.tree.command(name="find_player")
    @app_commands.describe(player="Returns the season stats for a given player")
    async def find_player(interaction: discord.Interaction, player: str):
        player_stats = JSON.findPlayer(player)
        embed = discord.Embed(title=f"Player Stats for {player}: ", description=player_stats)
        await interaction.response.send_message(embeds=[embed])

    @client.tree.command(name="player_strengths_weaknesses")
    async def player_strengths_weakness(interaction: discord.Interaction, player: str):
        playerInfo = JSON.player_strength_and_weakness(player)
        embed = discord.Embed(title=f"Player Strength and Weakness's for {player}: ", description=playerInfo)
        await interaction.response.send_message(embeds=[embed])

    @client.tree.command(name="filter_by_stat")
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
        statInfo = JSON.filter_by_stat(stat.value, threshold)
        embed = discord.Embed(title=f"Players with {stat.name} above {threshold}: ", description=statInfo)
        await interaction.response.send_message(embeds=[embed])

    client.run(TOKEN)