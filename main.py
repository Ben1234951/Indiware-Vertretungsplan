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
            channel = Discord_client.get_channel(1013376915949760562)
            data_9_5 = plan.get_data(9.5)
            data_8_5 = plan.get_data(8.5)
            embed2 = discord.Embed(title="Vertretungsplan der Klasse 8.5", description=f"{data_8_5}", color=0x00ff00)
            embed1 = discord.Embed(title="Vertretungsplan der Klasse 9.5", description=f"{data_9_5}", color=0x00ff00)
            await channel.send(embed=embed2)
            await channel.send(embed=embed1)
        elif "12:50" == current_time:
            channel = Discord_client.get_channel(1013376915949760562)
            data_9_5 = plan.get_data(9.5)
            data_8_5 = plan.get_data(8.5)
            embed2 = discord.Embed(title="Vertretungsplan der Klasse 8.5", description=f"{data_8_5}", color=0x00ff00)
            embed1 = discord.Embed(title="Vertretungsplan der Klasse 9.5", description=f"{data_9_5}", color=0x00ff00)
            await channel.send(embed=embed2)
            await channel.send(embed=embed1)
        

    Discord_client.run("MTAxMzM3NTc3NTYxNDk4MDEyNw.GE5a5E.41WnEoYeUscEr-SSO4NqRa9NHKGRCYYe5IH2Zs")

if __name__ == "__main__":
    Discord()