Quick dev setup: connect React (Vite) frontend to Flask backend

What I added

- src/lib/api.ts — small fetch wrapper that targets VITE_API_BASE or http://localhost:5000 by default
- src/components/BackendTest.tsx — a development UI to call backend health and mouse endpoints
- Landing.tsx — imports and renders the BackendTest component (development-only)

Run backend (Flask)

Open a terminal and activate your Python venv, then run:

```cmd
cd env1
Scripts\activate.bat
python app.py
```

This starts Flask on http://localhost:5000 (default in app.py).

Run frontend (Vite)

In a separate terminal run:

```cmd
cd "d:\Satwik\AMITY\CYBERCUP 5.0\TechTitans"
npm install
npm run dev
```

Vite usually serves on http://localhost:5173.

If you prefer to set the backend base URL via an environment variable, create a file named `.env` at the project root with:

```
VITE_API_BASE=http://localhost:5000
```

Smoke test

1. Start Flask and the React dev server.
2. Open the app in the browser (http://localhost:5173) and visit the landing page.
3. In the "Backend integration test" panel click "Check Health" — you should see the JSON message {"message":"✅ Backend running successfully!"}.
4. Click "Call Mouse API" — the component will send a small sample payload to `/api/mouse` and display the response.

Notes

- CORS is already enabled in `env1/app.py` via `flask_cors.CORS(app)`.
- The sample payload for the mouse API is minimal and may need to be adapted to match the model's expected features (check `models/*` preprocessing code).
- Remove the `BackendTest` import from `Landing.tsx` before deploying to production.
