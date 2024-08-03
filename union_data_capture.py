# import tkinter to use to build GUI
import tkinter as tk
# import themed tkinter for more up to date GUI widgets
from tkinter import ttk
# import messagebox for user input error feedback
from tkinter import messagebox
#import tkcalendar dateentry for date input
from tkcalendar import DateEntry
# import csv for read from / write to csv functionality
import csv
# import datetime for use with dates of birth
from datetime import datetime
# import re for regex use
import re

# define a class that inherits from tkinter as its parent class
class UnionCollect(tk.Tk):
    """
    The class 'UnionCollect' inherits from tkinter as its parent class.
    It contains additional attributes and methods as follows:
        Attributes
        Methods
        Constructor
    """

    def __init__(self):
        #call the constructor of the parent class to get the parent's attributes
        super().__init__()
        # define sub-class attributes where there are multiple options, in lists
        self.role = ["Member", "Advocate", "Rep"]
        self.rep_resp = ["Workplace rep", "Learning rep", "Health & safety rep", "Group executive committee",
                         "Branch executive committee", "Employer bargaining unit"]
        self.activity = ["2023 industrial action - voted", "2023 industrial action day 1 - strike",
                         "2023 industrial action day 1 - picket", "2023 industrial action day 2 - strike",
                         "2023 industrial action day 2 - picket", "2024 NEC elections - voted",
                         "2024 industrial action - voted"]

        # initialise all the variables, with default text where required
        self.member_name = tk.StringVar()  # a string var that will contain typed text
        self.member_dob = tk.StringVar()  # a string var that will contain a dd-mm-yyyy selected date as a string
        self.member_email = tk.StringVar()  # a string var that will contain typed text
        self.role_select = tk.StringVar(value="Select")  # a string var that will contain text selected from dropdown
        self.rep_resp_select = {}  # an empty dictionary to hold role responsibility names and selection status
        self.activity_select = {}  # an empty dictionary to hold activity names and selection status

        # create a main tkinter window in which all GUI elements will sit
        self.geometry("550x750")  # window size
        self.config(bg="#181738")  # window background colour -
        self.title("Union branch data portal")  # window title

        # Set thematic variables - colour
        self.thm_bg1 = "#323B59"
        self.thm_fg1 = "#EEB9FC"
        self.thm_bg2 = "#7789C9"
        self.thm_fg2 = "#55315E"
        # Set thematic variables - primary font
        self.thm_font = ("Calibri", 11, "bold")

        # call function to build all widgets and arrange according to specified coordinates
        self.build_widgets()

    # define function for building widgets for enter data screen
    def build_widgets(self):
        """
        Function to create all widgets associated with GUI.
        Sets up:
            - Title header
            - Info text box
            - Input box - member name
            - Input box - member date of birth
            - Input box - member work email
            - Dropdown selection menu - union role
            - Multiple tick box selection - rep role responsibilities
            - Multiple tick box selection - activities
            - Button - submit data
            - Button - view data
        """

        # Main title header for window
        (tk.Label(self, text="Union branch data collection", font=("Calibri", 20, "bold"), bg=self.thm_bg1,
                  fg=self.thm_fg1)
            .place(x=20, y=8, width=511, height=27))

        # Info text box
        tk.Label(self, text="Provide your details and information about your union role and activities to ensure "
                 "correct activist work is undertaken, e.g. you are not contacted about your industrial action vote "
                 "if you have already posted it.", font=self.thm_font, bg=self.thm_bg1, fg=self.thm_fg1,
                  wraplength=500, justify=tk.LEFT).place(x=20, y=48, width=511, height=70)

        # input box 1 - member name
        tk.Label(self, text="1. Enter your full name:", font=self.thm_font, bg=self.thm_bg1, fg=self.thm_fg1,
                 anchor="w").place(x=20, y=131, width=511, height=20)
        (tk.Entry(self, textvariable=self.member_name, font=self.thm_font, bg=self.thm_bg2, fg=self.thm_fg2)
            .place(x=344, y=131, width=187, height=20))

        # input box 2 - dob
        tk.Label(self, text="2. Enter your date of birth:", font=self.thm_font, bg=self.thm_bg1,
                 fg=self.thm_fg1, anchor="w").place(x=20, y=164, width=511, height=20)
        (DateEntry(self, textvariable=self.member_dob, date_pattern="dd-mm-yyyy", font=self.thm_font)
            .place(x=344, y=164, width=187, height=20))

        # input box 3 - work email
        tk.Label(self, text="3. Enter your work email:", font=self.thm_font, bg=self.thm_bg1, fg=self.thm_fg1,
                 anchor="w").place(x=20, y=197, width=511, height=20)
        (tk.Entry(self, textvariable=self.member_email, font=self.thm_font, bg=self.thm_bg2, fg=self.thm_fg2)
            .place(x=344, y=197, width=187, height=20))

        # input box 4 - union role
        tk.Label(self, text="4. Select your union role:", font=self.thm_font, bg=self.thm_bg1, fg=self.thm_fg1,
                 anchor="w").place(x=20, y=230, width=511, height=20)
        roles_ddown_4 = tk.OptionMenu(self, self.role_select, *self.role)
        roles_ddown_4.config(font=self.thm_font, bg=self.thm_bg2, fg=self.thm_fg2, activebackground=self.thm_bg2,
                           activeforeground=self.thm_fg2, anchor="w")
        roles_ddown_4.place(x=344, y=230, width=187, height=20)
        roles_ddown_4["menu"].config(font=self.thm_font, bg=self.thm_bg2, fg=self.thm_fg2)

        # input box 4a.- rep responsibilities
        (tk.Label(self, text="4a. If you have a rep role, select rep responsibilities (choose all that apply):",
                 font=self.thm_font, bg=self.thm_bg1, fg=self.thm_fg1, anchor="nw")
            .place(x=20, y=263, width=511, height=140))
        y_4a = 283  # set the y-coord of the first checkbutton - all other place parameter values remain the same
        # start a loop to loop through all values in the rep_resp list
        for i in self.rep_resp:
            self.rep_resp_select[i] = tk.BooleanVar()  # assign a variable as a boolean true/false (on/off)
            # set tickbox text and variable
            tickbox_4a = tk.Checkbutton(self, text=i, variable=self.rep_resp_select[i], anchor="w")
            tickbox_4a.config(font=self.thm_font, bg=self.thm_bg2, fg=self.thm_fg2)  # apply theme colours
            # define location in the app window, adjusting the y-coord so each loop creates a new line
            tickbox_4a.place(x=321, y=y_4a, width=210, height=20)
            y_4a += 20

        # input box 5.- activities
        (tk.Label(self, text="5. Select activities undertaking / undertaken (choose all that apply):",
                 font=self.thm_font, bg=self.thm_bg1, fg=self.thm_fg1, anchor="nw")
            .place(x=20, y=416, width=511, height=160))
        y_5 = 436  # set the y-coord of the first checkbutton - all other place parameter values remain the same

        # start a loop to loop through all values in the rep_resp list
        for i in self.activity:
            self.activity_select[i] = tk.BooleanVar()  # assign a variable as a boolean true/false (on/off)
            # set tickbox text and variable
            tickbox_5 = tk.Checkbutton(self, text=i, variable=self.activity_select[i], anchor="w")
            tickbox_5.config(font=self.thm_font, bg=self.thm_bg2, fg=self.thm_fg2)  # apply theme colours
            # define location in the app window, adjusting the y-coord so each loop creates a new line
            tickbox_5.place(x=281, y=y_5, width=250, height=20)
            y_5 += 20

        # submit data button to call function that writes data to csv
        (tk.Button(self, text="Submit data", command=self.submit_data, font=("Calibri", 16, "bold"),
                  bg=self.thm_bg2, fg=self.thm_fg2)
            .place(x=161, y=589, width=227, height=37))

        # view data button to call function that opens view data window
        (tk.Button(self, text="View data", command=self.view_data, font=("Calibri", 16, "bold"),
                  bg=self.thm_bg2, fg=self.thm_fg2)
            .place(x=161, y=635, width=227, height=37))


    # input validation check method for name not left blank
    def name_entered_check(self, name: str) -> bool:
        return bool(name)

    # input validation check method for name length
    def name_length_check(self, name: str) -> bool:
        return 1 < len(name) <=35

    # input validation check method for name to ensure appropriate characters are used
    def name_format_check(self, name: str) -> bool:
        return bool(re.compile(r"^[a-zA-Z-' ]+$").match(name))

    # input validation check method for date of birth - dob can't be before the oldest person in the world born 1907
    def dob_year_check_old(self, dob: str) -> bool:
        return bool(datetime.strptime(dob, "%d-%m-%Y") >
                    datetime.strptime("03-03-1907", "%d-%m-%Y"))

    # input validation check method for date of birth - dob must show person to be at least 16 years old/of working age
    def dob_year_check_young(self, dob: str) -> bool:
        dob_entered = datetime.strptime(dob, "%d-%m-%Y")
        date_now = datetime.strptime(datetime.now().strftime("%d-%m-%Y"), "%d-%m-%Y")
        date_16_y_ago = datetime(date_now.year - 16, date_now.month, date_now.day)
        return bool(dob_entered < date_16_y_ago)

    # input validation check method for email not left blank
    def email_entered_check(self, email: str) -> bool:
        return bool(email)

    # input validation check method for email length
    def email_length_check(self, email: str) -> bool:
        return len(email) <= 50

    # input validation check method to ensure work email contains only letters, numbers and appropriate characters
    def email_format_check(self, email: str) -> bool:
        return bool(re.compile(r"^[0-9a-zA-Z!#$%&'*+-/=?^_`{|}~.@]+$").match(email))

    # input validation check method to ensure work email ends @bigcorpo.uk
    def email_ending_check(self, email: str) -> bool:
        return bool(re.search("@bigcorpo.uk" + "$", email, re.IGNORECASE))

    # input validation check to ensure that there's something before the @ symbol
    def email_start_check(self, email: str) -> bool:
        return bool(re.search(r"^[0-9a-zA-Z!#$%&'*+-/=?^_`{|}~.]+@", email, re.IGNORECASE))

    # input validation check method for role nothing chosen, still default value
    def role_selected_check(self, role: str) -> bool:
        return role != "Select"

    #input validation check methods for rep responsibilities - can't select if not selected a rep role
    def rep_resp_notrep_check(self, role: str, responsibilities: str) -> bool:
        #  work out the number of responsibility values that user has selected
        not_rep_resp_count = sum(i == "True" for i in responsibilities)
        if role == "Rep":  # this test returns True if user has selected "Rep". It's testing non-rep role with rep-resps
            return True
        elif not_rep_resp_count > 0:  # if not rep and rep responsibilities selected test fails as False
            return False
        else:  # if non-rep but no rep responsibilities it's a True
            return True

    #input validation check methods for rep responsibilities - reps should have at least one responsibility
    def rep_resp_rep_check(self, role: str, responsibilities: str) -> bool:
        #  work out the number of responsibility values that user has selected
        rep_resp_count = sum(i == "True" for i in responsibilities)
        # this test returns True if user has selected any role other than rep. It's testing rep role with rep-resps
        if role != "Rep":
            return True
        elif rep_resp_count == 0:  # if rep and no rep responsibilities selected test fails as False
            return False
        else:  # if rep with rep responsibilities it's a True
            return True


    # define method for submitting data
    def submit_data(self):
        """
        Function to get values entered to GUI and write them to a csv file.
        """

        # get GUI widget values and current datetime
        now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = self.member_name.get()
        dob = self.member_dob.get()
        email = self.member_email.get()
        role = self.role_select.get()
        responsibilities = []
        #loop through the tick box dictionaries to get each bool value as strings in lists
        for i in self.rep_resp:
            responsibilities.append(str(self.rep_resp_select[i].get()))


        # loop through the tick box dictionaries to get each bool value as strings in lists
        activities = []
        for i in self.activity:
            activities.append(str(self.activity_select[i].get()))



        error_flag = "N"
        # call the name input validation check functions and test that they return True - if not, error message
        name_checks = True  # flag for first check pass/fail. don't error the latter name checks if this fails
        if not self.name_entered_check(name):
            name_checks = False  # No point in error message for later name input checks if nothing entered
            tk.messagebox.showerror("Name input error","No name was entered")
            error_flag = "Y"
        if not self.name_length_check(name) and name_checks:
            tk.messagebox.showerror("Name input error","Name entered must be 2-35 characters long")
            error_flag = "Y"
        if not self.name_format_check(name) and name_checks:
            tk.messagebox.showerror(
                "Name input error","Name entered can only contain a-z, hyphens and apostrophes")
            error_flag = "Y"

        #call the DOB input validation check funtions and test that they are True - if not, errors
        if not self.dob_year_check_old(dob):
            tk.messagebox.showerror(
                "DOB input error", "Date of birth entered makes you the oldest person alive")
            error_flag = "Y"
        if not self.dob_year_check_young(dob):
            tk.messagebox.showerror("DOB input error", "Employees must be at least 16 years of age")
            error_flag = "Y"

        # call the email input validation check functions and test that they return tru - if not, error message(s)
        email_checks1 = True  # flag for first check pass/fail. don't error the latter email checks if this fails
        if not self.email_entered_check(email):
            email_checks1 = False  # No point in error message for later email input checks if nothing entered
            tk.messagebox.showerror("Email input error", "No email was entered")
            error_flag = "Y"

        if (not self.email_length_check(email)) and email_checks1:
            tk.messagebox.showerror(
                "Email input error", "Email must be no more than 50 characters")
            error_flag = "Y"
        if not self.email_format_check(email) and email_checks1:
            tk.messagebox.showerror(
                "Email input error",
                "Email must only contain letters, numbers and email appropriate symbols")
            error_flag = "Y"
        if not self.email_ending_check(email) and email_checks1:
            tk.messagebox.showerror("Email input error", "Email must be an ""@bigcorpo.uk"" address")
            error_flag = "Y"
        if not self.email_start_check(email) and email_checks1:
            tk.messagebox.showerror("Email input error",
                                    "Email must have an addressee before the @ symbol")
            error_flag = "Y"

        role_check = True
        # call the role select validation method and test returns true - if not error message
        if not self.role_selected_check(role):
            role_check = False
            tk.messagebox.showerror("Role selection error", "No role was selected")
            error_flag = "Y"

        # call the rep responsbilities but not rep validation method and test returns true - if not error message
        if not self.rep_resp_notrep_check(role, responsibilities) and role_check:
            tk.messagebox.showerror(
                "Rep responsibilities error",
                f"{role} role selected: Only reps can select rep responsibilities")
        # call the rep responsbilities validation method and test returns true - if not error message
        if not self.rep_resp_rep_check(role, responsibilities) and role_check:
            tk.messagebox.showerror(
                "Rep responsibilities error",
                f"{role} role selected: Reps should select at least one responsibility")

        if error_flag == "Y":
            tk.messagebox.showinfo("Data input errors found", "Data was not saved. Please try again")
        else:
            #create a single list of GUI object values at point of button press to write to the csv file
            union_data_list = [now_date, name, dob, email, role]
            union_data_list.extend(responsibilities)  # responsibilites is its own list, needs all entries in that list
            union_data_list.extend(activities)  # activities is its own list, needs all entries in that list
            # open union data csv file for appending new data to
            with open("union_data.csv", mode="a", newline="") as output_csv:
                csv.writer(output_csv).writerow(union_data_list)
            tk.messagebox.showinfo("Success", "Data was saved to file")




    # define method for viewing existing data - should this be a different subclass?
    def view_data(self):
        sub_window = tk.Toplevel(self)
        sub_window.title("Union data collection")
        sub_window.geometry("1500x500")
        sub_window.config(bg="#181738")


        #create a ttk style
        #theme = ttk.Style()
        #theme.layout('TScrollbar',
        #            [('Horizontal.Scrollbar.trough',
        #            {'children': [('Horizontal.Scrollbar.leftarrow', {'side': 'left', 'sticky': ''}),
        #            ('Horizontal.Scrollbar.rightarrow', {'side': 'right', 'sticky': ''}),
        #           ('Horizontal.Scrollbar.thumb', {'expand': '1', 'sticky': 'nswe'})],
        #            'sticky': 'we'})])
        #theme.configure('TScrollbar', background='blue', troughcolor='blue', arrowcolor='black')

        table_frame = ttk.Frame(sub_window)
        table_frame.pack(expand=True, fill="both", padx=5, pady=5)

        view_table = ttk.Treeview(table_frame, columns=("Datetime submitted", "Name", "Date of birth", "Work email",
                            "Union role", "Rep responsibilities - workplace", "Rep responsibilities - learning",
                            "Rep responsibilities - health safety", "Rep responsibilities - GEC",
                            "Rep responsibilities - BEC", "Rep responsibilities - EBU",
                            "Activity - 2023 industrial action - voted",
                            "Activity - 2023 industrial action day 1 - strike",
                            "Activity - 2023 industrial action day 1 - picket",
                            "Activity - 2023 industrial action day 2 - strike",
                            "Activity - 2023 industrial action day 2 - picket",
                            "Activity - 2024 NEC elections - voted",
                            "Activity - 2024 industrial action - voted"))
        view_table.column("#0", width=0)  # undo treeview default of an empty column at index 0
        for j in view_table["columns"]:
            view_table.heading(j, text=j)
            view_table.column(j, width=150)
        view_table.pack(expand=True, fill="both")

        rows_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=view_table.yview)
        rows_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        cols_scrollbar = ttk.Scrollbar(table_frame, orient="horizontal", command=view_table.xview)
        cols_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        # Configure the treeview's y and x scrollcommand
        view_table.configure(yscrollcommand=rows_scrollbar.set, xscrollcommand=cols_scrollbar.set)

        # read all data from our csv file to the ttk treeview table
        with open("union_data.csv", mode="r", newline="") as output_csv:
            reader = csv.reader(output_csv)
            header = next(reader)
            for i in reader:
                view_table.insert("", tk.END, values=(*i,))

    #define error testing here for summative 2



summ_app = UnionCollect()
summ_app.mainloop()

