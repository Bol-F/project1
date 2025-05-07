from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Food
from django.db.models import Q
from .forms import FoodForm


class FoodListView(LoginRequiredMixin, ListView):
    model = Food
    template_name = 'actions/food_list.html'
    context_object_name = 'foods'
    login_url = 'login'
    paginate_by = 3


class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food
    template_name = 'actions/food_detail.html'
    context_object_name = 'food'
    login_url = 'login'


class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'actions/food_form.html'  # Update with your template path
    success_url = reverse_lazy('food_list')  # Redirect after successful creation

    def form_valid(self, form):
        # Any extra logic before saving the form
        return super().form_valid(form)


class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'actions/food_form.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('food_detail', kwargs={'pk': self.object.pk})


class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = reverse_lazy('food_list')
    login_url = 'login'


class FoodSearchView(ListView):
    model = Food
    template_name = 'actions/food_list.html'
    context_object_name = 'foods'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Food.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return Food.objects.all()
