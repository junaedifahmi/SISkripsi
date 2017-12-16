from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from base.forms import UserForm


class Index(View):
    form_class = UserForm
    template_name = 'indexform.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # untuk login
    def post(self, request):
        form = self.form_class(request.POST)
        username = form.data.get('username')
        password = form.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('proposal:index')

        return render(request, self.template_name,{'form': form})



class Home(View):
    template_name = 'home.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)


def logout_view(request):
    logout(request)
    return redirect("base:index")
