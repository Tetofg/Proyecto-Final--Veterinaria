from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView
from apps.rol.forms import AdopcionForm
from apps.rol.models import Adopcion

from apps.rol.models import Mascotas

class IndexView(ListView):
    model = Mascotas
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

class MascotasView(ListView):
    model = Mascotas
    paginate_by = 6
    template_name = "vet.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = self.model.objects.filter(sta__startswith = 'in' )
        return queryset


class AdopcionCreateView(CreateView):
    model = Adopcion
    form_class = AdopcionForm
    template_name = 'form11.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                petid = request.POST['pet']
                masc = Mascotas.objects.filter(pk=petid).update(sta='adopted')
                print(masc)
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            print(e)
            data['error'] = str(e)
        return JsonResponse(data)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adoptando una Mascota'
        context['entity'] = 'Adopcion'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class AboutView(TemplateView):
    model = Mascotas
    template_name = "about.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset