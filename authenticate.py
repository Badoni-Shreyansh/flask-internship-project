import pyrebase

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

email='test@gmail.com'
password='123456'

#user=auth.create_user_with_email_and_password(email,password)
#print(user)

user=auth.sign_in_with_email_and_password(email,password)

#info=auth.get_account_info(user['idToken'])
#print(info)

#email_verification=auth.send_email_verification(user['idToken'])

