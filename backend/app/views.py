from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from app.models import Paciente, Event, EventMember
from django.http import JsonResponse 
from app.forms import EventForm
from django.views import generic
from datetime import timedelta, datetime, date
from django.views.generic import ListView
from app.utils import Calendar
import calendar
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from app.models import EventMember, Event
from app.utils import Calendar
from app.forms import EventForm, AddMemberForm


@login_required(login_url="/")
def index(request):
    event = Event.objects.all()
    return render(request, 'frontend/index.html', {'events': event})

def login(request):
    if request.user.is_authenticated:
        # Se o usuário já estiver autenticado, redirecione para a página inicial
        return redirect('index')
    
    if request.method == "GET":
        return render(request, 'frontend/pages-login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect('index')
        return redirect('login_incorreto')
    
def login_incorreto(request):
    if request.user.is_authenticated:
        # Se o usuário já estiver autenticado, redirecione para a página inicial
        return redirect('index')
    
    if request.method == "GET":
        return render(request, 'frontend/pages-login-incorreto.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return redirect('index')
        return render(request, 'frontend/pages-login-incorreto.html')

@login_required(login_url="/")
@has_role_decorator('administrador')
def cadastro(request):
    if request.method == "GET":
        users = User.objects.all()
        return render(request, 'frontend/cadastro.html', {'users': users})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        grupo = request.POST.get('grupo')


        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Já existe um usuário com esse nome")

        # Cria o novo usuário
        user = User.objects.create_user(username=username, email=email, password=senha)

        # Verifica se o grupo existe, se não, cria-o

        # Adiciona o usuário ao grupo
        # Salva o usuário
        user.save()
        assign_role(user, grupo)
        users = User.objects.all()
        return render(request, 'frontend/cadastro.html', {'users': users})
@login_required(login_url="/")
def calendario(request):
    return render(request, 'frontend/calendario.html')
@login_required(login_url="/")
def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'frontend/pacientes.html', {'pacientes': pacientes})
@login_required(login_url="/")
def cadastrar_paciente(request):
    if request.method == "GET":
        pacientes = Paciente.objects.all()
        return render(request, 'frontend/cadastrar_paciente.html', {'pacientes': pacientes})
    else:
        nome = request.POST.get('nome')
        genero = request.POST.get('genero')
        data_cadastro = request.POST.get('data_cadastro')
        data_nascimento = request.POST.get('data_nascimento')
        observaçoes = request.POST.get('observaçoes')
        local_nascimento = request.POST.get('local_nascimento')
        estado_civil = request.POST.get('estado_civil')
        grupo = request.POST.get('grupo')
        situacao_atual = request.POST.get('situacao_atual')
        celular= request.POST.get('celular')
        email= request.POST.get('email')
        cep = request.POST.get('cep')
        endereço = request.POST.get('endereço')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        Estado = request.POST.get('Estado')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        orgao_emissor = request.POST.get('orgao_emissor')
        convénio = request.POST.get('convénio')
        plano = request.POST.get('plano')
        data_adesao = request.POST.get('data_adesao')
        nome_pai = request.POST.get('nome_pai')
        cpf_pai = request.POST.get('cpf_pai')
        rg_pai = request.POST.get('rg_pai')
        telefone_pai = request.POST.get('telefone_pai')
        nome_mae = request.POST.get('nome_mae')
        cpf_mae = request.POST.get('cpf_mae')
        rg_mae = request.POST.get('rg_mae')
        telefone_mae = request.POST.get('telefone_mae')
        paciente = Paciente.objects.filter(Nome=nome).first()
        paciente = Paciente(
            Nome=nome,
            genero=genero,
            Data_cadastro=data_cadastro,
            Data_Nascimento=data_nascimento,
            observacoes=observaçoes,
            local_nascimento=local_nascimento,
            Estado_civil=estado_civil,
            Situacao_atual=situacao_atual,
            Email=email,
            celular=celular,
            Grupo=grupo,
            CPF=cpf,
            RG=rg,
            Orgao_emissor=orgao_emissor,
            Convenio=convénio,
            Plano=plano,
            Data_adesao=data_adesao,
            Nome_pai=nome_pai,
            CPF_pai=cpf_pai,
            RG_pai=rg_pai,
            Telefone_pai=telefone_pai,
            Nome_mae=nome_mae,
            Cpf_mae=cpf_mae,
            Rg_mae=rg_mae,
            Telefone_mae=telefone_mae,
            CEP=cep,
            Endereco=endereço,
            Numero=numero,
            Complemento=complemento,
            Bairro=bairro,
            Cidade=cidade,
            Estado=Estado
        )
        paciente.save()
        
        return render(request, 'frontend/cadastrar_paciente.html')
    
@has_role_decorator('administrador')
@login_required(login_url="/")
def delete_paciente(request, paciente_id):
    context={}
    paciente=get_object_or_404(Paciente, id=paciente_id)
    context['object']=paciente
    if request.method == "POST":
        paciente.delete()
        return redirect('pacientes')
    return render(request, 'frontend/confirmar_excluir_paciente.html', context)

@login_required(login_url="/")
def pagina_usuario(request):
    return render(request, 'frontend/users-profile.html')

@login_required(login_url="/")
def pagina_paciente(request, paciente_id):
    context={}
    paciente=get_object_or_404(Paciente, id=paciente_id)
    context['object']=paciente
    return render(request, 'frontend/pagina_paciente.html', context)

@has_role_decorator('administrador')
@login_required(login_url="/")
def pagina_financeiro(request):
    return render(request, 'frontend/pagina_paciente.html')

@has_role_decorator('administrador')
@login_required(login_url="/")
def delete_user(request, user_id):
    context={}
    usuario=get_object_or_404(User, id=user_id)
    context['object']=usuario
    if request.method == "POST":
        usuario.delete()
        return redirect('cadastro')
    return render(request, 'frontend/confirmar_excluir.html', context)


def calendario(request):
    events = Event.objects.all()
    return render(request, 'frontend/calendario.html', {'events': events})

class CalendarViewNew(LoginRequiredMixin, generic.View):
    template_name = "frontend/calendario.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events(user=request.user)
        events_month = Event.objects.get_running_events(user=request.user)
        event_list = []
        # start: '2020-09-16T16:00:00'
        for event in events:
            event_list.append(
                {   "id": event.id,
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "description": event.description,
                }
            )
        
        context = {"form": forms, "events": event_list,
                   "events_month": events_month}
        return render(request, self.template_name, context)
    
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = "accounts:signin"
    model = Event
    template_name = "frontend/calendario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


@login_required(login_url="signup")
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
        )
        return HttpResponseRedirect(reverse("calendario"))
    return render(request, "event.html", {"form": form})


class EventEdit(generic.UpdateView):
    model = Event
    fields = ["title", "description", "start_time", "end_time"]
    template_name = "event.html"


@login_required(login_url="signup")
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {"event": event, "eventmember": eventmember}
    return render(request, "frontend/calendario.html", context)


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == "POST":
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                user = forms.cleaned_data["user"]
                EventMember.objects.create(event=event, user=user)
                return redirect("calendario")
            else:
                print("--------------User limit exceed!-----------------")
    context = {"form": forms}
    return render(request, "frontend/calendario.html", context)


class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = "frontend/calendario.html"
    success_url = reverse_lazy("calendario")

class CalendarViewNew(LoginRequiredMixin, generic.View):
    login_url = "accounts:signin"
    template_name = "frontend/calendario.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events(user=request.user)
        events_month = Event.objects.get_running_events(user=request.user)
        event_list = []
        # start: '2020-09-16T16:00:00'
        for event in events:
            event_list.append(
                {   "id": event.id,
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "description": event.description,
                }
            )
        
        context = {"form": forms, "events": event_list,
                   "events_month": events_month}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("calendario")
        context = {"form": forms}
        return render(request, self.template_name, context)



def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return JsonResponse({'message': 'Consulta deletada!.'})
    else:
        return JsonResponse({'message': 'Erro!'}, status=400)

def next_week(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        next = event
        next.id = None
        next.start_time += timedelta(days=7)
        next.end_time += timedelta(days=7)
        next.save()
        return JsonResponse({'message': 'Reagendado para semana que vem'})
    else:
        return JsonResponse({'message': 'Erro!'}, status=400)

def next_day(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        next = event
        next.id = None
        next.start_time += timedelta(days=1)
        next.end_time += timedelta(days=1)
        next.save()
        return JsonResponse({'message': 'Reagendado para amanha'})
    else:
        return JsonResponse({'message': 'Erro!'}, status=400)

class AllEventsListView(ListView):
    """ All event list views """

    template_name = "frontend/calendario.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)


class RunningEventsListView(ListView):
    """ Running events list view """

    template_name = "frontend/calendario.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)