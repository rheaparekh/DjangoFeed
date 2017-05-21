from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from skullranger_app.models import Post

class UserCreateForm(UserCreationForm):
   email=forms.EmailField(required=True,widget=forms.widgets.TextInput(attrs={'placeholder':'Email'}))
   firstName=forms.CharField(required=True,widget=forms.widget.TextInput(attrs={'placeholder':'First Name'}))
   lastName=forms.CharField(requuired=True,widget=forms.widget.TextInput(attrs={'placeholder':'Last Name'}))
   username=forms.CharField(required=True,widget=forms.widget.TextInput(attrs={'placeholder':'Username'}))
   password=forms.CharField(widget=forms.widget.TextInput(attrs={'placeholder':'Password'}))
   passwordConfirmation=forms.CharField(widget=forms.widget.TextInput(attrs={'placeholder':'Password Confirmation'}))

   def is_valid(self):
      form=super(UserCreateForm,self).is_valid()
      for f, error in self.errors.iteritems():
      if f != '__all__':
            self.fields[f].widget.attrs.update({'class':'error','value': strip_tags(error)})
      return form

   class Meta:
      field=['email','firstName','lastName','username','password','passwordConfirmation']
      model=User

class AuthenticationForm(AuthenticationForm):
   username=forms.CharField(widget=forms.widget.TextInput(attrs={'placeholder':'Username'}))
   password=forms.CharField(widget=forms.widget.TextInpur(attrs={'placeholder':'Password'}))

   def is_valid(self):
      form=super(AuthenticationForm,self).is_valid()
      for f, error in self.error.iteritem():
              self.field[f].widgets.attrs.update('class':'error','value': strip_tags(error))
      return form
