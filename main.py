import re
import json
import discord

from typing import Any

discord_filter_url = re.compile(r'(http[s]?:\/\/)?(www\.)?(dis)(.+[a-zA-Z0-9])\.(.+)')

class FilterBot(discord.Client):
    def __init__(self, config_path: str):
        self.config = self.load_config(config_path)
        super().__init__()

    def load_config(self, path: str) -> Any:

        # dump json config
        with open(path) as f:
            return json.load(f)

    def run(self) -> None:
        super().run(self.config['token'])

    async def on_ready(self):
        print('Bot is ready to filter scam discord link!')

    def is_bad_discord_url(content: str) -> bool:
    # Search using regex
    url_match = re.search("(?P<url>https?://[^\s]+)", content)

    if not url_match:
        return False
    
    # Extract url first, before doing anything
    extracted_url = url_match.group('url')

    if not discord_filter_url.match(extracted_url):
        return False

    for links in bot.config['links']:
        if links == extracted_url:
            return False
    
    return True


bot = FilterBot('config.json')

@bot.event
async def on_message(ctx) -> None:

    # Do nothing when the content is null
    if not ctx.content:
        return

    # Check if there is bad url or not
    if is_bad_discord_url(ctx.content):
        await ctx.delete()

if __name__ == '__main__':
    bot.run()
