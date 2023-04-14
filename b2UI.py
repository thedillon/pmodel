import tkinter as tk
import csv


# create a function to handle the button click event
def write_to_csv():
    # get the values from the input fields
    data = input_field.get()

    # process the data as needed
    data = data.replace('/', '', 1)  # remove first occurrence of '/'
    data = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '/' or x == '\n', data))
    lines = data.split('\n')

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

    for i, line in enumerate(lines):
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
    # write the values to the CSV file
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([climb_lo, climb_hi, climb_mach, mass_lo, cruise_lo, cruise_hi,
                         cruise_mach, nominal_mass, max_alt, descent_lo, descent_hi,
                         descent_mach, high_mass])

    # clear the input field
    input_field.delete(0, tk.END)


# create the GUI window
window = tk.Tk()

# create the input field and button
input_field = tk.Entry(window, width=50)
input_field.pack()
button = tk.Button(window, text="Write to CSV", command=write_to_csv)
button.pack()

# start the GUI event loop
window.mainloop()
