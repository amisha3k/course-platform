from django import forms
from . import css,services
from .models import Email


class EmailForm(forms.Form):
    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "id":"email-login-input",
                "class": css.EMAIL_FIELD_CSS,
                "placeholder":"your email login"
            }
        )
    )
    # class  Meta:
    #     model=EmailVerifiactionEvent
    #     fields=['email']
    def clean_email(self):
        email=self.cleaned_data.get('email')
        verified=services.verify_email(email)
        if verified :
            raise forms.ValidationError("invalid email type.Please try again")
        return email