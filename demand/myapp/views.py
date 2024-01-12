from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import registration
from .models import login
from .models import woregi
from .models import entry
from .models import chosse
from.models import booking
from.models import ufeed

# Create your views here.
def chumma(request):
    return render(request, 'index.html')  # index


# def admin_view(request):
#     return render(request,'admin.html')
def regi(request):  # user_registration
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = int(request.POST['n4'])
        # e=request.POST['n5']
        # f=int(request.POST['n6'])
        data = registration.objects.create(name=a, email=b)
        data.save()
        data1 = login.objects.create(username=c, password=d, status=1)
        data1.save()
        return HttpResponse("<script>alert('created');window.location='b'</script>")
    else:
        return render(request, 'registration.html')


def worregi(request):  # worker_registration
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = int(request.POST['n4'])
        data = woregi.objects.create(name=a, email=b)
        data.save()
        data1 = login.objects.create(username=c, password=d, status=2)
        data1.save()
        return HttpResponse("<script>alert('created');window.location='f'</script>")
    else:
        return render(request, 'workregi.html')


def profile(request):
    if 'id' in request.session:
        return render(request, 'inerindex.html')
    elif 'lo' in request.session:
        return render(request, 'admin.html')
    elif 'wor' in request.session:
        return render(request, 'workerindex.html')
    else:
        return redirect(uslogin)


def uslogin(request):
    if request.method == 'POST':
        u = request.POST['n1']
        p = int(request.POST['n2'])
        try:
            data = login.objects.get(username=u)
            if data.status == 1:
                if data.password == p:
                    request.session['id'] = u
                    return redirect(profile)
                else:
                    return HttpResponse("<script>alert('invalid password');window.location='c'</script>")
            elif data.status == 0:
                if data.password == p:
                    request.session['lo'] = u
                    return redirect(profile)
                else:
                    return HttpResponse("<script>alert('invalid password');window.location='c'</script>")
            elif data.status == 2:
                if data.password == p:
                    request.session['wor'] = u
                    return redirect(profile)
                else:
                    return HttpResponse("<script>alert('invalid password');window.location='c'</script>")
        except Exception:
            return HttpResponse("<script>alert('invalid username');window.location='c'</script>")
    else:
        return render(request, "userlogin.html")


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(uslogin)
    elif 'lo' in request.session:
        request.session.flush()
        return redirect(uslogin)
    elif 'wor' in request.session:
        request.session.flush()
        return redirect(uslogin)


def worentry(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        e = int(request.POST['n5'])
        f = request.FILES['n6']
        g = request.POST['n7']
        data = entry.objects.create(name=a, job_name=b, DOB=c, salary=d, phone=e, licence=f, duration=g,
                                    action='pending', select='available', choose='empty')
        data.save()
        if data.action == 'pending':
            return HttpResponse("<script>alert('request is pending');window.location='g'</script>")
    else:
        return render(request, 'detailsentry.html')  # detailsentry


def display(request):
    if request.method == 'GET':
        data = entry.objects.all()
        return render(request, 'table1.html', {'r': data})


def deletew(request):  # deleting worker
    if request.method == 'POST':
        r = request.POST['n1']
        d = entry.objects.filter(id=r)
        d.delete()
        return HttpResponse("<script>alert('deleted');window.location='i'</script>")
    else:
        return render(request, 'table1.html')


def acceptw(request):  # accept worker
    if request.method == 'POST':
        r = request.POST['n1']
        d = entry.objects.filter(id=r)
        d.update(action='confirm')
        return HttpResponse("accepted")
    else:
        return render(request, 'table1.html')


def display2(request):
    if request.method == 'GET':
        data = entry.objects.filter(select='available',action='confirm')
        return render(request, 'table2.html', {'r': data})
    else:
        return render(request, 'inerindex.html')


def userview(request):
    if request.method == 'GET':
        data = registration.objects.all()
        return render(request, 'table3.html', {'r': data})


def msg1(request):         #worker seeing whether his request is accepted or not
    if request.method == 'GET':
        x = request.session['wor']
        d = entry.objects.get(name=x)
        if d.action == 'confirm':
            a = "Accepted"
        else:
            a = "please wait!!!!"
        return render(request, 'msg1.html', {'r': a})
    else:
        return render(request, 'workerindex.html')


# def selectw(request):  # selecting worker #ini ith venda
#     if request.method == 'POST':
#         r = request.POST['n1']
#         d = entry.objects.filter(id=r)
#         d.update(choose='selected')
#         d.update(select='unavailable')
#         return HttpResponse("wrong")
#     else:
#         return render(request, 'table2.html')


def display3(request):         #admin viewing the selected worker
    if request.method == 'GET':
        d = entry.objects.filter(choose='selected')
        return render(request, 'table4.html', {'r': d})
    else:
        return render(request, 'admin.html')


def msg2(request):
    if request.method == 'GET':
        x = request.session['wor']
        d = entry.objects.get(name=x)
        if d.choose == 'selected':
            a = "your job is now available"
        else:
            a = "please wait"
        return render(request, 'msg2.html', {'r': a})
    else:
        return render(request, 'workerindex.html')



def choose_worker(request,id):
    request.session['id']=id
    return redirect(send_request)


def send_request(request,wor):
        user_id=request.session['id']
        cr=chosse.objects.create(worker_name=wor,user_name=user_id)
        # data = chosse.objects.filter(worker_name=wor)
        d=entry.objects.filter(name=wor)
        d.update(select='unavailable')
        d.update(choose='selected')
        return HttpResponse("<script>alert('please wait for the response');window.location='/select/'</script>")


def view_request(request):
    if request.method=='GET':
        x=request.session['wor']
        data=chosse.objects.filter(worker_name=x)
        return render(request,'userv.html',{'t':data})
    else:
        return render(request,'workerindex.html')


def accept_request(request):  #worker accepting the user
    if request.method == 'GET':
        x = request.session['id']
        d = chosse.objects.filter(user_name=x)
        return HttpResponse('please contact with me for further!!!')
    else:
        return render(request,'inerindex.html')


def reject_request(request):    #worker rejecting the user
    if request.method == 'GET':
        x=request.session['id']
        d = chosse.objects.filter(user_name=x)
        return HttpResponse('sorry wont available')
    else:
        return render(request,'inerindex.html')


def pay_start(request,wor):
     request.session['wore']=wor
     return redirect(payment)


def payment(request):#payment view
    if request.method=='POST':
        a=int(request.POST['n1'])
        i=request.session['wore']
        da=entry.objects.get(name=i)
        if da.duration=='Temporary':
            amount=da.salary*a
        elif da.duration=='Permanent':
            amount=da.salary*a
        else:
            amount=0*a
        data=booking.objects.create(no_of_working_days=a,total_amount=amount)  #'Permanent'
        data.save()
        d=booking.objects.all()
        return render(request,'view_pay_details.html',{'t':d})
    else:
        return render(request,'book.html')
        # return HttpResponse('sorry')




def customer_pay_view(request):  # selecting worker for payment
    if request.method=='GET':
        x=request.session['id']
        data=chosse.objects.filter(user_name=x)
        return render(request,'payment_view.html',{'t':data})
    else:
        return render(request,'inerindex.html')


def to_the_payment(request):
    return render(request,'book.html')


def feedback(request):
    if request.method=='POST':
        a=request.POST['n1']
        b = request.POST['n2']
        data=ufeed.objects.create(wname=a,feed=b)
        data.save()
        c=entry.objects.all()
        c.update(select='available')
        return HttpResponse("<script>alert('feedback has been sended');window.location='feed'</script>")
    else:
        return render(request,'feedba.html')

def adfeed(request):
    if request.method=='GET':
        data=ufeed.objects.all()
        return render(request,'afeed.html',{'r':data})

