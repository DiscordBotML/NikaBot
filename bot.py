from discord.ext.commands import Bot

from discord_components import DiscordComponents, Button, Select, SelectOption



bot = Bot(command_prefix = "w!")





@bot.event

async def on_ready():

    DiscordComponents(bot)

    print(f"Logged in as {bot.user}!")





@bot.command()

async def button(ctx):

    await ctx.send(

        "Hello, World!",

        components = [

            Button(label = "WOW button!")

        ]

    )



    interaction = await bot.wait_for("button_click", check = lambda i: i.component.label.startswith("WOW"))

    await interaction.respond(content = "Button clicked!")





@bot.command()

async def select(ctx):

    await ctx.send(

        "Hello, World!",

        components = [

            Select(placeholder="select something!", options=[SelectOption(label="a", value="A"), SelectOption(label="b", value="B")])

        ]

    )



    interaction = await bot.wait_for("select_option", check = lambda i: i.component[0].value == "A")

    await interaction.respond(content = f"{interaction.component[0].label} selected!")





bot.run("ODYzMDY5MjMyMzM2ODYzMjgy.YOhh3A.JLdtaIoqAje4ubHwJVBwXe7LP4U")