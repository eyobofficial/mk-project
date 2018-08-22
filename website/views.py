from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

# from .forms import SubscriberModelForm, MessageModelForm

from .models import Company, Service, Product, Message, Subscriber


class IndexView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['company'] = Company.objects.first()
        context['services'] = Service.objects.all()
        context['featured_products'] = Product.objects.filter(is_featured=True)
        return context


class MessageCreateView(CreateView):
    model = Message
    template_name = 'website/index.html'
    fields = ['name', 'email', 'message']
    success_url = reverse_lazy('website:index')


class SubscribeCreateView(CreateView):
    model = Subscriber
    fields = ['email']
    # success_url = reverse_lazy('website:index')
