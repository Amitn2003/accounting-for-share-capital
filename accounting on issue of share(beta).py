# Accounting on issue of share 
import time
print("Welcome to \nIssue of share!!!!")


showing_share = int(input("Enter total  issued share ammount : "))

# print(f"Total share is {showing_share}")

total_payable = int(input("Enter total payable ammount : "))

real_share = int(input("Receved received applications ammounts : "))

# print(f"\n \nIssued shares are {showing_share} \nPayable ammount {total_payable} \nTotal applications received {real_share}. \n")







app_money = int(input("Application money : "))
allotment_money = int(input("Allotment money : "))
firstcall = int(input("1st call money : "))
finalcall = int(input("Final call money : ") or "0")



advance = 0
advance = int(input("Advance control ? [Type 1 or 0(default 0)} :") or "0")



everything_is_ok = app_money + allotment_money + firstcall + finalcall 
everything_is_ok2 = total_payable

if everything_is_ok == everything_is_ok2:
    print(f"All ammounts are valid. Thank you. \n")
    # time.sleep(0.7)
elif everything_is_ok != everything_is_ok2:
    print(f"It would be better if you check all your ammounts! \nIt seems like wrong!!!!! \n")
    time.sleep(3.85)




# Receving applications 
def share_app():
    mny_recvd_app = real_share * app_money
    print(f"\n \n \n \nBank A/C ....... Dr.            {mny_recvd_app}")
    print(f"To Share Application A/C                  {mny_recvd_app}")


# Refunding if receving application ammount is gretter than issued application
def share_app_refund():
    refund_share_no = real_share - showing_share
    refund = refund_share_no * app_money
    print(f"\n  \nShare Application A/C ...... Dr.       {refund}")
    print(f"To Back A/C ......... Dr.                   {refund}")


# Share Application money transfurring to Share Capital A/C
def share_app_cap():
    money_receved_application = real_share * app_money
    print(f"\n \nShare Application A/C ...... Dr.       {money_receved_application}")
    print(f"To Share Capital A/C                     {money_receved_application}")


# Share Allotment money demanding
def share_all():
    shr_allot = real_share * allotment_money
    print(f"\n \nShare Allotment A/C ....... Dr.       {shr_allot}")
    print(f"To Share Capital A/C                     {shr_allot}")


# Share Allotment money receveing from bank
def share_all_cap():
    shr_allot = real_share * allotment_money
    print(f"\n \nBank A/C ........ Dr.              {shr_allot}")
    print(f"To Share Allotment A/                   {shr_allot}")



# Share 1stcall monney demanding
def first_call():
    shr_fst = real_share * firstcall
    print(f"\n \nShare 1st call A/C .... ... Dr.      {shr_fst}")
    print(f"To Share Capital A/C                     {shr_fst}")




# Share 1stcall monney receveing from bank
def first_call_cap():
    shr_fst = real_share * firstcall
    print(f"\n \nBank A/C ......... Dr.              {shr_fst}")
    print(f"To Share 1st call A/C                   {shr_fst}")



# Share Final call monney demanding
def final_call():
    shr_fnl = real_share * finalcall
    print(f"\n \nShare Final call A/C ...... Dr.      {shr_fnl}")
    print(f"To Share Capital A/C                     {shr_fnl}")



# Share 1stcall monney receveing from bank
def final_call_cap():
    shr_fnl = real_share * finalcall
    print(f"\n \nBank A/C ......... Dr.               {shr_fnl}")
    print(f"To Share Final call A/C                 {shr_fnl}")


# Share allotment including premium demanding
def share_all_premium():
    all_pre = allotment_money + premium
    all_premium = real_share * all_pre
    print(f"\n \nShare Allotment A/C ....... Dr.          {all_premium}")
    print(f"To Share Capital A/C                        {real_share * allotment_money}")
    print(f"To Security Premium Reserve A/C                     {real_share * premium}")


# Share allotment money including premium receving
def share_all_premium_cap():
    all_pre = allotment_money + premium
    all_premium = real_share * all_pre
    # all_premium = real_share * allotment_money
    
    print(f"\n \nBank A/C ........ Dr.              {all_premium}")
    print(f"To Share Allotment A/                   {all_premium}")


def first_final():
    shr_finl = real_share * finalcall
    print(f"\n \nShare First & Final call A/C ...... Dr.      {shr_finl}")
    print(f"To Share Capital A/C                     {shr_finl}")



def more_among_fst_fnl_call():
    if firstcall < finalcall:
        return finalcall
    elif firstcall > finalcall:
        return firstcall


def more_among_fst_fnl_call_arrear():
    if first_call_arrear_ammount < final_call_arrear_ammount:
        return final_call_arrear_ammount
    elif first_call_arrear_ammount > final_call_arrear_ammount:
        return first_call_arrear_ammount



def final_arrear(final_arrear):
    shr_fnl = real_share * finalcall
    calls = finalcall * final_arrear
    bank = shr_fnl - calls
    print(f"\n \nBank A/C ......... Dr.               {bank}")
    print(f"Calls in Arrear A/C ....... Dr.             {calls}")
    print(f"To Share Final call A/C                 {shr_fnl}")



def first_arrear(first_arrear):
    shr_fnl = real_share * firstcall
    calls = firstcall * first_arrear
    bank = shr_fnl - calls
    print(f"\n \nBank A/C ......... Dr.               {bank}")
    print(f"Calls in Arrear A/C ....... Dr.             {calls}")
    print(f"To Share Final call A/C                 {shr_fnl}")


def allotment_arrear(allot_arrear):
    shr_allot = real_share * allotment_money
    calls = allotment_money * allot_arrear
    
    bank = shr_allot - calls
    print(f"\n \nBank A/C ......... Dr.               {bank}")
    print(f"Calls in Arrear A/C ....... Dr.             {calls}")
    print(f"To Share Final call A/C                 {shr_allot}")





def share_forfeature(forfeited_share_num):
    shr_app_f = forfeited_share_num * total_payable
    call_arr_all = allotment_call_arrear_ammount * allotment_money
    call_arr_fst = first_call_arrear_ammount * firstcall
    call_arr_fnl = finalcall * final_call_arrear_ammount
    call_total_f = call_arr_all + call_arr_fst + call_arr_fnl
    sec_pre_f = 0
    print(f"\n \n \nShare Capital ....... A/C            Dr.    {shr_app_f}")
    # Security pre -------------------------
    if premium > 0:
        sec_pre_f = premium * forfeited_share_num
        print(f"Security Premium A/C  .......   Dr.          {sec_pre_f}")
        shr_app_f = shr_app_f + sec_pre_f
    # -----------------------
    print(f"To Calls in Arrear....... A/C                {call_total_f}")
    shr_frfture = shr_app_f - call_total_f 
    print(f"To Share forfeature....... A/C                 {shr_frfture}")
  
















# print(advance)
if advance == 1:
    print("You are now in a advance version!!")
    print("You have to give more details about shares...")
    # Checking premium on allotment
    premium = int(input("Enter the premium ammount : ") or "0")
    print(f"Total payable including premium is {premium + total_payable} .")
    #time.sleep(1)

    allotment_call_arrear_ammount = int(input("Enter the allotment arrear share ammount : ") or "0")



    first_call_arrear_ammount = int(input("Enter the first call arrear share ammount : ") or "0")


    final_call_arrear_ammount = int(input("Enter the final call arrear share ammount : ") or "0")
    
    forfeited_share_num = int(input("Enter Forfeated share amount : ") or "0")

    






    premium_ammount = int(premium)
    share_app()
    #time.sleep(1)#
    if showing_share < real_share:
        share_app_refund()
        real_share = showing_share # Share will calculate on issuing share
        #time.sleep(1)
    share_app_cap()

    #time.sleep(1)


    if premium_ammount > 0:
        share_all_premium()
        #time.sleep(1)
        if allotment_call_arrear_ammount > 0:
            allotment_arrear(allotment_call_arrear_ammount)
        share_all_premium_cap()
        #time.sleep(1)
    elif premium_ammount == 0:
        share_all()
        #time.sleep(1)
        if allotment_call_arrear_ammount > 0:
            allotment_arrear(allotment_call_arrear_ammount)

        elif allotment_call_arrear_ammount == 0:
            share_all_cap()
        #time.sleep(1)
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
        #time.sleep(1)
        if first_call_arrear_ammount > 0:
            first_arrear(first_call_arrear_ammount)

        elif first_call_arrear_ammount == 0:
            first_call_cap()

        #time.sleep(1)
        final_call()
        #time.sleep(1)
        if final_call_arrear_ammount > 0:
            final_arrear(final_call_arrear_ammount)


        elif final_call_arrear_ammount == 0:
            final_call_cap()
            #time.sleep(1)

        
        share_forfeature(forfeited_share_num)




elif advance == 0:
    print("You are using normal version.")
    share_app()


    time.sleep(0.25)
    if showing_share < real_share:
        share_app_refund()
        real_share = showing_share # Share will calculate on issuing share
        #time.sleep(1)
    share_app_cap()

    #time.sleep(1)

    share_all()
    #time.sleep(1)

    share_all_cap()
    #time.sleep(1)


    if firstcall == 0 or finalcall == 0:
        if first_call_arrear_ammount == 0 and final_call_arrear_ammount == 0:

            print(f"\n \nShare  First & Final call A/C ...... Dr.      {real_share * more_among_fst_fnl_call()}")
            print(f"To Share Capital A/C                     {real_share * more_among_fst_fnl_call()}")


           # time.sleep(1)
            print(f"\n \nBank A/C ......... Dr.               {real_share *     more_among_fst_fnl_call()}")
            print(f"To Share First & Final call A/C                 {real_share *  more_among_fst_fnl_call()}")

        elif first_call_arrear_ammount != 0 or final_call_arrear_ammount != 0:
            print(f"\n \nShare  First & Final call A/C ...... Dr.      {real_share * more_among_fst_fnl_call()}")
            print(f"Calls in arrear A/C .... Dr.                 {more_among_fst_fnl_call_arrear() * more_among_fst_fnl_call()}")
            print(f"To Share Capital A/C                     {real_share * more_among_fst_fnl_call()}")


           # time.sleep(1)
            print(f"\n \nBank A/C ......... Dr.               {real_share *     more_among_fst_fnl_call()}")
            print(f"To Share First & Final call A/C                 {real_share *  more_among_fst_fnl_call()}")


    else:
        first_call()
        #time.sleep(1)

    
        first_call_cap()
        #time.sleep(1)



        final_call()
        #time.sleep(1)
        final_call_cap()
        #time.sleep(1)








    



else:
    print(f"{advance} is invalid input!! \n")



print("\nThank you for using Issue of share tool...")
time.sleep(2.1)
print("Exiting...")
time.sleep(1.25)

print(exit())













