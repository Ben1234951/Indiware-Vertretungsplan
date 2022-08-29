import plan 
import discord
from discord.ext import commands, tasks
from datetime import datetime

def Discord():
    Discord_client = commands.Bot(command_prefix='!')

    @Discord_client.event
    async def on_ready():
        loop.start()
        print(f"{Discord_client.user} has connected")

    @Discord_client.command(aliases=["plan", "vertretungsplan", "Vertretungsplan"], pass_context=True)
    async def Plan(ctx, Klasse : discord.Member=None):
        if Klasse is None:
            with open(f"Klassen\\{ctx.author.id}", "r") as f:
                Klasse = f.read()
        data = plan.get_data(Klasse)
        embed=discord.Embed(title="Dein Vertretungsplan ist: ", description=f"{data}", color=0x00ff00)
        await ctx.send(embed=embed)

    @Discord_client.command()
    async def add_class(ctx, Klasse : str):
        with open(f"Klassen\\{ctx.author.id}", "w") as f:
            f.write(Klasse)
        embed = discord.Embed(title=f"Du wurdest zur Klasse {Klasse} hinzugefügt", color=0x00ff00)
        await ctx.send(embed=embed)

    @tasks.loop(minutes=1)
    async def loop():
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if "18:00" == current_time:
            channel = Discord_client.get_channel("Channel ID where it should be posted")
            data = plan.get_data("youre class")
            embed = discord.Embed(title="Vertretungsplan der Klasse[youre class]", description=f"{data}", color=0x00ff00)
            await channel.send(embed=embed)
        elif "12:50" == current_time:
            channel = Discord_client.get_channel("Channel ID where it should be posted")
            data = plan.get_data("youre class")
            embed = discord.Embed(title="Vertretungsplan der Klasse[youre class]", description=f"{data}", color=0x00ff00)
            await channel.send(embed=embed)
        

    Discord_client.run("Youre Token Here")

if __name__ == "__main__":
    Discord()
