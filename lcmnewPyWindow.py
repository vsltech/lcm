import RPi.GPIO as GPIO
import time
import math
import pyqtgraph as pg
import numpy as np
from PyQt4 import QtCore, QtGui


# import the UI from the generated file
from lcmnewUI import Ui_MainWindow

class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    #running = True
    d = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00])
    xs = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00])
    ys = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00])
    xd = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00])
    yd = np.array([0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00])

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # if you didn't subclass Ui_MainWindow simply do:
        # Ui_MainWindow().setupUi(self)
        my_plot = pg.PlotWidget()
        self.gridLayout.addWidget(my_plot, 2, 6, 1, 1)
        self.setMouseTracking(True)
        my_plot.clear()
        
    def help(self):
        print "HELP"
        self.msg = QtGui.QMessageBox()
        self.msg.setIcon(QtGui.QMessageBox.Information)
        self.msg.setWindowTitle("Help")
        self.msg.setWindowIcon(QtGui.QIcon('AIIMS Logo 32X32.png'))
        self.msg.setText("1.Click Start button to start sensor.\n2.Focus/Click on terminal & press Ctrl+C to stop sensor.\n3.Click checkboxes for desired options.\n4.Stop & Start again if any error occurs.\n5.Check errors in terminal.\n6. Right Click on graph to export x/y values.\n7. Put Bottle above pump while inspiring/expiring.\n8. Check the graph from right side & right click for various options.\n\nTechnical Queries: email@vslcreations.in")
        self.msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        self.msg.exec_() 
    def info(self):
        print "SOFTWARE INFO"
        self.msg = QtGui.QMessageBox()
        self.msg.setIcon(QtGui.QMessageBox.Information)
        self.msg.setWindowTitle("About Software")
        self.msg.setWindowIcon(QtGui.QIcon('AIIMS Logo 32X32.png'))
        self.msg.setText("Lungs Compliance Meter\nA simple automated device to demonstrate\nthe measure of volume-pressure change\nin lungs using compliance curve.")
        self.msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        self.msg.exec_() 
    def devinfo(self):
        print "DEVELOPER INFO"
        self.msg = QtGui.QMessageBox()
        self.msg.setIcon(QtGui.QMessageBox.Information)
        self.msg.setWindowTitle("About Developer")
        self.msg.setWindowIcon(QtGui.QIcon('AIIMS Logo 32X32.png'))
        self.msg.setText("Vishal Aditya\nIITJ-Intern 2016\nwww.vslcreations.com")
        self.msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        self.msg.exec_()

    def setpointsstatic(self,b):
        i = 0
        if b.isChecked() == True:
            i = 0
            while(i<20):
                item = self.listWidget_2.item(i)
                item.setText(str(self.ys[i]))
                item = self.listWidget.item(i)
                item.setText(str(self.xs[i]))
                i = i+1
        else:
            i = 0
            while(i<20):
                item = self.listWidget_2.item(i)
                item.setText(" ")
                item = self.listWidget.item(i)
                item.setText(" ")
                i = i+1

    def setpointsdynamic(self,b):
        i = 0
        if b.isChecked() == True:
            i = 0
            while(i<20):
                item = self.listWidget_2.item(i)
                item.setText(str(self.yd[i]))
                item = self.listWidget.item(i)
                item.setText(str(self.xd[i]))
                i = i+1
        else:
            i = 0
            while(i<20):
                item = self.listWidget_2.item(i)
                item.setText(" ")
                item = self.listWidget.item(i)
                item.setText(" ")
                i = i+1
                
    def staticcompliance(self):
        print "Static Compliance"
        #print self.d
        print self.xs
        print self.ys
        my_plot = pg.PlotWidget()
        self.gridLayout.addWidget(my_plot, 2, 6, 1, 1)
        my_plot.clear()
        my_plot.plot(self.xs, self.ys, pen=(0,0,255), symbolBrush=(255,0,0), symbolPen='w', name="Green")
        
    def dynamiccompliance(self):
        print "Dynamic Compliance"
        print self.xd
        print self.yd
        my_plot = pg.PlotWidget()
        self.gridLayout.addWidget(my_plot, 2, 6, 1, 1)
        my_plot.clear()
        my_plot.plot(self.xd, self.yd, pen=(255,0,0), name="Red")

    def startgraph(self):
        self.sensorstart()
        self.calculations()
        print "START GRAPH"
        self.staticcompliance()
        
    def stopgraph(self):
        self.sensorstop()
        print "STOP GRAPH"
        i = 0
        while(i<20):
            item = self.listWidget_2.item(i)
            item.setText("0")
            item = self.listWidget.item(i)
            item.setText("0")
            i = i+1
        my_plot = pg.PlotWidget()
        self.gridLayout.addWidget(my_plot, 2, 6, 1, 1)
        my_plot.clear()
    def comboboxvalue(self,i):
        if(i == 0):
            self.staticcompliance()
        elif(i == 1):
            self.dynamiccompliance()

    def sensor(self):
        GPIO.setmode(GPIO.BCM)
        TRIG =23
        ECHO= 24
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG,False)
        
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        while GPIO.input(ECHO)==0:
            pulse_start =  time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        return distance

    def sensorstart(self):
        i = 0
        j = 0
        k = 0
        tmp = 0.00
        try:
            while(True):
                distance1 = self.sensor()
                time.sleep(0.1)
                distance2 = self.sensor()
                time.sleep(0.1)
                distance3 = self.sensor()
                time.sleep(0.1)
                distance4 = self.sensor()
                time.sleep(0.1)
                distance5 = self.sensor()
                distance = (distance1 + distance2 + distance3 + distance4 + distance5)
                distance = distance / 5.0
                if(abs(distance - tmp) > 0.30): #check valid change
                    self.d[j]=distance
                    print "Distance:",self.d[j]
                    j = j+1
                tmp = distance
                i = i+1
                k = k+1
                time.sleep(1)            
        except KeyboardInterrupt:
            GPIO.cleanup()

    def sensorstop(self):
        GPIO.cleanup()
        
    def calculations(self):
        i = 0
        maxi = 0

        #calculating max index of distances
        while(self.d[i]!= 0.00):
            if self.d[i] == np.max(self.d):
                maxi = i
            i = i+1

        i = 0
        while(self.d[i]!= 0.00):
            distance = self.d[i]
            print "-----------------------------------"
            print "Distance:",distance,"cm"
            #calculate volume of balloon!
            height = 15.55 - distance #water level = distance from sensor
            v = 94.985 * height #V of cylinder = V of H2O = pi.(R^2).H
            print "Current volume of H2O:",round(v,3),"mL"

            #set max volume of bottle here!
            vol = 1400 - v   #V of balloon = initalV - finalV = 4/3.pi.(R^3)
            volume = round(vol,3) #in mL

            #calculate pressure of balloon
            radius_cube = 0.238 * volume #(R^3) = (3/4).(1/pi).V
            if(radius_cube > 0):
                radius = math.pow(radius_cube,(1/3.0))
            elif(radius_cube < 0):
                radius = -math.pow(abs(radius_cube),(1/3.0))
            print "Radius of balloon:",radius
            press = 100 / radius  #Laplace Law = P = (2*ST)/R
            #converting dynes/cm2 to cmH20!
            press = 0.00101972 * press
            pressure = round(press,3) #in cmH2O
            
            #store static x/y values upto maximum distance
            if(i <= maxi):
                self.xs[i] = pressure
                self.ys[i] = volume

            #store dynamic x/y values for all distances
            self.xd[i] = pressure
            self.yd[i] = volume
            print "V of balloon:",volume,"mL"
            print "P of balloon:",pressure,"cmH2O" 
            i = i+1

            
if __name__ == '__main__':
    app = QtGui.QApplication([])
    win = MyMainWindow()
    win.show()
    app.exec_()
    
GPIO.cleanup()
