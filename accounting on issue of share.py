# Accounting on issue of share 
import time
print("Welcome to \nIssue of share!!!!")


showing_share = int(input("Enter total  issued share ammount : "))

# print(f"Total share is {showing_share}")

total_payable = int(input("Enter total payable ammount : "))

real_share = int(input("Receved received applications ammounts : "))

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
    print(f"\n \n \n \nBank A/C ....... Dr.            {real_share * app_money}")
    print(f"To Share Application A/C                  {real_share * app_money}")


# Refunding if receving application ammount is gretter than issued application
def share_app_refund():
    refund_share_no = real_share - showing_share
    refund = refund_share_no * app_money
    print(f"\n  \nShare Application A/C ...... Dr.       {refund}")
    print(f"To Back A/C ......... Dr.                   {refund}")

# Share Application money transfurring to Share Capital A/C
def share_app_cap():
    print(f"\n \nShare Application A/C ...... Dr.       {real_share * app_money}")
    print(f"To Share Capital A/C                     {real_share * app_money}")




# Share Allotment money demanding
def share_all():
    print(f"\n \nShare Allotment A/C ....... Dr.       {real_share * allotment_money}")
    print(f"To Share Capital A/C                     {real_share * allotment_money}")


# Share Allotment money receveing from bank
def share_all_cap():
    print(f"\n \nBank A/C ........ Dr.              {real_share * allotment_money}")
    print(f"To Share Allotment A/                   {real_share * allotment_money}")



# Share 1stcall monney demanding
def first_call():
    print(f"\n \nShare 1st call A/C .... ... Dr.      {real_share * firstcall}")
    print(f"To Share Capital A/C                     {real_share * firstcall}")




# Share 1stcall monney receveing from bank
def first_call_cap():
    print(f"\n \nBank A/C ......... Dr.              {real_share * firstcall}")
    print(f"To Share 1st call A/C                   {real_share * firstcall}")



# Share Final call monney demanding
def final_call():
    print(f"\n \nShare Final call A/C ...... Dr.      {real_share * finalcall}")
    print(f"To Share Capital A/C                     {real_share * finalcall}")



# Share 1stcall monney receveing from bank
def final_call_cap():
    # final_arrear = finalcall - final_call_arrear
    # final_arr = real_share * finalcall
    # final_arr = final_arr - (final_call_arrear * finalcall)
    print(f"\n \nBank A/C ......... Dr.               {real_share * finalcall}")
    # print(f"Calls in Arrear A/C...... Dr.            {final_call_arrear * finalcall}")
    print(f"To Share Final call A/C                 {real_share * finalcall}")


# Share allotment including premium demanding
def share_all_premium():
    all_pre = allotment_money + premium
    all_premium = real_share * all_pre
    print(f"\n \nShare Allotment A/C ....... Dr.          {all_premium}")
    print(f"To Share Capital A/C                        {real_share * allotment_money}")
    print(f"To Security Premium A/C                     {real_share * premium}")


# Share allotment money including premium receving
def share_all_premium_cap():
    all_pre = allotment_money + premium
    all_premium = real_share * all_pre
    
    print(f"\n \nBank A/C ........ Dr.              {all_premium}")
    print(f"To Share Allotment A/                   {all_premium}")



def first_final():
    print(f"\n \nShare First & Final call A/C ...... Dr.      {real_share * finalcall}")
    print(f"To Share Capital A/C                     {real_share * finalcall}")



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









