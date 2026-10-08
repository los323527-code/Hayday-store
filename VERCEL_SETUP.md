# Hayday Store — Vercel setup

Set Vercel **Root Directory** to `api-shop`.

The Python API entrypoint is `api/index.py` and Vercel routing is configured in `vercel.json`.

## Required Vercel Environment Variables

Copy the values from `shop/.env.example` into Vercel Project Settings → Environment Variables. At minimum the Django settings require:

- `DEBUG`
- `SECRET_KEY`
- `DATABASE_URL` (or another database URL supported by `django-environ`)
- `GS_BUCKET_NAME`

Depending on the project configuration, also set:

- `SERVICE_URL`
- `FRONTEND_CLIENT_URL`
- `ADMIN_CLIENT_URL`
- Google Cloud credentials / project variables required by the storage configuration

Do not commit real secrets to GitHub.

## Deploy

1. Import the GitHub repository into Vercel.
2. Set Root Directory to `api-shop`.
3. Add the required environment variables.
4. Deploy.
