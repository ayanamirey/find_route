from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from trains.forms import TrainForm
from trains.models import Train

__all__ = (
    'home', 'TrainListView', 'TrainDetailView', 'TrainCreateView', 'TrainUpdateView', 'post_delete',
)


def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'trains/home.html', context)


class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно создан'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Поезд успешно отредактирован'


def post_delete(request, pk=None):
    post = get_object_or_404(Train, pk=pk).delete()
    messages.success(request, 'Поезд успешно удален')
    return redirect('trains:home')
