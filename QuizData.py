'''
Importing modules:
-plotly.express(px)
-pandas(pd)
-csv
-statistics
-time
'''
import plotly.express as px
import pandas as pd 
import csv
import statistics
import time

#Introductory statement, displaying all possible main choices and user inputs
print("Welcome to QuizData.py, teacher! We have created a program to statistically and graphically view and analyze your students' performance on a particular quiz. We wish you a smooth and ecstatic experience!")

initial_choice_list=["Unusable_Element","Display the statistics of all the levels' attempts","Display the statistics of all the levels' attempts","Display all the statistics of a particular student ","Display all the statistics of a particular level "]

initial_list_index=0
for initial_choice in initial_choice_list[1:]:
    initial_list_index+=1
    print(str(initial_list_index)+":"+initial_choice)

user_initial_choice=int(input("Please enter the corresponding index of the action you desire to be conducted:"))    
time.sleep(1.3)

intial_choice_final=initial_choice_list[user_initial_choice]

#Reading the data from the file 
dataframe_quiz_data=pd.read_csv("data.csv")

#Verifying and integrating the user input
#Case 1
if(int(user_initial_choice==1)):
    print(intial_choice_final)
    #Mean Value
    print("Calculating the mean value...")
    time.sleep(3.4)

    student_list_mean=[]

    student_dataframe_mean=dataframe_quiz_data.groupby("Student_Id")["Attempt"].mean()
    
    for row in student_dataframe_mean:
        student_list_mean.append(row)
        
    student_list_mean_min=round(min(student_list_mean),5)
    student_list_mean_max=round(max(student_list_mean),5)
    student_list_mean_mean=round(statistics.mean(student_list_mean),5)
    student_list_mean_standard_deviation=round(statistics.stdev(student_list_mean),5)
    
    scatter_all_mean=px.scatter(y=student_list_mean,x=["TRL_123","TRL_987","TRL_abc","TRL_imb","TRL_mda","TRL_mno","TRL_rst","TRL_xsl","TRL_xyz","TRL_zet","TRL_zny"],size=student_list_mean,color=student_list_mean)
    scatter_all_mean.update_layout(shapes=[dict(type="rect",y0=student_list_mean_min,y1=student_list_mean_max,x0=0,x1=11,fillcolor="green",layer="below"),dict(type="line",x0=0,x1=11,y0=student_list_mean_mean,y1=student_list_mean_mean)])
    scatter_all_mean.show()

    print("The minimum average is:"+str(student_list_mean_min))
    print("The mean value of the average is:"+str(student_list_mean_mean))
    print("The standard deviation of the attempts is:"+str(student_list_mean_standard_deviation))
    print("The maximum average is:"+str(student_list_mean_max)) 
    time.sleep(0.8)

    #Sum Value
    print("Calculating the sum value...")
    time.sleep(3.4)

    student_list_sum=[]

    student_dataframe_sum=dataframe_quiz_data.groupby("Student_Id")["Attempt"].sum()

    for row in student_dataframe_sum:
        student_list_sum.append(row)

    student_list_sum_min=min(student_list_sum)
    student_list_sum_max=max(student_list_sum)
    student_list_sum_mean=statistics.mean(student_list_sum)
    student_list_sum_standard_deviation=round(statistics.stdev(student_list_sum),5)

    
    scatter_all_sum=px.scatter(y=student_list_sum,x=["TRL_123","TRL_987","TRL_abc","TRL_imb","TRL_mda","TRL_mno","TRL_rst","TRL_xsl","TRL_xyz","TRL_zet","TRL_zny"],size=student_list_sum,color=student_list_sum)
    scatter_all_sum.update_layout(shapes=[dict(type="rect",y0=student_list_sum_min,y1=student_list_sum_max,x0=0,x1=11,fillcolor="green",layer="below"),dict(type="line",x0=0,x1=11,y0=student_list_sum_mean,y1=student_list_sum_mean)])
    scatter_all_sum.show()

    print("The minimum number of attempts is:"+str(student_list_sum_min))
    print("The mean value of the attempts is:"+str(student_list_sum_mean))
    print("The standard deviation of the attempts is:"+str(student_list_sum_standard_deviation))
    print("The maximum number of attempts is:"+str(student_list_sum_max)) 
    time.sleep(0.8)

    #Ending message  
    print("Thank you for using QuizData.py.")

#Case 2
if(int(user_initial_choice==2)):
    print(intial_choice_final)

    #Mean Value
    print("Calculating the mean value...")
    time.sleep(3.4)

    level_list_mean=[]

    level_dataframe_mean=dataframe_quiz_data.groupby("Level")["Attempt"].mean()

    for row in level_dataframe_mean:
        level_list_mean.append(row)

    level_list_mean_min=round(min(level_list_mean),5)
    level_list_mean_max=round(max(level_list_mean),5)
    level_list_mean_mean=round(statistics.mean(level_list_mean),5)
    level_list_mean_standard_deviation=round(statistics.stdev(level_list_mean),5)
  
    scatter_all_mean=px.scatter(y=level_list_mean,x=["Level 1","Level 2","Level 3","Level 4"],size=level_list_mean,color=level_list_mean)
    scatter_all_mean.update_layout(shapes=[dict(type="rect",y0=level_list_mean_min,y1=level_list_mean_max,x0=0,x1=11,fillcolor="green",layer="below"),dict(type="line",x0=0,x1=11,y0=level_list_mean_mean,y1=level_list_mean_mean)])
    scatter_all_mean.show()

    print("The minimum average is:"+str(student_list_mean_min))
    print("The mean value of the average is:"+str(student_list_mean_mean))
    print("The standard deviation of the attempts is:"+str(level_list_mean_standard_deviation))
    print("The maximum average is:"+str(student_list_mean_max))
    time.sleep(0.8) 

    #Sum Value
    print("Calculating the sum value...")
    time.sleep(3.4)

    level_list_sum=[]

    level_dataframe_sum=dataframe_quiz_data.groupby("Level")["Attempt"].sum()

    for row in level_dataframe_sum:
        level_list_sum.append(row)

    level_list_sum_min=min(level_list_sum)
    level_list_sum_max=max(level_list_sum)
    level_list_sum_mean=statistics.mean(level_list_sum)
    level_list_sum_standard_deviation=round(statistics.stdev(level_list_sum),5)

    scatter_all_sum=px.scatter(y=level_list_sum,x=["Level 1","Level 2","Level 3","Level 4"],size=level_list_sum,color=level_list_sum)
    scatter_all_sum.update_layout(shapes=[dict(type="rect",y0=level_list_sum_min,y1=level_list_sum_max,x0=0,x1=11,fillcolor="green",layer="below"),dict(type="line",x0=0,x1=11,y0=level_list_sum_mean,y1=level_list_sum_mean)])
    scatter_all_sum.update_yaxes(rangemode="tozero")
    scatter_all_sum.show()

    print("The minimum number of attempts is:"+str(level_list_sum_min))
    print("The mean value of the attempts is:"+str(level_list_sum_mean))
    print("The standard deviation of the attempts is:"+str(level_list_sum_standard_deviation))
    print("The maximum number of attempts is:"+str(level_list_sum_max)) 
    time.sleep(0.8)

    #Ending message  
    print("Thank you for using QuizData.py.")

#Case 3
if(int(user_initial_choice)==3):
    print(intial_choice_final)

    student_choice_index=0

    student_choice_list=["Unusable_Element","TRL_123","TRL_987","TRL_abc","TRL_imb","TRL_mda","TRL_mno","TRL_rst","TRL_xsl","TRL_xyz","TRL_zet","TRL_zny"]

    for student_choice in student_choice_list[1:]:
        student_choice_index+=1
        print(str(student_choice_index)+":"+student_choice)

    user_student_choice=int(input("Please enter the corresponding index of the student whose statistics are desired to see:"))

    user_selected_choice_merged_index=student_choice_list[user_student_choice]

    dataframe_students=dataframe_quiz_data.loc[dataframe_quiz_data["Student_Id"]==str(user_selected_choice_merged_index)]

    dataframe_students_grouped_mean=dataframe_students.groupby("Level")["Attempt"].mean()
    dataframe_students_grouped_sum=dataframe_students.groupby("Level")["Attempt"].sum()

    #Mean Value
    print("Calculating the mean value...")
    time.sleep(3.4)

    scatter_specific_students_mean=px.scatter(y=dataframe_students_grouped_mean,x=["Level 1","Level 2","Level 3","Level 4"],size=dataframe_students_grouped_mean,color=dataframe_students_grouped_mean)
    scatter_specific_students_mean.show()

    #Sum Value
    print("Calculating the sum value...")
    time.sleep(3.4)

    scatter_specific_students_sum=px.scatter(y=dataframe_students_grouped_sum,x=["Level 1","Level 2","Level 3","Level 4"],size=dataframe_students_grouped_sum,color=dataframe_students_grouped_sum)
    scatter_specific_students_sum.show()

    #Ending message  
    print("Thank you for using QuizData.py.")

#Case 4
if(int(user_initial_choice)==4):
    print(intial_choice_final)

    level_choice_index=0

    level_choice_list=["Unusable_Element","Level 1","Level 2","Level 3","Level 4"]

    for level_choice in level_choice_list[1:]:
        level_choice_index+=1
        print(str(level_choice_index)+":"+level_choice)

    user_level_choice=int(input("Please enter the corresponding index of the level whose statistics are desired to see:"))

    user_selected_choice_merged_index=level_choice_list[user_level_choice]    

    dataframe_levels=dataframe_quiz_data.loc[dataframe_quiz_data["Level"]==str(user_selected_choice_merged_index)]

    dataframe_levels_grouped_mean=dataframe_levels.groupby("Student_Id")["Attempt"].mean()
    dataframe_levels_grouped_sum=dataframe_levels.groupby("Student_Id")["Attempt"].sum()

    #Mean Value
    print("Calculating the mean value...")
    time.sleep(3.4)     

    scatter_specific_levels_mean=px.scatter(y=dataframe_levels_grouped_mean,x=["TRL_123","TRL_987","TRL_abc","TRL_imb","TRL_mda","TRL_mno","TRL_xsl","TRL_xyz","TRL_zet","TRL_zny"],size=dataframe_levels_grouped_mean,color=dataframe_levels_grouped_mean)
    scatter_specific_levels_mean.show()

    #Sum Value
    print("Calculating the sum value...")
    time.sleep(3.4)

    scatter_specific_levels_sum=px.scatter(y=dataframe_levels_grouped_sum,x=["TRL_123","TRL_987","TRL_abc","TRL_imb","TRL_mda","TRL_mno","TRL_xsl","TRL_xyz","TRL_zet","TRL_zny"],size=dataframe_levels_grouped_sum,color=dataframe_levels_grouped_sum)
    scatter_specific_levels_sum.show() 

    #Ending message  
    print("Thank you for using QuizData.py.")
    





  

