from django import forms  # inheriting from the forms class.

### WIDGET INPUT ###
class DateInput(forms.DateInput):
    input_type = 'date'

#### Form Class for the search bar ####
class FlightForm(forms.Form):
    origin = forms.CharField(max_length=20, label=' ', widget=forms.TextInput(attrs={'placeholder': 'From?'}))
    destination = forms.CharField(max_length=20, label=' ', widget=forms.TextInput(attrs={'placeholder': 'To?'}))
    startdate = forms.DateField(widget=DateInput)
    enddate = forms.DateField(widget=DateInput)

