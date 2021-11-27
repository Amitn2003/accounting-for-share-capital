# Accounting on issue of share 
import time
print("Welcome to \nIssue of share!!!!")


showing_share = int(input("Enter total  issued share ammount : "))

# print(f"Total share is {showing_share}")

total_payable = int(input("Enter total payable ammount : "))

real_share = int(input("Receved received applications ammounts : ") or showing_share)

print(f"\n \nIssued shares are {showing_share} \nPayable ammount {total_payable} \nTotal applications received {real_share}. \n")


# if showing_share >= real_share:
#     print("Everything is ok!")

# else:
#     print("Check your input!!!!!!")
#     time.sleep(8)





app_money = int(input("Application money : "))
allotment_money = int(input("Allotment money : "))
firstcall = int(input("1st call money : "))
finalcall = int(input("Final call money : "))



advance = 0
advance = int(input("Advance control ? [Type 1 or 0(default 0)} :") or "0")









# Receving applications 
def share_app():
    receved_money = real_share * app_money
    print(f"\n \n \n \nBank A/C ....... Dr.            {receved_money}")
    print(f"To Share Application A/C                  {receved_money}")
    return receved_money


# Refunding if receving application ammount is gretter than issued application
def share_app_refund():
    refund_share_no = real_share - showing_share
    refund = refund_share_no * app_money
    print(f"\n  \nShare Application A/C ...... Dr.       {refund}")
    print(f"To Back A/C ......... Dr.                   {refund}")
    return refund

# Share Application money transfurring to Share Capital A/C
def share_app_cap():
    transferred_application = real_share * app_money
    print(f"\n \nShare Application A/C ...... Dr.       {transferred_application}")
    print(f"To Share Capital A/C                     {transferred_application}")
    return transferred_application




# Share Allotment money demanding
def share_all():
    due_allotment = real_share * allotment_money
    print(f"\n \nShare Allotment A/C ....... Dr.       {due_allotment}")
    print(f"To Share Capital A/C                     {due_allotment}")
    return due_allotment


# Share Allotment money receveing from bank
def share_all_cap():
    transferred_allotment = real_share * allotment_money
    print(f"\n \nBank A/C ........ Dr.              {transferred_allotment}")
    print(f"To Share Allotment A/                   {transferred_allotment}")
    return transferred_allotment



# Share 1stcall monney demanding
def first_call():
    due_first = real_share * firstcall
    print(f"\n \nShare 1st call A/C .... ... Dr.      {due_first}")
    print(f"To Share Capital A/C                     {due_first}")
    return  due_first 



# Share 1stcall monney receveing from bank
def first_call_cap():
    transferred_first = real_share * firstcall
    print(f"\n \nBank A/C ......... Dr.              {transferred_first}")
    print(f"To Share 1st call A/C                   {transferred_first}")
    return transferred_first



# Share Final call monney demanding
def final_call():
    due_final = real_share * finalcall
    print(f"\n \nShare Final call A/C ...... Dr.      {due_final}")
    print(f"To Share Capital A/C                     {due_final}")
    return due_final



# Share 1stcall monney receveing from bank
def final_call_cap():
    transferred_final = real_share * finalcall
    print(f"\n \nBank A/C ......... Dr.               {transferred_final}")
    print(f"To Share Final call A/C                 {transferred_final}")
    return transferred_final


# Share allotment including premium demanding
def share_all_premium():
    all_pre = allotment_money + premium
    total_all = real_share * all_pre
    total_cap = real_share * allotment_money
    only_premium = real_share * premium
    print(f"\n \nShare Allotment A/C ....... Dr.          {total_all}")
    print(f"To Share Capital A/C                        {total_cap}")
    print(f"To Security Premium A/C                     {only_premium}")
    return (total_all, total_cap, only_premium)


# Share allotment money including premium receving
def share_all_premium_cap():
    all_pre = allotment_money + premium
    all_premium = real_share * all_pre
    print(f"\n \nBank A/C ........ Dr.              {all_premium}")
    print(f"To Share Allotment A/                   {all_premium}")
    return all_premium



def first_final():
    first_final = real_share * finalcall
    print(f"\n \nShare First & Final call A/C ...... Dr.      {first_final}")
    print(f"To Share Capital A/C                     {first_final}")
    return first_final



def more_among_fst_fnl_call():
    if firstcall < finalcall:
        return finalcall
    elif firstcall > finalcall:
        return firstcall


























# print(advance)
if advance == 1:
    print("You are now in a advance version!!")
    print("You have to give more details about shares...")
    # Checking premium on allotment
    premium = int(input("Enter the premium ammount : ") or "0")
    print(f"Total payable including premium is {premium + total_payable} .")
    time.sleep(1)
    # final_call_arrear = int(input("Final call arrear shares:") or "0")
    
    premium_ammount = int(premium)
    share_app()
    time.sleep(1)
    if showing_share < real_share:
        share_app_refund()
        real_share = showing_share # Share will calculate on issuing share
        time.sleep(1)
    share_app_cap()

    time.sleep(1)


    if premium_ammount != 0:
        share_all_premium()
        time.sleep(1)
        share_all_premium_cap()
        time.sleep(1)
    elif premium_ammount == 0:
        share_all()
        time.sleep(1)
        share_all_cap()
        time.sleep(1)
    else:
        print("Premium can't be less than 0 !!")
        print(exit())

    

    if firstcall == 0 or finalcall == 0:
    # Only one call is called among first cal & final call
        print(f"\n \nShare  First & Final call A/C ...... Dr.      {real_share * more_among_fst_fnl_call()}")
        print(f"To Share Capital A/C                     {real_share * more_among_fst_fnl_call()}")

        print(f"\n \nBank A/C ......... Dr.               {real_share * more_among_fst_fnl_call()}")
        print(f"To Share First & Final call A/C                 {real_share * more_among_fst_fnl_call()}")


    else:
        first_call()
        time.sleep(1)
        first_call_cap()
        time.sleep(1)
        final_call()
        time.sleep(1)
        final_call_cap()
        time.sleep(1)




      # if finalcall > 0:
      #   final_call()
      #   time.sleep(1)
     #   first_call_cap()
      
      
      

    #    print("\nThank you for using Issue of share tool...")
    #     time.sleep(2)
    # print("Exiting...")
    #     time.sleep(1)

    #    print(exit())
elif advance == 0:
    print("You are using normal version.")
    share_app()


    time.sleep(1)
    if showing_share < real_share:
        share_app_refund()
        real_share = showing_share # Share will calculate on issuing share
        time.sleep(1)
    share_app_cap()

    time.sleep(1)

    share_all()
    time.sleep(1)

    share_all_cap()
    time.sleep(1)

    first_call()
    time.sleep(1)

    first_call_cap()
    time.sleep(1)

    # if finalcall > 0:
    #   final_call()
    #   time.sleep(1)
    #   first_call_cap()
    final_call()
    time.sleep(1)
    final_call_cap()
    time.sleep(1)








    



else:
    print(f"{advance} is invalid input!! \n")






print("\nThank you for using Issue of share tool...")
time.sleep(2)
print("Exiting...")
time.sleep(1)

print(exit())




















# share_app()


# time.sleep(1)
# if showing_share < real_share:
#     share_app_refund()
#     real_share = showing_share # Share will calculate on issuing share
#     time.sleep(1)



# share_app_cap()

# time.sleep(1)

# share_all()
# time.sleep(1)

# share_all_cap()
# time.sleep(1)

# first_call()
# time.sleep(1)

# first_call_cap()
# time.sleep(1)

# if finalcall > 0:
#     final_call()
#     time.sleep(1)
#     first_call_cap()
# time.sleep(1)


# print("\nThank you for using Issue of share tool...")
# time.sleep(2)
# print("Exiting...")
# time.sleep(1)

# print(exit())









