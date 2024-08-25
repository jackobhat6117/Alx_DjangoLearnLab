from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'class': 'form-control'
        }),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        }),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your message',
            'class': 'form-control'
        }),
        required=True
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name should only contain letters.")
        return name
