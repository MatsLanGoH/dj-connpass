from django import forms
from datetime import datetime


class QueryForm(forms.Form):
    CHOICES = (('keyword', 'AND',), ('keyword_or', 'OR',))
    search_string = forms.CharField(label='Search string', max_length=100, required=False)
    keyword_option = forms.ChoiceField(widget=forms.RadioSelect, label='Keyword options', choices=CHOICES, initial='keyword')
    count = forms.IntegerField(label='Max results', initial=20, min_value=1, max_value=1000, required=False)
    # current_date = datetime.today().strftime('%Y%m%d')
    start = forms.DateField(widget=forms.SelectDateWidget(), label='Start date', initial=datetime.today())
    nickname = forms.CharField(label='Participant search', max_length=240, required=False)
    owner_nickname = forms.CharField(label='Owner search', max_length=240, required=False)


