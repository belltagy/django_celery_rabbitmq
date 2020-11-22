# django_celery_rabbitmq
this setup for creating background tasks when request come to django 
-first the user create random users so, take number of user required and generate it in back ground
-------------Setup---------------
install requirements
Install celery and runserver
>>pip install celery
>> python manage.py migrate # migrate and don't forget to add apps to installed apps
>> python manage.py runserver  # runserver

Run celery 
   *******if you on windows 7 or 10********
>>pip install eventlet

>>celery -A <module> worker -l info -P eventlet  # module here is celery_rabbitmq
  OR
  pip install gevent
  >>celery -A <module> worker -l info -P eventlet  # module here is celery_rabbitmq
   ******* if using linux **********
>>elery -A <module> worker -l info  #module here is celery_rabbitmq

then you must run the message broker from your choice (rabbitmq,redis,AWS....)here rabbit mq used 
run rabbitmq using docker 
>> docker run -d --name rabitmq -p 5672:5672 rabbitmq

note if something goes wrong with celery like import problem you can restart celery
