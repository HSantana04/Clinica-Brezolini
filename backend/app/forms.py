from django.forms import ModelForm, DateInput
from app.models import EventMember, Event
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "start_time", "end_time", "paciente"]
        # datetime-local is a HTML5 input type
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Insira o titulo da consulta"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Insira a descrição da consulta",
                }
            ),
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "paciente": forms.Select(
                attrs={"class": "form-control"}
            )
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]
