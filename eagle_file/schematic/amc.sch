EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:MyBeagleBone
LIBS:amc-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "27 apr 2015"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L 74HC595 U?
U 1 1 55672D41
P 3750 5650
F 0 "U?" H 3900 6250 70  0000 C CNN
F 1 "74HC595" H 3750 5050 70  0000 C CNN
F 2 "" H 3750 5650 60  0000 C CNN
F 3 "" H 3750 5650 60  0000 C CNN
	1    3750 5650
	1    0    0    -1  
$EndComp
$Comp
L C C?
U 1 1 55673388
P 1900 4650
F 0 "C?" H 1925 4750 50  0000 L CNN
F 1 "1uF" H 1925 4550 50  0000 L CNN
F 2 "" H 1938 4500 30  0000 C CNN
F 3 "" H 1900 4650 60  0000 C CNN
	1    1900 4650
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 556734BF
P 1900 5050
F 0 "#PWR?" H 1900 4800 50  0001 C CNN
F 1 "GND" H 1900 4900 50  0000 C CNN
F 2 "" H 1900 5050 60  0000 C CNN
F 3 "" H 1900 5050 60  0000 C CNN
	1    1900 5050
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 5567355B
P 2650 3950
F 0 "#PWR?" H 2650 3800 50  0001 C CNN
F 1 "+5V" H 2650 4090 50  0000 C CNN
F 2 "" H 2650 3950 60  0000 C CNN
F 3 "" H 2650 3950 60  0000 C CNN
	1    2650 3950
	1    0    0    -1  
$EndComp
$Comp
L 74HC595 U?
U 1 1 55670C75
P 3750 4150
F 0 "U?" H 3900 4750 70  0000 C CNN
F 1 "74HC595" H 3750 3550 70  0000 C CNN
F 2 "" H 3750 4150 60  0000 C CNN
F 3 "" H 3750 4150 60  0000 C CNN
	1    3750 4150
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR?
U 1 1 55673617
P 2750 5450
F 0 "#PWR?" H 2750 5300 50  0001 C CNN
F 1 "+5V" H 2750 5590 50  0000 C CNN
F 2 "" H 2750 5450 60  0000 C CNN
F 3 "" H 2750 5450 60  0000 C CNN
	1    2750 5450
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 55673659
P 3050 4450
F 0 "#PWR?" H 3050 4200 50  0001 C CNN
F 1 "GND" H 3050 4300 50  0000 C CNN
F 2 "" H 3050 4450 60  0000 C CNN
F 3 "" H 3050 4450 60  0000 C CNN
	1    3050 4450
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 55673673
P 3050 6000
F 0 "#PWR?" H 3050 5750 50  0001 C CNN
F 1 "GND" H 3050 5850 50  0000 C CNN
F 2 "" H 3050 6000 60  0000 C CNN
F 3 "" H 3050 6000 60  0000 C CNN
	1    3050 6000
	1    0    0    -1  
$EndComp
$Comp
L P9_I2C_SPI U?
U 1 1 55673A38
P 1400 2900
F 0 "U?" H 1400 3450 60  0000 C CNN
F 1 "P9_I2C_SPI" H 1550 2350 60  0000 C CNN
F 2 "" H 1400 2900 60  0000 C CNN
F 3 "" H 1400 2900 60  0000 C CNN
	1    1400 2900
	1    0    0    -1  
$EndComp
$Comp
L MCP23017_LOGIC J?
U 1 1 55674188
P 3700 2400
F 0 "J?" H 4000 3300 50  0000 C CNN
F 1 "MCP23017_LOGIC" H 3800 1450 50  0000 C CNN
F 2 "MODULE" H 3600 2400 50  0001 C CNN
F 3 "DOCUMENTATION" H 3600 2400 50  0001 C CNN
	1    3700 2400
	1    0    0    -1  
$EndComp
$Comp
L RG16080B-BIY-V_LOGIC D?
U 1 1 556751A2
P 7250 2500
F 0 "D?" H 7300 3500 50  0000 C CNN
F 1 "RG16080B-BIY-V_LOGIC" H 7400 3300 50  0000 C CNN
F 2 "MODULE" H 7400 2750 50  0001 C CNN
F 3 "DOCUMENTATION" H 7350 2750 50  0001 C CNN
	1    7250 2500
	1    0    0    -1  
$EndComp
$Comp
L POT RV?
U 1 1 55675676
P 7250 4000
F 0 "RV?" H 7250 3900 50  0000 C CNN
F 1 "20K" H 7250 4000 50  0000 C CNN
F 2 "" H 7250 4000 60  0000 C CNN
F 3 "" H 7250 4000 60  0000 C CNN
	1    7250 4000
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR?
U 1 1 556758E7
P 6600 4000
F 0 "#PWR?" H 6600 3850 50  0001 C CNN
F 1 "VCC" H 6600 4150 50  0000 C CNN
F 2 "" H 6600 4000 60  0000 C CNN
F 3 "" H 6600 4000 60  0000 C CNN
	1    6600 4000
	0    -1   1    0   
$EndComp
$Comp
L GND #PWR?
U 1 1 55675A25
P 7400 3650
F 0 "#PWR?" H 7400 3400 50  0001 C CNN
F 1 "GND" H 7400 3500 50  0000 C CNN
F 2 "" H 7400 3650 60  0000 C CNN
F 3 "" H 7400 3650 60  0000 C CNN
	1    7400 3650
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 55676322
P 4800 5200
F 0 "R?" V 4880 5200 50  0000 C CNN
F 1 "220" V 4800 5200 50  0000 C CNN
F 2 "" V 4730 5200 30  0000 C CNN
F 3 "" H 4800 5200 30  0000 C CNN
	1    4800 5200
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 556763F3
P 5450 5200
F 0 "D?" H 5450 5300 50  0000 C CNN
F 1 "LED" H 5450 5100 50  0000 C CNN
F 2 "" H 5450 5200 60  0000 C CNN
F 3 "" H 5450 5200 60  0000 C CNN
	1    5450 5200
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 55678F3C
P 5100 5300
F 0 "R?" V 5180 5300 50  0000 C CNN
F 1 "220" V 5100 5300 50  0000 C CNN
F 2 "" V 5030 5300 30  0000 C CNN
F 3 "" H 5100 5300 30  0000 C CNN
	1    5100 5300
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 55678F42
P 5750 5300
F 0 "D?" H 5750 5400 50  0000 C CNN
F 1 "LED" H 5750 5200 50  0000 C CNN
F 2 "" H 5750 5300 60  0000 C CNN
F 3 "" H 5750 5300 60  0000 C CNN
	1    5750 5300
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 556790E2
P 4800 5400
F 0 "R?" V 4880 5400 50  0000 C CNN
F 1 "220" V 4800 5400 50  0000 C CNN
F 2 "" V 4730 5400 30  0000 C CNN
F 3 "" H 4800 5400 30  0000 C CNN
	1    4800 5400
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 556790E8
P 5450 5400
F 0 "D?" H 5450 5500 50  0000 C CNN
F 1 "LED" H 5450 5300 50  0000 C CNN
F 2 "" H 5450 5400 60  0000 C CNN
F 3 "" H 5450 5400 60  0000 C CNN
	1    5450 5400
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 556790EF
P 5100 5500
F 0 "R?" V 5180 5500 50  0000 C CNN
F 1 "220" V 5100 5500 50  0000 C CNN
F 2 "" V 5030 5500 30  0000 C CNN
F 3 "" H 5100 5500 30  0000 C CNN
	1    5100 5500
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 556790F5
P 5750 5500
F 0 "D?" H 5750 5600 50  0000 C CNN
F 1 "LED" H 5750 5400 50  0000 C CNN
F 2 "" H 5750 5500 60  0000 C CNN
F 3 "" H 5750 5500 60  0000 C CNN
	1    5750 5500
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 55679ACD
P 4800 5600
F 0 "R?" V 4880 5600 50  0000 C CNN
F 1 "220" V 4800 5600 50  0000 C CNN
F 2 "" V 4730 5600 30  0000 C CNN
F 3 "" H 4800 5600 30  0000 C CNN
	1    4800 5600
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 55679AD3
P 5450 5600
F 0 "D?" H 5450 5700 50  0000 C CNN
F 1 "LED" H 5450 5500 50  0000 C CNN
F 2 "" H 5450 5600 60  0000 C CNN
F 3 "" H 5450 5600 60  0000 C CNN
	1    5450 5600
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 55679ADA
P 5100 5700
F 0 "R?" V 5180 5700 50  0000 C CNN
F 1 "220" V 5100 5700 50  0000 C CNN
F 2 "" V 5030 5700 30  0000 C CNN
F 3 "" H 5100 5700 30  0000 C CNN
	1    5100 5700
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 55679AE0
P 5750 5700
F 0 "D?" H 5750 5800 50  0000 C CNN
F 1 "LED" H 5750 5600 50  0000 C CNN
F 2 "" H 5750 5700 60  0000 C CNN
F 3 "" H 5750 5700 60  0000 C CNN
	1    5750 5700
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 55679AE7
P 4800 5800
F 0 "R?" V 4880 5800 50  0000 C CNN
F 1 "220" V 4800 5800 50  0000 C CNN
F 2 "" V 4730 5800 30  0000 C CNN
F 3 "" H 4800 5800 30  0000 C CNN
	1    4800 5800
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 55679AED
P 5450 5800
F 0 "D?" H 5450 5900 50  0000 C CNN
F 1 "LED" H 5450 5700 50  0000 C CNN
F 2 "" H 5450 5800 60  0000 C CNN
F 3 "" H 5450 5800 60  0000 C CNN
	1    5450 5800
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 55679AF4
P 5100 5900
F 0 "R?" V 5180 5900 50  0000 C CNN
F 1 "220" V 5100 5900 50  0000 C CNN
F 2 "" V 5030 5900 30  0000 C CNN
F 3 "" H 5100 5900 30  0000 C CNN
	1    5100 5900
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 55679AFA
P 5750 5900
F 0 "D?" H 5750 6000 50  0000 C CNN
F 1 "LED" H 5750 5800 50  0000 C CNN
F 2 "" H 5750 5900 60  0000 C CNN
F 3 "" H 5750 5900 60  0000 C CNN
	1    5750 5900
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5567A6C0
P 4750 3700
F 0 "R?" V 4830 3700 50  0000 C CNN
F 1 "220" V 4750 3700 50  0000 C CNN
F 2 "" V 4680 3700 30  0000 C CNN
F 3 "" H 4750 3700 30  0000 C CNN
	1    4750 3700
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 5567A6C6
P 5400 3700
F 0 "D?" H 5400 3800 50  0000 C CNN
F 1 "LED" H 5400 3600 50  0000 C CNN
F 2 "" H 5400 3700 60  0000 C CNN
F 3 "" H 5400 3700 60  0000 C CNN
	1    5400 3700
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5567A6CD
P 5050 3800
F 0 "R?" V 5130 3800 50  0000 C CNN
F 1 "220" V 5050 3800 50  0000 C CNN
F 2 "" V 4980 3800 30  0000 C CNN
F 3 "" H 5050 3800 30  0000 C CNN
	1    5050 3800
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 5567A6D3
P 5700 3800
F 0 "D?" H 5700 3900 50  0000 C CNN
F 1 "LED" H 5700 3700 50  0000 C CNN
F 2 "" H 5700 3800 60  0000 C CNN
F 3 "" H 5700 3800 60  0000 C CNN
	1    5700 3800
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5567A6DA
P 4750 3900
F 0 "R?" V 4830 3900 50  0000 C CNN
F 1 "220" V 4750 3900 50  0000 C CNN
F 2 "" V 4680 3900 30  0000 C CNN
F 3 "" H 4750 3900 30  0000 C CNN
	1    4750 3900
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 5567A6E0
P 5400 3900
F 0 "D?" H 5400 4000 50  0000 C CNN
F 1 "LED" H 5400 3800 50  0000 C CNN
F 2 "" H 5400 3900 60  0000 C CNN
F 3 "" H 5400 3900 60  0000 C CNN
	1    5400 3900
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5567A6E7
P 5050 4000
F 0 "R?" V 5130 4000 50  0000 C CNN
F 1 "220" V 5050 4000 50  0000 C CNN
F 2 "" V 4980 4000 30  0000 C CNN
F 3 "" H 5050 4000 30  0000 C CNN
	1    5050 4000
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 5567A6ED
P 5700 4000
F 0 "D?" H 5700 4100 50  0000 C CNN
F 1 "LED" H 5700 3900 50  0000 C CNN
F 2 "" H 5700 4000 60  0000 C CNN
F 3 "" H 5700 4000 60  0000 C CNN
	1    5700 4000
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5567A6F4
P 4750 4100
F 0 "R?" V 4830 4100 50  0000 C CNN
F 1 "220" V 4750 4100 50  0000 C CNN
F 2 "" V 4680 4100 30  0000 C CNN
F 3 "" H 4750 4100 30  0000 C CNN
	1    4750 4100
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 5567A6FA
P 5400 4100
F 0 "D?" H 5400 4200 50  0000 C CNN
F 1 "LED" H 5400 4000 50  0000 C CNN
F 2 "" H 5400 4100 60  0000 C CNN
F 3 "" H 5400 4100 60  0000 C CNN
	1    5400 4100
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5567A701
P 5050 4200
F 0 "R?" V 5130 4200 50  0000 C CNN
F 1 "220" V 5050 4200 50  0000 C CNN
F 2 "" V 4980 4200 30  0000 C CNN
F 3 "" H 5050 4200 30  0000 C CNN
	1    5050 4200
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 5567A707
P 5700 4200
F 0 "D?" H 5700 4300 50  0000 C CNN
F 1 "LED" H 5700 4100 50  0000 C CNN
F 2 "" H 5700 4200 60  0000 C CNN
F 3 "" H 5700 4200 60  0000 C CNN
	1    5700 4200
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5567A70E
P 4750 4300
F 0 "R?" V 4830 4300 50  0000 C CNN
F 1 "220" V 4750 4300 50  0000 C CNN
F 2 "" V 4680 4300 30  0000 C CNN
F 3 "" H 4750 4300 30  0000 C CNN
	1    4750 4300
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 5567A714
P 5400 4300
F 0 "D?" H 5400 4400 50  0000 C CNN
F 1 "LED" H 5400 4200 50  0000 C CNN
F 2 "" H 5400 4300 60  0000 C CNN
F 3 "" H 5400 4300 60  0000 C CNN
	1    5400 4300
	-1   0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 5567A71B
P 5050 4400
F 0 "R?" V 5130 4400 50  0000 C CNN
F 1 "220" V 5050 4400 50  0000 C CNN
F 2 "" V 4980 4400 30  0000 C CNN
F 3 "" H 5050 4400 30  0000 C CNN
	1    5050 4400
	0    1    1    0   
$EndComp
$Comp
L LED D?
U 1 1 5567A721
P 5700 4400
F 0 "D?" H 5700 4500 50  0000 C CNN
F 1 "LED" H 5700 4300 50  0000 C CNN
F 2 "" H 5700 4400 60  0000 C CNN
F 3 "" H 5700 4400 60  0000 C CNN
	1    5700 4400
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 5567BA7A
P 6050 6350
F 0 "#PWR?" H 6050 6100 50  0001 C CNN
F 1 "GND" H 6050 6200 50  0000 C CNN
F 2 "" H 6050 6350 60  0000 C CNN
F 3 "" H 6050 6350 60  0000 C CNN
	1    6050 6350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2900 3900 3050 3900
Wire Wire Line
	4450 6100 4600 6100
Wire Wire Line
	4600 6100 4600 6450
Wire Wire Line
	4600 6450 2300 6450
Wire Wire Line
	2300 6450 2300 3900
Wire Wire Line
	2100 5700 3050 5700
Wire Wire Line
	2100 4200 3050 4200
Connection ~ 2100 4200
Wire Wire Line
	4450 4600 4450 4900
Wire Wire Line
	4450 4900 3050 4900
Wire Wire Line
	3050 4900 3050 5200
Wire Wire Line
	2900 5400 3050 5400
Wire Wire Line
	2900 3500 2900 5400
Connection ~ 2900 3900
Wire Wire Line
	1900 4800 1900 5050
Wire Wire Line
	2100 4500 1900 4500
Connection ~ 2100 4500
Wire Wire Line
	3050 4000 2650 4000
Wire Wire Line
	2650 4000 2650 3950
Wire Wire Line
	2750 5450 2750 5500
Wire Wire Line
	2750 5500 3050 5500
Wire Wire Line
	3050 4300 3050 4450
Wire Wire Line
	3050 5800 3050 6000
Wire Wire Line
	4450 1650 6350 1650
Wire Wire Line
	6350 1750 4450 1750
Wire Wire Line
	6350 1850 4450 1850
Wire Wire Line
	4450 1950 6350 1950
Wire Wire Line
	6350 2050 4450 2050
Wire Wire Line
	4450 2250 6350 2250
Wire Wire Line
	6350 2350 4450 2350
Wire Wire Line
	6350 2150 4450 2150
Wire Wire Line
	4450 2500 6350 2500
Wire Wire Line
	6350 2600 4450 2600
Wire Wire Line
	4450 2700 6350 2700
Wire Wire Line
	6350 2800 4450 2800
Wire Wire Line
	4450 2900 6350 2900
Wire Wire Line
	6600 4000 7000 4000
Wire Wire Line
	6950 3500 6950 4000
Connection ~ 6950 4000
Wire Wire Line
	7250 3850 7750 3850
Wire Wire Line
	7750 3850 7750 3500
Wire Wire Line
	7250 3500 7250 3850
Wire Wire Line
	7400 3500 7400 3650
Wire Wire Line
	2100 2150 2100 1700
Wire Wire Line
	2100 1700 2950 1700
Wire Wire Line
	2950 1800 2250 1800
Wire Wire Line
	2250 1800 2250 2350
Wire Wire Line
	2250 2350 2100 2350
Wire Wire Line
	2900 3500 2100 3500
Wire Wire Line
	3050 3700 2100 3700
Wire Wire Line
	2300 3900 2100 3900
Wire Wire Line
	2100 4100 2100 5700
Wire Wire Line
	4950 5200 5250 5200
Wire Wire Line
	5250 5300 5550 5300
Wire Wire Line
	4950 5400 5250 5400
Wire Wire Line
	5250 5500 5550 5500
Wire Wire Line
	4950 5600 5250 5600
Wire Wire Line
	5250 5700 5550 5700
Wire Wire Line
	4950 5800 5250 5800
Wire Wire Line
	5250 5900 5550 5900
Wire Wire Line
	4900 3700 5200 3700
Wire Wire Line
	5200 3800 5500 3800
Wire Wire Line
	4900 3900 5200 3900
Wire Wire Line
	5200 4000 5500 4000
Wire Wire Line
	4900 4100 5200 4100
Wire Wire Line
	5200 4200 5500 4200
Wire Wire Line
	4900 4300 5200 4300
Wire Wire Line
	5200 4400 5500 4400
Wire Wire Line
	4450 3700 4600 3700
Wire Wire Line
	4450 3800 4900 3800
Wire Wire Line
	4450 3900 4600 3900
Wire Wire Line
	4450 4000 4900 4000
Wire Wire Line
	4450 4100 4600 4100
Wire Wire Line
	4450 4200 4900 4200
Wire Wire Line
	4450 4300 4600 4300
Wire Wire Line
	4450 4400 4900 4400
Wire Wire Line
	4450 5200 4650 5200
Wire Wire Line
	4450 5300 4950 5300
Wire Wire Line
	4450 5400 4650 5400
Wire Wire Line
	4450 5500 4950 5500
Wire Wire Line
	4450 5600 4650 5600
Wire Wire Line
	4450 5700 4950 5700
Wire Wire Line
	4450 5800 4650 5800
Wire Wire Line
	4500 5900 4950 5900
Wire Wire Line
	5600 3700 6050 3700
Wire Wire Line
	5900 3800 6050 3800
Connection ~ 6050 3800
Wire Wire Line
	5600 3900 6050 3900
Connection ~ 6050 3900
Wire Wire Line
	5900 4000 6050 4000
Connection ~ 6050 4000
Wire Wire Line
	5900 4200 6050 4200
Connection ~ 6050 4200
Wire Wire Line
	5900 4400 6050 4400
Connection ~ 6050 4400
Wire Wire Line
	5650 5200 6050 5200
Connection ~ 6050 5200
Wire Wire Line
	5950 5300 6050 5300
Connection ~ 6050 5300
Wire Wire Line
	5950 5500 6050 5500
Connection ~ 6050 5500
Wire Wire Line
	5700 5400 6050 5400
Connection ~ 6050 5400
Wire Wire Line
	5600 4100 6050 4100
Connection ~ 6050 4100
Wire Wire Line
	5600 4300 6050 4300
Connection ~ 6050 4300
Wire Wire Line
	5650 5600 6050 5600
Connection ~ 6050 5600
Wire Wire Line
	5950 5700 6050 5700
Connection ~ 6050 5700
Wire Wire Line
	5650 5800 6050 5800
Connection ~ 6050 5800
Wire Wire Line
	5950 5900 6050 5900
Connection ~ 6050 5900
Wire Wire Line
	6050 3700 6050 6350
$EndSCHEMATC