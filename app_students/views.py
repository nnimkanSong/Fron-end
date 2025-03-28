from django.shortcuts import render
from django.http.response import HttpResponse
from .models import GoogleSheetData
from .google_sheets import df

def sync_google_sheet_data():
    GoogleSheetData.objects.all().delete()
    for _, row in df.iterrows():
        birthdate = row.get('Birthdate', '')  # รับค่าจาก Google Sheet
        
        # ✅ ตรวจสอบว่า birthdate ไม่ใช่ "0000-00-00"
        if birthdate == "0000-00-00":
            birthdate = None  # หรือสามารถกำหนดค่าเป็นค่าอื่น เช่น '2000-01-01'

        # ✅ ตรวจสอบรูปแบบวันที่ให้ถูกต้องก่อนบันทึก
        if birthdate:
            try:
                birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()  
            except ValueError:
                birthdate = None  # ถ้ารูปแบบผิด ให้กำหนดเป็น None

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
def ce01s(request):
    sync_google_sheet_data()
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
