import sys
import os
import PySide6
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog, QLineEdit, QButtonGroup, QCompleter
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor


from genscheduleinterface import Ui_MainWindow
from geneditwindow import Ui_Dialog

conn = sqlite3.connect('schedule.db')
cursor = conn.cursor()

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class EditWindow(QDialog):
    def __init__(self):
        super(EditWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.current_time_slot = None
        self.current_group_number = None
        self.current_day_week = None
        self.current_edit_widget = None

        self.need_row = []
        self.index = 0

        self.ui.saveButton.clicked.connect(self.save_edit)
        self.ui.deleteButton.clicked.connect(self.delete_edit)
        self.ui.createButton.clicked.connect(self.create_edit)

        self.ui.nextBtn.clicked.connect(self.load_row)

        times = ["8.30-10.00", "10.10-11.40", "11.50-13.20", "13.50-15.20", "15.30-17.00", "17.10-18.40"]
        self.ui.timeBox.addItems(times)

        self.radChoose = QButtonGroup(self)
        self.radChoose.addButton(self.ui.radChot)
        self.radChoose.addButton(self.ui.radNech)
        self.radChoose.addButton(self.ui.radNo)
        self.radLess = QButtonGroup(self)
        self.radLess.addButton(self.ui.radLec)
        self.radLess.addButton(self.ui.radPrac)   

    def load_info(self, time_slot, group_number, day_week, edit_widget):
        self.current_edit_widget = edit_widget
        self.current_group_number = group_number
        self.current_day_week = day_week

        cursor.execute('''
            SELECT id, tme, type_week, subject, type_subject, teacher, room, group_number, day_week
            FROM schedule_h
            WHERE group_number = ? AND day_week = ?;
        ''', (group_number, day_week))
        self.need_row = cursor.fetchall()

        if self.need_row:
            self.show_row(self.index)
        else:
            index = self.ui.timeBox.findText(time_slot)
            if index >= 0:
                self.ui.timeBox.setCurrentIndex(index)
            self.ui.subjectETEXT.clear()
            self.ui.teacherETEXT.clear()
            self.ui.roomETEXT.clear()
            self.ui.groupETEXT.setText(str(group_number))
            self.ui.radNo.setChecked(True)
            self.ui.radLec.setChecked(False)
            self.ui.radPrac.setChecked(False)

            self.original_time_slot = time_slot
            self.original_group_number = group_number
            self.original_day_week = day_week

            self.current_time_slot = time_slot
            self.current_group_number = group_number
            self.current_day_week = day_week

    def show_row(self, index):
        if 0 <= index < len(self.need_row):
            self.current_id, time_val, nechot_val, subject_val, lesson_val, teacher_val, room_val, group_val, day_val = self.need_row[index]

            self.current_time_slot = time_val
            self.current_group_number = group_val
            self.current_day_week = day_val

            self.original_time_slot = time_val
            self.original_group_number = group_val
            self.original_day_week = day_val

            index_time = self.ui.timeBox.findText(str(time_val))
            if index_time >= 0:
                self.ui.timeBox.setCurrentIndex(index_time)
            self.ui.subjectETEXT.setText(str(subject_val))
            self.ui.teacherETEXT.setText(str(teacher_val))
            self.ui.roomETEXT.setText(str(room_val))
            self.ui.groupETEXT.setText(str(group_val))

            self.ui.radChot.setChecked(False)
            self.ui.radNech.setChecked(False)
            self.ui.radNo.setChecked(False)
            self.ui.radLec.setChecked(False)
            self.ui.radPrac.setChecked(False)

            if nechot_val == 'чёт':
                self.ui.radChot.setChecked(True)
            elif nechot_val == 'нечёт':
                self.ui.radNech.setChecked(True)
            else:
                self.ui.radNo.setChecked(True)

            if lesson_val == 'лекция':
                self.ui.radLec.setChecked(True)
            elif lesson_val == 'практика':
                self.ui.radPrac.setChecked(True)


    def load_row(self):
        if not self.need_row:
            return
        self.index += 1
        if self.index >= len(self.need_row):
            self.index = 0
        self.show_row(self.index)

    def save_edit(self):
        time_val = self.ui.timeBox.currentText()
        nechot_val = self.radChoose.checkedButton().text()
        subject_val = self.ui.subjectETEXT.text()
        lesson_val = self.radLess.checkedButton().text()
        teacher_val = self.ui.teacherETEXT.text()
        room_val = self.ui.roomETEXT.text()
        group_val = self.ui.groupETEXT.text()

        cursor.execute('''
            UPDATE schedule_h SET
                tme = ?,
                type_week = ?,
                subject = ?,
                type_subject = ?,
                teacher = ?,
                room = ?,
                group_number = ?,
                day_week = ?
            WHERE id = ?;
        ''', (time_val, nechot_val, subject_val, lesson_val, teacher_val, room_val, group_val, self.current_day_week, self.current_id))
        conn.commit()

        self.close()

    def delete_edit(self):
        cursor.execute('''
            DELETE FROM schedule_h
            WHERE id = ?;
        ''', (self.current_id,))
        conn.commit()
        self.close()

    def create_edit(self):
        time_val = self.ui.timeBox.currentText()
        nechot_val = self.radChoose.checkedButton().text()
        subject_val = self.ui.subjectETEXT.text()
        lesson_val = self.radLess.checkedButton().text()
        teacher_val = self.ui.teacherETEXT.text()
        room_val = self.ui.roomETEXT.text()
        group_val = self.ui.groupETEXT.text()
        day_val = self.current_day_week

        cursor.execute('''
            INSERT INTO schedule_h (tme, day_week, type_week, subject, type_subject, teacher, room, group_number)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        ''', (time_val, day_val, nechot_val, subject_val, lesson_val, teacher_val, room_val, group_val))
        conn.commit()
        self.close()


class ScheduleInterface(QMainWindow):
    def __init__(self):
        super(ScheduleInterface, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.editingFinished.connect(self.show_full)
        self.ui.allEdit.textChanged.connect(self.highlight)

        self.ui.roomBox.stateChanged.connect(self.checkbox_filters)
        self.ui.lessonBox.stateChanged.connect(self.checkbox_filters)
        self.ui.teacherBox.stateChanged.connect(self.checkbox_filters)
        self.ui.subjectBox.stateChanged.connect(self.checkbox_filters)
        self.ui.weekBox.stateChanged.connect(self.checkbox_filters)
        self.ui.timeBox.stateChanged.connect(self.checkbox_filters)

        self.possible_line()

        self.daysntimes = {
            'понедельник': [
                ("8.30-10.00", self.ui.mon1Edit),
                ("10.10-11.40", self.ui.mon2Edit),
                ("11.50-13.20", self.ui.mon3Edit),
                ("13.50-15.20", self.ui.mon4Edit),
                ("15.30-17.00", self.ui.mon5Edit),
                ("17.10-18.40", self.ui.mon6Edit)
            ],
            'вторник': [
                ("8.30-10.00", self.ui.tue1Edit),
                ("10.10-11.40", self.ui.tue2Edit),
                ("11.50-13.20", self.ui.tue3Edit),
                ("13.50-15.20", self.ui.tue4Edit),
                ("15.30-17.00", self.ui.tue5Edit),
                ("17.10-18.40", self.ui.tue6Edit)
            ],
            'среда': [
                ("8.30-10.00", self.ui.wed1Edit),
                ("10.10-11.40", self.ui.wed2Edit),
                ("11.50-13.20", self.ui.wed3Edit),
                ("13.50-15.20", self.ui.wed4Edit),
                ("15.30-17.00", self.ui.wed5Edit),
                ("17.10-18.40", self.ui.wed6Edit)
            ],
            'четверг': [
                ("8.30-10.00", self.ui.thr1Edit),
                ("10.10-11.40", self.ui.thr2Edit),
                ("11.50-13.20", self.ui.thr3Edit),
                ("13.50-15.20", self.ui.thr4Edit),
                ("15.30-17.00", self.ui.thr5Edit),
                ("17.10-18.40", self.ui.thr6Edit)
            ],
            'пятница': [
                ("8.30-10.00", self.ui.fri1Edit),
                ("10.10-11.40", self.ui.fri2Edit),
                ("11.50-13.20", self.ui.fri3Edit),
                ("13.50-15.20", self.ui.fri4Edit),
                ("15.30-17.00", self.ui.fri5Edit),
                ("17.10-18.40", self.ui.fri6Edit)
            ],
            'суббота': [
                ("8.30-10.00", self.ui.sat1Edit),
                ("10.10-11.40", self.ui.sat2Edit),
                ("11.50-13.20", self.ui.sat3Edit),
                ("13.50-15.20", self.ui.sat4Edit),
                ("15.30-17.00", self.ui.sat5Edit),
                ("17.10-18.40", self.ui.sat6Edit)
            ],
            'воскресенье': [
                ("8.30-10.00", self.ui.sun1Edit),
                ("10.10-11.40", self.ui.sun2Edit),
                ("11.50-13.20", self.ui.sun3Edit),
                ("13.50-15.20", self.ui.sun4Edit),
                ("15.30-17.00", self.ui.sun5Edit),
                ("17.10-18.40", self.ui.sun6Edit)
            ]
        }
        self.connect_double_clicks()

        self.edit_window = EditWindow()

    def highlight(self):
        highlightable = self.ui.allEdit.text()
        if not highlightable:
            self.clear_highlight()
            return
        for dayweek, timenwidget in self.daysntimes.items():
            for _, edit_widget in timenwidget:
                self.highlight_text(edit_widget, highlightable)

    def clear_highlight(self):
        for dayweek, timenwidget in self.daysntimes.items():
            for _, edit_widget in timenwidget:
                text = edit_widget.toPlainText() if hasattr(edit_widget, 'toPlainText') else edit_widget.text()
                if hasattr(edit_widget, 'clear'):
                    edit_widget.clear()
                if hasattr(edit_widget, 'setPlainText'):
                    edit_widget.setPlainText(text)
                elif hasattr(edit_widget, 'setText'):
                    edit_widget.setText(text)

    def highlight_text(self, widget, text):
        if not hasattr(widget, 'toPlainText'):
            return
        content = widget.toPlainText()
        widget.moveCursor(QTextCursor.Start)
        cursor = widget.textCursor()
        fmt_clear = QTextCharFormat()
        fmt_clear.setBackground(Qt.transparent)
        cursor.select(QTextCursor.Document)
        cursor.setCharFormat(fmt_clear)
        cursor.clearSelection()
        widget.setTextCursor(cursor)
        fmt = QTextCharFormat()
        fmt.setBackground(QColor('#F473B1'))
        pos = 0
        while True:
            pos = content.lower().find(text.lower(), pos)
            if pos == -1:
                break
            cursor.setPosition(pos)
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(text))
            cursor.mergeCharFormat(fmt)
            pos += len(text)
    
    def possible_line(self):
        cursor.execute('SELECT DISTINCT group_number FROM schedule_h')
        groups = [row[0] for row in cursor.fetchall() if row[0]]
        completer = QCompleter(groups)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.ui.lineEdit.setCompleter(completer)

    def connect_double_clicks(self):
        for dayweek, timenwidget in self.daysntimes.items():
            for time_slot, edit_widget in timenwidget:
                edit_widget.mouseDoubleClickEvent = lambda event, slot=time_slot, widget=edit_widget, day=dayweek: self.on_double_click(event, slot, widget, day)

    def on_double_click(self, event, time_slot, edit_widget, day_week):
        password, ok = QInputDialog.getText(self, 'Требуется пароль', 'Введите пароль:', echo=QLineEdit.Password)
        if ok and self.check_password(password):
            group_number = self.ui.lineEdit.text()
            self.edit_window.load_info(time_slot, group_number, day_week, edit_widget)
            self.edit_window.show()
            self.edit_window.raise_()
            self.edit_window.activateWindow()

    def check_password(self, password):
        return password == '1'
    
    def show_full(self):
        search = self.ui.lineEdit.text()
        for dayweek, timenwidget in self.daysntimes.items():
            self.display_schedule(search, dayweek, timenwidget)

    def display_schedule(self, search, dayweek, timenwidget):
        for time_sche, edit_widget in timenwidget:
            cursor.execute(f'''
                SELECT type_week, subject, type_subject, teacher, group_number, room
                FROM schedule_h
                WHERE group_number = ? and tme=? and day_week=?;		
            ''', (search, time_sche, dayweek))

            schedule = cursor.fetchall()
            line_row = []
            for row in schedule:
                line_connect = '\n==================\n'.join(str(item) for item in row if item)+'\n   |     |     |     |     |     |     |     |\n++++++++++++++++++\n   |     |     |     |     |     |     |     |'
                line_row.append(line_connect)
            text = '\n'.join(line_row)
            edit_widget.setText(text)

    def checkbox_filters(self):
        position = 0
        search = self.ui.lineEdit.text()
        columns = []
        if self.ui.timeBox.isChecked():
            columns.append('tme')
        if self.ui.teacherBox.isChecked():
            columns.append('teacher')
        if self.ui.lessonBox.isChecked():
            columns.append('type_subject')
        if self.ui.roomBox.isChecked():
            columns.append('room')
        if self.ui.subjectBox.isChecked():
            columns.append('subject')
        if self.ui.weekBox.isChecked():
            columns.append('type_week')
        if not columns:
            for dayweek, timenwidget in self.daysntimes.items():
                for _, edit_widget in timenwidget:
                    edit_widget.clear()
            return
        for dayweek, timenwidget in self.daysntimes.items():
            for time_sche, edit_widget in timenwidget:
                column_name = ', '.join(columns)
                cursor.execute(f'''
                    SELECT {column_name}
                    FROM schedule_h
                    WHERE group_number = ? AND tme = ? AND day_week = ?;
                ''', (search, time_sche, dayweek))
                rows = cursor.fetchall()
                line_row = []
                for row in rows:
                    position += 1
                    line_connect = f'{str(position)}) ' + ' ||| '.join(str(item) for item in row if item)
                    line_row.append(line_connect)
                position = 0
                text = '\n==================\n'.join(line_row)
                edit_widget.setText(text)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ScheduleInterface()
    window.show()

    sys.exit(app.exec())
