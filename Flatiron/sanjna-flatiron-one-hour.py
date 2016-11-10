#Sanjna Verma Flatiron Health Assessment
#Time duration: 1 hour
import csv
from datetime import date

def days_between(diag_date, treatment_date):
    diagnosis = date(int(diag_date[0]), int(diag_date[1]), int(diag_date[2]))
    start_treatment = date(int(treatment_date[0]), int(treatment_date[1]), int(treatment_date[2]))
    return abs((diagnosis - start_treatment).days)

def question2b(patient_treat_arr, patient_diag_dict): # Do any patients start treatment before being diagnosed?
    treatment_first = 0
    diagnosis_first = 0

    for row in range(len(patient_treat_arr)):
        patient_id = patient_treat_arr[row][0]
        treatment_date = patient_treat_arr[row][1].split("-")

        patient_diag_dict_id = patient_diag_dict.get(patient_id)
        diag_date = patient_diag_dict_id[0].split("-")

        if not (avg_length_of_time_to_start_treatment.get(patient_id)):
            diagnosis = date(int(diag_date[0]), int(diag_date[1]), int(diag_date[2]))
            start_treatment = date(int(treatment_date[0]), int(treatment_date[1]), int(treatment_date[2]))
            if(diag_date > treatment_date): #"2014-06-24" > "2010-06-23"
                #("Diagnosis came after treatment")
                treatment_first+=1
            else:
                #("Treatment came after diagnosis")
                diagnosis+=1

    if(treatment_first>0):
        return("There were some patients started treatment before being diagnosed")
    else:
        return("Patients started treatment after being diagnosed")


patient_diag_dict = {}  # key is the patient id, and the value is a list of the date, the diagnosis code, and the cancer type
counter_diag = 0  # start at negative one because we don't want to count the first line
patient_treat_arr = []
counter_treat = 0  # start at negative one because we don't want to count the first line

with open('Patient_Diagnosis.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        l = ','.join(row)  # for the sake of formating
        l_split = l.split(',')
        if "Patient_ID" not in l_split[0]:  # do not want to account for first row
            counter_diag += 1
            patient_diag_dict.update({l_split[0]: l_split[1:]})

with open('Patient_Treatment.csv', 'rb') as csvfile2:
    reader = csv.reader(csvfile2, delimiter=' ', quotechar='|')
    for row in reader:
        l = ','.join(row)  # for the sake of formating
        l_split = l.split(',')

        if "Patient_ID" not in l_split[0]:
            counter_treat += 1
            patient_treat_arr.append(l_split)

avg_length_of_time_to_start_treatment = {}  # key is the patient id, value is the first day x to start treatment for that patient
for row in range(len(patient_treat_arr)):
    patient_id = patient_treat_arr[row][0]
    treatment_date = patient_treat_arr[row][1].split("-")

    patient_diag_dict_id = patient_diag_dict.get(patient_id)
    diag_date = patient_diag_dict_id[0].split("-")

    if not (avg_length_of_time_to_start_treatment.get(patient_id)):
        avg_length_of_time_to_start_treatment[patient_id] = days_between(diag_date, treatment_date)

avg_length_of_time_to_start_treatment_after_being_diagnose = sum(
    avg_length_of_time_to_start_treatment.values()) / len(avg_length_of_time_to_start_treatment)

# 1.  How many patients does the clinic have for each cancer diagnosis?
print("How many patients does the clinic have for each cancer diagnosis?\n" + str(counter_diag))

# 2.  How long after being diagnosed does it take for a patient to start treatment?
print("How long after being diagnosed does it take for a patient to start treatment?\nOn average, it takes " + str(
    avg_length_of_time_to_start_treatment_after_being_diagnose) + " days")

# Do any patients start treatment before being diagnosed?
print(question2b(patient_treat_arr, patient_diag_dict))

# 3.  Is there a difference between Drug 201 and Drug 202 in terms of length of treatment?


