import disnake
from disnake.ext import commands
import config
from database import insert, select

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
bot = commands.Bot(intents=intents)

@bot.event
async def on_member_join(member):
    role_id = select(member.guild.id)
    if role_id is None: return

    role = member.guild.get_role(role_id)
    await member.add_roles(role)

@bot.slash_command(name="auto_role", description="Установить авто роль")
@commands.has_permissions(administrator=True)
async def auto_role(ctx, role: disnake.Role = commands.Param(default=None)):
    if role is None:
        insert(ctx.guild.id, None)
        await ctx.send(f"Авто роль была убрана", ephemeral=True)
    else:
        insert(ctx.guild.id, role.id)
        await ctx.send(f"Авто роль <@&{role.id}> успешно установлена", ephemeral=True)

bot.run(config.TOKEN)