from modeltranslation.translator import translator, TranslationOptions
from stadium.models import StadiumModel


class StadiumTranslation(TranslationOptions):
    fields = ('stadium_name','stadium_bio','stadium_rules')



translator.register(StadiumModel, StadiumTranslation)

