def Days_Passed(date) :
    l1 = date.split('/')
    year = int(l1[0])
    month = int(l1[1])
    day = int(l1[2])
    year_to_day = (year-1)*365
    if month <= 7 :
        month_to_day = (month-1)*31
    else :
        month_to_day = 6*31 + (month-7)*30
    return day + month_to_day + year_to_day 