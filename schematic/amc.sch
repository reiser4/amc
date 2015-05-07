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
L P9 U?
U 1 1 553E7EFA
P 2950 5600
F 0 "U?" H 2950 5500 50  0000 C CNN
F 1 "P9" H 2950 5700 50  0000 C CNN
F 2 "MODULE" H 2950 5600 50  0001 C CNN
F 3 "DOCUMENTATION" H 2950 5600 50  0001 C CNN
	1    2950 5600
	1    0    0    -1  
$EndComp
$Comp
L MCP23017 J?
U 1 1 5549E7C6
P 5000 5150
F 0 "J?" H 5000 5050 50  0000 C CNN
F 1 "MCP23017" H 5000 5250 50  0000 C CNN
F 2 "MODULE" H 5000 5150 50  0001 C CNN
F 3 "DOCUMENTATION" H 5000 5150 50  0001 C CNN
	1    5000 5150
	1    0    0    -1  
$EndComp
$Comp
L RG16080B-BIY-V D?
U 1 1 554B4170
P 7150 3250
F 0 "D?" H 7150 3400 50  0000 C CNN
F 1 "RG16080B-BIY-V" H 7150 3500 50  0000 C CNN
F 2 "MODULE" H 7150 3250 50  0001 C CNN
F 3 "DOCUMENTATION" H 7150 3250 50  0001 C CNN
	1    7150 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 5700 3700 5700
Wire Wire Line
	3700 5600 4250 5600
Wire Wire Line
	4250 5400 4100 5400
Wire Wire Line
	4100 5400 4100 4500
Wire Wire Line
	4100 4500 3700 4500
Wire Wire Line
	5750 4500 7500 4500
Wire Wire Line
	7500 4500 7500 3700
Wire Wire Line
	7400 3700 7400 4600
Wire Wire Line
	7400 4600 5750 4600
Wire Wire Line
	5750 4700 7300 4700
Wire Wire Line
	7300 4700 7300 3700
Wire Wire Line
	5750 4800 7200 4800
Wire Wire Line
	7200 4800 7200 3700
Wire Wire Line
	5750 4900 7100 4900
Wire Wire Line
	7100 4900 7100 3700
Wire Wire Line
	7000 3700 7000 5000
Wire Wire Line
	7000 5000 5750 5000
Wire Wire Line
	6900 3700 6900 5100
Wire Wire Line
	6900 5100 5750 5100
Wire Wire Line
	5750 5200 6800 5200
Wire Wire Line
	6800 5200 6800 3700
Wire Wire Line
	6200 3700 3700 3700
Wire Wire Line
	3700 3700 3700 4500
Wire Wire Line
	3700 4800 3950 4800
Wire Wire Line
	3950 4800 3950 5300
Wire Wire Line
	3950 5300 4250 5300
Wire Wire Line
	6300 3700 6300 3900
Wire Wire Line
	6300 3900 3800 3900
Wire Wire Line
	3800 3900 3800 4800
Connection ~ 3800 4800
$EndSCHEMATC
