# Random Unhelpful Error (RUE) — v0.1 🚨

![RUE Banner](https://img.shields.io/badge/RUE-v0.1-orange) [![Website](https://img.shields.io/website?url=https://rue.enrique53xd.com)](https://rue.enrique53xd.com) [![GitHub repo](https://img.shields.io/badge/GitHub-Enrique53xD/RUE-181717?logo=github)](https://github.com/Enrique53xD/RUE)

A tiny, playful Flask microservice that returns a random unhelpful error message in English or Spanish. Perfect for adding some humor to demos, bots, server responses, or just to generate a chuckle when debugging goes wrong.

---

## 🔍 What is this?

RUE (Random Unhelpful Error) is a lightweight Flask app that exposes a couple of endpoints:

- `GET /` - Basic status message indicating the server is running.
- `GET /en` - Returns a JSON payload with a random unhelpful error message in English.
- `GET /es` - Returns a JSON payload with a random unhelpful error message in Spanish.

Live API: https://rue.enrique53xd.com — try `/en` or `/es` (the API is hosted here)

Repository: https://github.com/Enrique53xD/RUE

A custom 404 handler picks a random message in the best language match based on the browser's accepted languages.

---

## ✨ Features

- Funny, unhelpful error strings (English & Spanish)
- Clean JSON for `/en` and `/es` endpoints
- Friendly 404 with a random message to keep things entertaining
- Ready for deployment (includes `Procfile` and `requirements.txt`)

---

## 🚀 Quick start (Run locally)

Prerequisites:
- Python 3.8+ (recommended)
- Optional: `virtualenv` or `venv`

Steps:

```bash
# clone the repo
git clone https://github.com/Enrique53xD/RUE.git
cd RUE

# create and activate a virtual env
python -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run app
python app.py
```

- The app listens by default on `0.0.0.0:8080` (or the value of the `PORT` env var).
- Open `http://localhost:8080/en` or `http://localhost:8080/es` to see example JSON responses.

Using `gunicorn` (production-ish):

```bash
# run with gunicorn
gunicorn app:app --bind 0.0.0.0:8080
```

Or on Heroku (automatically uses the provided `Procfile`):

```bash
# assuming you already have a Heroku app created
git push heroku main
heroku open
```

---

## 📡 API

GET /en
- Response (JSON):
```json
{
  "message": "Error 404: Motivation not found.",
  "status": "success"
}
```

GET /es
- Response (JSON):
```json
{
  "message": "Error 404: Ganas de trabajar no encontradas.",
  "status": "success"
}
```

GET /
- Response (text): `The Random Unhelpful Error (RUE) server is running.`

404 handling
- Uses `Accept-Language` header to return a single plain-text unhelpful message in `en` or `es`, and returns a 404 HTTP status code.

Example curl commands (local or live API endpoints):

```bash
# Local dev (if running locally):
curl http://localhost:8080/en
curl http://localhost:8080/es
curl http://localhost:8080/doesnotexist  # gets a random unhelpful 404 (local)

# Live API (hosted):
curl https://rue.enrique53xd.com/en
curl https://rue.enrique53xd.com/es
curl https://rue.enrique53xd.com/doesnotexist  # gets a random unhelpful 404 (hosted)
```

---

## 📦 Dependencies

- Flask
- gunicorn (for production)

See `requirements.txt` for details.

---

## 🛠️ Development

- Editing the messages: find `select_error` in `app.py`. Add new fun messages or adjust languages.
- To run locally, follow the Quick Start above.
- PRs welcome! Please ensure tests or checks are included if you add new behavior.

---

## 💡 Ideas & Roadmap

- Add community-contributed messages via a JSON or a simple admin UI
- Add more languages
- Add a simple UI that fetches and displays random messages with sound and animations

---

## 🤝 Contributing

Bugs, improvements, or PRs are welcome. Please open a GitHub issue or submit a pull request with a descriptive message and tests (when applicable).

---

## 📝 License

No license file is included in this project yet. Add an open-source license (e.g., MIT) if you want to make this project reusable by others.

---

Thanks for trying out RUE! If you'd like any enhancements — like adding more languages or UI — open an issue and I'll help you add it. 🙌

---

Version: v0.1 — Initial release 🎉
