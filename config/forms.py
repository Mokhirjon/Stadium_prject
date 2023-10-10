from django import forms
from stadium.models import StadiumModel

class Stadiumforms(forms.ModelForm):
    stadium_name_uz = forms.CharField()
    stadium_name_ru = forms.CharField(required=False)
    stadium_name_en = forms.CharField(required=False)

    stadium_bio_uz = forms.CharField()
    stadium_bio_ru = forms.CharField(required=False)
    stadium_bio_en = forms.CharField(required=False)

    stadium_rules_uz = forms.CharField()
    stadium_rules_ru = forms.CharField(required=False)
    stadium_rules_en = forms.CharField(required=False)

    class Meta:
        model = StadiumModel
        exclude = ('stadium_name','stadium_bio','stadium_rules')