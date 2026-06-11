# 🎬 Movie Search App

A modern and responsive **Movie Search Web Application** built using **Flask**, **HTML**, **CSS**, and the **OMDb API**. Users can search for any movie and instantly view detailed information including the movie poster, IMDb rating, release date, actors, genre, and plot.

---

## 📸 Preview
https://movie-search-app-54dw.onrender.com/

### 🏠 Home Page

- Clean Netflix-inspired interface
- Search movies by title
- Responsive and user-friendly design

### 🎥 Movie Details Page

Displays:

- 🎬 Movie Title
- ⭐ IMDb Rating
- 📅 Release Date
- 🎭 Top Cast
- 🎞️ Genre
- 📝 Plot Summary
- 🖼️ Official Movie Poster

---

## 🚀 Features

- 🔍 Search movies by name
- ⭐ Fetch real-time movie data using OMDb API
- 🖼️ Display high-quality movie posters
- 🎭 Show main cast members
- 📅 Display release date
- 🎬 Show movie genre
- 📝 Display plot summary
- 💻 Responsive and modern Netflix-inspired UI
- ⚡ Fast and lightweight Flask backend

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- Google Fonts (Poppins)

### Backend

- Python
- Flask

### API

- OMDb API

---

## 📂 Project Structure

```
movie_search/
│
├── static/
│   ├── style.css
│   ├── style2.css
│   └── movie-bg.jpg
│
├── templates/
│   ├── home.html
│   ├── result.html
│   └── result2.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/movie-search.git
```

### 2️⃣ Navigate to the project

```bash
cd movie-search
```

### 3️⃣ Create a virtual environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the application

```bash
python app.py
```

---

### 6️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🔑 OMDb API Setup

1. Visit:

```
https://www.omdbapi.com/apikey.aspx
```

2. Generate a free API key.

3. Replace your API key inside `app.py`:

```python
api_key = "YOUR_API_KEY"
```

For better security, it is recommended to store the key in a `.env` file.

---

## 📷 Example Search

Search for:

- Interstellar
- Inception
- Avengers
- Titanic
- The Dark Knight

The application will display:

- Poster
- IMDb Rating
- Release Date
- Actors
- Genre
- Plot

---

## 📦 Requirements

```
Flask
requests
```

Install them using:

```bash
pip install Flask requests
```

---

## 🎯 Future Improvements

- ❤️ Add Favorite Movies feature
- 🌙 Dark/Light Theme Toggle
- 🎬 Display Director & Runtime
- 🎥 Show Movie Trailer
- 🔎 Search Suggestions
- 📱 Enhanced Mobile Responsiveness
- 🕘 Search History
- ⭐ User Authentication

---

## 👨‍💻 Author

**Harsha Paloju**

- GitHub: https://github.com/harsha-paloju
- LinkedIn: https://in.linkedin.com/in/harsha-paloju-44388239b

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!

---

## 📄 License

This project is intended for educational and learning purposes.
