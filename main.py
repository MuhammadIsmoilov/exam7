# create table Customers
# (
# 	customer_id serial primary key,
# 	first_name varchar(60),
# 	last_name varchar(60),
# 	email varchar(60),
# 	phone_num integer
# )
# insert into Customers(first_name,last_name,email,phone_num) values('Abdullo','Mirzoev','amirzoev@gmail.com',901510331),
# insert into Customers(first_name,last_name,email,phone_num) values('Ahmad','Maxmadov','amaxmadov@gmail.com',901510245),
# insert into Customers(first_name,last_name,email,phone_num) values('Numon','Kenjaev','nkenjaev@gmail.com',901514321)
# select * from Customers
# create table Orders
# (
# 	order_id serial primary key,
# 	customer_id int references Customers(customer_id) on delete cascade,
# 	customer_date date,
# 	total_amt integer	
# )
# insert into Orders(customer_id,customer_date,total_amt) values(1,'2024/02/02',1500),
# insert into Orders(customer_id,customer_date,total_amt) values(2,'2024/03/12',2500),
# insert into Orders(customer_id,customer_date,total_amt) values(3,'2024/03/02',3500),
# insert into Orders(customer_id,customer_date,total_amt) values(1,'2024/02/23',4500),
# insert into Orders(customer_id,customer_date,total_amt) values(2,'2024/01/01',5500)
# select * from Orders				1

# select * from City			2	
# where pop >= 100000 and city_code = 'USA'


# select city,state from Station 3

# select distinct city_name from station where zip_code % 2 = 0       4


# class Nobel:
    # pass
#     def __init__(self,category,year,winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#     def display_info(self):
#         print(self.__str__())
        
#     def __str__(self):
#             return f"{self.category} {self.year} {self.winner}"		5

# np2005 = Nobel('Peace',2005,'Muhammad Yunus')
# print(np2005)


# class Staff:		
#     def __init__(self,role,department,salery):
#         self.role = role
#         self.department = department
#         self.salery = salery


# class Teacher(Staff):
# 	def __init__(self, role, department, salery):
# 			super().__init__(role, department, salery)
                                    
# 	def get_info(self):
#         	return f"Role:{self.role}\n Deoartment:{self.department}\n Salery:{self.salery}"
    
# teacher = Teacher('Mentor of Python it language','Sofclub',20000)
# print(teacher.get_info())					6



# class Student_Management:
#     def __init__(self):
#         self.list_of_clothes = []
#         self.list_of_dict = {}

#     def add(self,title, price):
#         self.list_of_dict[title] = price
#         self.list_of_clothes.append(self.list_of_dict.copy)
#     def get_info(self):
#         for i in self.list_of_clothes:
#             for key,value in i.items():
#                 return f"{key}\n {value}"
       
#     def delete(self,new_title):
#         for i in self.list_of_clothes:
#             if i == new_title:
#                 self.list_of_clothes.remove(i)
        



# store = Student_Management()

# while True:
#     print("""
#             a -> add
#             g -> get all
#             del -> delete
#             exit -> exit""") 
          
#     choice = input('Choose one please -> ')
#     match choice:
#         case 'a':
#             title = input('What you want to buy ? -> ')
#             price = int(input('How much ? -> '))
#             new_list = Student_Management(title,price)
#             store.add(new_list)
#         case 'g':
#             store.get_info()
#         case 'del':
#             store.delete()
#         case 'exit':
#             break
#         case _:
#             print('Please try again')				7




# num = int(input())
# empty_list = []
# for i in range(1,num + 1):			8
	
#     if i % 3 == 0 and i % 5 == 0:
#         i = 'FizzBuzz'
#         empty_list.append(i)
#     elif i % 3 == 0:
#         i = 'Fizz'
#         empty_list.append(i)
#     elif i % 5 == 0:
#         i = 'Buzz'
#         empty_list.append(i)
#     else:
#         empty_list.append(i)
# print(empty_list)	
        




        