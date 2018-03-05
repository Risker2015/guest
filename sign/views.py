from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
from sign.models import Event, Guest


def index(request):
    #return HttpResponse("Hello Django")
    return render(request,"index.html")

def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user and not None:
            auth.login(request,user) #登录
            response = HttpResponseRedirect('/sign/event_manage/')
            response.set_cookie("user",username,3600) #添加浏览器cookie
            request.session['user'] = username #将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error'})
    else:
        return render(request,"index",{"error":"username or password error"})
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    print(event_list)
    username = request.COOKIES.get("user",'') #读取浏览器cookie
    #username = request.session.get('user','') #读取浏览器session
    response = render(request,"event_manage.html",{"user":username,"events":event_list})
    response.set_cookie("search_type","event",3600)
    return response

@login_required
def guest_manage(request):
    username = request.session.get('user', '')  # 读取浏览器session
    guest_list = Guest.objects.all() #查询所有数据
    # 分页
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    contacts = None
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    response = render(request,"guest_manage.html",{"user":username,"guests":contacts})
    response.set_cookie("search_type","guest",3600)
    return response

#搜索
@login_required()
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get("name","")
    search_type = request.COOKIES.get("search_type","")
    if(search_type == "event"):
        event_list = Event.objects.filter(name__contains=search_name)
        return render(request, "event_manage.html", {"user": username, "events": event_list})
    elif(search_type == "guest"):
        guest_list = Guest.objects.filter(realname__contains=search_name)
        return render(request, "guest_manage.html", {"user": username, "guests": guest_list})

#页面签到
@login_required()
def sign_index(request,event_id):
    event = get_object_or_404(Event,id = event_id)
    return render(request,'sign_index.html',{'event':event})