"""
Description:
This Cog contains all the events and commands used for fun and hat-tricks.
"""
# IMPORTS
#import [Module/Package]
from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.


class FunCog(commands.Cog):
    """Cog for fun/wacky commands & events."""
    def __init__(self, bot):
        """Initializes the cog, passing in a bot to associate itself with."""
        self.bot = bot
    
    @commands.command(name="ping", aliases=["Ping", "pingpong", "Pingpong", "PingPong", "ping_pong","Ping_pong", "Ping_Pong"])
    async def ping(self, ctx):
    	"""Play ping-pong with the bot."""
    	await ctx.send(":ping_pong:Pong!")


def setup(bot):
    """Adds The Cog To The Client."""
    bot.add_cog(FunCog(bot))
