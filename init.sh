heroku ps:scale web=1
heroku buildpacks:set heroku/python
heroku git:remote -a lunch