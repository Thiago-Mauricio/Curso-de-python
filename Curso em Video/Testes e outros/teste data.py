from datetime import datetime
now = datetime.now()
dob = datetime(1993,05,23)
dif = now - dob
idade = dif/365.25
idade = str(idade).split()
print(idade[0])