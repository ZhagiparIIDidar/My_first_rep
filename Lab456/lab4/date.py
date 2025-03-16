import datetime

'''
a1 = datetime.datetime.today()

a2 = a1 - datetime.timedelta(days=5)
print(a1)
print(a2)
'''
'''
a1 = datetime.datetime.today()
a2 = a1 + datetime.timedelta(days=1)
a3 = a1 - datetime.timedelta(days=1)
print(a3.date())
print(a1.date())
print(a2.date())
'''
'''
a1 = datetime.datetime.now()
print(a1)
a2 = a1.replace(microsecond=0)
print(a2)
'''
'''
a1 = datetime.datetime.today()

a2 = a1 + datetime.timedelta(seconds=25)

a3 = a2 - a1
print(a3.seconds)
'''
