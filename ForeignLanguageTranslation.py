# Jackson Varzali
# ForeignLanguageTranslation translates written language from various
# languages into other languages

# imports
from googletrans import Translator, constants
from pprint import pprint

# initialize variables and objects
translator = Translator()

# translateForeign is called from main class
def translateForeign(input, outLanguage):

    # translate to english
    if outLanguage.lower() == "english":

        translation = translator.translate(input)
        