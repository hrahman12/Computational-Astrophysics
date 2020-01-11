import time
days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
LeapYears = [1900,1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068]
symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+qwertyuiopasdfghjklzxcvbnm"
def days_to_date(month,day,year):
    days = 0
    if(month>1):
        days+=days_per_month[0]
    if(month>2):
        days+=days_per_month[1]
    if(month>3):
        days+=days_per_month[2]
    if(month>4):
        days+=days_per_month[3]
    if(month>5):
        days+=days_per_month[4]
    if(month>6):
        days+=days_per_month[5]
    if(month>7):
        days+=days_per_month[6]
    if(month>8):
        days+=days_per_month[7]
    if(month>9):
        days+=days_per_month[8]
    if(month>10):
        days+=days_per_month[9]
    if(month>11):
        days+=days_per_month[10]

    days+=day
    return days

def CountLeapDays(BirthYear,ThisYear):

    LeapDays=0
    for i in range(BirthYear,ThisYear+1):
        for year in range(len(LeapYears)):
        #print(str(i)+" "+str(LeapYears[year]))
            if i == LeapYears[year]:
            #print(str(i)+" "+str(LeapYears[year]))
                LeapDays += 1

            #print(str(LeapDays)+" leap days.")
    return LeapDays

proxbyear = 11.186
month = 0
BirthYear = 0000
t = time.localtime()

while BirthYear < LeapYears[0] or BirthYear > t[0]:
    BirthYear = int(input('Enter birth year ('+str(LeapYears[0])+ '-' +str(t[0])+'): ' ))
#BirthYear must be valid by here
if (BirthYear==t[0]):
    BigMonth = t[1]
else:
    BigMonth = 12


while month <= 0 or month >12 or (BirthYear==t[0] and month>t[1]):
   month = int(input('Enter birth month (1-'+str(BigMonth)+ '): '))
if BirthYear == t[0] and BigMonth == t[1]:
    BigDay = t[2]
else:
    BigDay = days_per_month[month-1]
if month == 2:
    if BirthYear % 4 == 0:
        BigDay +=1
if BirthYear == 2000:
    BigDay -=1
day = 0

while day <= 00 or day > BigDay:
    day = int(input('Enter birth day (1-'+str(BigDay)+'): '))
DaysSoFar = t[7]
LastBirthYear = t[0]
DaysToBday = days_to_date(month,day,BirthYear)
if (DaysSoFar>DaysToBday):
    DaysSinceBday = DaysSoFar-DaysToBday
else:
    DaysSinceBday = 365-DaysToBday+DaysSoFar
    LastBirthYear -= 1

YearsSinceBirth = LastBirthYear - BirthYear
DaysSinceBirth = 365*YearsSinceBirth
DaysSinceBirth += DaysSinceBday + CountLeapDays(BirthYear,t[0])

AgeOnProxima = int(DaysSinceBirth/proxbyear)

print('You would be '+str(AgeOnProxima)+' years old on Proxima Centauri b.')
print("You're old. :P")
DaysAliveNexBday = int((AgeOnProxima +1)*proxbyear)
DaysToNexBday = (DaysAliveNexBday - DaysSinceBirth)
if DaysToNexBday == 0:
    print('HAPPY BIRTHDAY!!!!!!!!!! you turned '+str(AgeOnProxima)+' today!')
else:
    print("It is "+str(int(DaysToNexBday))+" days until your birthday on Proxima Centauri b.")
