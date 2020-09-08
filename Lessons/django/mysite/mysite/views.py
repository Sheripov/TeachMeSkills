from django.contrib.auth.models import User
from django.http import HttpResponse


def view(request):
    if not request.user.is_authenticated:
        return HttpResponse("Go away <a href='/admin/login'>Login</a>")
    return HttpResponse(f"Hello {request.user} <a href='/admin/logout'>Logout from {request.user}</a>")
    # is_stuff - возвращает True или False в  зависимости админ он или нет
    # import pdb;pdb.set_trace()
    # dir(request)
    # print(user)
    # return HttpResponse(f'Hello {user.first_name} {User.get_user_permissions(user)}')
