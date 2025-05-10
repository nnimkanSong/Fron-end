from django.shortcuts import render
from django.http.response import HttpResponse
from .models import GoogleSheetData
from .google_sheets import df

def sync_google_sheet_data():
    GoogleSheetData.objects.all().delete()
    for _, row in df.iterrows():
        GoogleSheetData.objects.create(
            D = row['D'],    
            email=row['email'],
            years = row['years'],
            student_id=row['student_id'],
            title=row['title'],
            name=row['name'],
            gender=row['gender'],
            phone=row['phone'],
            nickname=row['nickname'],
        )

# Create your views here.
sync_google_sheet_data()
def ce01s(request):
    ce01s = GoogleSheetData.objects.all()
    return render(request, 'app_students/ce01s.html',{'ce01s':ce01s})
def ce02s(request):
    sync_google_sheet_data()
    ce02s = GoogleSheetData.objects.all()
    return render(request, 'app_students/ce02s.html',{'ce02s':ce02s})
def ce03s(request):
    sync_google_sheet_data()
    ce03s = GoogleSheetData.objects.all()
    return render(request, 'app_students/ce03s.html',{'ce03s':ce03s})
def ce04s(request):
    sync_google_sheet_data()
    ce04s = GoogleSheetData.objects.all()
    return render(request, 'app_students/ce04s.html',{'ce04s':ce04s})
from django.shortcuts import render

def home(request):
    return render(request, 'TeamPro\app_general\templates\app_general\home.html')
