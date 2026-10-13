# Python: Multilevel Inheritance

## 📌 Overview

This project demonstrates **Multilevel Inheritance in Python** using simple examples and a real-world student management scenario.

It explains how a child class can inherit properties and methods from its parent class, how to use the `super()` function, and how constructors work in an inheritance hierarchy.

## 🎯 Concepts Covered

* **Multilevel Inheritance:** A class inherits from another class, which inherits from a third class.
* **Constructor (`__init__`):** A special method that initializes an object's attributes.
* **`super()` Function:** Used to access methods or constructors from a parent class.
* **Method Overriding:** A child class provides its own implementation of a method inherited from its parent.
* **Class and Object:** Classes define structures, while objects are instances of those classes.

## 📂 Examples Included

### 1. Basic Multilevel Inheritance

The first example defines three classes:

* `Grandpa`
* `Father`
* `Child`

The `Father` class inherits from `Grandpa`, and the `Child` class inherits from `Father`.

**Inheritance Flow:**

`Grandpa → Father → Child`

This demonstrates how inheritance works across multiple levels.

### 2. Method Overriding and `super()`

The second example demonstrates method overriding using a method named `villa()`.

* `Grandpa` defines the `villa()` method.
* `Father` overrides the method and uses `super().villa()` to call the parent's implementation.
* `Child` overrides the method again.

**Important:** In the original code, `c.villa` references the method but does not execute it. Use `c.villa()` to call the method.

### 3. Constructor Inheritance

The third example demonstrates how constructors work in multilevel inheritance.

* `Grandpa` defines an `__init__()` constructor.
* `Father` is intended to call the grandparent's constructor using `super().__init__()`.
* `Child` calls the constructor of its parent using `super().__init__()`.

**Important:** The original code contains a spelling mistake: `__innit__` should be `__init__`. Python requires the exact spelling of this special method.

### 4. Student Management System

The final example demonstrates multilevel inheritance through a student management scenario.

It contains three classes:

#### `PySpider`

Stores and displays student information:

* Total students
* Total girls
* Total boys

#### `Subject`

Inherits from `PySpider` and adds:

* Subject name
* Total classes

It uses `super().__init__()` to initialize the attributes inherited from `PySpider`.

#### `Result`

Inherits from `Subject` and adds:

* Total marks
* Grade

It uses `super().__init__()` to initialize the attributes of its parent class.

**Inheritance Flow:**

`PySpider → Subject → Result`

The `Result` class can access the information and methods inherited from both `Subject` and `PySpider`.

## 💻 Sample Output

For the following object:

```python
r = Result(250, 50, 30, "Python", 900, 20, "A++")

r.Information()
r.Data()
r.final()
```

The output will be:

```text
Total Students in PY 250
Total Girl 50
Total Boy 30
Subject Name Is Python
Total Class Output 900
Total Marks is 20
Total Grade A++
```

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Copy the code into a Python file, such as `multilevel_inheritance.py`.
3. Save the file.
4. Open a terminal in the folder containing the file.
5. Run the following command:

```bash
python multilevel_inheritance.py
```

## 📚 Learning Outcome

After completing this project, you should understand:

* How multilevel inheritance works in Python.
* How to inherit attributes and methods from parent classes.
* How to use `super()` to initialize parent classes.
* How method overriding changes inherited behavior.
* How to organize related information using classes and objects.

## 👨‍💻 Author

**Pranay Jadhao**

Learning Python, Object-Oriented Programming, and software development.


