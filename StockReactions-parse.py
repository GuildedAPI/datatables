import json
from urllib.parse import quote_plus

raw = json.load(open('StockReactions-raw.json'))

def parse():
    restructured = {}

    for category, emoji_list in raw.items():
        for emoji in emoji_list:
            emoji_id = emoji.pop('id')

            if emoji['category'] == 'Guilded':
                if emoji.get('png'):
                    emoji['png'] = 'https://www.guilded.gg' + emoji['png']
                if emoji.get('webp'):
                    emoji['webp'] = 'https://www.guilded.gg' + emoji['webp']
                if emoji.get('apng'):
                    emoji['apng'] = 'https://www.guilded.gg' + emoji['apng']

            elif not emoji.get('webp') or not emoji.get('png'):
                emoji['png'] = 'https://img.guildedcdn.com/asset/Emojis/{}.png'.format(quote_plus(emoji['name']))
                emoji['webp'] = 'https://img.guildedcdn.com/asset/Emojis/{}.webp'.format(quote_plus(emoji['name']))

            for tone, variation in emoji.get('skinVariations', {}).items():
                if not variation.get('webp') or not variation.get('png'):
                    variation['png'] = 'https://img.guildedcdn.com/asset/Emojis/{}.png'.format(quote_plus(variation['name']))
                    variation['webp'] = 'https://img.guildedcdn.com/asset/Emojis/{}.webp'.format(quote_plus(variation['name']))

            restructured[str(emoji_id)] = emoji

    json.dump(restructured, open('reactions.json', 'w+'))

parse()
print('-> reactions.json')
