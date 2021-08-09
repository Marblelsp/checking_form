import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

from .forms import MyForm
from .models import ModelForm


def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST or None)
        if form.is_valid():
            input_data = form.cleaned_data
            max_forms = ModelForm.objects.count()
            input_data['phone'] = str(input_data['phone'])

            for item in tuple(input_data):
                if input_data[item] is None or input_data[item] == '':
                    del input_data[item]

            input_field = list(input_data.keys())
            output_forms = []

            for count in range(max_forms):
                valies_form = ModelForm.objects.values()[count]
                for item in tuple(valies_form):
                    if valies_form[item] is None or valies_form[item] == '':
                        del valies_form[item]
                form_fields = list(valies_form.keys())[2:]
                if set(form_fields).issubset(input_field):
                    output_forms.append(valies_form['name'])

            if output_forms == []:
                ouput_json = json.dumps(input_data, sort_keys=True, indent=2, cls=DjangoJSONEncoder)
                return render(request, 'todoform/index.html', {'form': form, 'output_forms': ouput_json})
            return render(request, 'todoform/index.html', {'form': form, 'output_forms': output_forms})
        return render(request, 'todoform/index.html', {'form': form})
    form = MyForm()
    return render(request, 'todoform/index.html', {'form': form})
