from django.forms import ModelForm
from django import forms
from .models import Cliente, Equipe, Mecanico, Peca, Servico, Ordem, Carro

class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render_option(self, selected_choices, option_value, option_label, option_index, subindex=None, attrs=None):
        option_value = forms.force_text(option_value)
        return super().render_option(selected_choices, option_value, option_label, option_index, subindex, attrs)


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'endereco', 'telefone']
        

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'placa', 'cliente']

    def __init__(self, *args, **kwargs):
        super(CarroForm, self).__init__(*args, **kwargs)

        self.fields['cliente'].queryset = Cliente.objects.all()

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome']

class MecanicoForm(ModelForm):
    class Meta:
        model = Mecanico
        fields = ['nome', 'sobrenome', 'endereco', 'especialidade', 'equipe']

    def __init__(self, *args, **kwargs):
        super(MecanicoForm, self).__init__(*args, **kwargs)
        self.fields['equipe'].queryset = Equipe.objects.all()

class PecaForm(ModelForm):
    class Meta:
        model = Peca
        fields = ['nome', 'preco']
class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco']

class OrdemForm(ModelForm):
    class Meta:
        model = Ordem
        fields = ['concluida','cliente', 'carro', 'defeito', 'servicos', 'pecas', 'equipe', 'data', 'dataconclusao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'dataconclusao': forms.DateInput(attrs={'type': 'date'}),
            'concluida': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
        labels = {
            'dataconclusao': 'Data de conclusão',
            'concluida':'Ordem concluida?'
        }
    def __init__(self, *args, **kwargs):
        super(OrdemForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs.update({'onchange': 'filtercarros()'})

    def clean(self):
        cleaned_data = super().clean()
        cliente = cleaned_data.get('cliente')

        if cliente:
            self.fields['carro'].queryset = Carro.objects.filter(cliente=cliente)

        return cleaned_data

