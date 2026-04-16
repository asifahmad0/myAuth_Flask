from flask import Flask, request, session, redirect, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from models.model import collection
from flask_jwt_extended import JWTManager, create_access_token







app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_auth'
app.config['JWT_SECRET_KEY'] = '@nam1234' 
jwt = JWTManager(app)



@app.route('/user', methods=['GET','POST'])
def register():

    if request.method == 'POST':
        username = request.form.get('uname')
        email = request.form.get('uemail')
        mobile = request.form.get('umobile')
        password = request.form.get('upass')
        new_pass = generate_password_hash(password)

        if username and email and mobile and password:

            user_data = {
                "username": username,
                "email": email,
                "mobile": mobile,
                "password": new_pass
            }

            collection.insert_one(user_data) 

            print("Data inserted")
            return redirect('/user/login')

    return render_template('register.html')
           






@app.route('/user/login', methods=['GET','POST'])
def login():
    username = request.form.get('uname')
    password = request.form.get('upass')


    user = collection.find_one({"username": username})


    if user and check_password_hash(user['password'], password):

        access_token = create_access_token(identity=username)
        session[username]=access_token

        
        return redirect('/')
    else:
        print({"message": "Invalid credentials"}), 401
    
    return render_template('login.html')











if __name__ == "__main__":
    app.run(debug=True)