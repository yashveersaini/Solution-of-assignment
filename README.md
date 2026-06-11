# Django Signals Assignment

## Answers

### Question 1: Are Django signals synchronous or asynchronous by default?

Django signals are **synchronous by default**.

Proof:
The receiver contains a 5-second delay. The code after `signal.send()` executes only after the receiver finishes, showing that the caller waits for the signal execution to complete.

---

### Question 2: Do Django signals run in the same thread as the caller?

Yes, Django signals run in the **same thread** as the caller by default.

Proof:
The thread ID printed inside the caller and inside the signal receiver is the same.

---

### Question 3: Do Django signals run in the same database transaction as the caller?

Yes, Django signals run in the **same database transaction** as the caller by default.

Proof:
A model instance is created inside `transaction.atomic()`. The signal executes successfully, but when the transaction is rolled back, the record is not saved in the database. This shows that the signal execution is part of the same transaction.

---

## Project Structure

django_signals_assignment/

* manage.py
* django_signals_assignment/

  * settings.py
  * urls.py
  * wsgi.py
* signals_app/

  * apps.py
  * models.py
  * signals.py
  * management/

    * commands/

      * run_tests.py

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

requirements.txt

```txt
Django==5.0.6
```

---

## How to Run

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Assignment Tests

```bash
python manage.py run_tests
```

The command will demonstrate:

* Question 1: Synchronous execution
* Question 2: Same thread execution
* Question 3: Same database transaction execution
