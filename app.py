#add
#show
#search_id
#serach_skill
#edit
#delete
#report
#exit
import json
import os

# path = r"karvand.json"
jsonpath = r"karvand.json"
dirpath = r"data"
path = os.path.join(dirpath,jsonpath)

# bootcamp = input("bootcamp title : ")
# year = input("bootcamp year : ")
# karvand_inp ={"bootcamp" : {"title": bootcamp , "year" : year},"karvands":[]}

def pathfinder():
    jsonpath = r"karvand.json"
    dirpath = r"data"
    dirr = os.path.join(dirpath,jsonpath)
    
    if not os.path.exists(dirr):
        if not os.path.exists(dirpath):
                os.makedirs(dirpath)
        with open(dirr,'w') as file:
            jdic = {"bootcamp" : {"title": "karvand python" , "year" : 2026},"karvands":[]}
            json.dump(jdic,file)

    elif os.path.exists(dirr):

        with open(dirr,'r') as file:
            try:
                karvandss = json.load(file)
                if karvandss is None:
                    karvandss = jsonfix(dirr)
                    print("json file was empty,it's now fixed,with compatible format")
                    return karvandss
            
                if len(karvandss["karvands"] )== 0:
                    print("no karvand currently in the file,please press 1-add to add some.")
            except KeyError:
                karvandss = jsonfix(dirr)
            except json.decoder.JSONDecodeError:
                karvandss = jsonfix(dirr)
            
            return karvandss

def jsonfix(dirr):
        with open(dirr,'w') as file:
            jdic = {"bootcamp" : {"title": "karvand python" , "year" : 2026},"karvands":[]}
            json.dump(jdic,file)
            return jdic

karvand_inp = pathfinder()

while True:
    try:
        karvand = {
            "id" : "", "fullname" : "" , "email" : "" , "city" : "" ,
            "education" : { "degree" : "" , "field" : ""  
            }  ,
                "skills": 
                        []
                    }
        command = int(input("1-add , 2-show , 3-search_id , 4-search_skill , 5-edit , 6-delete , 7-report , 8-exit : \n"))

        if command == 1:
            id_count = 0
            try:
                for i in karvand_inp["karvands"]:
                    if i["id"] > id_count:
                        id_count  = i["id"]
            except TypeError:
                id_count = 0        
            id_count += 1
            
            karvand["fullname"] = input("Name : ")
            karvand["email"] = input("email : ")
            karvand["city"] = input("City : ")
            karvand["education"]["degree"] = input("degree : ")
            karvand["education"]["field"] = input("field : ")

            print("skills,level,score, 0 if none left : ")
            while True : 
        
        
                skill_name = input("skill name : ")
                if skill_name != "0":
                    skill_lvl  = input("level : ")
                    while True:
                        try:
                            score  = int(input("score : "))
                            if (score>100 or score <0):
                                print("score should be between 0-100 : ")
                                
                            else:
                                break
                        except ValueError:
                            print("score should be a number : ")


                    karvand["skills"].append({"name" : skill_name , "level" : skill_lvl ,"score" : score})
                else:
                    break

            karvand["id"] = id_count

            karvand_inp["karvands"].append(karvand)
            
            with open(path , "w")   as users:
                json.dump(karvand_inp,users,indent = 4)
                
                

                
           
        elif command == 2: #show
            with open(path,'r') as file:
                karvs = json.load(file)
                if len(karvs["karvands"]) == 0:
                    print("your have zero karvands!") 
                else:
                    for k in karvs["karvands"]:

                        print(k)

        elif command ==3: #search_id
            while True:
                try:
                    id_inp = int(input("id to serach : "))
                    break
                except ValueError:
                    print("id should be a valid number!")
            with open(path,'r') as file:
                karvs = json.load(file)
                truefalse = 0
                for karv in karvs["karvands"]:
                    
                    if id_inp == karv["id"]:
                        truefalse += 1
                        print(karv)
                
                if truefalse == 0:
                    print(f"id:{id_inp} does not exist!")

        elif command == 4: 
            skill_inp = input("skill : ")
            skill_list = []
            with open(path,'r') as file:
                karvs = json.load(file)
                for karv in karvs["karvands"]:
                    for sk in karv["skills"]:
                
                        if skill_inp  == sk["name"]  :
                            skill_list.append(karv["fullname"])
            if len(skill_list) != 0 :
                print(skill_list)


        elif command == 5: #edit
            ed_id = int(input("enter karvands id to edit : ")) #fname try except id

            with open(path,'r') as file:
                karvs = json.load(file)
                for karv,i in zip(karvs["karvands"],range(len(karvs["karvands"]))):
                    if ed_id == karv["id"] :
                        
                        for k,v in karv.items():
                            if k != "id" and k != "fullname" and k != "skills":    
                                
                                if  k != "education":
                                    edit_input = input(f"new {k}, if no change enter 'pass' :")
                                    if edit_input != 'pass':    
                                        
                                        karvs["karvands"][i][k] = edit_input

                                elif  k == "education":
                                    for edu_items in karvs["karvands"][i]["education"].keys() : 
                                        edit_input = input(f"new {edu_items}, if no change enter 'pass' :")
                                        if edit_input != 'pass': 
                                            karvs["karvands"][i]["education"][edu_items] = edit_input
                        print(f"karvand with id:{ed_id} has been succesfuly updated")
                        with open(path,'w') as users:
                            karvs = json.dump(karvs,users,indent = 4)
                        break



        elif command == 6: #del
            with open(path,'r') as file:
                karvs = json.load(file)#try except
                try:
                    del_inp = int(input("enter karvands id : "))
                except ValueError:
                    del_inp = int(input("enter a valid id : "))
                counter = 0
                for i in range(len(karvs["karvands"])):
                    if del_inp == karvs["karvands"][i]["id"] : 
                        counter += 1
                        del karvs["karvands"][i]
                        print("karvand has been succesfuly deleted.")
                        if len(karvs["karvands"]) == 0:
                            print("you have zero karvands now!") 
                        with open(path,'w') as users:
                            json.dump(karvs,users,indent = 4)  
                            
                        break
                if counter == 0 :
                    print(f"no karvand with {del_inp} exists!")
                
                
        elif command == 7 : #report #karvcount,skillcount,avgskillscore,citylist,uniqueskills
            #karvcount
            karvand_count = 0
            skill_count = 0
            sum_skill_score = 0
            cities = []
            uni_skills = []

            with open(path,'r') as file:
                karvs = json.load(file)
                karvand_count = len(karvs["karvands"])

                for karv in karvs["karvands"]:
                    if karv["city"] not in cities:
                        cities.append(karv["city"])
                    for skls in karv["skills"]:
                        sum_skill_score += skls["score"]
                        skill_count += 1
                        if skls["name"] not in uni_skills:
                            uni_skills.append(skls["name"])
                avg_skill_score = sum_skill_score/skill_count
                print(f"total karvands : {karvand_count}")
                print(f"total skills : {skill_count}")
                print(f"avg skill score : {avg_skill_score}")
                print(f"cities : {cities}")    
                print(f"unique skills : {uni_skills}")
                with open(path,'w') as rep:
                    json.dump({"total karvands" : karvand_count,"total skills" : skill_count,"avg skill score" : avg_skill_score
                            ,"cities" : cities, "unique skills" : uni_skills},rep,indent = 4)
                                
        elif command == 8 :
            break
    except json.decoder.JSONDecodeError:
        print("json file was incompatible,it has now been reset to the default format")
        karvand_inp =  jsonfix(path)