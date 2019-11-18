from django import forms

textarea = forms.Textarea(attrs = {
            'class':'form-control',
            'id':'summarization_area',
            'width':'100%'})
class TextSummarization(forms.Form):
    text = forms.CharField(widget=textarea,label='')
