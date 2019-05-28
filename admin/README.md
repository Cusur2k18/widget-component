# Widget Admin
> Admin system for the widget

## Development

First clone the project:

```bash
git clone
```

I strongly recommend use [virtual environments]().

Create your venv:

```bash
python -m venv .venv
```

Activate the venv:

```bash
source .venv/bin/activate
```

Now you can safely install the dependencies listed on `requirements.txt`:

```bash
$venv > pip install -r requirements.txt
```

Run the migrations:

```bash
$venv > python manage.py migrate
```

You'll need to create a `superuser`:

```bash
$venv > python manage.py createsuperuser
```
> Enter the username and password

Run the development server:

```bash
$venv > python manage.py runserver
```

Go to `localhost:8000/admin` and enjoy!
