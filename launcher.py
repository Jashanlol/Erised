from discord.ext import commands

import os
import aiohttp
import datetime
import traceback


def _prefix(bot, msg):
    user_id = bot.user.id
    base = [f'<@!{user_id}> ', f'<@{user_id}> ']
    default = ['eris ']
    if msg.guild is None:
        base.extend(default)
    else:
        base.extend(bot.prefixes.get(str(msg.guild.id), default))
    return base


initial_extensions = []
for i in os.listdir('cogs'):
    if '.py' in i:
        i = i.split('.py', 1)[0]
        initial_extensions.append(f'cogs.{i}')


class BotClient(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(max_messages=10000, description="Erised", command_prefix=_prefix)

        self.prefixes = {}

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
                print(f'Loaded extension {extension}')
            except Exception:
                print(f'Failed to load extension {extension}')
                traceback.print_exc()

    def timenow(self, utc=True, sqlTs=False):
        ts = datetime.datetime.now()
        if utc:
            ts = datetime.datetime.utcnow()
        if sqlTs:
            f = '%Y-%m-%d %H:%M:%S'
            ts = ts.strftime(f)
        return (ts)

    def uptime(self):
        delta = bot.timenow(utc=True) - bot.uptime_
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        values = [f'{days}d', f'{hours}h', f'{minutes}m', f'{seconds}s']
        return ', '.join(v for v in values if str(v)[0] != '0')

    async def on_ready(self):
        if not hasattr(self, 'uptime_'):
            self.uptime_ = datetime.datetime.utcnow()
        print(f'Ready: {self.user} (ID: {self.user.id})')

    async def on_resumed(self):
        print('resumed...')

    async def on_message(self, message):
        if message.author.bot:
            return

        if self.is_owner(message.author.id):
            pass

        await self.process_commands(message)

    async def close(self):
        await super().close()

    def is_owner(self, id):
        return True if id in [190298524699721729, 294894701708967936, 288457249389805569] else False

    def owners(self):
        return [190298524699721729, 288457249389805569, 294894701708967936]

    def run(self):
        super().run("NTYxNjY0Nzg2NzQ0NzM3ODMy.XJ_hHw.f9YqltPE2dWbNZJjAvvuP0R66fo", reconnect=True)


bot = BotClient()
bot.session = aiohttp.ClientSession(loop=bot.loop)
bot.run()
