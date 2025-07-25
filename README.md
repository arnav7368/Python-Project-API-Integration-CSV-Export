# My Project

This is a Django-based web application that allows users to enter multiple search queries and fetch real-time search results using the SerpApi (Google Search API).

The results (title, link, and snippet) are displayed in a tabular format and can be downloaded as a CSV file.

---

## ✅ Features

- Input multiple search queries (one per line)
- Uses SerpApi to fetch Google search results
- Displays title, URL, and snippet for each result
- Responsive and professional Bootstrap UI
- Download all results as a CSV file
- Error handling for:
  - Empty input
  - API issues
  - No results found

---

## 🛠️ Tech Stack

- **Framework**: Django 5.1.3  
- **Python Version**: 3.13  
- **Frontend**: HTML, CSS, Bootstrap 5  
- **API**: [SerpApi](https://serpapi.com/)  
- **Libraries**: `requests`, `pandas`

---

## 🚀 How to Run the Project

> 💡 **Note:** Make sure you're inside the `myproject` folder.

### ✅ Step 1: Install Required Libraries

```bash
pip install django requests pandas
