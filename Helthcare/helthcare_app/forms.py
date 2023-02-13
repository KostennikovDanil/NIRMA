from django import forms


class FirstState(forms.Form):
    yes_or_no = forms.BooleanField(label='Есть ли противопоказания к ТТ?', required=False)
    ptv = forms.FloatField(label='Введите претестовую вероятность',required=False, max_value=100, min_value=0)

class SecondState(forms.Form):
    res = forms.IntegerField(label='Результаты ТТ первого дня', required=False, max_value=2, min_value=0)

class ThirdState(forms.Form):
    yes_or_no = forms.BooleanField(label='Воспроизводимы ли результаты?', required=False)

class FourthState (forms.Form):
    yes_or_no = forms.BooleanField(label='Положительна ли проба?', required=False)