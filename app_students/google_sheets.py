import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# 1. ตั้งค่า Credentials
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

CREDS = ServiceAccountCredentials.from_json_keyfile_name("credentials/inbound-vim-453612-c7-547ef3cccba1.json", SCOPE)
CLIENT = gspread.authorize(CREDS)

# 2. เปิด Google Sheet ด้วย ID หรือชื่อไฟล์
SHEET_ID = "1vt693nmNfdUsTztuvA0EQJPkMRoemAMO2sJqNkW-ez8"
sheet = CLIENT.open_by_key(SHEET_ID).worksheet("students")  # เลือก Sheet1

# 3. ดึงข้อมูลเป็น DataFrame
data = sheet.get_all_records()
df = pd.DataFrame(data)
print(df)  # แสดงข้อมูลทั้งหมด
