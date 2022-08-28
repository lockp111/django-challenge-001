import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.forms.models import model_to_dict
from django.views import View
from app import articles, authors

# Create your views here.
class Login(View):
    def post(self, request: HttpRequest):
        req = json.loads(request.body)

        user = authenticate(username=req['name'], password=req['password'])
        if user is None:
            return JsonResponse({"code": -1, "msg": "login fail"})

        login(request, user)
        return JsonResponse({"code": 0, "msg": "success"})


class SignUp(View):
    def post(self, request: HttpRequest):
        req = json.loads(request.body)

        try:
            password = make_password(req['password'], salt='app')
            res = User.objects.create(
                username=req['name'], password=password, is_active=True
            )
            data = model_to_dict(res)
        except Exception as e:
            return JsonResponse({"code": -1, "msg": str(e)})

        del data['password']
        return JsonResponse(data)


class Authors(View):
    def get(self, request: HttpRequest):
        res = authors.list()
        return JsonResponse(res.data, safe=False)

    def post(self, request: HttpRequest):
        req = json.loads(request.body)

        try:
            authors.create(req)
        except Exception as e:
            return JsonResponse({"code": -1, "msg": str(e)})

        return JsonResponse({"code": 0, "msg": "success"})

    def put(self, request: HttpRequest):
        req = json.loads(request.body)

        try:
            authors.update(req['id'], req)
        except Exception as e:
            return JsonResponse({"code": -1, "msg": str(e)})

        return JsonResponse({"code": 0, "msg": "success"})

    def delete(self, request: HttpRequest):
        req = json.loads(request.body)

        try:
            authors.delete(req['id'])
        except Exception as e:
            return JsonResponse({"code": -1, "msg": str(e)})

        return JsonResponse({"code": 0, "msg": "success"})


class Articles(View):
    def get(self, request: HttpRequest):
        category = request.GET.get('category')
        res = articles.list(category)
        return JsonResponse(res.data, safe=False)

    def post(self, request: HttpRequest):
        req = json.loads(request.body)

        try:
            articles.create(req)
        except Exception as e:
            return JsonResponse({"code": -1, "msg": str(e)})

        return JsonResponse({"code": 0, "msg": "success"})


class ArticleDetail(View):
    def get(self, request: HttpRequest, id: int):
        if request.user.is_authenticated:
            return HttpResponse('user login')
        return HttpResponse('user logout')
