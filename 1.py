import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?")

async def tank(ctx, rang, vid, strana, sposop_poluchenia):
    if rang == 1:
        if strana == 1:
            await ctx.send("https://blitzhangar.com/ru/tank/m2-light")
        elif strana == 2:
            await ctx.send("https://blitzhangar.com/ru/tank/t-26")
        elif strana == 3:
            await ctx.send("https://blitzhangar.com/ru/tank/pz-ii")
        elif strana == 4:
            await ctx.send("https://blitzhangar.com/ru/tank/pz-ii")
        elif strana == 5:
            await ctx.send("https://blitzhangar.com/ru/tank/ha-go")
        elif strana == 6:
            await ctx.send("https://blitzhangar.com/ru/tank/vae-type-b")
        elif strana == 7:
            await ctx.send("https://blitzhangar.com/ru/tank/r35")
        elif strana == 8:
            await ctx.send("https://blitzhangar.com/ru/tank/vickers-mk-f")
        else:
            await ctx.send("Танк не найден. Попробуйте проверить параметры")
    elif rang == 2:
        if sposop_poluchenia == 1:
            if strana == 1:
                await ctx.send("https://blitzhangar.com/ru/tank/m3-stuart")
            elif strana == 2:
                await ctx.send("https://blitzhangar.com/ru/tank/bt-2")
            elif strana == 3:
                await ctx.send("https://blitzhangar.com/ru/tank/pz-35-t")
            elif strana == 4:
                await ctx.send("https://blitzhangar.com/ru/tank/cruiser-iii")
            elif strana == 5:
               await ctx.send("https://blitzhangar.com/ru/tank/chi-ni")
            elif strana == 6:
                await ctx.send("https://blitzhangar.com/ru/tank/lt-vz-38")
            elif strana == 7:
                await ctx.send("https://blitzhangar.com/ru/tank/amx-38")
            elif strana == 8:
                await ctx.send("https://blitzhangar.com/ru/tank/10tp")
            else:
                await ctx.send("Танк не найден. Попробуйте проверить параметры.")
        elif sposop_poluchenia == 3:
            if strana == 1:
                if vid == 3:
                    await ctx.send("https://blitzhangar.com/ru/tank/t2-light")
                    await ctx.send("https://blitzhangar.com/ru/tank/t1e6")
                    await ctx.send("https://blitzhangar.com/ru/tank/t7-car")
                elif vid == 2:
                    await ctx.send("https://blitzhangar.com/ru/tank/t2-medium")
                elif vid == 4:
                    await ctx.send("https://blitzhangar.com/ru/tank/t18")
                else:
                    await ctx.send("Танк не найден. Попробуйте проверить параметры.")
            elif strana == 2:
                if vid == 3:
                    await ctx.send("https://blitzhangar.com/ru/tank/tetrarch")
                elif vid == 4:
                    await  ctx.send("https://blitzhangar.com/ru/tank/at-1")
                else:
                    await ctx.send("Танк не найден. Попробуйте проверить параметры.")
            elif strana == 3:
                if vid == 3:
                    await ctx.send("https://blitzhangar.com/ru/tank/pz-38h")
                elif vid == 4:
                    await  ctx.send("https://blitzhangar.com/ru/tank/pzjag-i")
                else:
                    await ctx.send("Танк не найден. Попробуйте проверить параметры.")
            elif strana == 4:
                if vid == 3:
                    await ctx.send("https://blitzhangar.com/ru/tank/cruiser-i")
                    await ctx.send("https://blitzhangar.com/ru/tank/light-vic")
                elif vid == 2:
                    await ctx.send("https://blitzhangar.com/ru/tank/medium-ii")
                elif vid == 4:
                    await ctx.send("https://blitzhangar.com/ru/tank/uc-2-pdr")
                else:
                    await ctx.send("Танк не найден. Попробуйте проверить параметры.")
            elif strana == 7:
                if vid == 3:
                    await ctx.send("https://blitzhangar.com/ru/tank/d1")
                elif vid == 4:
                    await  ctx.send("https://blitzhangar.com/ru/tank/ft-ac")
                else:
                    await ctx.send("Танк не найден. Попробуйте проверить параметры.")
            else:
                await ctx.send("Танк не найден. Попробуйте проверить параметры.")
    else:
        await ctx.send("Танк не найден. Попробуйте проверить параметры.")

bot.run("ODQyOTk3MDE1NzM4MDU2NzQ0.YJ9cJg.6tjaj9mSvgGVpGGj2dHPpzUXZY4")