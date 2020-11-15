from discord.ext import commands
import discord
import requests

class Reddit(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="subscribe",aliases=['sub'],help="Subscribe to subreddit.")
    async def subscribe(self,ctx, name_of_subreddit: str = None, channel: discord.TextChannel = None):
        if not name_of_subreddit:
            await ctx.send("You need to write the name of subreddit. See &help subscribe.")
            return
        elif not channel:
            await ctx.send("You need to mention a channel to send posts. See &help subscribe.")
            return
        else:
            await channel.send("Mire e ke shkrujt po pertoj ta regjistroj.")

    @commands.command(name="reddit",aliases=['r'],help="Get the hottest post in a subreddit.")
    async def reddit(self,ctx,name_of_subreddit: str=None):
        if not name_of_subreddit:
            await ctx.send("You need to write the name of subreddit. See &help reddit.")
            return
        else:
            r = requests.get(f"https://www.reddit.com/r/{name_of_subreddit}/hot.json?sort=hot&limit=4",headers = {'User-agent': 'Haberet'})
            data = r.json()
            if 'error' in data:
                await ctx.send(f"Error {data['error']} occured.")
                return
            for obj in data['data']['children']:
                if obj['data']['pinned'] == False:
                    embed = discord.Embed(title=obj['data']['title'])
                    if 'thumbnail' in obj['data']:
                        if obj['data']['over_18'] == True and ctx.message.channel.nsfw == False:
                            await ctx.send("Jo nsfw se nuk do Dela.")
                            return
                        if obj['data']['url'].endswith(".jpg") or obj['data']['url'].endswith(".png") or obj['data']['url'].endswith(".gif"):
                            embed.set_image(url=obj['data']['url'])
                            await ctx.send(embed=embed)
                            return
        response = "Ik o rrk gjej shoket <:lod:773579563182981120>"
        await ctx.send(response)


def setup(bot):
    bot.add_cog(Reddit(bot))