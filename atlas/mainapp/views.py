from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from mainapp.models import Obj2Ai,Obj1Ai,Obj2Cmn,Obj1Cmn
from itertools import chain

values_1 = Obj1Ai.objects.order_by('idai').values_list('idai', flat=True).distinct()
values_2 = Obj2Ai.objects.order_by('idai').values_list('idai', flat=True).distinct()
errors_1 = Obj1Ai.objects.filter(err__gt=0,sts=1).order_by('idai').values_list().distinct()
errors_2 = Obj2Ai.objects.filter(err__gt=0,sts=1).order_by('idai').values_list().distinct()


# Create your views here.
@login_required(login_url='/auth/login/')
def index(request):
    if request.user.username == 'Atl':
        content = {
            'ai_1_value':values_1,
            'ai_2_value':values_2,
            'errors_1':errors_1,
            'errors_2':errors_2
        }
        return render(request,'mainapp/index.html',content)

    if request.user.username == 'Cm001':
        content = {
            'items':values_1
        }
        return render(request,'mainapp/index.html',content)

    if request.user.username == 'Cm002':
        content = {
            'items':values_2
        }
        return render(request,'mainapp/index.html',content)


@login_required(login_url='/auth/login/')
def info(request):
    if request.method == 'GET' and request.user.username == 'Atl':
        obj1_cmn = Obj1Cmn.objects.all().order_by('id')
        obj2_cmn = Obj2Cmn.objects.all().order_by('id')
        obj1_cmn_reversed = obj1_cmn.reverse()[:240]
        obj2_cmn_reversed = obj2_cmn.reverse()[:240]
        obj1_ai = Obj1Ai.objects.filter(err__gt=0,sts=1)[:20][::-1]
        obj2_ai = Obj2Ai.objects.filter(err__gt=0,sts=1)[:20][::-1]
        content = {
            'obj1_cmn':obj1_cmn_reversed,
            'obj2_cmn':obj2_cmn_reversed,
            'obj1_ai':obj1_ai,
            'obj2_ai':obj2_ai,
            'ai_1_value': values_1,
            'ai_2_value': values_2
        }
        return render(request,'mainapp/info.html',content)

    if request.method == 'POST' and request.user.username == 'Atl':
        obj1_cmn = Obj1Cmn.objects.all().order_by('id')
        obj2_cmn = Obj2Cmn.objects.all().order_by('id')
        obj1_cmn_reversed = obj1_cmn.reverse()[:240]
        obj2_cmn_reversed = obj2_cmn.reverse()[:240]
        obj1_ai = Obj1Ai.objects.filter(err__gt=0,sts=1)[:20][::-1]
        obj2_ai = Obj2Ai.objects.filter(err__gt=0,sts=1)[:20][::-1]
        content = {
            'obj1_cmn':obj1_cmn_reversed,
            'obj2_cmn':obj2_cmn_reversed,
            'obj1_ai':obj1_ai,
            'obj2_ai':obj2_ai,
            'ai_1_value': values_1,
            'ai_2_value': values_2
        }
        cmn_id = int(request.POST.get('cmn_id'))
        print(cmn_id)
        print(type(cmn_id))
        if cmn_id == 1:
            ai_id = int(request.POST.get('ai_id'))
            print('Find in 1')
            print(ai_id)
            obj = Obj1Ai.objects.get(id=ai_id)
            obj.sts = 2
            obj.save()
        else:
            ai_id = request.POST.get('ai_id')
            print('Find in 2')
            print(ai_id)
            obj = Obj2Ai.objects.get(id=ai_id)
            obj.sts = 2
            obj.save()

        return render(request, 'mainapp/info.html', content)

    if request.method == 'GET' and request.user.username == 'Cm001':
        obj_cmn = Obj1Cmn.objects.all().order_by('id')
        obj_cmn_reversed = obj_cmn.reverse()[:240]
        obj_ai = Obj1Ai.objects.filter(err__gt=0,sts=1)[:20][::-1]
        content = {
            'obj_cmn':obj_cmn_reversed,
            'obj_ai': obj_ai,
            'items':values_1
        }
        return render(request,'mainapp/info.html',content)

    if request.method == 'POST' and request.user.username == 'Cm001':
        obj_cmn = Obj1Cmn.objects.all().order_by('id')
        obj_cmn_reversed = obj_cmn.reverse()[:240]
        obj_ai = Obj1Ai.objects.filter(err__gt=0, sts=1)[:20][::-1]
        content = {
            'obj_cmn': obj_cmn_reversed,
            'obj_ai': obj_ai,
            'items': values_1
        }
        ai_id = request.POST.get('ai_id')
        print(ai_id)
        obj = Obj1Ai.objects.get(id=ai_id)
        obj.sts = 2
        obj.save()
        return render(request, 'mainapp/info.html', content)


    if request.method == 'GET' and request.user.username == 'Cm002':
        obj_cmn = Obj2Cmn.objects.all().order_by('id')
        obj_cmn_reversed = obj_cmn.reverse()[:240]
        obj_ai = Obj2Ai.objects.filter(err__gt=0,sts=1)[:20][::-1]
        content = {
            'obj_cmn':obj_cmn_reversed,
            'obj_ai':obj_ai,
            'items':values_2
        }
        return render(request,'mainapp/info.html',content)

    if request.method == 'POST' and request.user.username == 'Cm002':
        ai_id = request.POST.get('ai_id')
        obj = Obj2Ai.objects.get(id=ai_id)
        obj.sts = 2
        obj.save()
        obj_cmn = Obj2Cmn.objects.all().order_by('id')
        obj_cmn_reversed = obj_cmn.reverse()[:240]
        obj_ai = Obj2Ai.objects.filter(err__gt=0, sts=1)[:20][::-1]
        content = {
            'obj_cmn': obj_cmn_reversed,
            'obj_ai': obj_ai,
            'items':values_2
        }
        return render(request, 'mainapp/info.html', content)


@login_required(login_url='/auth/login/')
def info_ai(request,id):

    if request.method == 'GET' and request.user.username == 'Atl':

        Ai_1 = Obj1Ai.objects.filter(idai=id).order_by('datain')
        Ai_2 = Obj2Ai.objects.filter(idai=id).order_by('datain')
        obj_1_ai = Obj1Ai.objects.filter(idai=id, err__gt=0, sts=1)[:20][::-1]
        obj_2_ai = Obj2Ai.objects.filter(idai=id, err__gt=0, sts=1)[:20][::-1]
        content = {
            'ai_1':Ai_1,
            'ai_2':Ai_2,
            'obj1_ai': obj_1_ai,
            'obj2_ai': obj_2_ai,
            'ai_1_value': values_1,
            'ai_2_value': values_2
        }
        return render(request,'mainapp/info_ai.html',content)

    if request.method == 'POST' and request.user.username == 'Atl':
        Ai_1 = Obj1Ai.objects.filter(idai=id).order_by('datain')
        Ai_2 = Obj2Ai.objects.filter(idai=id).order_by('datain')
        obj_1_ai = Obj1Ai.objects.filter(idai=id, err__gt=0, sts=1)[:20][::-1]
        obj_2_ai = Obj2Ai.objects.filter(idai=id, err__gt=0, sts=1)[:20][::-1]
        content = {
            'ai_1': Ai_1,
            'ai_2': Ai_2,
            'obj1_ai': obj_1_ai,
            'obj2_ai': obj_2_ai,
            'ai_1_value': values_1,
            'ai_2_value': values_2
        }
        cmn_id = int(request.POST.get('cmn_id'))
        print(cmn_id)
        print(type(cmn_id))
        if cmn_id == 1:
            ai_id = int(request.POST.get('ai_id'))
            print('Find in 1')
            print(ai_id)
            obj = Obj1Ai.objects.get(id=ai_id)
            obj.sts = 2
            obj.save()
        else:
            ai_id = request.POST.get('ai_id')
            print('Find in 2')
            print(ai_id)
            obj = Obj2Ai.objects.get(id=ai_id)
            obj.sts = 2
            obj.save()
        return render(request,'mainapp/info_ai.html',content)


    if request.method == 'GET' and request.user.username == 'Cm001':
        Ai = Obj1Ai.objects.filter(idai=id).order_by('datain')
        obj_ai = Obj1Ai.objects.filter(idai=id, err__gt=0, sts=1)[:20][::-1]
        content = {
            'ai': Ai,
            'obj_ai': obj_ai,
            'items':values_1
        }
        return render(request, 'mainapp/info_ai.html', content)

    if request.method == 'GET' and request.user.username == 'Cm002':
        Ai = Obj2Ai.objects.filter(idai=id).order_by('datain')
        obj_ai = Obj2Ai.objects.filter(idai=id, err__gt=0, sts=1)[:20][::-1]
        content = {
            'ai': Ai,
            'obj_ai': obj_ai,
            'items':values_2
        }
        return render(request, 'mainapp/info_ai.html', content)

    if request.method == 'POST' and request.user.username == 'Cm001':
        Ai = Obj1Ai.objects.filter(idai=id).order_by('datain')
        obj_ai = Obj1Ai.objects.filter(idai=id, err__gt=0, sts=1)[:20][::-1]
        content = {
            'ai': Ai,
            'obj_ai': obj_ai,
            'items':values_1
        }
        ai_id = request.POST.get('ai_id')
        obj = Obj1Ai.objects.get(id=ai_id)
        obj.sts = 2
        obj.save()
        return render(request, 'mainapp/info_ai.html', content)

    if request.method == 'POST' and request.user.username == 'Cm002':
        Ai = Obj2Ai.objects.filter(idai=id).order_by('datain')
        obj_ai = Obj2Ai.objects.filter(idai=id, err__gt=0, sts=1)[:20][::-1]
        content = {
            'ai': Ai,
            'obj_ai': obj_ai,
            'items':values_2
        }
        ai_id = request.POST.get('ai_id')
        obj = Obj2Ai.objects.get(id=ai_id)
        obj.sts = 2
        obj.save()
        return render(request, 'mainapp/info_ai.html', content)

def test_page(request):
    if request.method == 'POST':
        cmn_id = request.POST.get('cmn_id')
        print(cmn_id)
    return render(request,'mainapp/test_page.html')

def archive(request,id):
    if request.user.username == 'Atl':
        if id == 1:
            Ai = Obj1Ai.objects.filter(err__gt=0).order_by('datain')
            paginator = Paginator(Ai,25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            content = {
                'name':'Таблица Obj1Ai',
                'obj_ai': Ai,
                'page_obj':page_obj,
                'ai_1_value':values_1,
                'ai_2_value':values_2
            }
            return render(request,'mainapp/archive.html',content)

        if id == 2:
            Ai = Obj2Ai.objects.filter(err__gt=0).order_by('datain')
            paginator = Paginator(Ai,25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            content = {
                'name':'Таблица Obj2Ai',
                'obj_ai': Ai,
                'page_obj':page_obj,
                'ai_1_value':values_1,
                'ai_2_value':values_2
            }
            return render(request,'mainapp/archive.html',content)

    if request.user.username == 'Cm001' and id == 1:
        Ai = Obj1Ai.objects.filter(err__gt=0).order_by('datain')
        paginator = Paginator(Ai,25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        content = {
            'name':'Таблица Obj1Ai',
            'ai': Ai,
            'page_obj': page_obj,
            'items':values_1
        }
        return render(request,'mainapp/archive.html',content)
    if request.user.username == 'Cm002' and id == 2:
        Ai = Obj2Ai.objects.filter(err__gt=0).order_by('datain')
        paginator = Paginator(Ai,25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        content = {
            'name':'Таблица Obj2Ai',
            'ai': Ai,
            'page_obj':page_obj,
            'items':values_2
        }
        return render(request,'mainapp/archive.html',content)


