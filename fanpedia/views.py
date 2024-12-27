from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import FanPedia
from .forms import FanPediaForm

class FanPediaView(ListView):
    model = FanPedia
    template_name = 'home.html'
    context_object_name = 'fanpedia_list'

class FanPediaCreateView(CreateView):
    model = FanPedia
    form_class = FanPediaForm
    template_name = 'fanpedia_create.html'
    success_url = reverse_lazy('home')

class FanPediaDetailView(DetailView):
    model = FanPedia
    template_name = 'fanpedia_detail.html'
    context_object_name = 'fanpedia'

    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(FanPedia, slug=slug)