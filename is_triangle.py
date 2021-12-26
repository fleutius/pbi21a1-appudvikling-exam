"""
Applikationsudvikling 1 - PBI21a1

Flemming Kærgaard
Dec 2021

"""

""" Spørgsmål 2 """
# 2.1 - is_triangle:
# defining if a triangle is feasable by comparing its sides. if any of 3 lenghts is bigger than sum of others combined = not feasable

def is_triangle(t1, t2, t3):
    test_t1 = t1 > t2 + t3
    test_t2 = t2 > t1 + t3
    test_t3 = t3 > t1 + t2
    triangle_type = ''

    if t1 + t2 == t3 or t1 + t3 == t2 or t2 + t3 == t1:
        triangle_type = 'Degenereret'
    else:
        triangle_type = 'Normal'

    if test_t1 is True:
        print("Nej- 1")
    elif test_t2 is True:
        print("Nej- 2")
    elif test_t3 is True:
        print("Nej- 3")
    else:
        print(f"Ja - {triangle_type}")


def is_triangle_input():
    t1_in = eval(input("Venligst indtast værdi for første side: "))
    t2_in = eval(input("Venligst indtast værdi for anden side: "))
    t3_in = eval(input("Venligst indtast værdi for tredje side: "))
    try:
       t1=round(t1_in)
       t2=round(t2_in)
       t3=round(t3_in)
    except (ValueError, TypeError):
        print("Venligst indtast et tal: ")
        print()
        is_triangle_input()
    
    is_triangle(t1,t2,t3)

is_triangle_input()