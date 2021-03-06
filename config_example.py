import os

# Flask settings
SECRET_KEY = os.getenv('SECRET_KEY',       'THIS IS AN INSECURE SECRET')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     'mysql://inception_web:inception_web@192.168.10.152:3306/inception_web?charset=utf8')
SQLALCHEMY_TRACK_MODIFICATIONS=False
CSRF_ENABLED = True


# Flask-Mail settings
MAIL_ON_OFF='ON'
MAIL_SERVER='smtp.qq.com'
MAIL_PORT=465
MAIL_USE_TLS=False
MAIL_USE_SSL=True
MAIL_USERNAME='cljqqyx@qq.com'
MAIL_PASSWORD='xxx'
MAIL_DEFAULT_SENDER='"test"<cljqqyx@qq.com>'


#Inception settings

INCEPTION_HOST='192.168.10.30'
INCEPTION_PORT=6669

#Inception backup settings
INCEPTION_REMOTE_BACKUP_HOST='192.168.10.152'
INCEPTION_REMOTE_BACKUP_PORT=3306
INCEPTION_REMOTE_BACKUP_USER='inception_web'
INCEPTION_REMOTE_BACKUP_PASSWORD='inception_web'

#Other optins
CRITICAL_DDL_ON_OFF='OFF'
AUDIT_SROLE_ON_OFF='OFF'



