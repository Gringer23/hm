from django.shortcuts import render
from applicants.models import Position
from employers.models import Employers, Vacancies, ResponseVacancies
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    user_group = None
    vacancies = None
    positions = None
    if request.user.groups.filter(name='Соискатель').exists():
        # Если пользователь является соискателем
        user_group = 'applicant'
        vacancies = Vacancies.objects.all()
    elif request.user.groups.filter(name='Работодатель').exists():
        # Если пользователь является работодателем
        user_group = 'employer'
        positions = Position.objects.all()

    return render(request, 'index.html', {'user_group': user_group, 'vacancies': vacancies, 'positions': positions})

def jobconnect(request, vacancies_id):
    vacancies = Vacancies.objects.all()
    position = Position.objects.all()
    vac = Vacancies.objects.get(id=vacancies_id)
    employers = Employers.objects.get(id=vac.employers.id)
    user = User.objects.get(id = request.user.id)
    create = ResponseVacancies.objects.create(employers=employers, user=user, vacancies=vac)
    responcevacansies = ResponseVacancies.objects.all()
    return render(request, 'index.html', {'position': position, 'vacancies': vacancies, 'responcevacansies': responcevacansies})



#
# def about(request):
#     vacancies = Vacancies.objects.all()
#     position = Position.objects.all()
#     return render(request, 'index.html', {'position': position, 'vacancies': vacancies})
