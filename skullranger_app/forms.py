from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from skullranger_app.models import Post

class UserCreateForm(UserCreationForm):
   email=forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Email'}))
   firstName=forms.CharField(required=True,min_length=3,widget=forms.widgets.TextInput(attrs={'placeholder':'First Name'}))
   lastName=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name'}))
   username=forms.CharField(min_length=6, widget=forms.widgets.TextInput(attrs={'placeholder':'Username'}))
   password1=forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password'}))
   password2=forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password Confirmation'}))

   def is_valid(self):
      form=super(UserCreateForm,self).is_valid()
      for f, error in self.errors.iteritems():
        if f != '__all__':
            self.fields[f].widget.attrs.update({'class':'error','value': strip_tags(error)})
      return form

   class Meta:
      fields=['email','firstName','lastName','username','password1','password2']
      model=User

class AuthenticateForm(AuthenticationForm):
   username=forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder':'Username'}))
   password=forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder':'Password'}))

   def is_valid(self):
      form=super(AuthenticateForm,self).is_valid()
      for f, error in self.errors.iteritems():
        if f != '__all__':
              self.fields[f].widget.attrs.update({'class':'error','value': strip_tags(error)})
      return form
