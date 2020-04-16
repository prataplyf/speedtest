from test1 import modules as ml
# MongoDB
myclient = ml.pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.Demo
login = mydb['emp_login']
company = mydb['company_details']
employee = mydb['employee_details']