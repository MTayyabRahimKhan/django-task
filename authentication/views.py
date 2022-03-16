from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from . import forms


class RegisterView(FormView):
    template_name = "auth/register.html"
    form_class = forms.RegisterForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


def login_view(request):
    template_name = "auth/login.html"
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            login(request, user)
            if not user.is_staff:
                return redirect('/supportdesk/create/ticket/')
            else:
                return redirect('/supportdesk/agent/list/tickets/')

    else:
        form = forms.LoginForm()
        context = {
            "form": form,
        }
        return render(request, template_name, context)
