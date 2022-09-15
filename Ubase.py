from tkinter import *
from tkinter import ttk
import mysql.connector
import csv


root=Tk()

root.title("Ubase")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rahul@123",
    database="temp"
)
c=mydb.cursor()

# c.execute("CREATE DATABASE  temp")
#checking database is created or not

c.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255),last_name VARCHAR(255), pincode INT(10),user_id INT AUTO_INCREMENT PRIMARY KEY)")
'''
c.execute("ALTER TABLE customers ADD(\
            email VARCHAR(255),\
            city VARCHAR(40),\
            mobileNo VARCHAR(20))")
'''
# c.execute("ALTER TABLE customers MODIFY mobileNo VARCHAR(20)")

def write_to_excel(records):
    with open('Customer.csv','a',newline='') as f:
        data=csv.writer(f,dialect="excel")
        for record in records:
            data.writerow(record)


def showrec():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rahul@123",
    database="temp"
    )
    c=mydb.cursor()
    showrec_win=Tk()
    Headline=Label(showrec_win,text="Records",font="BIGJOHN 22 bold ",padx=20,pady=30).grid(row=0,column=0,columnspan=5)
    l1=Label(showrec_win,text="First Name",padx=10,pady=10).grid(row=1,column=0)
    l2=Label(showrec_win,text="Last Name",padx=10,pady=10).grid(row=1,column=1)
    l3=Label(showrec_win,text="Pincode",padx=10,pady=10).grid(row=1,column=2)
    l4=Label(showrec_win,text="Email",padx=10,pady=10).grid(row=1,column=3)
    l5=Label(showrec_win,text="City",padx=10,pady=10).grid(row=1,column=4)
    l6=Label(showrec_win,text="Mobile",padx=10,pady=10).grid(row=1,column=5)
    c.execute("SELECT first_name,last_name,pincode,email,city,mobileNo"" FROM customers")
    records=c.fetchall()
    for things in c.description:
        print(things)
    rows=2
    for record in records:
        for index,c in enumerate(record):
            
            L1=Label(showrec_win,text=record[index],padx=10,pady=10).grid(row=rows,column=index)
        rows+=1
    saverec=Button(showrec_win,text="Save to Excel",command=lambda: write_to_excel(records)).grid(row=rows,column=0,columnspan=5)
    
def search_customer():
      search_win=Tk()
      search_win.title("Search Customers")
      search_win.geometry("1000x600")
      
      def editnow(id,rows):
            sql2="SELECT * FROM customers WHERE user_id=%s"
            name2=(id,)
            print(id)
            result2=c.execute(sql2,name2)
            result2=c.fetchall()
            print(result2)
            firstname_label=Label(search_win,text="First Name").grid(row=rows,column=0,sticky=W,padx=20)
            lastname_label=Label(search_win,text="Last Name").grid(row=rows+1,column=0,sticky=W,padx=20)
            pincode_label=Label(search_win,text="Pincode").grid(row=rows+2,column=0,sticky=W,padx=20)
            email_label=Label(search_win,text="Email").grid(row=rows+3,column=0,sticky=W,padx=20)
            city_label=Label(search_win,text="City").grid(row=rows+4,column=0,sticky=W,padx=20)
            mobile_label=Label(search_win,text="Mobile No.").grid(row=rows+5,column=0,sticky=W,padx=20)
            user_label=Label(search_win,text="User ID").grid(row=rows+6,column=0,sticky=W,padx=20)

            global firstname_entry
            firstname_entry=Entry(search_win)
            firstname_entry.grid(row=rows,column=1)
            firstname_entry.insert(0,result2[0][0])
            global lastname_entry
            lastname_entry=Entry(search_win)
            lastname_entry.grid(row=rows+1,column=1)
            lastname_entry.insert(0,result2[0][1])
            global pincode_entry
            pincode_entry=Entry(search_win)
            pincode_entry.grid(row=rows+2,column=1)
            pincode_entry.insert(0,result2[0][2])
            global email_entry
            email_entry=Entry(search_win)
            email_entry.grid(row=rows+3,column=1)
            email_entry.insert(0,result2[0][4])
            global city_entry
            city_entry=Entry(search_win)
            city_entry.grid(row=rows+4,column=1)
            city_entry.insert(0,result2[0][5])
            global mobile_entry
            mobile_entry=Entry(search_win)
            mobile_entry.grid(row=rows+5,column=1)
            mobile_entry.insert(0,result2[0][6])
            global userid_entry
            userid_entry=Entry(search_win)
            userid_entry.grid(row=rows+6,column=1)
            userid_entry.insert(0,result2[0][3])
            
            
            
            Edit_record_btn=Button(search_win,text="Edit").grid(row=rows+7,column=0)
      
      def search():
          selected=search_combo.get()
          sql=""
          if selected=="Search By...":
              pass
          if selected=="Last Name":
              sql=("SELECT * FROM customers WHERE last_name=%s")
          if selected=="Pincode":
              sql=("SELECT * FROM customers WHERE pincode=%s")
          if selected=="Email Address":
              sql=("SELECT * FROM customers WHERE email=%s")
         
          toSearch=search_box.get()
        #   sql=("SELECT * FROM customers WHERE last_name=%s")
          name=(toSearch,)
          c.execute(sql,name)
          result=c.fetchall()
          if not result:
            l1=Label(search_win,text="Result Not Found").grid(row=2,column=0)
          else:
            rows=3
            for i,res in enumerate(result):
                id_refernce=str(res[3])
                Button(search_win,text="Edit"+id_refernce,command=lambda:editnow(id_refernce,rows)).grid(row=rows,column=0)
                for index,items in enumerate(res):
                    
                    res_label=Label(search_win,text=items).grid(row=rows,column=index+1,padx=10)
                rows+=1
            
                  
                   
      search_box=Entry(search_win)
      search_box.grid(row=0,column=1)
      search_label=Label(search_win,text="Search ")
      search_label.grid(row=0,column=0)
      search_button=Button(search_win,text="Search",command=search).grid(row=1,column=0)
      search_combo=ttk.Combobox(search_win,values=["Search By...","Last Name","Pincode","Email Address"])
      search_combo.current(0)
      search_combo.grid(row=0,column=2)
    
def clear_fields():
    firstname_entry.delete(0,END)
    lastname_entry.delete(0,END)
    pincode_entry.delete(0,END)
    email_entry.delete(0,END)
    city_entry.delete(0,END)
    mobile_entry.delete(0,END)
    
        


def submit():
    
    sql_command=("INSERT INTO  customers (first_name,last_name,pincode,email,city,mobileNo) VALUES (%s,%s,%s,%s,%s,%s)")
    values=(firstname_entry.get(),lastname_entry.get(),pincode_entry.get(),email_entry.get(),city_entry.get(),mobile_entry.get())
    c.execute(sql_command,values)
    mydb.commit()
    clear_fields()
                    

heading=Label(root ,text="CONSUMER's DATABASE").grid(row=0,column=0,columnspan=2,padx=20)
firstname_label=Label(root,text="First Name").grid(row=1,column=0,sticky=W,padx=20)
lastname_label=Label(root,text="Last Name").grid(row=2,column=0,sticky=W,padx=20)
pincode_label=Label(root,text="Pincode").grid(row=3,column=0,sticky=W,padx=20)
email_label=Label(root,text="Email").grid(row=4,column=0,sticky=W,padx=20)
city_label=Label(root,text="City").grid(row=5,column=0,sticky=W,padx=20)
mobile_label=Label(root,text="Mobile No.").grid(row=6,column=0,sticky=W,padx=20)

firstname_entry=Entry(root)
firstname_entry.grid(row=1,column=1)
lastname_entry=Entry(root)
lastname_entry.grid(row=2,column=1)
pincode_entry=Entry(root)
pincode_entry.grid(row=3,column=1)
email_entry=Entry(root)
email_entry.grid(row=4,column=1)
city_entry=Entry(root)
city_entry.grid(row=5,column=1)
mobile_entry=Entry(root)
mobile_entry.grid(row=6,column=1)


submit_btn=Button(root,text="Add to Database",command= submit).grid(row=7,column=0,pady=20)
clear_btn=Button(root,text="Clear Fields",command=lambda: clear_fields()).grid(row=7,column=1,pady=20)
c.execute("SELECT * FROM customers")
records=c.fetchall()
for things in records:
    print(things)

show_rec=Button(root,text="Show records",command=lambda:showrec()).grid(row=8,column=0)
search_rec=Button(root,text="Search/Edit Customer",command=lambda:search_customer()).grid(row=8,column=1)

root.mainloop()