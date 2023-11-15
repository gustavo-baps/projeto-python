from django.forms import ModelForm
from .models import Cliente, Carro, Equipe, Mecanico, Peca, Servico, Ordem

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'endereco', 'telefone']

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'placa', 'cliente', 'equipe', 'defeito']

    def __init__(self, *args, **kwargs):
        super(CarroForm, self).__init__(*args, **kwargs)

        self.fields['cliente'].queryset = Cliente.objects.all()

        self.fields['equipe'].queryset = Equipe.objects.all()

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
        fields = ['cliente', 'carro', 'servicos', 'pecas', 'equipe', 'data', 'dataconclusao']
    def __init__(self, *args, **kwargs):
        super(OrdemForm, self).__init__(*args, **kwargs)
        self.fields['servicos'].widget.attrs['class'] = 'form-control'

        self.fields['pecas'].widget.attrs['class'] = 'form-control'