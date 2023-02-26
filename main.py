import sys
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Plotter")
        self.setFixedSize(400, 300)

        # Add logo image to the upper left corner
        logo = QLabel(self)
        pixmap = QPixmap('logo.png')
        pixmap = pixmap.scaled(8, 8, Qt.AspectRatioMode.KeepAspectRatio)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # Create the main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Create the input fields and button
        y_label = QLabel("Y values:", self)
        y_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        y_label.setFont(QFont('Arial', 24))
        y_input = QLineEdit(self)
        y_input.setPlaceholderText("Enter values separated by commas")
        plot_button = QPushButton("Plot", self)
        plot_button.setFont(QFont('Arial', 24))

        # Add the input fields and button to the layout
        layout.addWidget(logo)
        layout.addWidget(y_label)
        layout.addWidget(y_input)
        layout.addWidget(plot_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Connect the button to the plot function
        plot_button.clicked.connect(lambda: self.plot(y_input.text()))

    def plot(self, y_values):
        # Convert the input values to a list of integers
        y_list = []
        for y in y_values.split(","):
            try:
                y_int = int(y)
                # Exclude non-integer values
                if y_int == float(y_int):
                    y_list.append(y_int)
            except ValueError:
                # FIXME: There should be a better exception handler
                pass

        # Create a dictionary to store the count of values by first digit
        digit_dict = {}
        for y in y_list:
            first_digit = int(str(abs(y))[0])
            if first_digit not in digit_dict:
                digit_dict[first_digit] = 0
            digit_dict[first_digit] += 1

        # Get the counts for each first digit group
        counts = []
        for i in range(1, 10):
            if i in digit_dict:
                count = digit_dict[i]
            else:
                count = 0
            counts.append(count)

        # Generate the data for the plot
        x = list(range(1, 10))
        y = counts

        # Create the plot and show it
        plt.plot(x, y, 'bo-', markersize=8)
        plt.xticks(x, [str(i) for i in x])
        plt.xlabel("First Digits", fontsize=12)
        plt.ylabel("Occurrences", fontsize=12)
        plt.title("First Digit Graph", fontsize=14)
        plt.grid(True)

        # Show the plot in a new window
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
