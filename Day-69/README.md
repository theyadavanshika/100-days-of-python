# Flask Blog

Live demo: https://python-project-wvym.onrender.com

A multi-user blog built with Flask. Visitors can read posts, register and log in to comment, and the admin (the first registered user) can create, edit, and delete posts using a rich-text editor.

## Features

- User registration and login with hashed passwords (PBKDF2-SHA256)
- Session management with Flask-Login
- Admin-only post creation, editing, and deletion
- Rich-text post editor (CKEditor)
- Comments on posts (login required)
- Gravatar avatars for commenters
- Responsive layout with Bootstrap 5
- SQLite for local development, PostgreSQL in production (via Flask-SQLAlchemy)
- Deployment-ready with Gunicorn and a `Procfile`

## Tech Stack

| Area | Library |
|------|---------|
| Framework | Flask 3.1 |
| Database / ORM | Flask-SQLAlchemy, SQLAlchemy, SQLite (local), PostgreSQL (production) |
| Database driver | psycopg2-binary |
| Authentication | Flask-Login, Werkzeug |
| Forms | Flask-WTF, WTForms, email-validator |
| Editor | Flask-CKEditor |
| UI | Bootstrap-Flask (Bootstrap 5) |
| Config | python-dotenv |
| Production server | Gunicorn |

## Project Structure

```
.
├── main.py             # App setup, models, and routes
├── forms.py            # WTForms: register, login, post, comment
├── Procfile            # Process definition for deployment (Gunicorn)
├── requirements.txt
├── .env                # Secrets (not committed)
├── .gitignore
├── instance/
│   └── posts.db        # SQLite database (created automatically, not committed)
├── static/             # CSS, JS, images
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── post.html
    ├── make-post.html
    ├── login.html
    ├── register.html
    ├── about.html
    └── contact.html
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root. First generate a secret key:

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

Then add it to `.env` (no quotes, no spaces around `=`):

```
SECRET_KEY=your-generated-key-here
```

### 5. Run the app locally

```bash
python main.py
```

Open [http://127.0.0.1:5002](http://127.0.0.1:5002) in your browser. The database and tables are created automatically on first run.

Locally the app uses SQLite (`instance/posts.db`). If you set a `DB_URI` environment variable, it uses that database instead.

## Usage

1. **Register the first account.** The first user created gets ID 1 and becomes the **admin**. Do this yourself before sharing the app with anyone.
2. **Create posts.** Once logged in as admin, use the "New Post" button to write posts with the rich-text editor.
3. **Comment.** Any registered user can comment on a post. Logged-out visitors are redirected to the login page.

## Routes

| Route | Methods | Access | Description |
|-------|---------|--------|-------------|
| `/` | GET | Public | List all posts |
| `/post/<id>` | GET, POST | Public / login to comment | View a post and its comments |
| `/register` | GET, POST | Public | Create an account |
| `/login` | GET, POST | Public | Log in |
| `/logout` | GET | Logged in | Log out |
| `/new-post` | GET, POST | Admin | Create a post |
| `/edit-post/<id>` | GET, POST | Admin | Edit a post |
| `/delete/<id>` | GET | Admin | Delete a post |
| `/about` | GET | Public | About page |
| `/contact` | GET | Public | Contact page |

## Database Models

- **User**: email, hashed password, name; has many posts and comments
- **BlogPost**: title, subtitle, date, body, image URL; belongs to an author; has many comments
- **Comment**: text; belongs to an author and a post

## Deployment

The project includes a `Procfile` that tells hosting platforms (such as Render or Heroku) how to start the app:

```
web: gunicorn main:app
```

You can test Gunicorn locally with:

```bash
gunicorn main:app
```

Environment variables to set on your host:

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Signs login sessions. Use a long random value. |
| `DB_URI` | PostgreSQL connection string. The URL must start with `postgresql://` (not `postgres://`). |

Before deploying:

- Never commit `.env` or your secrets. Set them as environment variables on your host.
- `app.run(debug=True)` is inside the `if __name__ == "__main__":` block, so Gunicorn ignores it. Never deploy with the debugger enabled.
- Register your own account first on the fresh database so you become the admin.
- Use PostgreSQL in production. SQLite stores data in a local file, and many hosts reset their filesystem on every deploy or restart. On Render, create a PostgreSQL database and use its **Internal Database URL** as `DB_URI`.

## Security

- Passwords are salted and hashed; plain-text passwords are never stored.
- `.env`, `instance/`, and `*.db` are listed in `.gitignore`. Do not commit them.
- Admin routes are protected by the `admin_only` decorator.

## Acknowledgements

Built as a course project while learning Flask.