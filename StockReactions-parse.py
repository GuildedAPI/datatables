import json
from urllib.parse import quote_plus

raw = json.load(open('StockReactions-raw.json'))

def parse():
    restructured = {}
    restructured_stripped = {}

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
                variation.pop('category', None)
                variation.pop('order', None)
                if not variation.get('webp') or not variation.get('png'):
                    variation['png'] = 'https://img.guildedcdn.com/asset/Emojis/{}.png'.format(quote_plus(variation['name']))
                    variation['webp'] = 'https://img.guildedcdn.com/asset/Emojis/{}.webp'.format(quote_plus(variation['name']))

            restructured[str(emoji_id)] = emoji.copy()

            if 'apng' in emoji:
                emoji['isAnimated'] = True

            emoji.pop('png', None)
            emoji.pop('apng', None)
            emoji.pop('webp', None)
            for variation in emoji.get('skinVariations', {}).values():
                variation.pop('png', None)
                variation.pop('apng', None)
                variation.pop('webp', None)

            restructured_stripped[str(emoji_id)] = emoji

    json.dump(restructured, open('reactions.json', 'w+'))
    json.dump(restructured_stripped, open('reactions-stripped.json', 'w+'))

parse()
print('Full     -> reactions.json')
print('Stripped -> reactions-stripped.json')
