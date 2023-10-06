from school_management import id_name,branch_year,organising
import pandas as pd
id = []
name = []
per = []
branch = []
year = []
def data():
    ni = id_name.id()
    print(ni,type(ni))
    id.append(ni[0])
    name.append(ni[1])
    per.append(ni[2])
    byp = branch_year.by()
    branch.append(byp[0])
    year.append(byp[1])
def sorting(stu_num):
     organising.organise_data(stu_num,id,name,per,branch,year)
def display_data(num):
    print()
    for i in range(num):
        print('''Name: {}\tId: {}\tBranch: {}\t Year: {}\t percentage: {}%'''
              .format(name[i],id[i],branch[i],year[i],per[i]))
    d = pd.DataFrame(id,name,per,branch,year)
    print(d)
    # df_data = pd.DataFrame(columns=['id','name','year','branch','per'])
    # for i in range(len(id)):
    #     df_data.loc[i] = [id[i],name[i],year[i],branch[i],per[i]]
    # print(df_data)
        