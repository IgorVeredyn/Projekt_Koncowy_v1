from django.contrib import admin
from django.urls import path, include
from TaskTamer import views
from TaskTamer.views import SubmittableLoginView
from django.conf.urls.static import static
from django.conf import settings
from goallab import urls
urlpatterns = [
    path('admin/', admin.site.urls),

    path('home', views.HomeView.as_view(), name='home'),

    path('tasks/create', views.TasksCreateView.as_view(), name='tasks-create'),
    path('tasks/read', views.TasksReadView.as_view(), name='tasks-read'),
    path('tasks/update/<pk>', views.TasksUpdateView.as_view(), name='tasks-update'),
    path('tasks/delete/<pk>', views.TasksDeleteView.as_view(), name='tasks-delete'),


    path('challenge/create', views.ChallengeCreateView.as_view(), name='challenge-create'),
    path('challenge/read', views.ChallengeReadView.as_view(), name='challenge-read'),
    path('challenge/update/<pk>', views.ChallengeUpdateView.as_view(), name='challenge-update'),
    path('challenge/delete/<pk>', views.ChallengeDeleteView.as_view(), name='challenge-delete'),

    path('accounts/', include('allauth.urls')),
    path('email-confirmation/<str:key>/', views.email_confirmation_view, name='email-confirmation'),


    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', views.SubmittableLogoutView.as_view(next_page='login'), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),

    # path('picture/upload', views.PicturesCreateView.as_view(), name='picture_create'),
    path('picture/update/', views.PicturesUpdateView.as_view(), name='picture_update')



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)