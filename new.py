# sample 1 Python Programme
# By Wjsh
# On Raspberry Pi

namestr = raw_input('Hi, I\'m Raspberry Pi! What\'s your name?')

print 'Hi, %s! Here\'s a quick process.' % namestr

print '''
----------------------------------
In this short game, you\'ll be able to input two numbers which are ready
for me to minus against.
So here it starts:
----------------------------------
'''

inta = int(raw_input('Now please enter the first number: '))
intb = int(raw_input('Now please enter the second number: '))

if inta >= intb:
    print inta - intb
else:
    print intb - inta

print 'Thank you, %s! See you!' % namestr


