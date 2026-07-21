class Employee:
    def __init__(self):
        self.emp_id = int(input("Enter the id: "))
        self.emp_name = input("Enter the name: ")
        self.basic_pay = int(input("Enter the basic pay: "))
        self.ta = int(input("Enter the ta: "))
        self.da = int(input("Enter the da: "))

    def calc(self):
        self.gross_pay = self.basic_pay + (0.10 * self.ta) + (0.40 * self.da)

    def display(self):
        print("Emp details:")
        print("emp_id -", self.emp_id)
        print("emp_name -", self.emp_name)
        print("basic_pay -", self.basic_pay)
        print("ta -", self.ta)
        print("da -", self.da)
        print("gross_pay -", self.gross_pay)


e = Employee()
e.calc()
e.display()
