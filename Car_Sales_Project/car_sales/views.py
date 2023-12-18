from django.views.generic import TemplateView
from cars.models import Car  
from categories.models import Brand

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all() 
        context['brands'] = Brand.objects.all()

        selected_brand_slug = self.request.GET.get('brand_slug')
        if selected_brand_slug:
            context['selected_brand'] = Brand.objects.get(slug=selected_brand_slug)
            context['cars'] = Car.objects.filter(brand=context['selected_brand'])
        else:
            context['selected_brand'] = None

        return context