"""
URL configuration for ResortPortel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resortapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index.html"),
    path('aboutus', views.aboutus,name="about.html"),
    path('Service', views.service,name="service.html"),
    path('Team', views.team,name="team.html"),
    path('Testimonial', views.testimonial,name="testimonial.html"),
    path('Room', views.room,name="room.html"),
    path('Booking', views.booking,name="booking.html"),
    path('Contact', views.contact,name="contact.html"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
