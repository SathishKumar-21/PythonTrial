from prescription import *
non_usr = []
for patient in patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        non_usr.append(patient)
for i in non_usr:
    patients.pop(i)
    print(f"the patient {i} is not using \"warfarin\", removing {i}  from the list")
print(patients.values())
