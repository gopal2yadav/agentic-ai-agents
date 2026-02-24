# Running and Deploying a Sample Flask App

Use this guide to run a sample Flask app locally and then deploy it to a modern hosting platform.

## 1) Run the app locally

1. Create a virtual environment and install dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Initialize the SQLite database (if your sample app exposes `/init-db`).

   ```bash
   flask run &
   curl http://127.0.0.1:5000/init-db
   ```

3. Run with a WSGI server for realistic local testing.

   ```bash
   gunicorn app:app
   ```

   Gunicorn listens on port `8000` by default.

## 2) Prepare the project for deployment

1. Create a `Procfile` at the project root:

   ```text
   web: gunicorn --bind :$PORT app:app
   ```

2. Verify `requirements.txt` only includes needed runtime dependencies.
3. Commit the app code to Git and push to a hosted repository.

## 3) Deploy to a hosting service

Most modern PaaS providers support Flask. The overall flow is the same: connect a repository, set build/start commands, and deploy.

### Option A: Koyeb

1. Create a new Web Service.
2. Connect your GitHub repository and branch.
3. Keep default buildpack settings.
4. Deploy and open the generated `*.koyeb.app` URL.

### Option B: Render

1. Create a new Web Service and connect your repository.
2. Use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
3. Deploy and open the generated `*.onrender.com` URL.

## 4) Production considerations

- Do **not** use Flask's built-in development server in production.
- Use a reverse proxy (or platform-managed proxy) in front of Gunicorn.
- Store config and secrets in environment variables.
- Scale compute and move from SQLite to a managed database (for example, PostgreSQL) as needed.
