from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Car
from django.urls import reverse
from authentication.models import UserProfile
from .forms import CommentForm


# class CarDetailView(DetailView):
#     model = Car
#     template_name = 'car_detail.html'
#     context_object_name = 'car'

# def car_detail(request, car_id):
#     car = Car.objects.get(id=car_id)
#     return render(request, 'car_detail.html', {'car': car})

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class BuyNowView(View):
    template_name = 'out_of_stock.html'

    def get(self, request, car_id):
        car = get_object_or_404(Car, pk=car_id)

        if car.quantity > 0:
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            
            if car not in user_profile.bought_cars.all():
                user_profile.bought_cars.add(car)  

            car.quantity -= 1
            car.save()
            car_detail_url = reverse('car_detail', args=[car.id])
            return HttpResponseRedirect(car_detail_url) 
        else:
            return render(request, self.template_name, {'car': car})
        
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return HttpResponseRedirect(request.path) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
