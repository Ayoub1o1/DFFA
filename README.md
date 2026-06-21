# 🐉 DFFA: Data Fetcher for API & Explorer

DFFA is a robust, interactive **Command-Line Interface (CLI)** tool built for **Data Scientists and Developers**.

It allows users to dynamically fetch data from any JSON API and navigate through deeply nested structures in real-time.

Whether you are performing **Exploratory Data Analysis (EDA)** on a new API, inspecting schema structures before writing extraction scripts, or exploring public datasets like the **Rick and Morty API** or **Dragon Ball API**, DFFA provides a fast, secure, and intuitive interface.

---

# 🌟 Key Features

## 🔍 Interactive Recursive Navigation

Dynamically explores nested JSON structures:

- Dictionaries (`objects`)
- Lists (`arrays`)
- Primitive values

No need to write custom parsing logic.

---

# 🛠️ Installation

## Requirements

- Python **3.8+**
- `requests` library

---

## Clone Repository

```bash
git clone https://github.com/Ayoub1o1/DFFA.git

cd DFFA
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Usage

Run the application:

```bash
python main.py
```

---

# Example Workflow

## Using Rick and Morty API

Enter an API endpoint:

```text
Enter the API URL:
https://rickandmortyapi.com/api/character
```

DFFA displays available keys:

```text
Available items:

0 : info
1 : results
```

Select an item:

```text
Choose item (or "back"/"quit"):
1
```

Navigate through the JSON structure:

```text
Available items:

0 : dict
1 : dict
2 : dict
...
```

Choose the first character:

```text
Choose item:
0
```

Explore character fields:

```text
Available items:

0 : id
1 : name
2 : status
3 : species
...
```

Select the name:

```text
Choose item:
1
```

Final output:

```text
Final Value at root.results[0].name:

Rick Sanchez
```

---

# 🎮 Navigation Commands

| Command | Description |
|---------|-------------|
| `<Number>` | Selects an item by index |
| `back` | Returns to the previous level |
| `quit` | Exits the application |
| `Enter` | Returns to the JSON root (only on final values) |

---

# 💡 Data Science Use Cases

## 🔎 Schema Discovery

Before creating complex:

- Pandas pipelines
- ETL workflows
- Data extraction scripts

Use DFFA to understand unknown API structures quickly.

---

## ✅ Data Validation

Quickly check if API responses contain:

- Missing fields
- Empty objects `{}` 
- Empty arrays `[]`
- Null values `None`

---

## ⚡ Ad-Hoc API Exploration

Explore public APIs without creating temporary scripts.

Examples:

- Open datasets
- Public APIs
- Developer APIs

Avoid heavy GUI tools when you only need quick inspection.

---

# 📂 Project Structure

Example:

```
dffa-api-explorer/
│
├── dffa.py
├── main.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# ❤️ Built For

The **Data Science and Developer community**.

Explore APIs. Understand structures. Build better pipelines.

🐉 **DFFA — Data Fetcher For API & Explorer**
