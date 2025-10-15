def day_times():
    return "morning", "afternoon", "evening", "night"

times = day_times()
print(times)
print(type(times))

first, second, third, fourth = day_times()
print("Trzeci element to %s" % third)

#---------------
# funkcja i jej kolejne wywołania
def add(a, b):
    print(a + b)

add(2, 2)
add(54, 64)
add(40504, 232320)

#------------

def customized_hello(first_name, last_name):
    print("Hello Mr %s %s" % (first_name, last_name))

customized_hello("John", "Cleese")