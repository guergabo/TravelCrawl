from django import forms  # inheriting from the forms class.


#### Form Class for the search bar ####
class FlightForm(forms.Form):
    origin = forms.CharField(max_length=250, label=' ', widget=forms.TextInput(attrs={'placeholder': 'From?'}))
    destination = forms.CharField(max_length=250, label=' ', widget=forms.TextInput(attrs={'placeholder': 'To?'}))
    startdate = forms.CharField(max_length=250, label=' ', widget=forms.TextInput(attrs={'placeholder': 'Departure Date'}))
    enddate = forms.CharField(max_length=250, label=' ', widget=forms.TextInput(attrs={'placeholder': 'Return Date'}))

