from django import forms
from .models import Obj1Ai,Obj2Ai


class Obj1AiForm(forms.ModelForm):
    class Meta:
        model = Obj1Ai
        fields = ['id']
        widgets = {
            'id': forms.IntegerField(attrs={ 'class': 'btn  btn-outline-info' }),
      }
