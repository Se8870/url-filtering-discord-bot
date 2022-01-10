import nextcord 
import re
import json

# 2nd filtering url
FILTER_DISCORD_LINK = r'(http[s]?:\/\/)?(www\.)?(dis)(.+[a-zA-Z0-9])\.(.+)'

bot = nextcord.Client()
url_filter = re.compile(FILTER_DISCORD_LINK)

# dump json config
with open('config.json') as f:
    config = json.load(f)

@bot.event
async def on_ready():
    print('Bot is ready to filter scam discord link!')

@bot.event
async def on_message(ctx):
    try:
        # extract the url first, before doing any check
        extracted_url = re.search("(?P<url>https?://[^\s]+)", ctx.content).group("url")

        if extracted_url != None:
            print(f'found the url {extracted_url}')
                        
            if url_filter.match(extracted_url):
                print(f'found regex criteria of {extracted_url}')

            for links in config['links']:
                if links == extracted_url:
                    return

            print(f'Not in the list of good url, deleting it')
            await ctx.delete()
    except:
        pass

if __name__ == '__main__':
    bot.run(config['token'])
