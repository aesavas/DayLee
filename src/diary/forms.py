from django.forms import ModelForm
from .models import Diary

class DiaryCreationForm(ModelForm):
    class Meta:
        model = Diary
        fields = ['mood', 'diary']

    def __init__(self, *args, **kwargs):
        super(DiaryCreationForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})