from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.core.validators import validate_email
# Create your views here.


def indexs(request):
    return render(request, 'staticPages/index.html', {
    })


class LoginView(generic.View):

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST['next']
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            if not user:
                request.session['auth_error'] = 1
        return redirect(next_url)


class RegisterView(generic.View):

    def get(self, request, *args, **kwargs):
        try:
            request.session['registration']
        except KeyError:
            return render(request, 'staticPages/registration.html')

        step = request.GET.get('step', False)
        if step:
            if int(request.GET['step']) == 1:
                request.session['registration']['step_one'] = 0
                return render(request, 'staticPages/registration.html')
            elif int(request.GET['step']) == 2:
                if int(request.session['registration']['step_one']) == 1:
                    request.session['registration']['step_two'] = 0
                    return render(request, 'staticPages/registration2.html')
        else:
            if request.session['registration']['step_one'] == 0:
                return render(request, 'staticPages/registration.html')
            elif request.session['registration']['step_one'] == 1 and request.session['registration']['step_two'] == 0:
                return render(request, 'staticPages/registration2.html')

    def post(self, request, *args, **kwargs):
        try:
            request.session['registration']
        except KeyError:
            request.session['registration'] = {
                'First_Name': None,
                'Last_Name': None,
                'Email': None,
                'Sex': None,
                'step_one': 0,
                'State': None,
                'Login': None,
                'Password': None,
                'Type': None,
                'Terms': None,
                'step_two': 0,
            }

        errors = {
            'First_Name': None,
            'Last_Name': None,
            'Email': None,
            'Sex': None,
            'err': 0,
            'State': None,
            'Login': None,
            'Password': None,
            'Type': None,
            'Terms': None,
        }
        if request.session['registration']['step_one'] == 0:
            if request.POST['First_Name']:
                if len(request.POST['First_Name']) < 1 or request.POST['First_Name'] == '':
                    errors['First_Name'] = True
                    errors['err'] = 1
                else:
                    request.session['registration']['First_Name'] = request.POST['First_Name']
            if request.POST['Last_Name']:
                if len(request.POST['Last_Name']) < 1 or request.POST['Last_Name'] == '':
                    errors['Last_Name'] = True
                    errors['err'] = 1
                else:
                    request.session['registration']['Last_Name'] = request.POST['Last_Name']
            if request.POST['Email']:
                try:
                    request.session['registration']['Email'] = request.POST['Email']
                    validate_email(request.POST['Email'])
                except Exception:
                    errors['Email'] = True
                    errors['err'] = 1
            if request.POST['Sex']:
                request.session['registration']['Sex'] = 1
            else:
                request.session['registration']['Sex'] = 0

            if errors['err']:
                request.session['registration']['step_one'] = 0
                return render(request, 'staticPages/registration.html', {
                    'errors': errors,
                })
            else:
                request.session['registration']['step_one'] = 1
                return render(request, 'staticPages/registration2.html')
        elif request.session['registration']['step_two'] == 0:
            return render(request, 'staticPages/registration2.html')


def LogoutView(request):
    logout(request)
    return redirect('dashboard')
