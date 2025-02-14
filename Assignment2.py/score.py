scores=[83,76,95,64,55,92,67,42,61,72]
for score in scores:
    if score>80:
        grade='A'
    elif score>=70:
        grade='B'
    elif score>=60:
        grade='C'
    elif score>=50:
        grade='D'
    else:
        grade='F'
    print ("score:",score ,"Grade:",grade)