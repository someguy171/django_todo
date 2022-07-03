from django import forms

from .models import Homework, Lesson

class HomeworkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super (HomeworkForm, self).__init__(*args,**kwargs)
        self.fields['lesson'].queryset = Lesson.objects.all().exclude(name="placeholder")
        
    class Meta:
        model = Homework
        exclude = ['pub_date']
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(),
            'reminder': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        
        help_texts = {
            'attachment': 'optional!',
            'link': 'optional!',
            'reminder': 'optional!',
        }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"

class FetchForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)