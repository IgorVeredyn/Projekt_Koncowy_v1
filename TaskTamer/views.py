from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, View
from TaskTamer import models
from TaskTamer import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='base/task_list.html', context={'task': models.Tasks.objects.filter(challenge= False).all()})




class TasksCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('home')
    form_class = forms.TasksForm
    model = models.Tasks
    template_name = 'base/tasks_create.html'


class TasksReadView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name='base/tasks_read.html', context={'task': models.Tasks.objects.filter(challenge= False).all()})

class TasksUpdateView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('home')
    form_class = forms.TasksForm
    model = models.Tasks
    template_name = 'base/tasks_create.html'


class TasksDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('home')
    model = models.Tasks
    template_name = 'base/tasks_delete.html'







class SubmittableLoginView(LoginView, LoginRequiredMixin):
    template_name = 'accounts/login.html'
    fields = "__all__"
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('email-confirmation') #endpoint

def email_confirmation_view(request, key):
    try:
        confirmation = EmailConfirmation.objects.get(key=key)
        confirmation.confirm(request)
        return render(request, 'email/email_confirmation_success.html')
    except EmailConfirmation.DoesNotExist:
        return render(request, 'email/email_confirmation_error.html')

from allauth.account.models import EmailConfirmation


class SubmittablePasswordChangeView(PasswordChangeView):
  template_name = 'change_password.html'
  success_url = reverse_lazy('home')


class SubmittableLogoutView(LogoutView):
    success_url = reverse_lazy('home')





class ChallengeCreateView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('home')
    form_class = forms.TasksForm
    model = models.Tasks
    template_name = 'challenges/challenge_create.html'

class ChallengeReadView(LoginRequiredMixin, View):
    def get(self, request):
        challenges = models.Tasks.objects.filter(challenge=True).all()
        point_earned = models.User_Tasks.objects.all()
        context = {
            'challenges': challenges,
            'point_earned': point_earned,  # Add the data from AnotherModel to the context
        }
        return render(request, template_name='challenges/challenge_list.html', context=context)

class ChallengeUpdateView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('challenge-read')
    form_class = forms.TasksForm
    model = models.Tasks
    template_name = 'challenges/challenge_update.html'

class ChallengeDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('challenge-read')
    model = models.Tasks
    template_name = 'challenges/challenge_delete.html'







class PicturesUpdateView(LoginRequiredMixin, UpdateView):
    success_url = 'home'
    form_class = forms.ProfileForm
    model = models.Profil
    template_name = 'user/edit_profile.html'
    def get_object(self, queryset=None):
        return self.request.user