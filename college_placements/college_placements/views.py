from django.http import HttpResponse
from django.shortcuts import render
import pickle
def index(request):
    return render(request,'index.html')
def result(request):
    model=pickle.load(open('college_placements.sav','rb'))
    Age=request.GET['Age']
    Gender=request.GET['Gender']
    Gender=Gender.lower()
    Stream=request.GET['Stream']
    Stream=Stream.lower()
    Internship=request.GET['Internship']
    CGPA=request.GET['CGPA']
    Hostel=request.GET['Hostel']
    HistoryOfBacklog=request.GET['HistoryOfBacklogs']
    s={'computer science':1,'information technology':4,'mechanical':5,'electronics and communication':3,
    'electrical':2,'civil':0}
    x={'m':1,'f':0}
    print(model.predict([[Age,x[Gender],s[Stream],Internship,CGPA,Hostel,HistoryOfBacklog]]))
    ans=model.predict([[Age,x[Gender],s[Stream],Internship,CGPA,Hostel,HistoryOfBacklog]])
    return render(request,'result.html',{'ans':ans[0]})