# Accounting on issue of share 
import time
print("Welcome to \nIssue of share!!!!")


showing_share = int(input("Enter total  issued share ammount : "))

# print(f"Total share is {showing_share}")

total_payable = int(input("Enter total payable ammount : "))

real_share = int(input("Receved received applications ammounts : "))

print(f"\n \nIssued shares are {showing_share} \nPayable ammount {total_payable} \nTotal applications received {real_share}.")


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

# print(advance)
if advance == 1:
    print("You are now in a advance version!!")
    print("You have to give more details about shares...")

elif advance == 0:
    print("You are using normal version.")
else:
    print(f"{advance} is invalid input!! \n")






















# Receving applications 
def share_app():
    print(f"\n \n \n \nBank A/C ....... Dr.            {real_share * app_money}")
    print(f"Share Application A/C                  {real_share * app_money}")


# Refunding if receving application ammount is gretter than issued application
def share_app_refund():
    refund_share_no = real_share - showing_share
    refund = refund_share_no * app_money
    print(f"\n  \nShare Application A/C ...... Dr.       {refund}")
    print(f"Back A/C ......... Dr.                   {refund}")

# Share Application money transfurring to Share Capital A/C
def share_app_cap():
    print(f"\n \nShare Application A/C ...... Dr.       {real_share * app_money}")
    print(f"Share Capital A/C                     {real_share * app_money}")




# Share Allotment money demanding
def share_all():
    print(f"\n \nShare Allotment A/C ....... Dr.       {real_share * allotment_money}")
    print(f"Share Capital A/C                     {real_share * allotment_money}")


# Share Allotment money receveing from bank
def share_all_cap():
    print(f"\n \nBank A/C ........ Dr.              {real_share * allotment_money}")
    print(f"Share Allotment A/                   {real_share * allotment_money}")



# Share 1stcall monney demanding
def first_call():
    print(f"\n \nShare 1st call A/C .... ... Dr.      {real_share * firstcall}")
    print(f"Share Capital A/C                     {real_share * firstcall}")




# Share 1stcall monney receveing from bank
def first_call_cap():
    print(f"\n \nBank A/C ......... Dr.              {real_share * firstcall}")
    print(f"Share 1st call A/C                   {real_share * firstcall}")



# Share Final call monney demanding
def final_call():
    print(f"\n \nShare Final call A/C ...... Dr.      {real_share * finalcall}")
    print(f"Share Capital A/C                     {real_share * finalcall}")



# Share 1stcall monney receveing from bank
def final_call_cap():
    print(f"\n \nBank A/C ......... Dr.               {real_share * finalcall}")
    print(f"Share Final call A/C                 {real_share * finalcall}")









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

if finalcall > 0:
    final_call()
    time.sleep(1)
    first_call_cap()
time.sleep(1)


print("\nThank you for using Issue of share tool...")
time.sleep(2)
print("Exiting...")
time.sleep(1)

print(exit())









