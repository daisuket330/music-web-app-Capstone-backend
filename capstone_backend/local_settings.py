SECRET_KEY = 'django-insecure-innv-nvp_5b-ly34fwmlp!6+7445c5*#vdoizulu=-n!j51cn0'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'capstone_backend',
        'USER': 'root',
        'PASSWORD': 'Taco1234',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS':{
            'autocommit': True
        }    
    }
}