# -*- coding: utf-8 -*-
import sys, time

from PySide import QtGui, QtCore

from presentacion.form_abm_paciente import FormPacienteABM


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QtGui.QPixmap('splash.png')

    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(
        QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
    splash.setEnabled(False)
    # splash = QSplashScreen(splash_pix)
    # adding progress bar
    progressBar = QtGui.QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(0, 0, splash_pix.width(),
                            20)
    css = "QProgressBar::chunk { background: yellow; }"
    progressBar.setStyleSheet(css)
    # splash.setMask(splash_pix.mask())

    splash.show()

    for i in range(1, 11):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    # Simulate something that takes time
    time.sleep(1)
    form = FormPacienteABM()
    form.show()
    splash.close()

    sys.exit(app.exec_())
