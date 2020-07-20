# G0 CORONA GO
# Importing covid library for getting details about Covid19
# Importing tkinter for GUI purpose
# Importing matplotlib to show the details of corona
from covid import Covid
from tkinter import *
from matplotlib import pyplot as plt

# Initializing screen for GUI
# Setting size of the screen
# setting title and adding background color
master = Tk()
master.geometry('800x800')
master.title("Corona Cases Details of Country ")
master.configure(bg="yellow")


# function to show the data and plot the data
def showdata():
    # initializing variable corona of Covid class
    corona = Covid()
    # Lists to store cases,confirmed cases , active cases , deaths cases, recovered cases
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    # Using try except insures that when input in incorrect or
    # Internet connectivity is not good it will not execute
    try:
        # updating gui screen
        master.update()
        # getting country names entered by user
        countries = data.get()
        # removing leading and trailing spaces(if any)
        country_names = countries.strip()
        # if country names are space separated
        # make it comma separated string
        country_names = country_names.replace(" ", ",")
        # splitting string on "," to make it as list
        country_names = country_names.split(",")
        # for each country names , get the details of covid
        # using inbuilt function (get_status_by_country_name) of
        # Covid class to save the details in variable cases
        for x in country_names:
            cases.append(corona.get_status_by_country_name(x))
            master.update()
        # print(cases)
        # cases list will store dictionary of details of given countries
        for y in cases:
            # adding country wise confirmed into confirmed list
            confirmed.append(y['confirmed'])
            # adding country wise active into active list
            active.append(y['active'])
            # adding country wise deaths into deaths list
            deaths.append(y["deaths"])
            # adding country wise recovered into recovered list
            recovered.append(y['recovered'])

        for x in range(len(country_names)):
            # variable details will store country wise details to be printed on gui screen
            details = "\n"+country_names[x] + ' : Confirmed (' + str(confirmed[x]) + "), Recovered (" + str(recovered[x])
            details += "), Deaths (" + str(deaths[x]) + ") Active (" + str(active[x]) + ")"
            # show on screen
            Label(master, text=details, font='Consolas 13 bold', width=85, bg='pink').pack()
        print(confirmed, recovered, active, deaths)

        # Making 2x2 to show all 4 cases of different countries
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
        # setting title of plot
        fig.suptitle("Comparison of Covid19 ", size=20)

        # bar graph of countries vs Confirmed case
        ax1.bar(country_names, confirmed, color='brown')
        ax1.set_title("CONFIRMED CASES")
        ax1.set_xlabel("Countries")
        ax1.set_ylabel("Total cases)")

        # bar graph of countries vs deaths
        ax2.bar(country_names, deaths, color='red')
        ax2.set_title("DEATHS")
        ax2.set_xlabel("Countries")

        # bar graph of countries vs active cases
        ax3.bar(country_names, active, color='green')
        ax3.set_title("ACTIVE CASES")
        ax3.set_xlabel("Countries")
        ax3.set_ylabel("Total active cases)")

        # bar graph of countries vs recovered cases
        ax4.bar(country_names, recovered, color='blue')
        ax4.set_title("RECOVERED CASES")
        ax4.set_xlabel("Countries")
        # showing plots
        plt.show()

    except Exception as e:
        Label(master, text="Incorrect Information", font='Consolas 20 bold').pack()


# title on gui screen
Label(master, text="\n\n!!! GO CORONA GO !!!\n\n||| Stay Home Stay Safe |||\n\n", bg='yellow', font='Consolas 25 bold').pack()
# heading above input box
Label(master, text="Enter Country names \n(comma separated)\n", bg='yellow',font='Consolas 14 bold').pack()
# using string variable to store data
data = StringVar()
# by default set data to "India,US,China"
data.set("India,US,China")
Label(master, text='\n')
# Input box to take data
entry = Entry(master, textvariable=data, bd=4, font='Consolas 15 bold', width=40).pack()
# button to get data and plot results after clicking it
Button(master, text="  SHOW DETAILS  ", width=15, height=2, bg='green', command=showdata,font='Consolas 14 bold').pack()
# Done
master.mainloop()
