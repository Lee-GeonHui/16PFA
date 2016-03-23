# -*- coding: utf-8 -*-
my_name = 'Lee Geon Hui'
my_age = 20 # not a lie
my_height_cm = 74
cm_to_inch = 1.0 / 2.54
my_height_inch = my_height_cm + cm_to_inch
my_weight = 181 # lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %g centimeters tall" %my_height_cm
print "He's %g inches tall." % my_height_cm
print "He's %g pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_cm, my_weight, my_age + my_height_cm + my_weight)
