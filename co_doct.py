#consultant doctor
from hospita_code import pat_id_name
def doctor():
    doctor_data = {1:'shyam',2:'charan',3:'venkat_sai',4:'nithin',5:'manideep',6:'tharun'}
    pat_doc = []
    print("Enter your consultant doctor: ")
    for i,j in doctor_data.items():
        print(i,":",j)
    c_doc = int(input("number: "))
    for x in doctor_data.keys():
        if c_doc == x:
            y = doctor_data.get(c_doc)
            pat_doc.append(y)
    return pat_doc