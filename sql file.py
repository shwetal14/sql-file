#!/usr/bin/env python
# coding: utf-8

# In[ ]:




 1.Count the number of Salesperson whose name begin with ‘a’/’A’.
    
    
  
    Select count(Snum) from SalesPeople where Sname like ‘a%’or Sname like‘A%’
    
    
    
    
 2. Display all the Salesperson whose all orders worth is more than Rs. 2000.


   SQL> Select  * from orders where amt>2000; 

    
    
    
 3. Count the number of Salesperson belonging to Newyork.


   SQL> Select count(Snum) from Salespeople where city='Newyork';
    
    
    
    
    
 4.Display the number of Salespeople belonging to London and belonging to Paris.
    
  

    SQL> Select count(city) from Salesperson where city='London' and 'Paris';
    
    
 5. Display the number of orders taken by each Salesperson and their date of orders.


    
    SQL> Select snum,odate, from orders group by odate,snum;










