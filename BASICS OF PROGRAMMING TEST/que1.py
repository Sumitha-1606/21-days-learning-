credit score=int(input("Enter your credit score")
income=int(input("Enter your income")
emi=int(input("Enter your emi")
employment=input("Enter the employment status")
if credit_score < 600:
    print("rejected")
elif 600 <= credit_score < 750:
    status = " Review"
    return status
else 
    print("check")
if income < 25000:
        print ("Rejected")
if emi > 0.5 * income:
        print("Rejected")
if employment not in ["Salaried", "Self-Employed"]:
        print("Rejected")
if credit_score >= 800:
        interest_rate = 7
else >=750 credit_score <= 799:
        interest_rate = 8
return status, interest_rate
  
  
