PROJECT ON GROCERY SHOP MANAGEMENT SYSTEM

INTRODUCTION
  This software is used to maintain the customer details, product details, workers detail of the shop updated and maintain records of in and out data of the shop

OBJECTIVES OF THE PROJECT

  The objective of this project is to let the students apply the programming knowledge into a real world situation/problem and exposed the students how programming skills helps in developing a good software.
    1. Write programs utilizing modern software tools.
    2. Apply Python Connectivity with MySQL effectively when developing small to medium sized projects.
    3. Write effective procedural code to solve small to medium sized problems.
    4. Students will demonstrate a breadth of knowledge in computer science, as exemplified in the areas of systems, theory and software development.
    5. Students will demonstrate ability to conduct a research or applied Computer Science project, requiring writing and presentation skills which exemplify scholarly style in computer science.

TABLES GENERATED
  
  PERMANENT TABLES
  
  · WORKERS DETAILS TABLE
    A table by the name of workers_deatil is created at the time of registration of any new user. This table has following Attributes:
    § Worker_Code
    § Name
    § Phone_number
    § Address
    § Position
    § Salary
  
  · PRODUCT DETAILS TABLE
    A table by the name of product_detail is created at the time of registration of any new user. This table has following Attributes:
    § Product_Code
    § Name
    § Cost
    § Discount
    § Net_cost
    § Quantity
  
DYNAMIC/TEMPORARY TABLES
  
  · COUSTOMER DETAILS TABLE
    A Table can be formed for any customer by unique combination of his/her Name and Number. This table has following Attributes:
    § Product
    § Net_cost

WORKING DESCRIPTION
This Program shows sets of actions that can be taken and asks the user to select his/her preferable choice and then it executes what user wants to do. The program consists of the following options:

  1. REGISTER
  After choosing this option the program will ask you to enter a unique username. After receiving the required details it will create a database under that username along with two other tables. The message “Successfully registered” will come on screen after successful implementation of code block. In case the username is not unique it will pop up a message saying “This username already exist. Please choose a different username”.
  
  2. LOGIN
  After choosing this option the program will ask you to enter your username. After receiving the required details it will log you in and show the message “Successfully logged in”, along with a 4 more options. In case the username is incorrect it will show the message “Invalid Input”.
  
  2.1 CUSTOMER
  After choosing this option the program will show the following list to choose from:
  
  2.1.1 VIEW
  After choosing this option the program will ask for Name and Phone Number of the customer and then display all the detail from that customer’s table.
  
  2.1.2 EDIT
  After choosing this option the program will show the following list to choose from:
  
  2.1.2.1 Update Record
  After choosing this option the program will ask for required details of customer and Fill the record in the customer’s table.
  
  2.1.2.2 Clear All Records
  After choosing this option program will ask for required details of customer and then delete all the records from that customer’s table.
  
  2.1.2.3 Delete
  After choosing this option program will ask for required details of customer and then remove the customer from the database along with all the records.
  
  2.1.2.4 Back
  This option will take you to previous menu
  
  2.1.3 ADD
  After choosing this option the program will ask for name and phone number of the customer, then it will create a unique table for that customer to store his records
  
  2.1.4 BACK
  This option will take you to previous menu
  
  2.2 PRODUCT
  After choosing this option the program will show the following list to choose from:
  
  2.2.1 View All
  This option will show all records of all the products in the product_detail table
  
  2.2.2 View One
  After Choosing this option program will ask for Product Code and then display all the records of that product
  
  2.2.3 Update List
  After choosing this option program will ask for required details of existing product and then update it in the table
  
  2.2.4 Add New
  After choosing this option program will ask for required details of new product and then add it in the table
  
  2.2.5 Delete
  After choosing this option the program will ask for the Product Code and then delete all records of that product
  
  2.2.6 Back
  This option will take you to previous menu
  
  2.3 WORKER
  After choosing this option the program will show the following list to choose from:
  
  2.3.1 View All
  This option will show all records of all the workers in the workers_detail table
  
  2.3.2 View One
  After Choosing this option program will ask for Worker Code and then display all the records of that worker
  
  2.3.3 Update List
  After choosing this option program will ask for required details of existing worker and then update it in the table
  
  2.3.4 Add New
  After choosing this option program will ask for required details of new worker and then add it in the table
  
  2.3.5 Delete
  After choosing this option the program will ask for the Worker Code and then delete all records of that product
  
  2.3.6 Back
  This option will take you to previous menu
  
  2.4 LOGOUT
  This option will log out the user to the main menu
  
  3. DELETE ACCOUNT
  After choosing this option the program will ask for username and then show a confirmatory option showing two options as follows:
  
  3.1 PROCEED
  This option will delete the account of the user along with all the data
  
  3.2 CANCEL
  This option will stop deletion of account
  
  4. EXIT
  This option will stop the running program
