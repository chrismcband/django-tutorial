# Create your views here.
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse
from signup.models import Signup


class SignupForm(ModelForm):
    class Meta:
        model = Signup
        exclude = ('use', 'seek_feedback', 'find_world')


class QuestionsForm(ModelForm):
    class Meta:
        model = Signup
        exclude = ('firstname', 'lastname', 'email', 'password', 'subdomain')


class SignupView(generic.FormView):
    template_name = "signup/form.html"
    form_class = SignupForm
    success_url = "/signup/questions"


def post(request):
    f = SignupForm(request.POST)

    new_signup = f.save()
    request.session.signup = new_signup
    return HttpResponseRedirect(reverse('signup:questions'))

def success(request):
    render(request, "signup/success.html")

class QuestionsView(generic.FormView):
    template_name = "signup/questions.html"
    form_class = QuestionsForm
    success_url = "/signup/success",

    def post(self, request):
        signup = request.session.new_signup
        signup.use = request.POST.use
        signup.seek_feedback = request.POST.seek_feedback
        signup.find_world = request.POST.find_world
        signup.save()
