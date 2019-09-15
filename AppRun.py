import HospitalDataProcessor
import time

class AppRun():
	def Main(self):
		app = HospitalDataProcessor.HospitalDataProcessor()
		app.loadData()
		app.HospitalByStateGovernmentMeaningfulUseEHR("TX")

time1 = time.time()
app = AppRun()
app.Main()
time2 = time.time()
print((time2-time1)*1000)