with open("input.txt", "r") as f:
    data = f.read()
    data = data.replace('/', '', 1) # remove first occurrence of '/'

# remove all non-numeric, period, and non-linebreak characters from data
data = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '/' or x == '\n', data))

# split the cleaned data into lines
lines = data.split('\n')

# initialize variables
climb_lo = ''
climb_hi = ''
climb_mach = ''
mass_lo = ''
cruise_lo = ''
cruise_hi = ''
cruise_mach = ''
nominal_mass = ''
max_alt = ''
descent_lo = ''
descent_hi = ''
descent_mach = ''
high_mass = ''
print(data)
# loop through lines and assign values to variables
for i, line in enumerate(lines):
    print(i, line)
    if i == 6:
        climb_lo, climb_hi = line.split('/')
    elif i == 7:
        climb_mach = line.strip()
    elif i == 9:
        mass_lo = line.strip()
    elif i == 10:
        cruise_lo, cruise_hi = line.split('/')
    elif i == 11:
        cruise_mach = line.strip()
    elif i == 12:
        nominal_mass = line.strip()
    elif i == 13:
        max_alt = line.strip()
    elif i == 14:
        descent_lo, descent_hi = line.split('/')
    elif i == 15:
        descent_mach = line.strip()
    elif i == 17:
        high_mass = line.strip()

max_alt = max_alt.strip().replace('.', '')

# print the variables to verify they contain the correct values
print("climb_lo:", climb_lo)
print("climb_hi:", climb_hi)
print("climb_mach:", climb_mach)
print("mass_lo:", mass_lo)
print("cruise_lo:", cruise_lo)
print("cruise_hi:", cruise_hi)
print("cruise_mach:", cruise_mach)
print("nominal_mass:", nominal_mass)
print("max_alt:", max_alt)
print("descent_lo:", descent_lo)
print("descent_hi:", descent_hi)
print("descent_mach:", descent_mach)
print("high_mass:", high_mass)


