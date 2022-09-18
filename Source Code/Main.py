import mysql.connector as sql

conn=sql.connect(host='localhost',user='root', passwd='M@sterS4M4')
if conn.is_connected():
    print("***Successfully connected***")

while True:

    try:
        print("SHOP MANAGEMENT SYSTEM")
        print("1. Register")
        print("2. Login")
        print("3. Delete Account")
        print("4. Exits")
        choice=int(input("Enter your choice :"))
    except:
        print("Invalid Input")
    # REGISTER BLOCK :

    if choice == 1:
        try:
            name = input("Enter a unique username :")
            c=conn.cursor()
            c.execute('create database {} ;'.format(name))
            c.execute('use {} ;'.format(name))
            c.execute('create table product_detail(Product_Code varchar(20) not null PRIMARY KEY, Name varchar(30), Cost integer, Discount integer, Net_cost integer, Quantity integer) ;')#####
            c.execute('create table workers_detail(Worker_Code varchar(20) not null PRIMARY KEY, Name varchar(30), Phone_number char(10), Address varchar(100), Position varchar(30), Salary integer) ;')#####
            conn.commit()
            print("Successfully registered")
        except:
            print("This username already exist. Please Choose a different username")

    # LOGIN BLOCK
               
    elif choice == 2:
        try:
            name = input("Enter your usernamename :")
            c=conn.cursor()
            c.execute('use {} ;'.format(name))
            conn.commit()
            print("Successfully logged in")
        except:
            print("Invalid Input")
            break

        while True:

            try:
                print("List :")
                print("1. Customer")
                print("2. Product")
                print("3. Worker")
                print("4. Logout")
                choice_l = int(input("Enter your choice :"))
            except:
                print("Invalid Input")
            # CUSTOMER BLOCK
                           
            if choice_l==1:
                try:
                    print("List :")
                    print("1. View")
                    print("2. Edit exiting")
                    print("3. Add New")
                    print("4. Back")
                    choice_c=int(input("Enter your choice :"))
                except:
                    print("Invalid Input")
                    
                # VIEW BLOCK

                if choice_c==1:
                    try:
                        customer_name=input("Enter name of customer :")
                        phone_number=input("Enter phone number of customer :")
                        table_name= customer_name+phone_number
                        c=conn.cursor()
                        c.execute('select * from {} ;'.format(table_name))#####
                        data=c.fetchall()
                        for row in data:
                            print(row)
                        conn.commit()
                    except:
                        print("Invalid Input")
                        
                # EDIT BLOCK
                                       
                elif choice_c==2:
                    try:
                        print("List :")
                        print("1. Update Record")
                        print("2. Clear All Records")
                        print("3. Delete")
                        print("4. Back")
                        choice_e=int(input("Enter your choice :"))
                    except:
                        print("Invalid Input")

                    # UPDATE BLOCK
                                                                
                    if choice_e==1:
                        try:
                            customer_name=input("Enter name of customer :")
                            phone_number=input("Enter phone number of customer :")
                            table_name= customer_name+phone_number
                            product_code=int(input("Enter product code :"))
                            c=conn.cursor()
                            c.execute('insert into {} select Name, Net_cost from product_detail where Product_code= {} ;'.format(table_name,product_code))#####
                            conn.commit()
                        except:
                            print("Invalid Input")

                    # CLEAR BLOCK
                                                                
                    elif choice_e==2:
                        try:
                            customer_name=input("Enter name of customer :")
                            phone_number=input("enter phone number of customer :")
                            table_name= customer_name+phone_number
                            c=conn.cursor()
                            c.execute('delete from {} ;'.format(table_name))#####
                            conn.commit()
                        except:
                            print("Invalid Input")
                                                                    
                    # DELETE BLOCK
                                                                
                    elif choice_e==3:
                        try:
                            customer_name=input("Enter name of customer :")
                            phone_number=input("enter phone number of customer :")
                            table_name= customer_name+phone_number
                            c=conn.cursor()
                            c.execute('drop table {}'.format(table_name))#####
                            conn.commit()
                        except:
                            print("Invalid Input")

                    #BACK BLOCK

                    elif choice_e==4:
                        pass
                                                                
                # ADD BLOCK
                                                                
                elif choice_c==3:
                    try:
                        customer_name=input("Enter name of customer :")
                        phone_number=input("enter phone number of customer :")
                        table_name= customer_name + phone_number
                        c=conn.cursor()
                        c.execute('create table {} (Product varchar(30), Net_cost integer) ;'.format(table_name))#####
                        conn.commit()
                        print("Customer Added Successfully")
                        print("Go to Edit to add record")
                    except:
                        print("Invalid Input")
                    
            # PRODUCT BLOCK
                                                                
            elif choice_l==2:
                try:
                    print("List :")
                    print("1. View All")
                    print("2. View One")
                    print("3. Update List")
                    print("4. Add New")
                    print("5. Delete")
                    print("6. Back")
                    choice_p=int(input("Enter your choice :"))
                except:
                    print("Invalid Input")

                #VIEW ALL BLOCK
                
                if choice_p==1:
                    try:
                        c=conn.cursor()
                        c.execute('select * from product_detail ;')#####
                        data=c.fetchall()
                        for row in data:
                            print(row)
                        conn.commit()
                    except:
                        print("Invalid Input")

                #VIEW ONE BLOCK
                    
                elif choice_p==2:
                    try:
                        product_code=input("Enter Product Code :")
                        c=conn.cursor()
                        c.execute('select * from product_detail where Product_Code={};'.format(product_code))#####
                        data=c.fetchall()
                        for row in data:
                            print(row)
                        conn.commit()
                    except:
                        print("Invalid Input")

                #UPDATE BLOCK
                    
                elif choice_p==3:
                    try:
                        product_code=int(input("Enter Product Code :"))
                        product_name=input("Enter Product name :")
                        product_cost=int(input("Enter Product cost :"))
                        product_discount=int(input("Enter Product discount :"))
                        product_net_cost=product_cost-product_discount
                        product_quantity=int(input("Enter Product quantity :"))
                        c=conn.cursor()
                        c.execute('update product_detail set Name="{}", Cost={}, Discount={}, Net_cost={}, Quantity={} where Product_code={} ;'.format(product_name,product_cost,product_discount,product_net_cost,product_quantity,product_code))#####
                        conn.commit()
                    except:
                        print("Invalid Input")
                    
                #ADD BLOCK
                        
                elif choice_p==4:
                    try:
                        product_code=int(input("Enter Product Code(Only numeric and should be unique) :"))
                        product_name=input("Enter Product name :")
                        product_cost=int(input("Enter Product cost :"))
                        product_discount=int(input("Enter Product discount :"))
                        product_net_cost=product_cost - product_discount
                        product_quantity=int(input("Enter Product quantity :"))
                        c=conn.cursor()
                        c.execute('insert into product_detail values({},"{}",{},{},{},{}) ;'.format( product_code, product_name, product_cost, product_discount, product_net_cost, product_quantity))#####
                        conn.commit()
                    except:
                        print("Invalid Input")
                    
                # DELETE BLOCK
                                                            
                elif choice_p==5:
                    try:
                        product_code=int(input("Enter Product Code :"))
                        c=conn.cursor()
                        c.execute('delete from product_detail where Product_code={}'.format(product_code))#####
                        conn.commit()
                    except:
                        print("Invalid Input")
                    
                #BACK BLOCK
                    
                elif choice_p==6:
                    pass
                    
            # WORKER BLOCK
                                                                
            elif choice_l==3:
                try:
                    print("List :")
                    print("1. View All")
                    print("2. View One")
                    print("3. Update List")
                    print("4. Add New")
                    print("5. Delete")
                    print("6. Back")
                    choice_w=int(input("Enter your choice :"))
                except:
                    print("Invalid Input")

                #VIEW ALL BLOCK
                
                if choice_w==1:
                    try:
                        c=conn.cursor()
                        c.execute('select * from Workers_Detail ;')#####
                        data=c.fetchall()
                        for row in data:
                            print(row)
                        conn.commit()
                    except:
                        print("Invalid Input")

                #VIEW ON EBLOCK
                    
                elif choice_w==2:
                    try:
                        worker_code=input("Enter Worker code :")
                        c=conn.cursor()
                        c.execute('select * from Workers_Detail where Worker_Code={} ;'.format(worker_code))#####
                        data=c.fetchall()
                        for row in data:
                            print(row)
                        conn.commit()
                    except:
                        print("Invalid Input")
                   
                #UPDATE BLOCK
                        
                elif choice_w==3:
                    try:
                        worker_code=int(input("Enter Worker code :"))
                        worker_name=input("Enter new name of worker :")
                        worker_phone=input("Enter new phone number of worker :")
                        worker_address=input("Enter new address of worker :")
                        worker_position=input("Enter new position of worker :")
                        worker_salary=int(input("Enter new salary of worker :"))
                        c=conn.cursor()
                        c.execute('update workers_detail set Name="{}", Phone_number="{}", Address="{}", Position="{}", Salary={} where Worker_code={} ;'.format(worker_name,worker_phone,worker_address,worker_position,worker_salary,worker_code))#####
                        conn.commit()
                    except:
                        print("Invalid Input")

                #ADD BLOCK
                    
                elif choice_w==4:
                    try:
                        worker_code=int(input("Enter Worker Code( Should contain numeric values only and should be unique ) :"))
                        worker_name=input("Enter Worker name :")
                        worker_phone=input("Enter Worker phone number :")
                        worker_address=input("Enter Worker address :")
                        worker_position=input("Enter Worker position :")
                        worker_salary=int(input("Enter Worker salary :"))
                        c=conn.cursor()
                        c.execute('insert into workers_detail values({},"{}","{}","{}","{}",{});'.format(worker_code,worker_name,worker_phone,worker_address,worker_position,worker_salary))#####
                        conn.commit()
                    except:
                        print("Invalid Input")

                # DELETE BLOCK
                                                            
                elif choice_w==5:
                    try:
                        worker_code=int(input("Enter Worker Code :"))
                        c=conn.cursor()
                        c.execute('delete from workers_detail where Worker_code={}'.format(worker_code))#####
                        conn.commit()
                    except:
                        print("Invalid Input")

                #BACK BLOCK
                    
                elif choice_w==6:
                    pass

            #LOGOUT BLOCK
                    
            elif choice_l==4:
                break

    #DELETE ACOUNT BLOCK

    elif choice==3:
        try:
            acc_name=input("Enter name of account to be deleted :")
            print("***WARNING: This will permanently delete the account along with all the records***")
            print("1. Proceed")
            print("2. Cancel")
            choice_b=int(input("Enter your choice :"))
        except:
            print("Invalid Input")
        #PEOCEED BLOCK

        if choice_b==1:
            c=conn.cursor()
            c.execute('drop database {}'.format(acc_name))
            conn.commit()
            print("Account successfully deleted")

        #CANCEL BLOCK

        elif choice_b==2:
            pass
    # EXIT BLOCK

    elif choice == 4:
        exit()
