from  django import forms
from formexample.models import Collage


def validateName(name):
    pass


class CollageForm(forms.ModelForm):
    #collage_name = forms.CharField(
      #  min_length=8,
       # max_length=20
    #)

    class Meta:

        model = Collage
        #fields = '__all__'
        fields = ('collage_email', 'collage_city', 'collage_address')