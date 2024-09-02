from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Paciente(models.Model):
    Nome = models.CharField(max_length=100, blank=False, null=True)
    Email = models.CharField(max_length=100, blank=False, null=True)
    Data_cadastro = models.DateField(blank=False, null=True)
    Data_Nascimento = models.DateField(blank=False, null=True)
    Estado_civil = models.CharField(max_length=100, blank=False, null=True)
    Grupo = models.CharField(max_length=100, blank=False, null=True)
    Situacao_atual = models.CharField(max_length=100, blank=False, null=True)
    observacoes= models.CharField(max_length=256, blank=False, null=True)
    genero = models.CharField(max_length=100, blank=False, null=True)
    celular = models.CharField(max_length=20, blank=False, null=True)
    clinica = models.CharField(max_length=100, blank=False, null=True)
    local_nascimento = models.CharField(max_length=100, blank=False, null=True)
    CPF = models.CharField(max_length=100, blank=False, null=True)
    RG = models.CharField(max_length=100, blank=False, null=True)
    Orgao_emissor = models.CharField(max_length=100, blank=False, null=True)
    Convenio = models.CharField(max_length=100, blank=False, null=True)
    Plano = models.CharField(max_length=100, blank=False, null=True)
    Data_adesao = models.DateField(blank=False, null=True)
    Nome_pai = models.CharField(max_length=100, blank=True, null=True)
    CPF_pai = models.CharField(max_length=100, blank=True, null=True)
    RG_pai = models.CharField(max_length=100, blank=True, null=True)
    Telefone_pai = models.CharField(max_length=100, blank=True, null=True)
    Nome_mae = models.CharField(max_length=100, blank=True, null=True)
    Cpf_mae = models.CharField(max_length=100, blank=True, null=True)
    Rg_mae = models.CharField(max_length=100, blank=True, null=True)
    Telefone_mae=models.CharField(max_length=100, blank=True, null=True)
    CEP=models.IntegerField(blank=False, null=True)
    Endereco = models.CharField(max_length=100, blank=False, null=True)
    Numero = models.IntegerField(blank=False, null=True)
    Complemento = models.CharField(max_length=100, blank=False, null=True)
    Bairro = models.CharField(max_length=100, blank=False, null=True)
    Cidade = models.CharField(max_length=100, blank=False, null=True)
    Estado = models.CharField(max_length=100, blank=False, null=True)
    def __str__(self):
        return '{}; id<{}>'.format(self.Nome, self.id)
class Cadeira(models.Model):
    nome=models.CharField(max_length=100, blank=True, null=True)
class Agendar(models.Model):
    horario=models.DateTimeField()
    paciente=models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)
    duracao=models.IntegerField(blank=True, null=True)
    dentista=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cadeira=models.ForeignKey(Cadeira, on_delete=models.SET_NULL, null=True)
    confirmacao=models.CharField(max_length=100, blank=True, null=True)

class EventAbstract(models.Model):
    """ Event abstract model """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events


class Event(EventAbstract):
    """ Event model """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="events", blank=True, null=True)

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
class EventMember(EventAbstract):
    """ Event member model """

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_members"
    )

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)
    
class EventAbstract(models.Model):
    """ Event abstract model """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Anotacao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='anotacoes')
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Anotação de {self.paciente.nome} - {self.data_criacao}'
    
class Odontograma(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='odontograma')
    dente1=models.TextField(blank=True)
    dente2=models.TextField(blank=True, null=True)
    dente3=models.TextField(blank=True, null=True)
    dente4=models.TextField(blank=True, null=True)
    dente5=models.TextField(blank=True, null=True)
    dente6=models.TextField(blank=True, null=True)
    dente7=models.TextField(blank=True, null=True)
    dente8=models.TextField(blank=True, null=True)
    dente9=models.TextField(blank=True, null=True)
    dente10=models.TextField(blank=True, null=True)
    dente11=models.TextField(blank=True, null=True)
    dente12=models.TextField(blank=True, null=True)
    dente13=models.TextField(blank=True, null=True)
    dente14=models.TextField(blank=True, null=True)
    dente15=models.TextField(blank=True, null=True)
    dente16=models.TextField(blank=True, null=True)
    dente17=models.TextField(blank=True, null=True)
    dente18=models.TextField(blank=True, null=True)
    dente19=models.TextField(blank=True, null=True)
    dente20=models.TextField(blank=True, null=True)
    dente21=models.TextField(blank=True, null=True)
    dente22=models.TextField(blank=True, null=True)
    dente23=models.TextField(blank=True, null=True)
    dente24=models.TextField(blank=True, null=True)
    dente25=models.TextField(blank=True, null=True)
    dente26=models.TextField(blank=True, null=True)
    dente27=models.TextField(blank=True, null=True)
    dente28=models.TextField(blank=True, null=True)
    dente29=models.TextField(blank=True, null=True)
    dente30=models.TextField(blank=True, null=True)
    dente31=models.TextField(blank=True, null=True)
    dente32=models.TextField(blank=True, null=True)


#anamnese: Como chegou ate nos, e esta em tratamento