import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("L5")

        content = QWidget()
        layout = QVBoxLayout(content)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10000)
        layout.addWidget(self.spin_box)

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self._update_button_text)
        layout.addWidget(self.toggle_button)

        self.setCentralWidget(content)

    def _update_button_text(self, is_started):
        self.toggle_button.setText("Stop" if is_started else "Start")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
