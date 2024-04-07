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
    responcevacansies = ResponseVacancies.objects.all()
    response_dict = {}
    for response in responcevacansies:
        if response.position:
           response_dict[response.position.id] = response
    if request.user.groups.filter(name='Соискатель').exists():
        # Если пользователь является соискателем
        user_group = 'applicant'
        vacancies = Vacancies.objects.all()
    elif request.user.groups.filter(name='Работодатель').exists():
        # Если пользователь является работодателем
        user_group = 'employer'
        positions = Position.objects.all()

    return render(request, 'index.html', {'user_group': user_group, 'vacancies': vacancies, 'positions': positions, 'responcevacansies': responcevacansies, 'response_dict': response_dict})

def jobconnect(request, vacancies_id):
    vacancies = Vacancies.objects.all()
    vac = Vacancies.objects.get(id=vacancies_id)
    employers = Employers.objects.get(id=vac.employers.id)
    user = User.objects.get(id = request.user.id)
    position = Position.objects.get(user=user)
    create = ResponseVacancies.objects.create(employers=employers, user=user, vacancies=vac, position=position)

    responcevacansies = ResponseVacancies.objects.all()
    response_dict = {}
    for response in responcevacansies:
        if response.vacancies:
           response_dict[response.vacancies.id] = response
    user_group = None
    if request.user.groups.filter(name='Соискатель').exists():
            # Если пользователь является соискателем
       user_group = 'applicant'
       vacancies = Vacancies.objects.all()
    elif request.user.groups.filter(name='Работодатель').exists():
            # Если пользователь является работодателем
         user_group = 'employer'
         positions = Position.objects.all()
    return render(request, 'index.html', {'user_group': user_group, 'position': position, 'vacancies': vacancies, 'responcevacansies': responcevacansies, 'response_dict': response_dict})

def jobreject(request, vacancies_id):
    response = ResponseVacancies.objects.filter(vacancies_id=vacancies_id)
    if response.exists():
       response.delete()
    user_group = None
    vacancies = None  # Инициализация переменной vacancies
    positions = None
    responcevacansies = ResponseVacancies.objects.all()
    user = User.objects.get(id=request.user.id)
    response_dict = {}
    for response in responcevacansies:
        if response.vacancies:
           response_dict[response.vacancies.id] = response
    if user.groups.filter(name='Соискатель').exists():
            # Если пользователь является соискателем
            user_group = 'applicant'
            vacancies = Vacancies.objects.all()
    elif user.groups.filter(name='Работодатель').exists():
            # Если пользователь является работодателем
            user_group = 'employer'
            positions = Position.objects.all()
    return render(request, 'index.html', {'user_group': user_group, 'positions': positions, 'vacancies': vacancies, 'responcevacansies': responcevacansies, 'response_dict': response_dict})

def invite(request, position_id):
    vacancies = Vacancies.objects.all()
    positions = Position.objects.all()
    position = Position.objects.get(id=position_id)
    user = User.objects.get(id=request.user.id)
    employers = Employers.objects.filter(user=user).first()  # Используйте атрибут user объекта User
    is_invite = True
    create = ResponseVacancies.objects.create(employers=employers, user=user, position=position, is_invitation=is_invite)
    responcevacansies = ResponseVacancies.objects.all()
    response_dict = {}
    for response in responcevacansies:
        if response.position:
           response_dict[response.position.id] = response
    user_group = None
    if request.user.groups.filter(name='Соискатель').exists():
        # Если пользователь является соискателем
        user_group = 'applicant'
        vacancies = Vacancies.objects.all()
    elif request.user.groups.filter(name='Работодатель').exists():
        # Если пользователь является работодателем
        user_group = 'employer'
        positions = Position.objects.all()
    return render(request, 'index.html', {'user_group': user_group, 'positions': positions, 'vacancies': vacancies, 'responcevacansies': responcevacansies, 'response_dict': response_dict})

def reject(request, position_id):
    response = ResponseVacancies.objects.filter(position_id=position_id)
    if response.exists():
        response.delete()
    responcevacansies = ResponseVacancies.objects.all()
    response_dict = {}
    for response in responcevacansies:
        if response.position:
           response_dict[response.position.id] = response
    user = User.objects.get(id=request.user.id)
    user_group = None
    vacancies = None  # Инициализация переменной vacancies
    if user.groups.filter(name='Соискатель').exists():
        # Если пользователь является соискателем
        user_group = 'applicant'
        vacancies = Vacancies.objects.all()
    elif user.groups.filter(name='Работодатель').exists():
        # Если пользователь является работодателем
        user_group = 'employer'
        positions = Position.objects.all()
    return render(request, 'index.html', {'user_group': user_group, 'positions': positions, 'vacancies': vacancies, 'responcevacansies': responcevacansies, 'response_dict': response_dict})


# def about(request):
#     vacancies = Vacancies.objects.all()
#     position = Position.objects.all()
#     return render(request, 'index.html', {'position': position, 'vacancies': vacancies})
