from django import forms

class NameForm(forms.Form):
    input_prompt = forms.CharField(label='Input Prompt', max_length=1000)