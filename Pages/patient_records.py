class PatientRecords:
    def __init__ (self, page):
        self.page = page

    def logout (self):
        self.driver.locator (".Patient Records").click ()

    def patient_search (self, search_in_patient):
        self.page.locator ("#searchInput").fill (search_in_patient)

    def patient_high_priority (self):
        self.page.locator ("#filterBtn").click()

    def add_patient (self):
        self.page.locator ("#addPatientBtn").click()

    def delete_patient (self):
        self.page.locator (".btn-delete").click()