import nextcord 
import re
import json

FILTER_DISCORD_LINK = r'(http[s]?:\/\/)?(www\.)?(dis)(.+[a-zA-Z0-9])\.(.+)'

def main():
    bot = nextcord.Client()
    url_filter = re.compile(FILTER_DISCORD_LINK)

    # dump json
    with open('config.json') as f:
        config = json.load(f)

    @bot.event
    async def on_ready():
        print('Bot is ready to filter scam discord link!')
    
    @bot.event
    async def on_message(ctx):
        try:
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

    bot.run(config['token'])
    

if __name__ == '__main__':
    main()
