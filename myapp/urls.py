from django.urls import path
from . import views
from .views import book_appointment
from myapp.views import robots_txt
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('why-choose-us/', views.why_choose_us, name='why_choose_us'),
    path('car-software-repair-and-programming/', views.car_software_repair_and_programming, name='car_software_repair_and_programming'),
    path('comfort-system-repair/', views.comfort_system_repair, name='comfort_system_repair'),
    path('engine-control-unit-repair/', views.engine_control_unit_repair, name='engine_control_unit_repair'),
    path('touchless-wheel-alignment/', views.touchless_wheel_alignment, name='touchless_wheel_alignment'),
    path('transmission-repair/', views.transmission_repair, name='transmission_repair'),
    path('fleet-maintenance/', views.fleet_maintenance, name='fleet_maintenance'),
    path('body-and-repair-service/', views.body_and_repair_service, name='body_and_repair_service'),
    path('car-facelift/', views.car_facelift, name='car_facelift'),
    path('car-insurance/', views.car_insurance, name='car_insurance'),
    path('electric-car-repair/', views.electric_car_repair, name='electric_car_repair'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('tinting/', views.tinting, name='tinting'),
    path('suspension/', views.suspension, name='suspension'),
    path('software/', views.software, name='software'),
    path('reviews/', views.review_page, name='review_page'),
    path('ppf/', views.ppf, name='ppf'),
    path('navigation/', views.navigation, name='navigation'),
    path('minor/', views.minor, name='minor'),
    path('management/', views.management, name='management'),
    path('major/', views.major, name='major'),
    path('inspection/', views.inspection, name='inspection'),
    path('gearbox/', views.gearbox, name='gearbox'),
    path('gallery/', views.gallery, name='gallery'),
    path('dip/', views.dip, name='dip'),
    path('detailing/', views.detailing, name='detailing'),
    path('cooling/', views.cooling, name='cooling'),
    path('ceramic/', views.ceramic, name='ceramic'),
    path('camera/', views.camera, name='camera'),
    path('caliper/', views.caliper, name='caliper'),
    path('brake/', views.brake, name='brake'),
    path('axle/', views.axle, name='axle'),
    path('ac/', views.ac, name='ac'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('appointment-success/', views.appointment_success, name='appointment_success'),
    path('packages/', views.packages, name='packages'),
    path("robots.txt", robots_txt),
    
    # SEO Files
    path("robots.txt", robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

]