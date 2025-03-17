# 📚 The Library's Lost Books

## 📝 Project Description  
Imagine you're helping a library that recently digitized its collection. Unfortunately, the digital catalog has become corrupted, and some book records are missing crucial information.  

Your task is to **organize and fix the library's digital catalog** by processing a CSV file with book entries.  

---

## 📂 Input Format  
The CSV file contains book entries with the following fields:  

- **Title** (always present)  
- **Author** (may be missing)  
- **Publication Year** (may be invalid: negative, far in the future, or non-numeric)  

---

## 🔧 Objectives  
✔️ Create a **structured system** to store book information.  
✔️ Identify and **correct missing or invalid data**:  
   - Assign **"Author Unknown"** to books without an author.  
   - Replace **invalid publication years** with `0`.  
✔️ **Remove duplicate** entries (same title and author).  
✔️ Present a **clean, organized list** of books.  
✔️ Allow users to view books **grouped by Author or Publication Year**.  

---

## 🚀 Features  
✅ Load and clean book data from a CSV file.  
✅ Search for books by **title** or **author**.  
✅ **Add new books** dynamically.  
✅ Save cleaned data back to a **CSV file**.  
✅ Export organized book lists to **.txt files**.  

---

## 🛠️ Installation & Usage  

1️⃣ **Clone this repository:**  
```bash
git clone https://github.com/paulachudnosky/The-Librarys-Lost-Books.git
cd The-Librarys-Lost-Books
```


2️⃣ **Run the program:**
```bash
python main.py
```

## 📜 License
This project is for educational purposes. Feel free to use and modify it!
