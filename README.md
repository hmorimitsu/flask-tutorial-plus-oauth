# Flask Tutorial Plus with OAuth

This repository contains a modified version of the code at [https://github.com/hmorimitsu/flask-tutorial-plus](https://github.com/hmorimitsu/flask-tutorial-plus). The code was changed to replace the login stage to OAuth using Google and Github to authenticate the user.

This code, in turn, implements an adapted version of the official [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial).
The code of the tutorial was adapted to use OAuth authentication and also to take advantage of some common Flask libraries, including:
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/),
- [Flask WTForms](https://flask-wtf.readthedocs.io/),
- [Flask Login](https://flask-login.readthedocs.io/),
- [Flask Migrate](https://flask-migrate.readthedocs.io/), and
- [Flask Dance](https://flask-dance.readthedocs.io/).

The application is still the same as in the original tutorial, and a significant part of the code remains unchanged.
If you are interested in learning more about the code, I recommend you check the original tutorial, which explains everything nicely.

I wrote this code mostly to learn Flask myself, but I decided to make it public in case someone else wanted to see
a relatively simple example of how to use OAuth to login and how to employ those Flask libraries in practice (as I did).

I did my best to follow good practices to write the code, but as I am new to Flask, I cannot guarantee everything is implemented in the best way.
I consulted a few other sources to learn about the libraries, and they are listed in the [Acknowledgements](#acknowledgements).

## Requirements

- Python 3
- Flask
- Flask Dance
- Flask SQLAlchemy
- Flask WTForms
- Flask Login
- Flask Migrate
- Flask Script

It is assumed you already have Python 3 with pip installed (if not, there are many tutorials about it).
You should also be using some type environment, such as [Virtualenv](https://virtualenv.pypa.io/en/latest/) or [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

You can install all other required libraries with the command below:
```bash
pip install flask Flask-Dance Flask-SQLAlchemy flask-login Flask-WTF Flask-Migrate Flask-Script
```

Alternatively, if you are using an environment, and you want to install the same versions of the libraries I used when writing this code, first complete the first two steps of the [Running the app](#running-the-app) and then run:
```bash
pip install -r requirements.txt
```

## Usage

### Obtaining OAuth tokens

In order to use this app, you will need to first have access to Google and/or Github OAuth keys.

I will explain how to get these keys here, as you can probably find better tutorials elsewhere. When I was writing this app, I used the official Flask Dance examples:
- for Github: [https://github.com/singingwolfboy/flask-dance-github](https://github.com/singingwolfboy/flask-dance-github),
- for Google: [https://github.com/singingwolfboy/flask-dance-google](https://github.com/singingwolfboy/flask-dance-google).

You will need to know your Client ID and Client Secret values from any of these providers before continuing.

### Running the app

The instructions below show how to run this code using terminal in a Linux machine. If you are using another OS, you may have to adapt the instructions.

1. Clone this repository:
```bash
git clone https://github.com/hmorimitsu/flask-tutorial-plus-oauth.git
```

2. Enter the folder that was created by cloning the repository.
```bash
cd flask-tutorial-plus-oauth
```

3. Export environment variables. You can find more details about this step on the official examples linked at [Obtaining OAuth tokens](#obtaining-oauth-tokens).
   
    1. First some basic OAuth variables:
        ```bash
        export OAUTHLIB_RELAX_TOKEN_SCOPE=true
        export OAUTHLIB_INSECURE_TRANSPORT=true
        ```
        **IMPORTANT**: These settings are only for testing! If you are going to deploy your website publicly, **DO NOT** set these variables! 
    2. If you use Github OAuth, then set these:
        ```bash
        export GITHUB_OAUTH_CLIENT_ID=<your_github_id>
        export GITHUB_OAUTH_CLIENT_SECRET=<your_github_secret>
        ```
        Replace `<your_github_id>` and `<your_github_secret>` by the values you got from [Obtaining OAuth tokens](#obtaining-oauth-tokens).
    3. If you use Google OAuth, then set these:
        ```bash
        export GOOGLE_OAUTH_CLIENT_ID=<your_google_id>
        export GOOGLE_OAUTH_CLIENT_SECRET=<your_google_secret>
        ```
        Replace `<your_google_id>` and `<your_google_secret>` by the values you got from [Obtaining OAuth tokens](#obtaining-oauth-tokens).

4. Use Flask Migrate to initialize the sqlite database. If you want to use another database (such as Postgres or MySQL), you will have the edit the `DATABASE_URL` in [config.py](instance/config.py)) before starting this step.
```bash
bash manage_db.sh
```

5. If there were any error during the migration, fix them before proceeding. If there are no errors, then you can start to serve the application by running:
```bash
python app.py
```

6. Again, check for error messages and fix them. If no errors, then open a browser and enter the address informed in the terminal (tipically `http://127.0.0.1:5000/`). If everything goes well, you should see the login page of the website showing a message asking you to login.

## Acknowledgements

A significant part of the code comes from the official [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial).

Besides, the following websites were used to implement parts related to other Flask libraries:

- [https://pusher.com/tutorials/oauth-flask-dance](https://pusher.com/tutorials/oauth-flask-dance)
- [https://realpython.com/flask-google-login/](https://realpython.com/flask-google-login/)
- [https://hackersandslackers.com/your-first-flask-application](https://hackersandslackers.com/your-first-flask-application)
- [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [https://realpython.com/flask-by-example-part-1-project-setup/](https://realpython.com/flask-by-example-part-1-project-setup/)

## LICENSE

This code is licensed under the [MIT License](LICENSE).
