from PyQt5.QtCore import QDate , QTime , QDateTime , Qt 
now = QDate.currentDate()

print(now.toString(Qt.ISODate))
time =QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))