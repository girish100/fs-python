from hospita_code import co_doct,date_time,disease,pat_id_name
import pandas as pd
p_date = []
p_time = []
p_name = []
p_id = []
p_dis = []
p_gdis = []
p_cdis = []
p_cdox = []
def data():
    date = date_time.date()
    time = date_time.time()
    name = pat_id_name.pat_name()
    id = pat_id_name.pat_id()
    dis = disease.dise()
    cdis = disease.cdis()
    gdis = disease.gdis()
    cdox = co_doct.doctor()
    p_date.append(date)
    p_time.append(time)
    p_name.append(name)
    p_id.append(id)
    p_dis.append(dis)
    p_cdis.append(cdis)
    p_gdis.append(gdis)
    p_cdox.append(cdox)
def display_data(pat_num):
    print("\t\t\t=================PATIENT DATA=================")
    for i in range(pat_num):
        print('''Date:{}||\tTime:{}||\tName:{}||\tId:{}\nDisease:{}||\tCause of disease:{}||\tGenetic diseases:{}||\tconcultant doctor:{}||\n'''
              .format(p_date[i],p_time[i],p_name[i],p_id[i],p_dis[i],p_cdis[i],p_gdis[i],p_cdox[i]))
    df_data = pd.DataFrame(columns=['Date of admit','Time of admit','Patient name','Patient ID','Patient: disease','Cause of disease','Any Genetic disease/s','Consultant doctor'])
    for i in range(len(p_id)):
        df_data.loc[i] = [p_date[i],p_time[i],p_name[i],p_id[i],p_dis[i],p_cdis[i],p_gdis[i],p_cdox[i]]
    print(df_data)