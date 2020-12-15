import tkinter as tk
import xlsxwriter
import pandas as pd
import numpy as np

def user_LoginDetails():
    loginwindow=tk.Tk()
    loginwindow.geometry("350x250") 
    loginwindow.title("GJC Gubbi")
    
    lblName = tk.Label(loginwindow, text="GJC Gubbi Welcomes you", font=("Times New Roman", 20), fg ="Blue").place(x = 30, y = 0)
    lbl1Name = tk.Label(loginwindow, text="LOGIN as ",font=("Times New Roman", 15), fg = "Green").place(x = 90, y =40 ) 

    chkParent=tk.Checkbutton(loginwindow, text="Parent").place(x = 120, y = 70)
    chkTeacher=tk.Checkbutton(loginwindow, text="Teacher").place(x = 120, y = 100)
    chkClassTeacher=tk.Checkbutton(loginwindow, text="Class Teacher").place(x = 120, y = 130)
    chkStudent=tk.Checkbutton(loginwindow, text="Student").place(x = 120, y = 160) 
    
    def LoginCommand():
        #try(): 
        #Check any one of the checkbox has checked or not
        #except():  
        #return a print output as warning msg on Tikinter window
        loginwindow.destroy()

    btn=tk.Button(loginwindow, text=" Login ", bg="blue", fg="white", command = LoginCommand ).place(x=120, y=200)
   
    loginwindow.mainloop()
    
    
def classdetailswindow():
    classdetailswindow = tk.Tk()  
    classdetailswindow.title("Class Details")
    classdetailswindow.geometry("500x200") 

    lbl =tk.Label(classdetailswindow, text = "Please fill the below details : ", font=("Times New Roman", 15)).place(x= 25, y=15)
    std = tk.Label(classdetailswindow, text = "Enter the standard ").place(x = 30,y = 50)  
    no_Students = tk.Label(classdetailswindow, text = "Total number of student in Class : ").place(x = 30,y = 90)  
    no_Subjects = tk.Label(classdetailswindow, text = "Total number of subjects Class \"5\" Studying :").place(x = 30, y = 130)  


    std = tk.Entry(classdetailswindow).place(x = 280, y = 50)  
    no_Students = tk.Entry(classdetailswindow).place(x = 280, y = 90)  
    no_Subjects = tk.Entry(classdetailswindow).place(x = 280, y = 130) 

    def submitdetailswindow():
            #try(): 
            #Check all the entries
            #except():  
            #return a print output to write all entries as integer
            classdetailswindow.destroy()

    submitbtn = tk.Button(classdetailswindow, text = "Submit", command=submitdetailswindow , activebackground = "red", activeforeground = "blue").place(x = 250, y = 170) 
    classdetailswindow.mainloop()
    
    
def stud_subEntry():
    stud_subEntrywindow = tk.Tk()  
    stud_subEntrywindow.title("Entry Order")
    stud_subEntrywindow.geometry("380x200") 
    
    lbl =tk.Label(stud_subEntrywindow, text = "Please select the order of entry you make : ", font=("Times New Roman", 15)).place(x= 25, y=15)
    entrybyStud=tk.Checkbutton(stud_subEntrywindow, text="Student").place(x = 120, y = 70)
    entrybySubj=tk.Checkbutton(stud_subEntrywindow, text="Subject").place(x = 120, y = 100)
    
    def stud_subEntryCommand():
        #try(): 
        #Check any one of the checkbox has checked or not
        #except():  
        #return a print output as warning msg on Tikinter window
        stud_subEntrywindow.destroy()

    btn=tk.Button(stud_subEntrywindow, text=" Submit ", bg="blue", fg="white", command = stud_subEntryCommand ).place(x=120, y=150)
    stud_subEntrywindow.mainloop()
    
     
def studentList():
    studentlistwindow=tk.Tk()
    studentlistwindow.title("Student Detail Entries. ")
    studentlistwindow.geometry("350x200")
    lbl=tk.Label(studentlistwindow, text="Please add the entries for in alphabetical order : ").place(x=30, y= 10)
    student_Name =tk.Label(studentlistwindow, text="Enter the Student Name:", font=("Arial, 10")).place(x=30, y=50)
    roll_No = tk.Label(studentlistwindow, text="Enter the Roll No :", font= ("Arial, 10")).place(x=30, y=100)

    student_Name=tk.Entry(studentlistwindow).place(x=200, y= 50)
    roll_No=tk.Entry(studentlistwindow).place(x=200, y= 100)
    def studentlist_window():
            #try(): 
            #Check any one of the checkbox has checked or not
            #except():  
            #return a print output as warning msg on Tikinter window
        studentlistwindow.destroy()

    btn=tk.Button(studentlistwindow, text=" Submit ", command=studentlist_window).place(x=175, y=150)

    studentlistwindow.mainloop()
    
    
# Create as excel file and add the entries of student name by row, subjects in column
def create_excel():
    
    workbook=xlsxwriter.Workbook("Studentdata.xlsx")
    worksheet= workbook.add_worksheet("Class 7")
    worksheet.merge_range('C1:G1', 'Subjects')
    worksheet.write(1, 0, "Student Name")
    worksheet.write(1, 1, "Roll No")
    worksheet.merge_range('C1:G1') 

    row=1
    column=2
    subjects = []
    no_Of_Subjects= int(input("No of Subjects :"))
    for i in range(no_Of_Subjects):
        subjects1=str(input("Enter the subjects {}: ".format(i))).capitalize()
        subjects.append(subjects1)
    for ele in subjects:
        worksheet.write(row, column, ele)
        column +=1

    row=2
    column=0
    studentName=[]
    studentRollNo=[]

    no_of_Students = int(input(" Enter the Total Number of students : "))
    for i in range(no_of_Students):
        studentName1=str(input("Enter the student name : ")).capitalize()
        studentName.append(studentName1)
    for item in studentName:
        worksheet.write(row, column, item)
        row +=1

    workbook.close()

if __name__ == "__main__":
    
    #"""below functions request the user to logon to data as a Teacher student adn parents"""
    #user_LoginDetails()
    #"""Request user to enter class details"""
    #classdetailswindow()
    #"""Request the teacher to opt the add of entries in order of subject marks or students marks"""
    #stud_subEntry()
    #studentList()
    create_excel()