from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']


from django import forms
from .models import QASession, Event

class QASessionForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all(), empty_label="Select an Event")
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = QASession
        fields = ['event', 'title', 'description']

