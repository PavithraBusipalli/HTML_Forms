from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    if request.method == 'POST':
        cd = request.POST['tn']
        TO = Topic.objects.get_or_create(topicname=cd)[0]
        TO.save()
        QLTO = Topic.objects.all()
        return render(request,'display_topic.html',{'topic': QLTO})
    return render(request,'insert_topic.html')


def insert_Webpage(request):
    TO = Topic.objects.all()
    d = {'topics': TO}
    if request.method == 'POST':
        tn = request.POST['tn'] # tn is name attribute value
        na = request.POST['n']
        url = request.POST['url']
        em = request.POST['e']
        
        TO = Topic.objects.get(topicname=tn)
        QLWO = Webpage.objects.get_or_create(topicname=TO, name=na, url=url, email=em)[0]
        QLWO.save()
        QLWO = Webpage.objects.all()
        return render(request,'display_webpage.html',{'webpage': QLWO})
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    WO = Webpage.objects.all()
    d = {'webpage':WO}
    if request.method == 'POST':
        n = request.POST['n']
        au = request.POST['au']
        da = request.POST['da']
        NO = Webpage.objects.get(pk = n)
        QLWO = AccessRecord.objects.get_or_create(name=NO, author=au,date=da)[0]
        QLWO.save()
        QO = AccessRecord.objects.all()
        d1 = {'access' : QO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)







def multiple_webpages(request):
    TO = Topic.objects.all()
    d = {'topics': TO}
    if request.method == 'POST':
        # getlist for collecting multiple data of dropdown list as a list format
        GO = request.POST.getlist('tn')
        #GO = ['Python', 'Django', 'Java']
        # Creating empty query set using none() method
        EQWO = Webpage.objects.none()
        for to in GO:
            EQWO = EQWO | Webpage.objects.filter(topicname=to) # get() shouldn't be used here as it returns more than one obj(webpages may have more than one topic)
        d1 = { 'webpage' :EQWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'display_topic_multi_selection.html',d) 





def multiple_accessrecords(request):
    WO = Webpage.objects.all()
    d = {'webpage':WO}
    if request.method == 'POST':
        WO = request.POST.getlist('na')
        EQAO = AccessRecord.objects.none()
        for ao in WO:
            EQAO = EQAO | AccessRecord.objects.filter(name=ao)
        d2 = {'access': EQAO}
        return render(request, 'display_accessrecord.html',d2)

    return render(request,'display_webpage_multiselection.html',d)



def checkbox(request):
    TO = Topic.objects.all()
    # Shouldn't have same keys as they are used previously
    d = {'top':TO}
    return render(request,'checkbox.html',d)
    # Here Checkbox task is to select multiple options in topic to display webpages with the help checkboxes as we've already done with display topics to select multiple options 
    # Simply using the task of multiple_webpage at checkbox as we need to display multiple webpages of selected topcis. This all done by action attribute of form.
'''
        if request.method == 'POST':
        TD = request.POST.getlist('tn')
        QLWO = Webpage.objects.none()
        for to in TD:
            QLWO = QLWO | Webpage.objects.filter(topicname=to)
        d = {'webpage':QLWO}
        return render(request,'display_webpage.html',d)

'''


def checkbox_for_webpage(request):
    WO = Webpage.objects.all()
    d = {}






