from django.shortcuts import render

# Create your views here.
from app.models import AdminLogin, DonorLogin, DonorRegDetails


def showIndex(request):
    return render(request, "index.html")


def home(request):
    return render(request, "index.html")


def adm(request):
    return render(request, "admin.html")


def login(request):
    u = request.POST.get("uname")
    p = request.POST.get("pwd")
    if AdminLogin.objects.filter(username=u, password=p):
        return render(request, "login.html")
    else:
        return render(request, "index.html")


def donor(request):
    na = request.POST.get("name")
    gen = request.POST.get("gender")
    em = request.POST.get("email")
    con = request.POST.get("contact")
    bg = request.POST.get("bloodgroup")
    st = request.POST.get("state")
    ci = request.POST.get("city")
    ag = request.POST.get("age")
    wt = request.POST.get("weight")
    ld = request.POST.get("lastdonation")
    DonorRegDetails(name=na, gender=gen, email=em, contact=con, bloodgroup=bg, state=st, city=ci, age=ag, weight=wt, lastdonationdate=ld).save()
    return render(request, "donor.html")


def donorhome(request):
    du = request.POST.get("uname")
    dp = request.POST.get("pwd")
    if DonorLogin.objects.filter(d_uname=du, d_pwd=dp):
        return render(request, "donorhome.html")
    else:
        return render(request, "donor.html")


def donorreg(request):
    return render(request, "donorreg.html")

