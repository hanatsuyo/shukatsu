from django import forms
import bootstrap_datepicker_plus as datetimepicker

from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'mypage_id', 'mypage_pwd', 'mypage_url','progress','next_date','next_time')
        widgets = {
            'next_date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),

            'next_time': datetimepicker.TimePickerInput(
                format='%H:%M:%S',
                options={
                    'locale': 'ja',
                }

            ),
        }