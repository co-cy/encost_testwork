from django import forms
from .models import *
from datetime import date, timedelta, datetime, time


class SearchForm(forms.Form):
    client_name = forms.ModelChoiceField(required=False, queryset=Clients.objects.all(),
                                         empty_label="ALL", to_field_name="id")
    equipment_name = forms.ModelChoiceField(required=False, queryset=Equipment.objects.all(),
                                            empty_label="ALL", to_field_name="name")
    modes_name = forms.ModelChoiceField(required=False, queryset=Modes.objects.all(),
                                        empty_label="ALL", to_field_name="name")

    duration = forms.IntegerField(required=False, label="Duration>:", min_value=0, initial=0)

    start_date = forms.DateField(required=False, label="Start date", initial=date.today)
    end_date = forms.DateField(required=False, label="End date", initial=lambda: date.today() + timedelta(days=1))

    start_time = forms.TimeField(required=False, label="Start time",
                                 initial=datetime.now().time)
    end_time = forms.TimeField(required=False, label="End time",
                               initial=lambda: (datetime.now() + timedelta(hours=1)).time())

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

        if self.cleaned_data.get("duration"):
            result["minutes__gt"] = str(self.cleaned_data.get("duration"))

        if self.cleaned_data.get("start_date"):
            datetime_tmp = datetime.combine(self.cleaned_data.get("start_date"), time.min)
            if self.cleaned_data.get("start_time"):
                datetime_tmp += datetime.combine(date.min, self.cleaned_data.get("start_time")) - datetime.min
            result["start__gt"] = str(datetime_tmp)

        if self.cleaned_data.get("end_date"):
            datetime_tmp = datetime.combine(self.cleaned_data.get("end_date"), time.min)
            if self.cleaned_data.get("end_time"):
                datetime_tmp += datetime.combine(date.min, self.cleaned_data.get("end_time")) - datetime.min
            result["start__lt"] = str(datetime_tmp)

        return result
