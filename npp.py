 

---

### 🛠️ Project: Password Strength Meter

#### ✅ Features:
- User inputs a password.
- App evaluates password strength (Weak, Medium, Strong).
- Checks for length, use of uppercase, lowercase, numbers, and symbols.

---

### 📁 Project Structure

```
password_strength_meter/
│
├── main.py
├── requirements.txt
└── README.md
```

---

### 📦 Step 1: Create `requirements.txt`

```txt
streamlit
```

---

### 🧠 Step 2: Create `main.py`

```python
import streamlit as st
import re

def check_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    total_errors = sum([length_error, lowercase_error, uppercase_error, digit_error, symbol_error])

    if total_errors == 0:
        return "Strong 💪"
    elif total_errors <= 2:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength = check_strength(password)
    st.write(f"**Password Strength:** {strength}")
```

---

### 🧪 Step 3: Run Your Project

1. Open your terminal in VS Code.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run main.py
```

---

### ✅ Optional `README.md`

```md
# Password Strength Meter

A beginner-friendly app built with Streamlit to check how strong your password is.

## How it works

- Analyzes the password for:
  - Length (8+ characters)
  - Uppercase and lowercase letters
  - Numbers
  - Symbols

## Run it locally

```bash
pip install -r requirements.txt
streamlit run main.py
```
```

---

