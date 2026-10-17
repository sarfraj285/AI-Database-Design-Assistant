
import re

DATABASE_RULES = {
    "student": {
        "table": "students",
        "columns": [
            ("student_id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("name", "VARCHAR(100) NOT NULL"),
            ("email", "VARCHAR(150) UNIQUE"),
            ("course", "VARCHAR(100)")
        ]
    },
    "teacher": {
        "table": "teachers",
        "columns": [
            ("teacher_id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("name", "VARCHAR(100) NOT NULL"),
            ("email", "VARCHAR(150) UNIQUE"),
            ("department", "VARCHAR(100)")
        ]
    },
    "customer": {
        "table": "customers",
        "columns": [
            ("customer_id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("name", "VARCHAR(100) NOT NULL"),
            ("email", "VARCHAR(150) UNIQUE"),
            ("phone", "VARCHAR(20)")
        ]
    },
    "product": {
        "table": "products",
        "columns": [
            ("product_id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("product_name", "VARCHAR(150) NOT NULL"),
            ("price", "DECIMAL(10,2) NOT NULL"),
            ("stock", "INT DEFAULT 0")
        ]
    },
    "employee": {
        "table": "employees",
        "columns": [
            ("employee_id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("name", "VARCHAR(100) NOT NULL"),
            ("email", "VARCHAR(150) UNIQUE"),
            ("salary", "DECIMAL(10,2)")
        ]
    },
    "book": {
        "table": "books",
        "columns": [
            ("book_id", "INT PRIMARY KEY AUTO_INCREMENT"),
            ("title", "VARCHAR(200) NOT NULL"),
            ("author", "VARCHAR(100)"),
            ("isbn", "VARCHAR(20) UNIQUE")
        ]
    }
}

def generate_schema(requirement):
    text = requirement.lower()
    tables = []

    for keyword, data in DATABASE_RULES.items():
        if re.search(r"\b" + keyword + r"s?\b", text):
            sql_columns = [
                f"    {name} {datatype}"
                for name, datatype in data["columns"]
            ]

            sql = (
                f"CREATE TABLE {data['table']} (\n"
                + ",\n".join(sql_columns)
                + "\n);"
            )

            tables.append({
                "name": data["table"],
                "columns": data["columns"],
                "sql": sql
            })

    if not tables:
        return {
            "tables": [],
            "note": "No supported entity found. Try student, teacher, customer, product, employee, or book."
        }

    return {
        "tables": tables,
        "note": "Schema generated successfully. Review the design before using it in a real database."
    }
