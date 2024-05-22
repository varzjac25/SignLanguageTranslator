# Jackson Varzali
# ForeignLanguageTranslation translates written language from various
# languages into other languages

# imports
from googletrans import Translator, constants
from pprint import pprint

# initialize variables and objects
translator = Translator()

# langDict translates language names into the required shorthand for Google translation
langDict = {
    "Spanish": "es",
    "Chinese":"zh-CN",
    "Italian":"it"
    # add more languages
}

# translateForeign is called from main class
def translateForeign(input, outLanguage):

    # translate to english
    if outLanguage.lower() == "english":

        # translator translates into english by default
        translation = translator.translate(input)

        # return translated text
        return translation.text

    # translating into languages other than english
    else:

        # check if language entered is a valid language
        if langDict.__contains__(outLanguage.lower()):

            # convert language title into shorthand

            # translate language
            translation = translator.translate(input, dest = "ar")

            # return translation
            return translation.text

        # return error message
        else:
            return "Error: language entered is invalid"