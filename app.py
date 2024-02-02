from flask import Flask,render_template,request,redirect, session,url_for
import pyrebase

app= Flask(__name__,template_folder='templates', static_folder='static')

config={
    'apiKey': "AIzaSyCvV58o7KJXetCyJE9VUMa_YskRauoiZGM",
    'authDomain': "authenticatepy-b804e.firebaseapp.com",
    'projectId': "authenticatepy-b804e",
    'storageBucket': "authenticatepy-b804e.appspot.com",
    'messagingSenderId': "1095511612566",
    'appId': "1:1095511612566:web:07f4d3af56d62b09ddb6b7",
    'measurementId': "G-VWVPTZQBCY",
    'databaseURL':""
}

firebase= pyrebase.initialize_app(config)
auth=firebase.auth()

app.secret_key='secret'

@app.route('/', methods=['POST','GET'])
def index():
    if('user' in session):
        return redirect('/new_page')
    if request.method=='POST':
        email= request.form.get('email')
        password= request.form.get('password')
        try:
            user= auth.sign_in_with_email_and_password(email,password)
            session['user'] =email
        except:
            return render_template('failed_login.html')
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/new_page')
def new_page():
    return render_template('new_page.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        try:
            new_user=auth.create_user_with_email_and_password(email,password)
            return redirect('/')
        except:
            return "Failed to create Account!"
        
    return render_template('signup.html')




if __name__=='__main__':
    app.run(port=1111)
