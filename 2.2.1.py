import datetime
date = datetime.datetime.strptime(input(), "%Y %m %d")  #Thats some bullshit. It doesn't work with just one datetime
date = date + datetime.timedelta(days=int(input()))     #Probably because datetime is simultaniously module and class
print(date.year, date.month, date.day)                  #So strptime is a method in datetime class in datetime module