from django import forms
from django.core import validators

def starts_with_p(value):
    if value[0].lower()!='p':
        raise forms.ValidationError('Name should be starts with p')

def gmail_verification(value):
    if value[len(value)-9:]!='gmail.com':
        raise forms.ValidationError('Must be gmail')

class FeedBackForm(forms.Form):
    name=forms.CharField(validators=[starts_with_p])
    rollno=forms.IntegerField()
    email=forms.EmailField(validators=[gmail_verification])
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    #bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

#ExplicitValidation
    '''def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('The length of name field should be >=4')
        return inputname

    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print('Validating rollno')
        return inputrollno

    def clean_email(self):
       inputemail=self.cleaned_data['email']
       print('Validating email')
       return inputemail

    def clean_feedback(self):
         inputfeedback=self.cleaned_data['feedback']
         print('Validating feedback')
         return inputfeedback'''
    'def clean(self):
        print('Total Form Validation')
        cleaned_data=super().clean()
        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']
        if inputpwd!=inputrpwd:
            raise forms.ValidationError('passwords not matched')
    '''def clean(self):
        print('Total Form Validation...')
        cleaned_data=super().clean()
        bot_handler_value=cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Thanks Bot'''!!')'''
