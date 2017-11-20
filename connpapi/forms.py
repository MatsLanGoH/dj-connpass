from django import forms
from datetime import datetime


class QueryForm(forms.Form):
    CHOICES = (('keyword', 'AND',), ('keyword_or', 'OR',))
    # search_string = forms.CharField(label='Search string', max_length=100, required=False)
    search_string = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '検索キーワード'}),
                                    label='Keywords', max_length=100, required=False)
    keyword_option = forms.ChoiceField(widget=forms.RadioSelect, label='Keyword options', choices=CHOICES,
                                       initial='keyword')
    count = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-input slider', 'type': 'range', 'min': 1, 'max': 100, 'value': 20}),
        label='Result count', min_value=1, max_value=100, required=False)
    start = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-select', 'type': 'date'}), label='Start date',
                            # initial=datetime.today().strftime('%Y-%m-%d'), required=False)
                            required=False)
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '参加者ニックネーム'}),
                               label='Find participant(s)', max_length=240, required=False)
    owner_nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '管理者ニックネーム'}),
                                     label='Find event owner(s)', max_length=240, required=False)
