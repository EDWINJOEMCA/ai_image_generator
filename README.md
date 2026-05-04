# AI Image Generator (Django + OpenAI)

A modern AI-powered image generation web app built using **Django** and **OpenAI Image API**.

Users can enter a prompt, generate images using AI, preview them instantly, download them, and store them in a database.

---

## Features

- Generate AI images from text prompts
- Fast API integration with OpenAI
- Live preview of generated images
- Download generated images
- Store prompt + image in SQLite database
- CSRF-secured Django backend
- Loading spinner + UI lock during generation
- Toast notifications for success/error
- Clean modern UI (glassmorphism design)

---

## Tech Stack

- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Database: SQLite
- API: OpenAI (`gpt-image-1`)
- Image Handling: Base64 → File conversion

---

## Installation

### 1. Clone the repo
```bash
git clone https://github.com/EDWINJOEMCA/ai_image_generator.git
cd ai-image-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
Create a .env file:
OPENAI_API_KEY=your_openai_api_key_here

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver

# Usage
1. Open browser → http://127.0.0.1:8000/
2. Enter a prompt (e.g., "A futuristic city at sunset")
3. Click Generate
4. View the image
5. Download if needed

# Project Structure
ai_image_app/
│
├── ai_generator/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   └── index.html
│
├── media/
│   └── generated/
│
├── manage.py
├── .env
└── db.sqlite3

# How it works
User submits prompt
Django sends request to OpenAI API
API returns Base64 image
Image is decoded and saved
Path stored in database
Image URL returned to frontend
Display + download enabled