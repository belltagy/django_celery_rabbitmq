# django_celery_rabbitmq
-- this setup for creating background tasks when request come to django 
-- first the user create random users so, take number of user required and generate it in back ground
#  **Setup**
1. install requirements
2. Install celery and runserver
```
>>pip install celery

>> python manage.py migrate # migrate and don't forget to add apps to installed apps
>> python manage.py runserver  # runserver
```
* Run celery 
   *******if you on windows 7 or 10********
```
>>pip install eventlet

>>celery -A <module> worker -l info -P eventlet  # module here is celery_rabbitmq
  OR
  pip install gevent
  >>celery -A <module> worker -l info -P gevent  # module here is celery_rabbitmq
   ******* if using linux **********
>>celery -A <module> worker -l info  #module here is celery_rabbitmq
```
then you must run the message broker from your choice (rabbitmq,redis,AWS....)here rabbit mq used 
run rabbitmq using docker 
```
>> docker run -d --name rabitmq -p 5672:5672 rabbitmq
```
#### you also can run redis docker image as follow
```
docker container run  -d -p 6379:6379 --name redis redis
```
note if something goes wrong with celery like import problem you can restart celery
