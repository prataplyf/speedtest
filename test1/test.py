from flask import Flask, render_template, redirect, url_for, request, jsonify, request
import pymongo
import unittest
# import pandas as pd
# db connection
myclient = pymongo.MongoClient("mongodb+srv://prataplyf:Ashish12@ashish-hbjy0.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient.Demo
login = mydb['emp_login']
company = mydb['company_details']
employee = mydb['employee_details']
# useremail and password
useremail = 'ipetryi@whitehouse.gov'
userpassword = 'bkr5Z4iTo8pL'
# app = Flask(__name__)

# @app.route('/login')
# def login():
class SimpleTest(unittest.TestCase):
    def testcode(self):
        login_user = login.find_one({'email' :useremail})
        if login_user:
            if login_user['password'] == userpassword:
                print('successful login')
                result1 = company.find_one({'email':useremail}, {'_id':0})
                result2 = employee.find_one({'email':useremail}, {'email':0, '_id':0})
                result1.update(result2)
                print(result1)
                # print(result)
            else:
                print('incorrect pwd')
        else:
            print('Invalid User')
# SimpleTest()
if __name__ == '__main__':
   unittest.main()
