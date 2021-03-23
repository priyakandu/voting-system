nominee={"1":{"BJP":"RAM"},
"2":{"BSP":"SHYAM"},
"3":{"INC":"GITA"},
}
for n in nominee.keys():
    for k,v in nominee[n].items():
        print(n,k,v)

BJP=0
BSP=0
INC=0
voter_id_list=[234,346,454,789,987,780]
while True:
    if voter_id_list==[]:
        print("voting session expired")
        if BJP>BSP:
            if BJP>INC:
                print("BJP won by:",BJP)
        elif BSP>BJP:
            if BSP>INC:
                print("BSP won by:",BSP)
        else:
            print("INC won by:",INC)
        break
    else:
        voter_id=int(input("please enter your valid voter id>>>"))
        if voter_id in voter_id_list:
            option=str(input("select the number to choose for your leader>>>"))
            if option=="1":
                BJP=BJP+1
                voter_id_list.remove(voter_id)
            elif option=="2":
                BSP=BSP+1
                voter_id_list.remove(voter_id)
            elif option=="3":
                INC=INC+1
                voter_id_list.remove(voter_id)
            else:
                print("Please select valid option")
                continue
        else:
            print("You are not in voter id list or you are already voted..")