import time

timeSpam = time.strftime("%I:%M:%S~%p")
print(timeSpam)
print(time.strftime("%I"))  # this is to give hour at now in this divice for 0 to 12h
print(time.strftime("%H"))  # this is to give hour at now in this divice for 0 to 24h
print(time.strftime("%M"))  # this is to give Minute at now in this divice for 0 to 59
print(time.strftime("%S"))  # this is to give second at now in this divice for 0 to 59
print(time.strftime("%a"))  # short ma aaj no weekday print kare che
print(time.strftime("%A"))  # full ma aaj no weekday print kare che
print(time.strftime("%b"))  # short ma chalu mounth print kare che
print(time.strftime("%B"))  # full ma chalu mounth print kare che
print(time.strftime("%c"))  # aa date time month year week day badhu ape che
print(time.strftime("%d"))  # aa decimal month no day kahe che 01 to 31
print(time.strftime("%j"))  # aa decimal ma day of year kahe 001 to 366
print(time.strftime("%m"))  # aa decimal ma month kahe che 01 to 12
print(time.strftime("%p"))  # aa AM and PM kahe che
print(time.strftime("%U"))  # aa week of year decimal ma kahe che 00 to 53
print(time.strftime("%w"))  # aa week days 0 to 6
