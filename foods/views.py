from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Food
from .forms import FoodForm


@login_required(login_url='login')
def food_list(request):
    foods = Food.objects.all()
    return render(request, 'actions/food_list.html', {'foods': foods})


@login_required(login_url='login')
def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'actions/food_detail.html', {'food': food})


@login_required(login_url='login')
def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'actions/food_form.html', {'form': form})


@login_required(login_url='login')
def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('food_list')


@login_required(login_url='login')
def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_detail', pk=pk)  # or to 'food_list' if you prefer
    else:
        form = FoodForm(instance=food)
    return render(request, 'actions/food_form.html', {'form': form})  # fallback to form


@login_required(login_url='login')
def search(request):
    query = request.GET.get('q', '')
    results = Food.objects.all()
    print(query)
    if query:
        results = Food.objects.filter(name__icontains=query) | Food.objects.filter(description__icontains=query)
    print(results)
    return render(request, 'actions/food_list.html', {
        'foods': results,
        'query': query,
    })
