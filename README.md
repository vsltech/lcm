# Lungs Compliance Meter

Lungs Compliance Meter: A simple automated device to demonstrate the measure of volume/pressure change in lungs using compliance curve.


It is working model for teaching Dynamic Airway Compression. The concept of lung compliance is generally considered to be difficult by students and therefore, over the years, medical educators have attempted to explain it in novel ways. However, all the methods published till now pertain to “static lung compliance”. We have constructed a simple device for demonstrating “dynamic lung compliance” and generating the flow-volume loop on any screen. The device comprises a 1500 mL plastic bottle filled with water and fitted with a balloon with a long neck, an ultrasonic sensor, and a syringe for sucking water, so that it can create negative pressure inside and air through tube inflates the balloon. Ultrasonic Sensor fitted in the cap of bottle measures the water level, further volume & pressure is calculated to plot the graph. Digitized data from the pressure and volume gauges are fed to the screen, enabling students to observe and record how dynamic compliance varies with the rate of increase in pressure inside the bottle. The recorded data enabled students in understanding the mechanism and significance of dynamic airway compression that occurs in chronic obstructive pulmonary diseases.

INDEX

Content	Page
1. Raspberry Pi Setup	3
   1.1 Noobs Installation	3
   1.2 Raspberry Pi Configuration	3
   1.3 Dependencies Installation	3
   1.4 Network Configuration	3
   1.5 Remote Desktop Installation	3
2. Lungs Compliance Meter Software	3
   2.1 Starting Software	4
   2.2 Directory Information	5
   2.3 Starting & Stopping Sensor	5
   2.4 Checking Plots	5
   2.5 Graph GUI Options	5
   2.6 Exporting Points	5
3. Lungs Compliance Meter Calculations	6
   3.1 Logic of Sensor	6
   3.2 Measurements	6
   3.3 Volume Calculation	6
   3.4 Pressure Calculation	6
   3.5 Height Approximation for Static & Dynamic Compliances	6
4. Summary	7
   4.1 Hyperlinks	7
   4.2 Project Links	7





1. Raspberry Pi Setup

●	Download & Boot latest Noobs in SD Card.
●	Connect HDMI Display, USB Keyboard & Mouse.
●	Power Raspberry Pi: 5V, 700mA - 2.5A.
●	Install Raspbian from the list.

1. 1 Raspberry Pi Configuration
●	Plug Ethernet cable for network connection or check section-1.3 for Wi-Fi.
●	Update & Upgrade System: sudo apt-get update && upgrade

1.2 Dependencies Installation
●	Install GPIO libraries: sudo apt-get install python-dev python-rpi.gpio
●	Install PyQt4 package: sudo apt-get install python-qt4
●	Install PyQt4 dev-tools: sudo apt-get install pyqt4-dev-tools

1.3 Network Configuration(Optional)
●	Install wpa_gui for easy configuration of network: sudo apt-get install wpagui
●	Add your network and check your eth0 ip address to access pi using Laptop/PC
●	Make eth0 ip static, so it doesn’t change if connected to dhcp.

1.4 Remote Desktop Installation
●	Install XRDP module to access using Remote Desktop Connection:
            sudo apt-get install xrdp
●	Linux users can directly ssh using terminal.
●	More ssh clients: putty, vnc.




2. Lungs Compliance Meter Software

A simple GUI software to automate the process of inspiration/expiration of volume & pressure graph that can be plotted in real-time to study various compliances during the simulation.







2.1 Starting Software

●	Double click from desktop or click from LXDE menu of raspbian.
 


●	GUI interface with terminal opens. Terminal prints some helpful information’s if any error occurs.
 



2.2 Directory Information
●	Software directory: /home/pi/lungscompliancemeter/lcmnewPyWindow.py
●	lcmnewPyWindow.py: contains calculations, sensor & functions for menus, buttons, checkboxes codes.
●	lcmnewUI.py: contains GUI codes.

2.3 Starting & Stopping Sensor
●	Click start button to on sensor & start inspiration.
●	Focus on terminal & Press “Ctrl+C” to stop sensor.

2.4 Checking Plots
●	Maximize the GUI for smooth plot view.
●	Check plot from right side.
●	Use mouse wheel to zoom to points.

2.5 Graph GUI Options: Right click on graph to check

  


2.6 Exporting Points: Right click on graph & click Export option to generate file like csv.



3. Lungs Compliance Meter Calculations

All calculations are done simultaneously for each reading based on formulas application for Lungs Compliance.

3.1 Logic of Sensor
●	Ultrasonic Sensor to calculate water level each time, level changes up to 0.3cm
●	Sense distance of H2O level from sensor.
●	Calculate current H20 level H = Total distance from sensor to bottom - Current Distance.

3.2 Measurements
●	Total distance from sensor to bottom of bottle = 15.5cm
●	Radius of bottle = 5.5cm
●	Initial Volume of water = 1500mL
●	Surface Tension acting on balloon for normal fluid = 50dynes/cm2

3.3 Volume Calculation
●	Calculate height up to water level = 15.5cm - current distance from sensor
●	Calculate current water volume = πR2H
●	Calculate volume of balloon V = (1500mL) initial V - final V

3.4 Pressure Calculation
●	Calculate current radius of balloon r = cube root ((3/4). (1/π))
●	Calculate pressure using Laplace law = (2 x ST) / r

3.5 Height Approximation for Static & Dynamic Compliances
●	For a valid point user must inspire approx. 0.30cm change of water level in bottle.
●	Now, store up to maximum height for static compliance.
●	Store all heights for dynamic compliance.


4. Summary

Lungs Compliance Meter can be further automated completely for ease of students to learn dynamic air compression. Lungs Compliance is the change in lung volume for each unit change in trans pulmonary pressure. Compliance is seen at low volumes (because of difficulty with initial lung inflation) and at high volumes (because of the limit of chest wall expansion). The total work of breathing of the cycle is the area contained in the loop.


4.1 Hyperlinks

➢	RaspberryPi: https://www.raspberrypi.org/
➢	Python: https://www.python.org/
➢	Mymodpi: https://www.modmypi.com/


4.2 Project Links

➢	Lungs Compliance Meter: http://www.vslcreations.in/lcm/
➢	IIT Jodhpur: http://www.iitj.ac.in/
➢	AIIMS Jodhpur: http://www.aiimsjodhpur.edu.in/

