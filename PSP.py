from datetime import date,time,datetime,timezone,timedelta

while True:
    print()
    print("1. adjust amount_threshold")
    print("2. adjust time limit")
    print("3. adjust no of transactions in a time limit:")
    print("4. exit")
    try:
        choice=int(input("Enter Your choice:"))
    except ValueError:
        print("It must be a integer from listed pattern")
        continue
    if choice==1:
        try:
            amount_threshold=int(input("Enter the amount you want to set for a daily maximum limit:"))
        except ValueError:
            print("amount must be a integer")
            continue
    elif choice==2:
        try:
            time_limit_minutes=int(input("Set a time limit for a fraud checking transaction:"))
        except ValueError:
            print("It must be a integer")
            continue
    elif choice==3:
        try:
            max_transaction_limit=int(input("Enter The limit of transactions with in a time limit:"))
        except ValueError:
            print("It must be a integer")
            continue
    elif choice==4:
        break
    else:
        print("Please select a valid number")
def select_option():
    print("\n                               ===============WELCOME================")
    print("__________________________***---DIGITAL PAYMENT FRAUD RULE CHECKER---****___________________________")
    print("\n1. VIEW ALL TRANSACTIONS")
    print("2. DETECTION RULES")
    print("3. CHECK TRANSACTIONS")
    print("4. SEARCH BY ACCOUNT ID")
    print("5. VIEW FLAGGED TRANSACTIONS")
    print("6. SHOW TRANSACTION SUMMARY")
    print("7. SAVE A FLAGGED TRANSACTIONS TO A FILE")
    print("8. EXIT")
#save flagged file
all_payments = [
    {"transaction_id": "T001", "account": "ACC101", "amount": 500, "time": "2026-11-06 09:00:00", "recipient": "REC201"},
    {"transaction_id": "T002", "account": "ACC102", "amount": 1000, "time": "2026-11-06 09:02:00", "recipient": "REC202"},
    {"transaction_id": "T003", "account": "ACC103", "amount": 25000, "time": "2026-11-06 09:05:00", "recipient": "REC203"},
    {"transaction_id": "T004", "account": "ACC104", "amount": 750, "time": "2026-11-06 09:07:00", "recipient": "REC204"},
    {"transaction_id": "T005", "account": "ACC105", "amount": 300, "time": "2026-11-06 09:10:00", "recipient": "REC205"},
    {"transaction_id": "T006", "account": "ACC106", "amount": 500, "time": "2026-11-06 09:15:00", "recipient": "REC210"},
    {"transaction_id": "T007", "account": "ACC106", "amount": 700, "time": "2026-11-06 09:16:00", "recipient": "REC210"},
    {"transaction_id": "T008", "account": "ACC106", "amount": 900, "time": "2026-11-06 09:18:00", "recipient": "REC210"},
    {"transaction_id": "T009", "account": "ACC107", "amount": 1200, "time": "2026-11-06 09:20:00", "recipient": "REC211"},
    {"transaction_id": "T010", "account": "ACC108", "amount": 200, "time": "2026-11-06 09:30:00", "recipient": "REC212"},
    {"transaction_id": "T011", "account": "ACC108", "amount": 300, "time": "2026-11-06 09:32:00", "recipient": "REC213"},
    {"transaction_id": "T012", "account": "ACC108", "amount": 400, "time": "2026-11-06 09:34:00", "recipient": "REC214"},
    {"transaction_id": "T013", "account": "ACC108", "amount": 500, "time": "2026-11-06 09:36:00", "recipient": "REC215"},
    {"transaction_id": "T014", "account": "ACC109", "amount": 30000, "time": "2026-11-06 09:40:00", "recipient": "REC216"},
    {"transaction_id": "T015", "account": "ACC110", "amount": 2500, "time": "2026-11-06 09:45:00", "recipient": "REC217"},
    {"transaction_id": "T016", "account": "ACC111", "amount": 600, "time": "2026-11-06 09:50:00", "recipient": "REC218"},
    {"transaction_id": "T017", "account": "ACC112", "amount": 1800, "time": "2026-11-06 10:00:00", "recipient": "REC219"},
    {"transaction_id": "T018", "account": "ACC113", "amount": 22000, "time": "2026-11-06 10:05:00", "recipient": "REC220"},
    {"transaction_id": "T019", "account": "ACC114", "amount": 950, "time": "2026-11-06 10:10:00", "recipient": "REC221"},
    {"transaction_id": "T020", "account": "ACC115", "amount": 400, "time": "2026-11-06 10:15:00", "recipient": "REC222"},
    {"transaction_id": "T021", "account": "ACC116", "amount": 1500, "time": "2026-11-07 11:00:00", "recipient": "REC223"},
    {"transaction_id": "T022", "account": "ACC117", "amount": 2000, "time": "2026-11-07 14:30:00", "recipient": "REC224"},
    {"transaction_id": "T023", "account": "ACC118", "amount": 800, "time": "2026-11-07 23:30:00", "recipient": "REC225"},
    {"transaction_id": "T024", "account": "ACC119", "amount": 3000, "time": "2026-11-07 05:15:00", "recipient": "REC226"},
    {"transaction_id": "T025", "account": "ACC120", "amount": 1200, "time": "2026-11-08 16:00:00", "recipient": "REC227"},
    {"transaction_id": "T026", "account": "ACC121", "amount": 4500, "time": "2026-11-08 22:45:00", "recipient": "REC228"},
    {"transaction_id": "T027", "account": "ACC122", "amount": 700, "time": "2026-11-09 08:00:00", "recipient": "REC229"},
    {"transaction_id": "T028", "account": "ACC123", "amount": 28000, "time": "2026-11-09 12:00:00", "recipient": "REC230"},
    {"transaction_id": "T029", "account": "ACC124", "amount": 600, "time": "2026-11-09 23:15:00", "recipient": "REC231"},
    {"transaction_id": "T030", "account": "ACC125", "amount": 900, "time": "2026-11-09 15:00:00", "recipient": "REC232"}
]
def display_transactions():
    for transaction in all_payments:
        print("\n----------------------------------------------------------")
        print("Transacton ID :",transaction["transaction_id"])
        print("Account_ID:",transaction["account"])
        print("Payment_amount:",transaction["amount"])
        print("DATE TIME:",transaction["time"])
        print("Recepient ID:",transaction["recipient"])
def rules():
    print("\n______________________Rules for a verification_______________________")
    print("1. More transactions happened within a limited time")
    print("2. Amount above a chosen threshold")
    print("3. Repeated payment has made for a same account with in a limited time")
    return 
def check_transactions():
    flagged=[]
    # Detection settings
    amount_limit = amount_threshold
    time_limit = timedelta(minutes=time_limit_minutes)
    transaction_limit = max_transaction_limit
    for transaction in all_payments:
        reasons = []
        account = transaction["account"]
        recipient = transaction["recipient"]
        amount = transaction["amount"]
        transaction_time = datetime.strptime(transaction["time"], "%Y-%m-%d %H:%M:%S")

# here used Rule: Multiple transactions from same account
        account_transactions = []
        for payment in all_payments:
            if payment["account"] == account:
                payment_time = datetime.strptime(payment["time"], "%Y-%m-%d %H:%M:%S")
                if abs(transaction_time - payment_time) <= time_limit:
                    account_transactions.append(payment)
        if len(account_transactions) >= transaction_limit:
            reasons.append("Multiple transactions within 10 minutes")
 #here used Rule : Transaction amount above threshold
        if amount > amount_limit:
            reasons.append("Transaction amount exceeds the limit")
 #here used  Rule : Repeated payment to same recipient
        repeated_payments = []
        for payment in all_payments:
            if (payment["account"] == account and payment["recipient"] == recipient):
                payment_time = datetime.strptime(payment["time"], "%Y-%m-%d %H:%M:%S")
                if abs(transaction_time - payment_time) <= time_limit:
                    repeated_payments.append(payment)
        if len(repeated_payments) >= 2:
            reasons.append("Repeated payments to same recipient")
        # we Stored flagged transactions here by using kwargs (**)concept of dictionsry
        if reasons:
            flagged.append({
                **transaction,
                "reasons": reasons
            })
    if flagged:
        print("total no of flagged transactions are :",len(flagged))
    else:
        print("\nNo transactions detected for review.")
    return flagged
def search_account():
    found_account_id=False
    found_transaction_id=False
    while True:
        print("\n1. Transaction ID")
        print("2. Search ID")
        print("3. Exit")
        try:
            choice=int(input("Enter your choice:"))
            if not choice:
                print("Please choose any choice it cannot be empty")
        except ValueError:
            print("Please Enter a integer")
            continue
        if choice==1:
            search_transaction_id=input("Enter transaction ID:")
            if not search_transaction_id:
                print("Please Enter ID --It cannot be empty!")
            if search_transaction_id:
                for transaction in all_payments:
                    if transaction["transaction_id"].casefold()==search_transaction_id.casefold():
                        found_transaction_id=True
                        print("\nTransacton ID :",transaction["transaction_id"])
                        print("Account_ID:",transaction["account"])
                        print("Payment_amount:",transaction["amount"])
                        print("DATE TIME:",transaction["time"])
                        print("Recepient ID:",transaction["recipient"])
                        print()#---->flagged for review or not is filled
                if found_transaction_id==False:
                        print("\nTransaction History not found Please search a valid account number!")
                        return   
        if choice==2:
                search_id=input("Enter Accound ID :")
                if not search_id:
                    print("Please Enter ID --It cannot be empty!")
                if search_id:
                    for transaction in all_payments:
                        if transaction["account"].casefold()==search_id.casefold():
                            found_account_id=True
                            print("\nTransacton ID :",transaction["transaction_id"])
                            print("ccount_ID:",transaction["account"])
                            print("Payment_amount:",transaction["amount"])
                            print("DATE TIME:",transaction["time"])
                            print("Recepient ID:",transaction["recipient"])
                            print()#---->flagged for review or not is filled
                            return   
                    if found_account_id==False:
                        print("\nTransaction History not found Please search a valid account number!")
        if choice==3:
            break
def flagged_transactions(flagged):
    if not flagged:
        print("\nNo flagged transactions available. Please check transactions first.")
        return

    print("\n========== FLAGGED TRANSACTIONS ==========")

    for transaction in flagged:
        print("\n-----------------------------------")
        print("Transaction ID:", transaction["transaction_id"])
        print("Account:", transaction["account"])
        print("Amount:", transaction["amount"])
        print("Recipient:", transaction["recipient"])
        print("Time:", transaction["time"])

        print("Reasons:")
        for reason in transaction["reasons"]:
            print("-", reason)
   
def transaction_summary(flagged):
    total_transactions = len(all_payments)
    total_flagged = len(flagged)
    total_amount = sum(transaction["amount"] for transaction in all_payments)
    flagged_amount = sum(transaction["amount"] for transaction in flagged)

    print("\n========== TRANSACTION SUMMARY ==========")
    print("Total Transactions:", total_transactions)
    print("Total Flagged Transactions:", total_flagged)
    print("Normal Transactions:", total_transactions - total_flagged)
    print("Total Transaction Amount:", total_amount)
    print("Total Flagged Amount:", flagged_amount)   
def save_file(flagged):
    if not flagged:
        print("\nNo flagged transactions available. Please check transactions first.")
        return

    with open("flagged_transactions.txt", "w", encoding="utf-8") as file:
        for transaction in flagged:
            file.write("\n-----------------------------\n")
            file.write(f"Transaction ID: {transaction['transaction_id']}\n")
            file.write(f"Account: {transaction['account']}\n")
            file.write(f"Amount: {transaction['amount']}\n")
            file.write(f"Recipient: {transaction['recipient']}\n")
            file.write(f"Time: {transaction['time']}\n")
            file.write("Status: FLAGGED FOR REVIEW\n")
            file.write("Reasons:\n")

            for reason in transaction["reasons"]:
                file.write(f"- {reason}\n")
    print("\nFlagged transactions saved successfully!")
while True:
    select_option()
    try:
        choice=int(input("\nEnter your choice:"))
    except ValueError:
        print("___________Please Enter a integer value!!!!___________")
        continue
    if choice==1:
        display_transactions()
    elif choice==2:
        rules()
    elif choice==3:
        check_transactions()
    elif choice==4:
        search_account()
    elif choice==5:
        flagged_transactions(check_transactions())
    elif choice==6:
        transaction_summary(check_transactions())
    elif choice==7:
        save_file(check_transactions())
    elif choice==8:
        break
    else:
        print("Please choice integer according to above list")

