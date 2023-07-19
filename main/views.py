from django.http import HttpResponseRedirect, JsonResponse
from post_office import mail
from thehalo.settings import DEFAULT_FROM_EMAIL
from django.views.generic import TemplateView
from . import models


class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        catalog = models.Catalog.objects.all()
        for cats in catalog:
            cats.content = cats.content.split(',')
        context['catalog'] = catalog
        size = models.Size.objects.all()
        context['size'] = size
        slider = models.Slider.objects.all()
        context['slider'] = slider
        about = models.About.objects.all()
        context['about'] = about
        sertificate = models.Sertificate.objects.all()
        context['sertificate'] = sertificate
        return context


def SendPost(requset):
    response = {'req': requset.GET['email']}
    mail.send(
        requset.GET['email'],
        DEFAULT_FROM_EMAIL,
        template='sendPost',
        context=requset.GET,
        priority='now',
    )
    return JsonResponse(response)
