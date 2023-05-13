from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup, QTextEdit, QLineEdit, QListWidget, QInputDialog
import json

app = QApplication([])
main_wid = QWidget()
main_wid.setWindowTitle('Умные заметки')
#TextGroupBox = QGroupBox('Список заметок')
r_list1 = QListWidget()
r_text = QTextEdit()
r_list2 = QListWidget()
create_z = QPushButton('Создать заметку')
delete_z = QPushButton('Удалить заметку')
save_z = QPushButton('Сохранить заметку')
r_line = QLineEdit()
add_z = QPushButton('Добавить к заметке')
unpin_z = QPushButton('Открепить от заметки')
find_z = QPushButton('Искать заметки по тэгу')
label1 = QLabel('Список заметок')
label2 = QLabel('Список тэгов')

Layout1 = QHBoxLayout()
Layout2 = QHBoxLayout()
Layout11 = QVBoxLayout()
Layout22 = QVBoxLayout()
Layout111 = QHBoxLayout()
Layout11.addWidget(r_text)
Layout22.addWidget(label1)
Layout22.addWidget(r_list1)
Layout1.addWidget(create_z)
Layout1.addWidget(delete_z)
Layout22.addLayout(Layout1)
Layout22.addWidget(save_z)
Layout22.addWidget(label2)
Layout22.addWidget(r_list2)
Layout22.addWidget(r_line)
Layout2.addWidget(add_z)
Layout2.addWidget(unpin_z)
Layout22.addLayout(Layout2)
Layout22.addWidget(find_z)
Layout111.addLayout(Layout11)
Layout111.addLayout(Layout22)
main_wid.setLayout(Layout111)

notes = dict()
notes = {'Добро пожаловать отсюда':
            {'text':'жжжжжжжжжжжжжжжжжжжжжжжжжжжжжж',
             'tags':['эээээээээ1','эээээээээ2']}
}

with open('notes_data.json', 'w', encoding = 'utf-8')as file:
    json.dump(notes, file, sort_keys=True)



main_wid.show()

with open('notes_data.json', 'r', encoding = 'utf-8')as file:
    notes = json.load(file)
    key = notes.keys()
r_list1.addItems(key)
# r_text.setText(text)

def show_note():
    name = r_list1.selectedItems()[0].text()
    r_text.setText(notes[name]['text'])
    r_list2.clear()
    r_list2.addItems(notes[name]['tags'])
    
def add_note():
    r_note, result = QInputDialog.getText(main_wid, 'добавить заметку', 'название заметки:')
    if result and r_note != '':
        notes[r_note] = {'text':'', 'tags':[]}
    r_list1.addItem(r_note)

def save_note():
    if r_list1.selectedItems():
        r_thing2 = r_list1.selectedItems()[0].text()
        r_thing1 = r_text.toPlainText()
        notes[r_thing2]['text'] = r_thing1

def del_note():
    if r_list1.selectedItems():
        r_thing3 = r_list1.selectedItems()[0].text()
        global notes
        del notes[r_thing3]
        r_list1.clear()
        r_text.clear()
        with open('notes_data.json', 'r', encoding = 'utf-8')as file:
            notes = json.load(file)
            key = notes.keys()
        r_list1.addItems(key)

def search_tag():
    r_tag1 = r_line.text()
    if find_z.text() == 'Искать заметки по тэгу' and r_tag1:
        r_list11 = {}
        for note in notes:
            if r_tag1 in notes[note]['tags']:
                r_list11[note]=notes[note]
        find_z.setText('Сбросить поиск')
        r_list1.clear()
        r_list2.clear()
        r_list1.addItems(r_list11)
    elif find_z.text() == 'Сбросить поиск':
        r_line.clear()
        r_list1.clear()
        r_list2.clear()
        r_list1.addItems(notes)
        find_z.setText('Искать заметки по тэгу')
    
def save_tag():
    if r_list1.selectedItems():
        r_thing2 = r_list1.selectedItems()[0].text()
        r_thing1 = r_line.text()
        notes[r_thing2]['tags'].append(r_thing1)



create_z.clicked.connect(add_note) 
save_z.clicked.connect(save_note)
delete_z.clicked.connect(del_note)
find_z.clicked.connect(search_tag)
add_z.clicked.connect(save_tag)
r_list1.itemClicked.connect(show_note)
app.exec_()