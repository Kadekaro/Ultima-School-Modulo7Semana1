from datetime import datetime, timedelta

from django import forms
from Base.models import Contato, Reserva


class contatoForms(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']


class reservaForms(forms.ModelForm):
    # Adicione as opções de datas e horários desejados
    DATAS_HORARIOS_CHOICES = [
        (datetime.now() + timedelta(days=i), f"{datetime.now() + timedelta(days=i):%d/%m/%Y}") for i in range(365)
    ]

    HORARIOS_CHOICES = [
        ('1º:', '08:00'),
        ('2º:', '10:00'),
        ('3º:', '13:00'),
        ('4º:', '15:00'),
    ]

    # Defina o número máximo de reservas por intervalo de tempo
    MAX_RESERVAS_POR_DIA = 4

    # Campos do formulário
    nome = forms.CharField(max_length=50, label='Nome:')
    email = forms.EmailField(max_length=75, label='Email:')
    data_reserva = forms.DateField(widget=forms.Select(choices=DATAS_HORARIOS_CHOICES), label='Data da Reserva:')
    horario_reserva = forms.ChoiceField(choices=HORARIOS_CHOICES, label='Horário da Reserva:')
    mensagem = forms.CharField(widget=forms.Textarea, label='Mensagem:')

    class Meta:
        model = Reserva
        fields = ['nome', 'email', 'data_reserva', 'horario_reserva', 'mensagem']

    def clean_data_reserva(self):
        # Verifica se a data escolhida é no futuro
        data_reserva = self.cleaned_data['data_reserva']
        if data_reserva < datetime.now().date():
            raise forms.ValidationError("Selecione uma data no futuro.")
        return data_reserva

    def clean(self):
        cleaned_data = super().clean()
        # Verifica o número de reservas para o horário escolhido
        data_reserva = cleaned_data.get('data_reserva')
        horario_reserva = cleaned_data.get('horario_reserva')
        if data_reserva and horario_reserva:
            reservas_exist = Reserva.objects.filter(data_reserva=data_reserva, horario_reserva=horario_reserva).count()
            if reservas_exist >= self.MAX_RESERVAS_POR_DIA:
                raise forms.ValidationError(f"O horário {horario_reserva} já atingiu o número máximo de reservas para "
                                            f"o dia.")
        return cleaned_data
