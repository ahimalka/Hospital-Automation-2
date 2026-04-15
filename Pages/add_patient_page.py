class AddPatientPage:
    def __init__(self, page):
        self.page = page

    def add_patient (self):
        self.page.locator("#addPatientBtn").click()
        self.page.locator("#patientId").fill ()
        self.page.locator("#patientName")
        self.page.locator("#patientCategory")
        self.page.locator("#patientStatus")
        self.page.locator("#patientDoctor")
        self.page.locator("#patientWard")
        self.page.locator("#submitPatientBtn")
        self.page.locator("#searchInput")
