# Running and Deploying the Sample Flask App

This guide summarizes how to run a sample Flask application locally and deploy it using a modern hosting platform.

## 1) Run the app locally

1. Create a virtual environment and install dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Initialize the SQLite database (if your sample app includes an init route):

```bash
flask run &
curl http://127.0.0.1:5000/init-db
```

3. Run with a WSGI server for realistic local testing. Do **not** use Flask's development server for production.

```bash
gunicorn app:app
```

Gunicorn serves on port `8000` by default. Test endpoints with `curl` at `http://localhost:8000`.

## 2) Prepare for deployment

1. Add a `Procfile` in the project root:

```text
web: gunicorn --bind :$PORT app:app
```

2. Verify `requirements.txt` only includes needed runtime dependencies.
3. Commit and push your code:

```bash
git init
git add app.py requirements.txt Procfile
git commit -m "Initial commit"
git remote add origin git@github.com:<YOUR_USERNAME>/<YOUR_REPO>.git
git push -u origin main
```

## 3) Deploy to a hosting provider

### Option A: Koyeb

1. Create a **Web Service** in Koyeb.
2. Choose **GitHub** as source and select your repo.
3. Keep default buildpack settings; Koyeb detects `Procfile`.
4. Pick an instance size and deploy.
5. Open the generated `*.koyeb.app` URL.

### Option B: Render

1. Create a new **Web Service** and connect your GitHub repo.
2. Configure:
   - Language: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
3. Deploy and visit the generated `onrender.com` URL.
4. Future pushes to the selected branch trigger auto-deploys.

## 4) Production considerations

- Never use Flask's built-in development server in production.
- Use a reverse proxy (or your platform's managed ingress/proxy).
- Configure secrets and env vars in platform settings, not in code.
- Scale compute as needed and consider PostgreSQL instead of SQLite for production workloads.
