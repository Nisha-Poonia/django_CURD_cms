from multiprocessing import context
from django.shortcuts import render
from c_m_s.models import *
from django.http import HttpResponse
# Create your views here.

def view_customer(request):
    if request.method=='GET':
        resp=render(request,'c_m_s/index.html')
        return resp
    
    elif request.method=='POST':
        if 'btnadd' in request.POST:
            cmp=Customer()
            cmp.name=request.POST.get('textname','NA')
            cmp.age=request.POST.get('textage',0)
            cmp.mobileno=request.POST.get('textmob',0)
            cmp.email=request.POST.get('textemail','NA')
            cmp.city=request.POST.get('textcity','NA')
            cmp.save()
            resp=HttpResponse("<h1>Data Added SuccessFully!! Whose ID is " + str(cmp.id)+"</h1>")
            return resp
        # elif 'btnsearch' in request.POST:
        #     cmpid=int(request.POST.get('textid',0))
        #     cmp=request.objects.get(id=cmpid)  
        #     d1={'cmp':cmp}  
        #     resp=render(request,'c_m_s/index.html',context=d1)
        #     return resp

        elif 'btnsearch' in request.POST:
            cmpid=int(request.POST.get('textid',0))
            print(cmpid)
            cmp=Customer.objects.get(id=cmpid)
            d1={'cmp':cmp}
            resp=render(request,'c_m_s/index.html',context=d1)
            return resp 
        elif 'btnupdate' in request.POST:
            cmp=Customer()
            cmp.id=int(request.POST.get('textid',0))
            if Customer.objects.filter(id=cmp.id).exists():
                cmp.name=request.POST.get('textname','NA')
                cmp.age=request.POST.get('textage','NA')
                cmp.mobileno=request.POST.get('textmob',0)
                cmp.email=request.POST.get('textemail','NA')
                cmp.city=request.POST.get('textcity','NA')
                cmp.save()
                resp=HttpResponse("<h1>Data Updated SuccessFully!! Whose ID is "+str(cmp.id)+"</h1>")
                return resp
        elif 'btndelete' in request.POST:
            cmp=Customer()
            cmp.id=int(request.POST.get('textid','NA'))
            if Customer.objects.filter(id=cmp.id).delete():
                resp=HttpResponse("<h1>Data Deleted SuccessFully!! Whose ID is "+str(cmp.id)+"</h1>")
                return resp
        
        elif 'btnshow' in request.POST:
            allcmp=Customer.objects.all()
            d1={'allcmp':allcmp}
            resp=render(request,'c_m_s/index.html',context=d1)
            return resp






        
