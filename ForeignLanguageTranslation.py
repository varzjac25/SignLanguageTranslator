# ForeignLanguageTranslation translates written language from various
# languages into other languages

# imports
from googletrans import Translator, constants
from pprint import pprint

# initialize variables and objects
translator = Translator()

# langDict translates language names into the required shorthand for Google translation
langDict = {
     'af': 'afrikaans',
     'am': 'amharic',
     'ar': 'arabic',
     'az': 'azerbaijani',
     'be': 'belarusian',
     'bg': 'bulgarian',
     'bn': 'bengali',
     'bs': 'bosnian',
     'ca': 'catalan',
     'ceb': 'cebuano',
     'co': 'corsican',
     'cs': 'czech',
     'cy': 'welsh',
     'da': 'danish',
     'de': 'german',
     'el': 'greek',
     'en': 'english',
     'eo': 'esperanto',
     'es': 'spanish',
     'et': 'estonian',
     'eu': 'basque',
     'fa': 'persian',
     'fi': 'finnish',
     'fr': 'french',
     'fy': 'frisian',
     'ga': 'irish',
     'gd': 'scots gaelic',
     'gl': 'galician',
     'gu': 'gujarati',
     'ha': 'hausa',
     'haw': 'hawaiian',
     'he': 'hebrew',
     'hi': 'hindi',
     'hmn': 'hmong',
     'hr': 'croatian',
     'ht': 'haitian creole',
     'hu': 'hungarian',
     'hy': 'armenian',
     'id': 'indonesian',
     'ig': 'igbo',
     'is': 'icelandic',
     'it': 'italian',
     'iw': 'hebrew',
     'ja': 'japanese',
     'jw': 'javanese',
     'ka': 'georgian',
     'kk': 'kazakh',
     'km': 'khmer',
     'kn': 'kannada',
     'ko': 'korean',
     'ku': 'kurdish (kurmanji)',
     'ky': 'kyrgyz',
     'la': 'latin',
     'lb': 'luxembourgish',
     'lo': 'lao',
     'lt': 'lithuanian',
     'lv': 'latvian',
     'mg': 'malagasy',
     'mi': 'maori',
     'mk': 'macedonian',
     'ml': 'malayalam',
     'mn': 'mongolian',
     'mr': 'marathi',
     'ms': 'malay',
     'mt': 'maltese',
     'my': 'myanmar (burmese)',
     'ne': 'nepali',
     'nl': 'dutch',
     'no': 'norwegian',
     'ny': 'chichewa',
     'or': 'odia',
     'pa': 'punjabi',
     'pl': 'polish',
     'ps': 'pashto',
     'pt': 'portuguese',
     'ro': 'romanian',
     'ru': 'russian',
     'sd': 'sindhi',
     'si': 'sinhala',
     'sk': 'slovak',
     'sl': 'slovenian',
     'sm': 'samoan',
     'sn': 'shona',
     'so': 'somali',
     'sq': 'albanian',
     'sr': 'serbian',
     'st': 'sesotho',
     'su': 'sundanese',
     'sv': 'swedish',
     'sw': 'swahili',
     'ta': 'tamil',
     'te': 'telugu',
     'tg': 'tajik',
     'th': 'thai',
     'tl': 'filipino',
     'tr': 'turkish',
     'ug': 'uyghur',
     'uk': 'ukrainian',
     'ur': 'urdu',
     'uz': 'uzbek',
     'vi': 'vietnamese',
     'xh': 'xhosa',
     'yi': 'yiddish',
     'yo': 'yoruba',
     'zh-cn': 'chinese (simplified)',
     'zh-tw': 'chinese (traditional)',
     'zu': 'zulu'
}

# translateForeign is called from main class
def translateForeign(input, outLanguage) -> str:

    # translate to english
    if outLanguage.lower() == "english":

        # translator translates into english by default
        translation = translator.translate(input)

        # return translated text
        return translation.text

    # translating into languages other than english
    else:

        # swap dictionary keys and values
        swappedDict = dict((v, k) for k, v in langDict.items())

        # check if language entered is a valid language
        if swappedDict.__contains__(outLanguage.lower()):

            # convert language title into shorthand
            for key in swappedDict.keys():
                outLanguage = outLanguage.lower().replace(key, swappedDict[key])

            # translate language
            translation = translator.translate(input, dest = outLanguage    )

            # return translation
            return translation.text

        # return error message
        else:
            return "Error: language entered is invalid"