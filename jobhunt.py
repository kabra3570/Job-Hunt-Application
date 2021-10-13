import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



print("Welcome to the Job Hunt application!")
print("You are looking for a job, and so you are using this program ")
print("to view job information you can use in your job search to help you ")
print("find a job.")

print("Is this your first time using this Job Hunt Application? ")
choice = input("Enter Y for yes. Enter anything else for no. ")

# if first time user using this application, load data from a default file
# called jobs.csv
if (choice == "Y"):
    jobs_data_frame = pd.read_csv("jobs.csv", index_col = 0)

else :
    print("Enter the name of the csv file you want to load the job data from. ")
    job_data_file = input("Make sure to end the file name with .csv ")
    jobs_data_frame = pd.read_csv(job_data_file, index_col = 0)

position_openings = jobs_data_frame[['Employee Name']].isna()
jobs_data_frame["Openings"] = jobs_data_frame['Openings'] = position_openings == True

company_jobs = jobs_data_frame.pivot_table(values="Salary", index=["Position"], columns="Company")
company_jobs = company_jobs.fillna("job doesn't exist")
salary_per_position = jobs_data_frame.pivot_table(values="Salary", index="Position", aggfunc=np.mean)
salary_per_position["Position"] = salary_per_position.index
openings_only = jobs_data_frame[jobs_data_frame['Openings'] == True]
openings_only["Applied?"] = "No"
jobs_data_frame["Applied?"] = "No"
# create an option menu so that the user can choose which part of the program
# to do at anytime, in any order

user_input = "start"



while user_input != "Q":
    print("\n\nOPTION MENU")
    print("1.) View the jobs")
    print("2.) See which jobs have openings")
    print("3.) View salary information about each available job")
    print("4.) View average salary per position")
    print("5.) Display bar graph about the average salary per position")
    print("6.) Apply for a job")
    print("Press Q to quit.")
    user_input = input()
#print("Would you like to view the jobs? ")
#user_input = input("Enter Y for yes. Enter anything else for no. ")

    if user_input == '1':
        print()
        print("Here are the jobs: ")
        print()
        # dont include that last openings column and include all the rows
        # regardless of the openigns value for them
        print(jobs_data_frame.loc[:, "Employee Name":"Location"])

    if user_input == '2':
        openings_only = openings_only.iloc[:, 1:]
        print(openings_only)
#print("Would you like to see which jobs have openings?")
#user_input = input("Enter Y for yes. Enter anything else for no. ")

#if user_input == 'Y':
#    jobs_data_frame['Openings'] = position_openings == True
#    openings_only = jobs_data_frame[jobs_data_frame['Openings'] == True]
#    openings_only = openings_only.iloc[:, 1:]
#    print(openings_only)

#print("Would you like to view salary information about each available job at each company? ")
#user_input = input("Enter Y for yes. Enter anything else for no. ")


    if user_input == "3":
        print(company_jobs)

#print("Would you like to view average salary per position? ")
#user_input = input("Enter Y for yes. Enter anything else for no. ")

    #salary_per_position.reset_index(drop=True)
    if user_input == "4":
        print(salary_per_position)
        #salary_per_position.reset_index(drop=True)

#print(jobs_data_frame)

#print("Would you like to display bar graph about the average salary per position? ")
#user_input = input("Enter Y for yes. Enter anything else for no. ")
    if user_input == "5":
        salary_per_position.plot(x="Position", y="Salary", title="Average Salary by Position", kind="bar")
        plt.xticks(rotation="0", ha="right")
        plt.show()
        plt.clf()

    if user_input == "6":
        print("Again, once more, here are the jobs that have openings: ")
        print(openings_only)

#print("Would you like to apply for a job? ")
#user_input = input("Enter Y for yes. Enter anything else for no. ")

        # initialize the entire applied column to no since the user
        # hasn't applied to anything yet
        user_input = 'Y'
        # create a list of all the names of the current jobs which exist
        # if the user types in a job name that isn't in the list, a new job shall
        # be created and added to the jobs dataframe
        names_of_current_jobs = openings_only.index
        while user_input == 'Y':
            job = input("Enter the name of the job you'd like to apply to, such as Job 1.")

            # if the user types in a job name that already exists,
            # the only piece of information needed to be added is to the Applied? column
            if job in names_of_current_jobs:
                openings_only.loc[job, "Applied?"] = "Yes"
                jobs_data_frame.loc[job, "Applied?"] = "Yes"
                print()
                print(openings_only)
                print()
                print("Would you like to apply for another job? ")
                user_input = input("Enter Y for yes. Enter anything else for no. ")
            # but if the user types in a job name that does not currently exist,
            # then more information is needed about each column
            else:
                openings_only.loc[job, "Applied?"] = "Yes"
                jobs_data_frame.loc[job, "Applied?"] = "Yes"
                # ask the user for more data (retrieve more data from the user about this job)
                # since it already doesn't currently exist
                print("You entered a job which does not already currently exist.")
                print("Therefore more information is needed about this job.")
                job_company = input("Please enter the company: ")
                job_position = input("Please enter the position: ")
                job_salary = int(input("Please enter the salary: "))
                job_location = input("Please enter the location: ")

                openings_only.loc[job, "Company"] = job_company
                openings_only.loc[job, "Position"] = job_position
                openings_only.loc[job, "Salary"] = job_salary
                openings_only.loc[job, "Location"] = job_location
                openings_only.loc[job, "Openings"] = True

                jobs_data_frame.loc[job, "Company"] = job_company
                jobs_data_frame.loc[job, "Position"] = job_position
                jobs_data_frame.loc[job, "Salary"] = job_salary
                jobs_data_frame.loc[job, "Location"] = job_location
                jobs_data_frame.loc[job, "Openings"] = True

                company_jobs = jobs_data_frame.pivot_table(values="Salary", index=["Position"], columns="Company")
                company_jobs = company_jobs.fillna("job doesn't exist")

                salary_per_position = jobs_data_frame.pivot_table(values="Salary", index="Position", aggfunc=np.mean)
                salary_per_position["Position"] = salary_per_position.index

                print(openings_only)
                print("Your new job has successfully been added, and your application has been sent.")
                print("Would you like to apply for another job? ")
                user_input = input("Enter Y for yes. Enter anything else for no.")

    if user_input != 'Q':
        enter = input("Press enter to continue.")


print("Enter the name of the csv file you would like your changes to be exported to ")
job_data_file = input("Make sure to end the file name with .csv ")
jobs_data_frame.to_csv(job_data_file);

print("Thank you for using this Job Hunt Application to view, look for, and apply for jobs!")
print("Your changes have been exported to a file.")
