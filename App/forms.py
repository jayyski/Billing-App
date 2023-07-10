from django import forms
from .models import Bill
import datetime

class BillForm(forms.ModelForm):
    bill_name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Please enter a valid bill name'})
    date = forms.DateField(required=True)
    amount = forms.DecimalField(max_digits=8, decimal_places=2, required=True, error_messages={'required': 'Please enter a valid amount'})
    
    def clean_date(self):
        date = self.cleaned_data['date']

        if date < datetime.date.today():
            raise forms.ValidationError("Date cannot be in the past")
        return date
    
    class Meta:
        model = Bill
        fields = ['date', 'bill_name', 'amount']