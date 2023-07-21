#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import qdarktheme
import traceback


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)    
    

from mainwindow import MainWindow


def Main() -> None:
    """Main Routine for the Application. """
    
    try:
        """Try, Except, Finally"""
        
        app = QApplication(sys.argv)
        """First we instantiate the App."""

        window = MainWindow(app)
        window.show()

    except Exception as err:
        
        print("Unfortunately we have encountered an error \
and are unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception() # type: ignore

    finally:
        sys.exit(app.exec())


if __name__ == '__main__':
    Main()