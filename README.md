# Social todo Django

Check out the app 
[here](https://colleen-social-todo.herokuapp.com/).

To install this locally, clone the repository. Then, before you run it
for the first time, you'd do

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
This installs your Python dependencies. Then you need to run your database
migrations with 

```
python manage.py migrate
```

This will create a file called `db.sqlite3`, which is ignored in your
`.gitignore` file. 

Now you're ready to run the application.Then you can run it with the following

```
python manage.py runserver
```

Then you can go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view.