
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    service_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Appointment
        fields = ['name', 'email', 'service', 'service_date', 'message']



from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']




from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'body']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-input'}),
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}),
        }


