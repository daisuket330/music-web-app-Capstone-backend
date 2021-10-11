# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iq(qiajr&7*39ux4r^iz3cxas^k6klh((01l0u)riwkr(gm#p4'


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