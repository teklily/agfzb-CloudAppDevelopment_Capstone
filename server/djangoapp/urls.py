from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    #todo
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.get_dealerships, name='index'),
    # path for about view
    path(route='about', view=views.about, name='about'),
    # path for contact us view
    path(route='contact', view=views.contact, name='contact'),
    # path for registration
    path('registration/', views.registration_request, name='registration'),
    # path for login
    path('login/', views.login_request, name='login'),
    
    # path for logout
    path('logout/', views.logout_request, name='logout'),
    #path('add_review', views.add_review, name='add_review'),
    path(route='', view=views.get_dealerships, name='index'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),
    #path('dealer/<int:id>/', views.get_dealer_details, name='dealer_details'),
    # path for dealer reviews view
    
    # path for add a review view
    path(route='dealer/<int:id>/review', view=views.add_review, name='add_review'),
    #path(dealer='/<Dealer name>/', view=views.dealer_details, name="details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)