from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from tourism_app.models import City, VRVideo, Attraction

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cities = City.objects.prefetch_related('attractions', 'videos').all()
        attractions = Attraction.objects.all()
        videos = VRVideo.objects.all().order_by('-created_at')

        context.update({
            'cities': cities,
            'videos': videos,
            'attractions': attractions,
        })
        return context