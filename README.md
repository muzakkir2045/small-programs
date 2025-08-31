




# Projects Collection

## Table of Contents
1. [Simple CLI Calculator](#simple-cli-calculator)
2. [Simple To-Do List (CLI)](#-simple-to-do-list-cli)
3. [Headline Web Scraper](#-headline-web-scraper)
4. [Flask REST API - User Management](#-flask-rest-api---user-management)
5. [Sales Data Analysis](#-sales-data-analysis-using-pandas--matplotlib)
6. [Image Resizer Tool](#-image-resizer-tool-batch-processor)
7. [Flask Portfolio Website](#-flask-portfolio-website)
8. [Rule-Based Chatbot](#-rule-based-chatbot-in-python)

## Repository Structure
```
.
├── task1/
│   └── calculator.py
├── task2/
│   ├── todo.py
│   └── todo.txt
├── task3/
│   └── web-scraper.py
├── task4/
│   └── rest_api.py
├── task5/
│   ├── data_analysis.ipynb
│   └── sales.csv
├── task6/
│   └── portfolio_site/
├── task7/
│   └── image_resizer.py
├── task8/
│   └── chatbot.py
└── README.md
```

---

# Simple CLI Calculator 

A simple command-line calculator written in Python.  
Supports basic operations: Addition, Subtraction, Multiplication, and Division.

## Features

- Function-based operations (`add`, `sub`, `mul`, `div`)
- Input taken interactively using `input()`
- Runs in a loop until user chooses to exit
- Error handling for invalid numbers and division by zero

## How to Run
Run the script in bash or command prompt:
```bash
python calculator.py
```



---

# 📝 Simple To-Do List (CLI)

A basic command-line To-Do List application written in Python. This tool lets you add, view, remove, and save tasks using a simple text file (`todo.txt`) for storage.

## 📦 Features
- ✅ Add a task
- 📋 View all tasks
- ❌ Remove a task by number
- 💾 Save tasks to file
- 🔁 Automatically loads tasks from file on start

## 🚀 How to Use

1. **Run the script:**
   ```bash
   python todo.py




# 📰 Headline Web Scraper

This is a simple Python script that fetches a webpage and extracts all `<h1>`, `<h2>`, and `<h3>` headings using `requests` and `BeautifulSoup`. The headings are saved into a file named `headings.txt`.

---

## 🚀 Features

- Fetch raw HTML from any URL
- Extract and save all main headings (`h1`, `h2`, `h3`)
- Handles:
  - HTTP errors (like 404)
  - Request issues (e.g. timeout, bad connection)
  - File writing errors

---

## 🛠 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

  ---

## 🧠 What I Learned

For this project, I first learned how to use the `requests` module to fetch HTML content from websites and then used `BeautifulSoup` to parse and extract specific elements from the page.

This helped me understand:

- How web pages are structured with HTML
- How to extract useful content like headlines using Python
- The difference between HTTP methods and error handling
- Real-world use of Python for automation and data scraping

---


Install dependencies with:

```bash
pip install requests beautifulsoup4




# 🧠 Flask REST API - User Management

## 📌 Project Overview
This project is a simple **RESTful API** built using **Flask** that allows you to manage user data. It supports basic CRUD operations — Create, Read, Update, and Delete users — using in-memory storage (a Python dictionary).

---

## 🚀 Features

- `GET /users` → Retrieve all users  
- `GET /users/<user_id>` → Retrieve a single user  
- `POST /users` → Add a new user  
- `PUT /users/<user_id>` → Update an existing user  
- `DELETE /users/<user_id>` → Delete a user  

All data is stored temporarily in-memory, making this ideal for practice and learning.

---

## ✅ What I Learned

Through this project, I gained hands-on experience in:

- Building a RESTful API from scratch using **Flask**
- Creating multiple routes with different HTTP methods (`GET`, `POST`, `PUT`, `DELETE`)
- Structuring Python code for clean backend development
- Using Postman or Curl to test API endpoints
- Handling user data in Python with dictionaries

---

## 📚 What I Had to Learn

To successfully complete this project, I learned the following key components:

| Topic         | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `Flask`       | A lightweight Python web framework used to build the entire API            |
| `request`     | Flask’s module to handle incoming JSON data from client requests           |
| `jsonify`     | A Flask function to return proper JSON responses from the server           |

---

## 🔧 How to Run

1. Make sure you have Python and Flask installed:
   ```bash
   pip install Flask
   ```

2. Run the server:
   ```bash
   python app.py
   ```

3. Open Postman or use Curl to test the endpoints at:
   ```
   http://127.0.0.1:5000/
   ```


---





# 📊 Sales Data Analysis using Pandas & Matplotlib

## 📌 Project Overview

This project is a simple **sales data analysis** pipeline built using **Pandas** and **Matplotlib** inside a **Jupyter Notebook**.  
It demonstrates how to import data from a CSV file, perform calculations, group the data, and visualize insights using bar plots.

---

## 🚀 Features

- 📁 Reads structured sales data from a CSV file
- 🧮 Calculates `Total Sales` from `Units Sold × Unit Price`
- 📊 Groups data by `Product` and summarizes total revenue
- 📈 Visualizes the total sales per product using a bar chart

---

## ✅ What I Learned

Through this project, I gained hands-on experience in:

- Creating and modifying Pandas DataFrames
- Performing column-wise arithmetic operations
- Using `.groupby()` and `.sum()` for data aggregation
- Plotting charts using `Matplotlib` and `Pandas`' built-in plotting
- Saving and updating CSV files with `to_csv()`

---

## 📚 What I Had to Learn

| 🧠 Topic         | 📘 Description                                                                 |
|------------------|--------------------------------------------------------------------------------|
| `pandas`         | Python library used for data manipulation and analysis                         |
| `matplotlib`     | Visualization library for plotting data                                        |
| `groupby()`      | Pandas function to group data and apply aggregate functions like `.sum()`      |
| `to_csv()`       | Saves the modified DataFrame to a `.csv` file                                  |
| `plot(kind='bar')` | Used to create a bar chart directly from a Pandas Series or DataFrame         |

---

## 🔧 How to Run

### 1️⃣ Install Requirements

```bash
pip install pandas matplotlib





# 🖼️ Image Resizer Tool (Batch Processor)

A simple Python tool to **resize and convert multiple images** in a folder using the `Pillow` library. Automate image tasks like standardizing dimensions or preparing for web uploads.

---

## 📌 Features

- ✅ Batch resize all images in a folder
- ✅ Convert image formats (e.g., PNG → JPG)
- ✅ Set custom dimensions and output quality
- ✅ Works with JPG, PNG, WebP, BMP, etc.

---

## ⚙️ How It Works

1. Reads all images from the `images/` folder.
2. Resizes them to the defined target size (default: `800x800`).
3. Converts the format (default: `JPEG`) and saves them to the `resized/` folder.

---

## 📚 What You’ll Learn

To understand and modify this project, you'll need:

- Basics of **Python scripting**
- File operations using the `os` module
- Image processing with **Pillow** (`PIL`)
- Exception handling and directory automation

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/image-resizer-batch-tool.git
cd image-resizer-batch-tool




# 🌐 Flask Portfolio Website

A clean and responsive personal portfolio website built using Python and Flask.  
Perfect for showcasing your skills, projects, and education — with a functional contact form for leads or collaboration.

---

## 📌 Features

✅ Dynamic portfolio using Flask and Jinja2 templating  
✅ Clean homepage with objective, skills, education, and certifications  
✅ Contact form with flash message feedback  
✅ Mobile-friendly layout with modern CSS  
✅ Easy to expand: Add blogs, projects, or resume pages  

---

## ⚙️ How It Works

1. Flask handles routing and rendering HTML templates  
2. Pages are styled with custom CSS (located in `static/css`)  
3. Contact form sends POST data and triggers a thank-you flash  
4. Content is modular and editable in the `templates/` folder  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/muzakkir2045/portfolio.git
cd flask-portfolio-site
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Then go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## 📁 Project Structure

```
portfolio_site/
├── app.py                  # Main Flask app
├── requirements.txt        # Flask dependency
├── static/
│   └── css/
│       └── styles.css      # Styling rules
└── templates/
    ├── base.html           # Reusable layout
    ├── index.html          # Portfolio content
    └── contact.html        # Contact form
```




# 🧠 Rule-Based Chatbot in Python

This is a simple **rule-based chatbot** built using Python's `if-elif-else` logic. It simulates a basic conversation and demonstrates the fundamentals of how traditional chatbots work without using any machine learning or NLP libraries.

---

## 📌 Features

- Responds to common greetings like "hi", "hello"
- Answers simple questions like:
  - "What is your name?"
  - "How are you?"
  - "What time is it?"
- Handles unknown inputs gracefully
- Exits the conversation when the user types "bye"

---

## 🚀 Getting Started

### How to Run

1. Clone this repo or copy the script to a `.py` file:
    ```bash
    python chatbot.py
    ```
2. Start chatting with the bot in your terminal!
3. Type `bye` to end the conversation.

---

## 📘 Concepts Used

- Input/output handling with `input()` and `print()`
- Conditional statements (`if`, `elif`, `else`)
- Basic string matching
- Using built-in modules (`datetime`)

---

## 📦 Outcome

This chatbot is a great beginner-friendly project to understand how traditional chatbots work using simple rules and logic.

---

## 💡 Future Improvements

- Add more responses for different inputs
- Use regex or keyword lists for better matching
- Build a GUI using Tkinter or a web interface using Flask


