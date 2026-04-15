from Pages.patient_records import PatientRecords
from Pages.a_login_page import LoginPage
import time

def test_smoke (hospital_page):
    login_page_obj = LoginPage (hospital_page)

    login_page_obj.login ("nurse_admin", "clinical2026")

    time.sleep (2)

