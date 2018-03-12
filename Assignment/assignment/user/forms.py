from django import forms
from user.models import Users,Friend

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('user_name','First_name','last_name','place_of_birth','current_address','favourite_colour','personal_interest', 'my_friend')

class FriendFrom(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'
