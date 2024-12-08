from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator for the Nerds')
        self.setGeometry(300,300,500,400)

        # Setting Window Icon
        icon_pixmap = QPixmap('Icon.png')
        icon_pixmap = icon_pixmap.scaled(64,64)
        self.setWindowIcon(QIcon(icon_pixmap))

        # Fixed Window Size
        self.setFixedSize(600,350)

       

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Input Fields
        self.value1_input = QLineEdit()
        self.value1_input.setPlaceholderText("Enter Value 1")
        self.value1_input.setMinimumHeight(40) # Bigger Display
        self.value1_input.setStyleSheet("font-size: 16px;")
        self.main_layout.addWidget(self.value1_input)

        self.operator_input = QLineEdit()
        self.operator_input.setPlaceholderText("Enter Operator (+, -, *, /)")
        self.operator_input.setMinimumHeight(40) # Bigger Display
        self.operator_input.setStyleSheet("font-size: 16px;")
        self.main_layout.addWidget(self.operator_input)

        self.value2_input = QLineEdit()
        self.value2_input.setPlaceholderText("Enter Value 2")
        self.value2_input.setMinimumHeight(40) # Bigger Display
        self.value2_input.setStyleSheet("font-size: 16px;")
        self.main_layout.addWidget(self.value2_input)

        # Label for the results
        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignLeft)
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText("Result: ")
        self.result_display.setMinimumHeight(50) # Bigger Display
        self.result_display.setStyleSheet("font-size: 18px;")
        self.main_layout.addWidget(self.result_display)

        # Buttons
        self.buttons_layout = QVBoxLayout()
        self.calculate_button = QPushButton("Calculate")
        self.clear_button = QPushButton("Clear")

        self.calculate_button.setMinimumHeight(40)
        self.clear_button.setMinimumHeight(40)
        self.calculate_button.setStyleSheet("font-size: 16px;")
        self.clear_button.setStyleSheet("font-size: 16px;")

        self.buttons_layout.addWidget(self.calculate_button)
        self.buttons_layout.addWidget(self.clear_button)
        self.main_layout.addLayout(self.buttons_layout)

        # Bind Button Clicks
        self.calculate_button.clicked.connect(self.calculate)
        self.clear_button.clicked.connect(self.clear_inputs)

        # Message Label
        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setMinimumHeight(40)
        self.message_label.setStyleSheet("font-size: 40px;")
        self.main_layout.addWidget(self.message_label)

    def check_input(self, value):
        try:
            # Returns the value as an int
            return int(value)
        except ValueError:
            try:
                # If it's not an int, it might be a float
                return float(value)
            except ValueError:
                return None

    def calculate(self):
        value1 = self.check_input(self.value1_input.text())
        operator = self.operator_input.text()
        value2 = self.check_input(self.value2_input.text())

        if value1 is None or value2 is None:
            self.message_label.setText("Error: Invalid Input. Please enter numbers only.")
            self.message_label.setStyleSheet("color: red;")
            return

        try:
            match operator:
                case '+':
                    result = value1 + value2
                case '-':
                    result = value1 - value2
                case '*':
                    result = value1 * value2
                case '/':
                    if value2 == 0:
                        raise ZeroDivisionError("Division by Zero is not allowed.")
                    result = value1 / value2
                case _:
                    self.message_label.setText("Error: Invalid Operator.")
                    self.message_label.setStyleSheet("color: red;")
                    return

            self.result_display.setText(str(result))
            self.message_label.setText("Calculation Successful!")
            self.message_label.setStyleSheet("font-size: 16px;")
            self.message_label.setMinimumHeight(40)
            self.message_label.setStyleSheet("color: green;")
        except ZeroDivisionError as e:
            self.result_display.setText("")
            self.message_label.setText(str(e))
            self.message_label.setStyleSheet("color: red;")

    def clear_inputs(self):
        self.value1_input.clear()
        self.operator_input.clear()
        self.value2_input.clear()
        self.result_display.clear()
        self.message_label.setText("")

# Main entry point
if __name__ == "__main__":
    app = QApplication([])  # Create the application instance
    calculator = CalculatorApp()  # Create the CalculatorApp window
    calculator.show()  # Show the window
    app.exec()  # Start the application's event loop