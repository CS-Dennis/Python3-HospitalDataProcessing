class HospitalDataProcessor():
	dataLineSplit = []
	hospitals = []
	searchResults = []
	# reading and loading data
	def loadData(self):
		rawData = open("/Users/dennis/Desktop/python3/Hospital_General_Information.txt", "r")
		rawLines = rawData.readlines()
		rawData.close()

		
		for hospital in rawLines:
			dataLineSplit = hospital.split("\t")
			self.hospitals.append({"ProviderID": dataLineSplit[0], "HospitalName": dataLineSplit[1], "Address": dataLineSplit[2], "City": dataLineSplit[3], "State": dataLineSplit[4], "ZIPCode": dataLineSplit[5], "CountyName": dataLineSplit[6], "PhoneNumber": dataLineSplit[7], "HospitalType": dataLineSplit[8], "HospitalOwnership": dataLineSplit[9], "EmergencyServices": dataLineSplit[10], "MeetsCriteriaForMeaningfulUseOfEHRs": dataLineSplit[11], "HospitalOverallRating": dataLineSplit[12], "HospitalOverallRatingFootnote": dataLineSplit[13], "MortalityNationalComparison": dataLineSplit[14], "MortalityNationalComparisonFootnote": dataLineSplit[15], "SafetyOfCareNationalComparison": dataLineSplit[16], "SafetyOfCareNationalComparisonFootnote": dataLineSplit[17], "ReadmissionNationalComparison": dataLineSplit[18], "ReadmissionNationalComparisonFootnote": dataLineSplit[19], "PatientExperienceNationalComparison": dataLineSplit[20], "PatientExperienceNationalComparisonFootnote": dataLineSplit[21], "EffectivenessOfCareNationalComparison": dataLineSplit[22], "EffectivenessOfCareNationalComparisonFootnote": dataLineSplit[23], "TimelinessOfCareNationalComparison": dataLineSplit[24], "TimelinessOfCareNationalComparisonFootnote": dataLineSplit[25], "EfficientUseOfMedicalImagingNationalComparison": dataLineSplit[26], "EfficientUseOfMedicalImagingNationalComparisonFootnote": dataLineSplit[27], "Location": dataLineSplit[28]})
		
		self.hospitals.pop(0)

	# find all hospitals by state that are government owend with meaningful use of EHR and same as or above the national average of patient experience
	def HospitalByStateGovernmentMeaningfulUseEHR(self, state):
		for hospital in self.hospitals:
			if((hospital["State"]==state) and ("government" in str.lower(hospital["HospitalOwnership"])) and ("true" in str.lower(hospital["MeetsCriteriaForMeaningfulUseOfEHRs"])) and (("same" in str.lower(hospital["PatientExperienceNationalComparison"])) or ("above" in str.lower(hospital["PatientExperienceNationalComparison"])))):
				self.searchResults.append(hospital)


		writeData = open("/Users/dennis/Desktop/python3/new.txt", "w")
		writeData.writelines("Provider ID\tHospital Name\tAddress\tCity\tState\tZIP Code\tCounty Name\tPhone Number\tHospital Type\tHospital Ownership\tEmergency Services\tMeets criteria for meaningful use of EHRs\tHospital overall rating\tHospital overall rating footnote\tMortality national comparison\tMortality national comparison footnote\tSafety of care national comparison\tSafety of care national comparison footnote\tReadmission national comparison\tReadmission national comparison footnote\tPatient experience national comparison\tPatient experience national comparison footnote\tEffectiveness of care national comparison\tEffectiveness of care national comparison footnote\tTimeliness of care national comparison\tTimeliness of care national comparison footnote\tEfficient use of medical imaging national comparison\tEfficient use of medical imaging national comparison footnote\tLocation\n")
		
		for hospital in self.searchResults:
			print(hospital["HospitalName"]+", "+hospital["HospitalOwnership"]+", "+hospital["MeetsCriteriaForMeaningfulUseOfEHRs"]+", "+hospital["PatientExperienceNationalComparison"])
			writeData.writelines(hospital["ProviderID"]+"\t"+hospital["HospitalName"]+"\t"+hospital["Address"]+"\t"+hospital["City"]+"\t"+hospital["State"]+"\t"+hospital["ZIPCode"]+"\t"+hospital["CountyName"]+"\t"+hospital["PhoneNumber"]+"\t"+hospital["HospitalType"]+"\t"+hospital["HospitalOwnership"]+"\t"+hospital["EmergencyServices"]+"\t"+hospital["MeetsCriteriaForMeaningfulUseOfEHRs"]+"\t"+hospital["HospitalOverallRating"]+"\t"+hospital["HospitalOverallRatingFootnote"]+"\t"+hospital["MortalityNationalComparison"]+"\t"+hospital["MortalityNationalComparisonFootnote"]+"\t"+hospital["SafetyOfCareNationalComparison"]+"\t"+hospital["SafetyOfCareNationalComparisonFootnote"]+"\t"+hospital["ReadmissionNationalComparison"]+"\t"+hospital["ReadmissionNationalComparisonFootnote"]+"\t"+hospital["PatientExperienceNationalComparison"]+"\t"+hospital["PatientExperienceNationalComparisonFootnote"]+"\t"+hospital["EffectivenessOfCareNationalComparison"]+"\t"+hospital["EffectivenessOfCareNationalComparisonFootnote"]+"\t"+hospital["TimelinessOfCareNationalComparison"]+"\t"+hospital["TimelinessOfCareNationalComparisonFootnote"]+"\t"+hospital["EfficientUseOfMedicalImagingNationalComparison"]+"\t"+hospital["EfficientUseOfMedicalImagingNationalComparisonFootnote"]+"\t"+hospital["Location"])
		writeData.close()
			