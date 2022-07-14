from django import forms
from .models import *


class SearchForm(forms.Form):
    client_name = forms.ModelChoiceField(required=False, queryset=Clients.objects.all(),
                                         empty_label="ALL", to_field_name="id")
    equipment_name = forms.ModelChoiceField(required=False, queryset=Equipment.objects.all(),
                                            empty_label="ALL", to_field_name="name")
    modes_name = forms.ModelChoiceField(required=False, queryset=Modes.objects.all(),
                                        empty_label="ALL", to_field_name="name")

    # duration = forms.DurationField(required=False, label="Minutes:", d)

    # start_date = forms.DateField(required=False, label="Start date")
    # end_date = forms.DateField(required=False, label="End date")

    # start_time = forms.TimeField(required=False, input_formats="%H:%M", label="Hour:Minutes")
    # end_time = forms.TimeField(required=False, input_formats="%H:%M", label="Hour:Minutes")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> dict:
        result = dict()
        if self.cleaned_data.get("client_name"):
            result["client__name"] = str(self.cleaned_data["client_name"])

        if self.cleaned_data.get("equipment_name"):
            result["equipment__name"] = str(self.cleaned_data["equipment_name"])

        if self.cleaned_data.get("modes_name"):
            result["mode__name"] = str(self.cleaned_data["modes_name"])

        return result
