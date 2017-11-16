from django import forms
from datetime import datetime


class QueryForm(forms.Form):
    CHOICES = (('keyword', 'AND',), ('keyword_or', 'OR',))
    # search_string = forms.CharField(label='Search string', max_length=100, required=False)
    search_string = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '検索キーワード'}),
                                    label='Search string', max_length=100, required=False)
    keyword_option = forms.ChoiceField(widget=forms.RadioSelect, label='Keyword options', choices=CHOICES,
                                       initial='keyword')
    count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-input'}), label='Max results', initial=20,
                               min_value=1, max_value=1000)
    start = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-select', 'type': 'date'}), label='Start date', initial=datetime.today().strftime('%Y-%m-%d'))
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '参加者ニックネーム'}),
                               label='Participant search', max_length=240, required=False)
    owner_nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '管理者ニックネーム'}),
                                     label='Owner search', max_length=240, required=False)
