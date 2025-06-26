import sys
import os
import PySide6
import sqlite3
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog, QLineEdit, QButtonGroup, QCompleter, QLabel, QVBoxLayout
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
        self.radLess.addButton(self.ui.radOther)
        self.ui.typeEdit.setEnabled(False)
        self.radLess.buttonClicked.connect(self.on_radLess_changed)

    def on_radLess_changed(self):
        checked_button = self.radLess.checkedButton()
        if checked_button == self.ui.radOther:
            self.ui.typeEdit.setEnabled(True)
        else:
            self.ui.typeEdit.setEnabled(False)   

    def load_info(self, time_slot, group_number, day_week):
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
            self.ui.radOther.setChecked(True)
            self.current_group_number = group_number
            self.current_day_week = day_week

    def show_row(self, index):
        if 0 <= index < len(self.need_row):
            self.current_id, time_val, nechot_val, subject_val, lesson_val, teacher_val, room_val, group_val, day_val = self.need_row[index]

            self.current_time_slot = time_val
            self.current_group_number = group_val
            self.current_day_week = day_val

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
                self.ui.typeEdit.setEnabled(False)
            elif lesson_val == 'практика':
                self.ui.radPrac.setChecked(True)
                self.ui.typeEdit.setEnabled(False)
            else:
                self.ui.radOther.setChecked(True)
                self.ui.typeEdit.setEnabled(True)
                self.ui.typeEdit.setText(lesson_val)

    def load_row(self):
        self.index += 1
        if self.index >= len(self.need_row):
            self.index = 0
        self.show_row(self.index)

    def save_edit(self):
        time_val = self.ui.timeBox.currentText()
        nechot_val = self.radChoose.checkedButton().text()
        subject_val = self.ui.subjectETEXT.text()
        teacher_val = self.ui.teacherETEXT.text()
        room_val = self.ui.roomETEXT.text()
        group_val = self.ui.groupETEXT.text()
        lesson_val = None
        checked_button = self.radLess.checkedButton()
        if checked_button == self.ui.radOther:
            lesson_val = self.ui.typeEdit.text()
        else:
            lesson_val = checked_button.text()

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
        teacher_val = self.ui.teacherETEXT.text()
        room_val = self.ui.roomETEXT.text()
        group_val = self.ui.groupETEXT.text()
        day_val = self.current_day_week
        lesson_val = None
        checked_button = self.radLess.checkedButton()
        if checked_button == self.ui.radOther:
            lesson_val = self.ui.typeEdit.text()
        else:
            lesson_val = checked_button.text()

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

        self.legend_label = QLabel()
        self.legend_label.setText(
            '<b>Цвет недели:</b> '
            '<span style="background-color:#D0E7FF; padding:2px 6px; border-radius:3px;">&nbsp;&nbsp;</span> — нечёт, '
            '<span style="background-color:#E6D0FF; padding:2px 6px; border-radius:3px;">&nbsp;&nbsp;</span> — чёт'
        )
        self.legend_label.setAlignment(Qt.AlignCenter)
        self.legend_label.setStyleSheet("font-size: 14pt; margin: 8px;")

        self.statusBar().addPermanentWidget(self.legend_label)

        self.ui.lineEdit.editingFinished.connect(self.show_fuller)
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

        self.load_for_saved()

    def highlight_html(self, widget, text):
        if not hasattr(widget, 'saved_html'):
            return
        if not text:
            widget.setHtml(widget.saved_html)
            return
        pattern = re.escape(text)
        regex = re.compile(pattern, re.IGNORECASE)
        def repl(m):
            return f'<span style="background-color:#F473B1;">{m.group(0)}</span>'
        highlighted_html = regex.sub(repl, widget.saved_html)
        widget.setHtml(highlighted_html)

    def save_for_load(self, group_number):
        cursor.execute('DELETE FROM saved_g;')
        cursor.execute('INSERT INTO saved_g (group_number) VALUES (?);', (group_number,))
        conn.commit()

    def load_for_saved(self):
        cursor.execute('SELECT group_number FROM saved_g LIMIT 1;')
        row = cursor.fetchone()
        group_number = row[0]
        self.ui.lineEdit.setText(group_number)
        self.show_full()

    def show_fuller(self):
        group_number = self.ui.lineEdit.text()
        self.save_for_load(group_number)
        self.show_full()

    def highlight(self):
        highlightable = self.ui.allEdit.text()
        if not highlightable:
            self.clear_highlight()
            return
        for dayweek, timenwidget in self.daysntimes.items():
            for _, edit_widget in timenwidget:
                self.highlight_html(edit_widget, highlightable)


    def clear_highlight(self):
        for dayweek, timenwidget in self.daysntimes.items():
            for _, edit_widget in timenwidget:
                if hasattr(edit_widget, 'saved_html'):
                    edit_widget.setHtml(edit_widget.saved_html)

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
                edit_widget.mouseDoubleClickEvent = lambda event, slot=time_slot, day=dayweek: self.on_double_click(event, slot, day)

    def on_double_click(self, event, time_slot, day_week):
        password, ok = QInputDialog.getText(self, 'Требуется пароль', 'Введите пароль:', echo=QLineEdit.Password)
        if ok and self.check_password(password):
            group_number = self.ui.lineEdit.text()
            self.edit_window.load_info(time_slot, group_number, day_week)
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
            cursor.execute('''
                SELECT type_week, subject, type_subject, teacher, group_number, room
                FROM schedule_h
                WHERE group_number = ? and tme=? and day_week=?;		
            ''', (search, time_sche, dayweek))

            schedule = cursor.fetchall()
            html_parts = []
            colors_variants = [
                ["#68607A", "#C07AAA", "#8C9092", "#C07AAA"],
                ["#68607A", "#86a6da", "#8C9092", "#86a6da"],
            ]

            for row in schedule:
                type_week, subject, type_subject, teacher, _, room = row

                if type_week == 'нечёт':
                    colors = colors_variants[1]
                    subject_color = colors[1]
                elif type_week == 'чёт':
                    colors = colors_variants[0]
                    subject_color = colors[1]
                else:
                    colors = colors_variants[0]
                    subject_color = colors[0]

                html = f'''
                <div style="border-radius:4px; margin:8px 0; padding:6px 12px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                    <p style="color:{subject_color}; font-size:16pt; font-weight:900; margin:4px 0; padding: 2px 6px; border-radius: 3px;">{subject}</p>
                    <p style="color:{colors[2]}; font-size:13pt; font-weight:700; margin:2px 0;">{type_subject}</p>
                    <p style="color:{colors[0]}; font-size:12pt; font-weight:800; margin:2px 0;">{teacher}</p>
                    <p style="color:{subject_color}; font-size:12pt; font-weight:900; margin:2px 0;">{room}</p>
                </div>
                '''
                html_parts.append(html)

            full_html = f'''
            <!DOCTYPE HTML>
            <html><head><meta charset="utf-8" /></head><body style="margin:0; padding:0;">
            {''.join(html_parts)}
            </body></html>
            '''
            edit_widget.saved_html = full_html
            edit_widget.setHtml(full_html)



    def checkbox_filters(self):
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

                if not rows:
                    edit_widget.clear()
                    continue

                html_rows = []
                for idx, row in enumerate(rows, 1):
                    line_connect = ' ||| '.join(str(item) for item in row if item)
                    color = "#808080" if idx % 2 == 1 else "#a390c2"
                    html_rows.append(f'<p style="margin:0; padding:2px 6px; color:{color}; font-family:Segoe UI, Tahoma, Geneva, Verdana, sans-serif; font-size: 12pt; font-weight: bold;">{idx}) {line_connect}</p>')

                separator = '<hr style="border:none; border-top:1px solid #D0D0D0; margin:4px 0;">'

                html_text = separator.join(html_rows)

                full_html = f'''
                <!DOCTYPE HTML>
                <html>
                <head><meta charset="utf-8" /></head>
                <body style="background: #ffffff; margin:0; padding:4px;">
                {html_text}
                </body>
                </html>
                '''
                edit_widget.saved_html = full_html
                edit_widget.setHtml(full_html)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ScheduleInterface()
    window.show()

    sys.exit(app.exec())
