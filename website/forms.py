from django.forms import ModelForm

from .models import Subscriber, Message


class SubscriberModelForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email', 'message']


class MessageModelForm(ModelForm):
    class Meta:
        model = Message
        fields = ['email']
