# publicize your heroku database

1. Build an empty project with a database.

2. This
```
heroku git:remote -a {your-project-name}
git push heroku master
```

3. Find your aws rds connection and creds at: https://{your-project-name}.herokuapp.com/