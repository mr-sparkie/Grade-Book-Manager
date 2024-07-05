
# GradeBook Manager

GradeBook Manager is a Python application that manages student records in a SQLite database. It provides functionalities to insert, delete, display, and order student records based on grades or names.

![GradeBook Manager](db1.jpg)  <!-- Replace with an image related to your project if available -->

## Features

- **Insert**: Add new student records including first name, last name, major, and grade.
- **Delete**: Remove existing student records by their unique identifier.
- **Display**: View all student records in a tabular format.
- **Orderby**: Sort student records either by grade descending or by first name ascending.
- **Password Protection**: Secure access with a password prompt.

## Requirements

- Python 3.x
- SQLite3
- pandas (for data manipulation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mr-sparkie/GradeBook-Manager.git
   cd GradeBook-Manager
   ```

2. Install dependencies:
   ```bash
   pip install pandas
   ```

## Usage

- Run the application:
  ```bash
  python functions.py
  ```

- Upon running `functions.py`, you will be prompted to enter a password. The default password is `root` (can be changed in `db.py`).

- Choose from the menu options to perform different operations on the student database.

### Example Outputs

#### Insert

```
Kindly enter your name: John
Hello John! Here are the available functions:
1. Insert
2. Delete
3. Orderby
4. Display
Select the number of function you want to do: 1

Enter the first name: Alice
Enter the second name: Smith
Enter the major: Computer Science
Enter grade: 85

Inserted successfully!

Current Records:
   first_name last_name           major  grade
0      Alice     Smith  Computer Science     85

```

#### Delete

```
Kindly enter your name: John
Hello John! Here are the available functions:
1. Insert
2. Delete
3. Orderby
4. Display
Select the number of function you want to do: 2

Records to Delete:
   rowid first_name last_name           major  grade
0      1      Alice     Smith  Computer Science     85

Enter row id you want to delete: 1

Deleted successfully!

Current Records:
Empty DataFrame
Columns: [first_name, last_name, major, grade]
Index: []

```

#### Orderby

```
Kindly enter your name: John
Hello John! Here are the available functions:
1. Insert
2. Delete
3. Orderby
4. Display
Select the number of function you want to do: 3

Select the number of function u want to do: 3
If u want to order them using mark enter 1
if u want to order them in name wise enter 0 1
   first_name last_name           major  grade
0      Alice     Smith  Computer Science     85

```

#### Display

```
Kindly enter your name: John
Hello John! Here are the available functions:
1. Insert
2. Delete
3. Orderby
4. Display
Select the number of function u want to do: 4
  first_name last_name           major  grade
0      Alice     Smith  Computer Science     85

```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


