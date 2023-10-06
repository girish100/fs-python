#organising student information according to their branch and year[i]
def organise_data(num,*data):
    import pandas as p
    id = data[0]
    name = data[1]
    per = data[2]
    branch = data[3]
    year = data[4]
    b2 = []
    n2 = []
    p2 = []
    y2 = []
    i2 = []
    a = 0
    print("======================REORGANISED DATA: BRANCH & YEAR WISE======================")
    for i in range(len(branch)):
        if branch[i].lower() == 'cse' or branch[i].lower() == 'computer science and engineering':
            if year[i] == 1 or year[i] == '1' or year[i] == 'one':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 2 or year[i] == '2' or year[i] == 'two':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 3 or year[i] == '3' or year[i] == 'three':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 4 or year[i] == '4' or year[i] == 'four':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
    for i in range(len(branch)):
        if branch[i].lower() == 'ece' or branch[i].lower() == 'electronics and communication engineering':
            if year[i] == 1 or year[i] == '1' or year[i] == 'one':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 2 or year[i] == '2' or year[i] == 'two':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 3 or year[i] == '3' or year[i] == 'three':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 4 or year[i] == '4' or year[i] == 'four':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
    for i in range(len(branch)):
        if branch[i].lower() == 'eee' or branch[i].lower() == 'electrical and electronic engineering':
            if year[i] == 1 or year[i] == '1' or year[i] == 'one':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 2 or year[i] == '2' or year[i] == 'two':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 3 or year[i] == '3' or year[i] == 'three':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 4 or year[i] == '4' or year[i] == 'four':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
    for i in range(len(branch)):
        if branch[i].lower() == 'mech' or branch[i].lower() == 'mechanical engineering' or branch[i].lower == 'mechanical':
            if year[i] == 1 or year[i] == '1' or year[i] == 'one':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 2 or year[i] == '2' or year[i] == 'two':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 3 or year[i] == '3' or year[i] == 'three':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 4 or year[i] == '4' or year[i] == 'four':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
    for i in range(len(branch)):
        if branch[i].lower() == 'civil' or branch[i].lower() == 'civil engineering':
            if year[i] == 1 or year[i] == '1' or year[i] == 'one':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 2 or year[i] == '2' or year[i] == 'two':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 3 or year[i] == '3' or year[i] == 'three':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
            elif year[i] == 4 or year[i] == '4' or year[i] == 'four':
                b2.insert(a,branch[i])
                n2.insert(a,name[i])
                i2.insert(a,id[i])
                p2.insert(a,per[i])
                y2.insert(a,year[i])
                a += 1
    print("==============CSE students: ==============\n")
    for i in range(len(b2)):
        if b2[i].lower() == 'cse' or b2[i].lower() == 'computer science and engineering':
            if y2[i] == 1 or y2[i] == '1' or y2[i] == 'one':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 2 or y2[i] == '2' or y2[i] == 'two':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 3 or y2[i] == '3' or y2[i] == 'three':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 4 or y2[i] == '4' or y2[i] == 'four':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
    print("===================ECE students: ==============\n")
    for i in range(len(b2)):
        if b2[i].lower() == 'ece' or b2[i].lower() == 'electronic and communication engineering':
            if y2[i] == 1 or y2[i] == '1' or y2[i] == 'one':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 2 or y2[i] == '2' or y2[i] == 'two':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 3 or y2[i] == '3' or y2[i] == 'three':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 4 or y2[i] == '4' or y2[i] == 'four':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
    print("=================EEE students: ===============\n")
    for i in range(len(b2)):
        if b2[i].lower() == 'eee' or b2[i].lower() == 'electrical and electronic engineering':
            if y2[i] == 1 or y2[i] == '1' or y2[i] == 'one':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 2 or y2[i] == '2' or y2[i] == 'two':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 3 or y2[i] == '3' or y2[i] == 'three':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 4 or y2[i] == '4' or y2[i] == 'four':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
    print("==================Mechanical Students: ===================\n")
    for i in range(len(b2)):
        if b2[i].lower() == 'mech' or b2[i].lower() == 'meachanical engineering' or b2[i] == 'mechanical':
            if y2[i] == 1 or y2[i] == '1' or y2[i] == 'one':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 2 or y2[i] == '2' or y2[i] == 'two':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 3 or y2[i] == '3' or y2[i] == 'three':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 4 or y2[i] == '4' or y2[i] == 'four':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
    print("=================Civil Engineering students: ==================\n")
    for i in range(len(b2)):
        if b2[i].lower() == 'civil' or b2[i].lower() == 'civil engineering':
            if y2[i] == 1 or y2[i] == '1' or y2[i] == 'one':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 2 or y2[i] == '2' or y2[i] == 'two':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 3 or y2[i] == '3' or y2[i] == 'three':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))
            elif y2[i] == 4 or y2[i] == '4' or y2[i] == 'four':
                print("""Branch: {}\tYear: {}\nName: {} | Id: {} | Percentage secured: {}\n"""
                      .format(b2[i].upper(),y2[i],n2[i],i2[i],p2[i]))