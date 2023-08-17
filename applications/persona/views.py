from django.shortcuts import render
from django.urls import reverse_lazy

#import en una linea
#from django.views.generic import ListView, DetailView, CreateView

#import en mas de una linea
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)


# Models
from .models import Empleado
# forms
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """ Vista que carga la pagina de Inicio(home)"""
    template_name = "inicio.html"


# Create your views here.
class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 5
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
            )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = "persona/lista_empleados.html"
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


class ListByAreaEmpleado(ListView):
    """ Lista empleados de una area    """
    template_name = "persona/list_by_area.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista


class ListEmpleadosByKword(ListView):
    """ Lista empleado por clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleado'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(first_name = palabra_clave)
        return lista


class ListHabilidadesEmpleado(ListView):
    """ Lista habilidades de un empleado """
    template_name = 'persona/habilidades.html'
    tmp_var='Hola Vista'
    context_object_name = 'habilidades'

    def get_queryset(self):
        id = self.kwargs['id']
        empleado = Empleado.objects.get(id=id)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empelado del Mes'
        return context


class SucessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm


    #fields = ('__all__') # Para agregar todos los campos del Modelo
    # fields = [
    #     'first_name',
    #     'last_name',
    #     'job',
    #     'departamento',
    #     'habilidades',
    #     'avatar',
    # ]

    #success_url = '.' # Para que se recargue en la misma pagina
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        # Logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]

    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**************METODO POST******************')
        print('=========================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Logica del proceso
        print('**************METODO FORM VALID******************')
        print('=========================')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')
