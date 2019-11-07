#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows text which 
is entered in a QLineEdit
in a QLabel widget.
 
Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication, QPushButton)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):      

        self.label = QLabel(self)
        self.label.move(180, 150)

        self.description_label = QLabel(self)
        self.description_label.setText("Please enter some search terms. \n" +
                                        "This program will search for the articles\n" +
                                        "to use as documents.")
        self.description_label.adjustSize() 
        self.description_label.move(10,10)

        wiki_line_edit = QLineEdit(self)
        wiki_line_edit.move(180, 200)
        wiki_line_edit.textChanged[str].connect(self.onChanged)

        search_button = QPushButton('Search Wikipedia', self)
        search_button.move(180,250)
        search_button.setToolTip('Select three articles to search for on Wikipedia')

      
        

        
        self.setGeometry(400, 175, 500, 500)
        self.setWindowTitle('Search Project')
        self.show()
        
        
    def onChanged(self, text):
        
        self.label.setText(text)
        self.label.adjustSize()        

           
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())