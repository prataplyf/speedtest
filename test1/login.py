from test1 import modules as ml
from test1 import app
from test1 import config

# @app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if ml.request.method == 'POST':
        useremail = ml.request.form.get('useremail')   #login mailID
        userpassword = ml.request.form.get('userpassword')  # login Password
        # if usermail in [temp['email'] for temp in config]
        login_user = config.login.find_one({'email' :useremail})
        if login_user:
            if login_user['password'] == userpassword:
                print('successful login')
                result1 = config.company.find_one({'email':useremail}, {'_id':0})
                result2 = config.employee.find_one({'email':useremail}, {'email':0, '_id':0})
                result1.update(result2)
                print(result1)
                return ml.jsonify({'message':'get data', 'status':'success','data':result1})
            else:
                return ml.jsonify({'message':'Invalid data', 'status':'success'})
        else:
            return ml.jsonify({'message':'Invalid Username', 'status':'success'})
    else:
        return ml.render_template('login.html')
# useremail and password
# useremail = 'ipetryi@whitehouse.gov'
# userpassword = 'bkr5Z4iTo8pL'

# class SimpleTest(unittest.TestCase):
