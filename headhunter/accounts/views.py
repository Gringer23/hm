from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
            group_id = request.POST.get('group')
            group = Group.objects.get(id=group_id)
            group.user_set.add(user)
            return redirect('accounts:login')  # Измените на вашу домашнюю страницу
    else:
        form = UserCreationForm()
    groups = Group.objects.all()
    return render(request, 'registration/signup.html', {'form': form, 'groups': groups})


# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"