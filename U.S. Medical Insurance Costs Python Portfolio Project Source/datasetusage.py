
# # U.S. Medical Insurance Costs
# In this project, a **CSV** file with medical insurance costs will be investigated using Python fundamentals. 
# The goal with this project will be to analyze various attributes within **insurance.csv** to learn more about the 
# patient information in the file and gain insight into potential use cases for the dataset.

import csv

# STEP 1: creating the necessary lists for the data in insurance.csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []




def load_data(lst, file, column_name):
    with open(file) as data:
        dict = csv.DictReader(data)
        for row in dict:
            lst.append(row[column_name])
        return lst


load_data(ages, 'insurance.csv', 'age')
load_data(sexes, 'insurance.csv', 'sex')
load_data(bmis, 'insurance.csv', 'bmi')
load_data(num_children, 'insurance.csv', 'children')
load_data(smoker_statuses, 'insurance.csv', 'smoker')
load_data(regions, 'insurance.csv', 'region')
load_data(insurance_charges, 'insurance.csv', 'charges')

class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, 
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    def analyze_ages(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        return ("Average Patient Age: " + str(round(total_age/len(self.patients_ages), 2)) + " years")

    def analyze_sexes(self):
        females = 0
        males = 0
        for sex in self.patients_sexes:
            if sex == 'female':
                females += 1
            elif sex == 'male':
                males += 1
        print("Count for female: ", females)
        print("Count for male: ", males)

    def unique_regions(self): 
        unique_regions = [] 
        for region in self.patients_regions:  
            if region not in unique_regions: 
                unique_regions.append(region) 
        return unique_regions
 
    def average_charges(self): 
        total_charges = 0 
        for charge in self.patients_charges:
            total_charges += float(charge) 
        return ("Average Yearly Medical Insurance Charges: " +  
                str(round(total_charges/len(self.patients_charges), 2)) + " dollars.")
     
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary


# We can now analyse the dataset with the functions built:
patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

# patient_info.analyze_ages()
# patient_info.analyze_sexes()
# patient_info.unique_regions()
# patient_info.average_charges()
# patient_info.create_dictionary()