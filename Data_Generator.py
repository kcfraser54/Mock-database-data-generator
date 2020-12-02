#Kyle Fraser
#PDA4
#CPSC 3300
#2/17/2020
#This program generates data to go into a ski resort database.
#Data is read from and written to csv files.

import random
import string
import csv


#Creates the lift ticket table  

type = ["standard season pass",
"college season pass",
"youth season pass",
"senior season pass",
"night season pass"]

ssp = "$500.00"
csp = "$400.00"
ysp = "$300.00"
seniorsp = "$200.00"
nsp = "$275.00"


with open('ticket_id.csv', 'w', newline='') as f:
    writeTo = csv.writer(f)

    writeTo.writerow(['T_ID', 'T_Type', 'Price'])


    for i in range(0,3000):

        random_type = random.choice(type)

        if random_type == type[0]:
            writeTo.writerow([i, random_type, ssp])


        elif random_type == type[1]:
            writeTo.writerow([i, random_type, csp])


        elif random_type == type[2]:
            writeTo.writerow([i, random_type, ysp])


        elif random_type == type[3]:
            writeTo.writerow([i, random_type, seniorsp])


        elif random_type == type[4]:
            writeTo.writerow([i, random_type, nsp])


f.close()


#Creates the customer table

cids = []
fname = []
lname = []
phone = []
email = []
dob = []
t_id = []
count = 0;
with open('customerData.csv', 'w', newline='') as cusF:
    writeTo = csv.writer(cusF)

    writeTo.writerow(['Cus_ID', 'Fname', 'Lname', 'Phone', 'Email', 'DOB', 'T_ID'])
    with open('Customerdata1.csv') as Cfile1:
        csvReader = csv.reader(Cfile1)
        next(csvReader)
        for row in csvReader:
            cids.append(count)
            fname.append(row[1])
            lname.append(row[2])
            phone.append(row[3])
            email.append(row[4])
            dob.append(row[5])
            need = True
            while need == True:
                random_tid = random.randint(0,2999)
                if random_tid not in t_id:
                    str(random_tid)
                    t_id.append(random_tid)
                    need = False
                elif random_tid in t_id:
                    need = True

                


            writeTo.writerow([cids[count], fname[count], lname[count], phone[count], email[count], dob[count], t_id[count]])
            count = count + 1
        
    


    Cfile1.close()
    count = 1000
    with open('Customerdata2.csv') as Cfile2:
        csvReader = csv.reader(Cfile2)
        next(csvReader)
        for row in csvReader:
            cids.append(count)
            fname.append(row[1])
            lname.append(row[2])
            phone.append(row[3])
            email.append(row[4])
            dob.append(row[5])
            need = True
            while need == True:
                random_tid = random.randint(0,2999)
                if random_tid not in t_id:
                    str(random_tid)
                    t_id.append(random_tid)
                    need = False
                elif random_tid in t_id:
                    need = True
            writeTo.writerow([cids[count], fname[count], lname[count], phone[count], email[count], dob[count], t_id[count]])
            count = count + 1


    Cfile2.close()
    count = 2000
    with open('Customerdata3.csv') as Cfile3:
        csvReader = csv.reader(Cfile3)
        next(csvReader)
        for row in csvReader:
            cids.append(count)
            fname.append(row[1])
            lname.append(row[2])
            phone.append(row[3])
            email.append(row[4])
            dob.append(row[5])
            need = True
            while need == True:
                random_tid = random.randint(0,2999)
                if random_tid not in t_id:
                    str(random_tid)
                    t_id.append(random_tid)
                    need = False
                elif random_tid in t_id:
                    need = True
            writeTo.writerow([cids[count], fname[count], lname[count], phone[count], email[count], dob[count], t_id[count]])
            count = count + 1


    Cfile3.close()
    cusF.close()


#Creates the employee table 


emp_id = []
emp_fname = []
emp_lname = []
salary = []
street = []
city = []
state = []
z_code = []
dob = []
job_Title = ["lift operator", "clerk", "instructor"]


count = 0
with open('employeeData.csv', 'w', newline = '') as empF:
    writeTo = csv.writer(empF)

    writeTo.writerow(['Emp_ID', 'Emp_Fname', 'Emp_Lname', 'Salary', 'Street', 'City', 'State', 'ZIP', 'DOB', 'Job_Title'])
    with open('Employeedata1.csv') as empFile1:
        csvReader = csv.reader(empFile1)
        next(csvReader)
        for row in csvReader:
            emp_id.append(count)
            emp_fname.append(row[1])
            emp_lname.append(row[2])
            salary.append(row[3])
            street.append(row[4])
            city.append(row[5])
            state.append(row[6])
            dob.append(row[7])

            zipCode = random.randint(10000, 99999)
            str(zipCode)
            z_code.append(zipCode)
            if count <= 30:
                jobName = job_Title[0]
            elif count <= 60:
                jobName = job_Title[1]
            elif count <= 100:
                jobName = job_Title[2]
            writeTo.writerow([emp_id[count], emp_fname[count], emp_lname[count], salary[count], street[count], city[count], state[count], z_code[count], dob[count], jobName])
            count = count + 1

    empFile1.close()

empF.close()


#Creates the class table 


class_price = ["$25.00", "$50.00", "$75.00", "$100.00"]

with open('classData.csv', 'w', newline = '') as classF:
    writeTo = csv.writer(classF)
    writeTo.writerow(['Class_ID', 'Class_Price'])
    for i in range(0, 40):
        if i <= 10:
            writeTo.writerow([i, "$25.00"])

        elif i <= 20:
            writeTo.writerow([i, "$50.00"])

        elif i <= 30:
            writeTo.writerow([i, "$75.00"])

        else:
            writeTo.writerow([i, "$100.00"])

    classF.close()
                
                



#creates the lift table 


lift_name = ["Bunny hill", "Easy Ride", "Smooth sailing", "Park", "Backcountry", "Green mountain",
             "Blue Mountain", "Big Mountain", "Golden Nugget", "Holiday"]

with open('liftData.csv', 'w', newline = '') as liftF:
    writeTo = csv.writer(liftF)
    writeTo.writerow(['Lift_ID', 'Lift_Name'])
    for i in range(0, 10):
        writeTo.writerow([i, lift_name[i]])

liftF.close()





#Creates the accesses table

with open('accessData.csv', 'w', newline = '') as accessF:
    writeTo = csv.writer(accessF)
    writeTo.writerow(['T_ID', 'Lift_ID'])
    for i in range(0,499):
        for j in range(0,4):
            writeTo.writerow([i, j])

    for i in range(500,999):
        for j in range(4,8):
            writeTo.writerow([i, j])

    for i in range(1000,1999):
        for j in range(0,8):
            writeTo.writerow([i, j])

    for i in range(2000,2999):
        for j in range(0,10):
            writeTo.writerow([i, j])

accessF.close()



#Creates the operates table 

with open('operateData.csv', 'w', newline = '') as operateF:
    writeTo = csv.writer(operateF)
    writeTo.writerow(['Emp_ID', 'Lift_ID'])

    for i in range(0,3):
        writeTo.writerow([i, '0'])

    for i in range(3,6):
        writeTo.writerow([i, '1'])

    for i in range(6,9):
        writeTo.writerow([i, '2'])

    for i in range(9,12):
        writeTo.writerow([i, '3'])

    for i in range(12,15):
        writeTo.writerow([i, '4'])

    for i in range(15,18):
        writeTo.writerow([i, '5'])

    for i in range(18,21):
        writeTo.writerow([i, '6'])

    for i in range(21,24):
        writeTo.writerow([i, '7'])

    for i in range(24,27):
        writeTo.writerow([i, '8'])

    for i in range(27,31):
        writeTo.writerow([i, '9'])

operateF.close()


#Creates the teaches table


with open('teachesData.csv', 'w', newline = '') as teachesF:
    writeTo = csv.writer(teachesF)
    writeTo.writerow(['Emp_ID', 'Class_ID'])


    count = 0;
    for i in range(61,72):
        writeTo.writerow([i, count])
        count = count +1;
        if count != 11 & i == 70:
            range = 69

    count = 11;
    for i in range(70,80):
        writeTo.writerow([i, count])
        count = count + 1

    count = 21
    for i in range(80,90):
        writeTo.writerow([i, count])
        count = count + 1
        

    count = 30
    for i in range(90,100):
        writeTo.writerow([i, count])
        count = count + 1

teachesF.close()



#Creates the class type table

class_type = ["Beginner", "Intermediate", "Expert", "Freestyle"]

with open('class_typeData.csv', 'w', newline = '') as classTypeF:
    writeTo = csv.writer(classTypeF)
    writeTo.writerow(['Class_ID', 'Class_Type'])


    for i in range(0,10):
        writeTo.writerow([i, class_type[0]])

    for i in range(10,20):
        writeTo.writerow([i, class_type[1]])

    for i in range(20,30):
        writeTo.writerow([i, class_type[2]])

    for i in range(30,40):
        writeTo.writerow([i, class_type[3]])


classTypeF.close()



    
#creates the takes table 


with open('takesData.csv', 'w', newline = '') as takesF:
    writeTo = csv.writer(takesF)
    writeTo.writerow(['Cus_ID', 'Class_ID'])

    count = 0;
    for i in range(1000,1200):
        writeTo.writerow([i, count])
        if i % 20 == 0:
            count = count + 1

    count = 10
    for i in range(1200,1400):
        writeTo.writerow([i, count])
        if i % 20 == 0:
            count = count + 1

    count = 20
    for i in range(1400,1600):
        writeTo.writerow([i, count])
        if i % 20 == 0:
            count = count + 1


    count = 30
    for i in range(1600,1800):
        writeTo.writerow([i, count])
        if i % 20 == 0:
            count = count + 1
            if count == 40:
                break


takesF.close()






#creates the payment method table 

cashPaid = ['$0.00', '$25.00', '$50.00', '$75.00', '$100.00', '$250.00', '$500.00']
ccNum = []

with open('paymentData.csv', 'w', newline = '') as paymentF:
    writeTo = csv.writer(paymentF)
    writeTo.writerow(['Cus_ID', 'Credit Card Number', 'Cash Paid'])

    with open('ccdata1.csv') as ccfile1:
        csvReader = csv.reader(ccfile1)
        next(csvReader)
        for row in csvReader:
            ccNum.append(row)
    ccfile1.close()


    with open('ccdata2.csv') as ccfile2:
        csvReader = csv.reader(ccfile2)
        next(csvReader)
        for row in csvReader:
            ccNum.append(row)
    ccfile2.close()

    with open('ccdata3.csv') as ccfile3:
        csvReader = csv.reader(ccfile3)
        next(csvReader)
        for row in csvReader:
            ccNum.append(row)
    ccfile3.close()
    
    for i in range(0,3000):
        if i < 500:
            writeTo.writerow([i, ccNum[i], cashPaid[0]])

        elif i < 1000:
            writeTo.writerow([i, ccNum[i], cashPaid[1]])

        elif i < 1300:
            writeTo.writerow([i, ccNum[i], cashPaid[2]])

        elif i < 1800:
            writeTo.writerow([i, ccNum[i], cashPaid[3]])

        elif i < 2100:
            writeTo.writerow([i, ccNum[i], cashPaid[4]])

        elif i < 2500:
            writeTo.writerow([i, ccNum[i], cashPaid[5]])

        elif i < 3000:
            writeTo.writerow([i, ccNum[i], cashPaid[6]])

paymentF.close()
        


