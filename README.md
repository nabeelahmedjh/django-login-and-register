# Simple Django Login and Registration

An example of Django project with basic user functionality.

## Screenshots

| Landing Page | Login Page | Register page |
| -------|--------------|-----------------|
| <img src="./screenshots/landing_page.png" width="200"> | <img src="./screenshots/login_page.png" width="200"> | <img src="./screenshots/register_page.png" width="200"> |

| Home/profile Page | Set new password | Set new Username |
| ---------------|------------------|-----------------|
| <img src="./screenshots/home_profile_page.png" width="200"> | <img src="./screenshots/change_password_page.png" width="200"> | <img src="./screenshots/change_username_page.png" width="200"> |

## Functionality

- Log in
    - via username & password
- Create an account
- Log out
- Change password
- Change username


## Learned Topics

- Django Authenication
- Django Forms
- Error Checking
- Django Built-in User Model


## Installing

### Clone the project

```bash
git clone https://github.com/nabeelahmedjh/django-login-and-register.git
cd django_login_register
```

### Install dependencies & activate virtualenv

#### Create a virtualenv using pipenv (optional)

```bash
pipenv shell

```

#### Install dependencies

```bash
pipenv install
```

### Apply migrations (Optional)

```bash
python source/manage.py migrate
```

### Collect static files (only on a production server)

```bash
python source/manage.py collectstatic
```

### Running

#### A development server

Just run this command:

```bash
python source/manage.py runserver
```