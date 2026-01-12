# Python Calculator with Pytest & GitHub Actions

This project is a **Python Calculator** built to demonstrate:

- Clean **Git & GitHub repository structure**
- Writing **unit tests using pytest**
- Enforcing **code quality with Black and Flake8**
- Running automated tests and linting via **GitHub Actions (CI pipeline)**

It is designed to showcase practical skills for entry-level **DevOps / Cloud / Software Engineer** roles.

---

## 🚀 Features

- Basic calculator operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Automated unit testing using **pytest**
- Code formatting with **Black**
- Code linting with **Flake8**
- Continuous Integration using **GitHub Actions**

---

## 📂 Project Structure

Python_github/
│
├── operations/
│ ├── init.py
│ └── calculator.py
│
├── tests/
│ ├── init.py
│ └── test_calculator.py
│
├── .github/
│ └── workflows/
│ └── ci.yml
│
├── .gitignore
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🧠 How It Works

### Calculator Functions
All calculator logic is implemented in:

```text
operations/calculator.py
Functions:

add(x, y)

sub(x, y)

mul(x, y)

div(x, y)

Unit Testing
Tests are in:

text
Copy code
tests/test_calculator.py
Written with pytest

Automatically discovered and run by GitHub Actions

Ensures correctness of all calculator operations

Code Quality & Linting
Black: enforces consistent code formatting

Flake8: enforces linting rules and catches syntax issues

Both run automatically in GitHub Actions

Continuous Integration
GitHub Actions pipeline:

Checks out the code

Installs dependencies

Runs pytest

Runs Black and Flake8

Fails the workflow if any test or lint check fails

This ensures code quality and reliability for every push or pull request.

▶️ Run Locally
1️⃣ Clone the repository
bash
Copy code
git clone <your-repo-url>
cd Python_github
2️⃣ Create a virtual environment
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run tests
bash
Copy code
pytest -v
5️⃣ Check code quality
bash
Copy code
flake8 .
black --check .
🧹 Repository Hygiene
.venv/ is ignored using .gitignore

.DS_Store is ignored

Modular folder structure

Clear naming conventions

🔮 Future Improvements
Add test coverage reporting

Integrate pre-commit hooks for linting

Add Docker support later for containerized CI/CD

👩‍💻 Author
Suhani Sharma
Cloud / DevOps Enthusiast
AWS | Terraform | GitHub | CI/CD | Python
