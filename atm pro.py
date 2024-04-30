amount=int(input("enter your amount"))

if amount>500:
    notes=amount//500
    print("500 notes are",notes)
    amount=amount%500

if amount>100:
    notes=amount//100
    print("100 notes are",notes)
    amount=amount%100

if amount>200:
    notes=amount//200
    print("200 notes are",notes)
    amount=amount%200    
    
