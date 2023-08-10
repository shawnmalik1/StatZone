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


    @client.tree.command(name="trade")
    @app_commands.describe(player = "Enter in the player you'd like to find a trade for")
    async def trade(interaction: discord.Interaction, player: str):
        await interaction.response.send_message(f'Searching for trades for {player}')


    @client.tree.command(name="ping")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")

    @client.tree.command(name="team_weakness")
    @app_commands.describe(team = "Tells you the strengths and weakness's of your team")
    async def team_weakness(interaction: discord.Interaction, team: str):
        await interaction.response.send_message("Done")
        #await interaction.response.send_message(JSON.load_data())

    @client.tree.command(name="east_all_stars")
    async def east_all_stars(interaction: discord.Interaction):
        #await interaction.response.send_message("Done")
        east = JSON.eastAllStars()
        embed = discord.Embed(title="East All-Stars", description=east)
        await interaction.response.send_message(embeds=[embed])

    @client.tree.command(name="west_all_stars")
    async def west_all_stars(interaction: discord.Interaction):
        #await interaction.response.send_message("Done")
        west = JSON.westAllStars()
        embed = discord.Embed(title="West All-Stars", description=west)
        await interaction.response.send_message(embeds=[embed])


    client.run(TOKEN)