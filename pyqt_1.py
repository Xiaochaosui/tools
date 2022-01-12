import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from plot_box import plot_one_img
from pathlib import Path
from tools import mkdir

class picture(QWidget):

    def __init__(self):
        super(picture, self).__init__()
        self.setWindowTitle('Image with mouse control')
        self.setGeometry(100, 50, 1200, 800)
        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)
        self.setAcceptDrops(True)
        self.label = QLabel(self)
        # self.label.setText("显示图片")
        # self.label.setAlignment(Qt.AlignCenter)
        # self.label.setFixedSize(1600, 929)
        # self.label.move(95, 15)
        #
        # self.label.setStyleSheet(
        #                          "QLabel{color:rgb(300,300,300,120);font-size:30px;font-weight:bold;font-family:宋体;}"
        #                          )

    def get_file(self, es):
        res = []
        for e in es:
            data = e.toString().split("///")[1]
            print("img:", data)
            res.append(data)
        return res

    def dragEnterEvent(self, e):
        self.setWindowTitle("鼠标拖入窗口")
        if e.mimeData().hasUrls():
            # print("aaa")
            # print(e.mimeData().urls()[0])
            e.accept()
        else:
            print("请拖取正确的文件")
            e.ignore()

    def dropEvent(self, e):
        print("dropEvent")
        # print(e.mimeData().urls())
        try:
            self.imgfiles = self.get_file(e.mimeData().urls())
            for imgfile in self.imgfiles:
                self.show_img(imgfile)
            self.setWindowTitle(self.res_file)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("挑选图片文件夹错误 或者 xml没有")

    def show_img(self,imgName):
        w, h = 0, 0
        p = Path(imgName)
        root_path = p.parents[1]
        img = cv2.imread(imgName)  # 原图
        xml_file = imgName.replace("images", "Annotations")[:-4] + ".xml"
        print("xml:",xml_file)
        res_img_path = root_path / "new"
        mkdir(res_img_path)
        res_img_file = imgName.replace("images", "new")
        self.res_file = res_img_file
        print("save plot_img:",res_img_file)
        res_img = plot_one_img(img, xml_file, res_img_file)
        # print("###")
        size_w = img.shape[1]  # 原图的 w
        size_h = img.shape[0]  # 原图的 h
        print("img size:",size_w, size_h)
        # print(imgName)
        # if len(imgName):
        #     w, h = self.m_resize(size_w, size_h)
        # self.label.setScaledContents(True)
        # # print(w, h)
        # jpg = QtGui.QPixmap(res_img_file).scaled(w, h)
        # # jpg = QPixmap(imgName)
        # self.label.setPixmap(jpg)  # show img
        widget = ImageWithMouseControl(self)
        widget.setGeometry(100, 50, 1200, 800)
        widget.show()


    def m_resize(self, w, h):
        # print(self.label.width(), self.label.height())
        f1 = 1.0*1200/w
        f2 = 1.0*800/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return width, height

    def openimage(self):
        try:
            imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
            self.show_img(imgName)

        except Exception as e:
            import traceback
            traceback.print_exc()
            print("重新选择图片")


class ImageWithMouseControl(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
        # print(path)
        # path = r'D:/1Data/person/new/00000000-01-20170213033107740.jpg'
        print("@@@",parent.res_file)
        # print("$",file)
        self.img = QPixmap(parent.res_file)
        self.scaled_img = self.img.scaled(self.size())
        self.point = QPoint(0, 0)
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.parent.res_file)

    def paintEvent(self, e):
        '''
        绘图
        :param e:
        :return:
        '''
        painter = QPainter()
        painter.begin(self)
        self.draw_img(painter)
        painter.end()

    def draw_img(self, painter):
        painter.drawPixmap(self.point, self.scaled_img)

    def mouseMoveEvent(self, e):  # 重写移动事件
        if self.left_click:
            self._endPos = e.pos() - self._startPos
            self.point = self.point + self._endPos
            self._startPos = e.pos()
            self.repaint()
        elif self.right_click:
            self._endPos = e.pos() - self._startPos
            self.point = self.point + self._endPos
            self._startPos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self._startPos = e.pos()
        if e.button() == Qt.RightButton:
            self.left_click = True
            self._startPos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = False
        elif e.button() == Qt.RightButton:
            self.right_click = False
            self.point = QPoint(0, 0)
            self.scaled_img = self.img.scaled(self.size())
            self.repaint()

    def wheelEvent(self, e):
        # print("鼠标滚轮：", e.angleDelta().y())
        # rate = abs(e.angleDelta().y() // 2)
        if e.angleDelta().y() < 0:
            # 放大图片
            self.scaled_img = self.img.scaled(self.scaled_img.width()-60, self.scaled_img.height()-60)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() + 5)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() + 5)
            self.point = QPoint(new_w, new_h)
            self.repaint()
        elif e.angleDelta().y() > 0:
            # 缩小图片
            self.scaled_img = self.img.scaled(self.scaled_img.width()+60, self.scaled_img.height()+60)
            new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() - 5)
            new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() - 5)
            self.point = QPoint(new_w, new_h)
            self.repaint()

    def resizeEvent(self, e):
        if self.parent is not None:
            self.scaled_img = self.img.scaled(self.size())
            self.point = QPoint(0, 0)
            self.update()


if __name__ == "__main__":

    print(QImageReader.supportedImageFormats())
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
