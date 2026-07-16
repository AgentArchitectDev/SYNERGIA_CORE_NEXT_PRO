"""
=========================================================
SYNERGIA OS

Language Manager V1.0

Global Interface Language System

Enterprise Cognitive Operating System AI
=========================================================
"""


import json

import os



class LanguageManager:


    def __init__(self):


        self.current_language = "es"


        self.languages = {

            "es":"Español",

            "en":"English",

            "pt":"Português",

            "de":"Deutsch",

            "zh":"中文",

            "ja":"日本語"

        }



    def set_language(
        self,
        language
    ):


        if language in self.languages:

            self.current_language = language

            return True


        return False



    def get_language(self):

        return self.current_language



    def available_languages(self):

        return self.languages



    def translate(
        self,
        key
    ):


        translations = {


            "dashboard":

            {

                "es":"Panel Principal",

                "en":"Dashboard"

            },


            "runtime":

            {

                "es":"Tiempo de Ejecución",

                "en":"Runtime"

            }


        }



        if key in translations:


            return translations[key].get(
                self.current_language,
                key
            )


        return key
