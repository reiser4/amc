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
LIBS:special
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
LIBS:MODULO2-cache
EELAYER 27 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Modulo 2"
Date "22 jul 2015"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L 74HC595 U1
U 1 1 55B023EB
P 3750 3500
F 0 "U1" H 3900 4100 70  0000 C CNN
F 1 "74HC595" H 3750 2900 70  0000 C CNN
F 2 "~" H 3750 3500 60  0000 C CNN
F 3 "~" H 3750 3500 60  0000 C CNN
	1    3750 3500
	1    0    0    -1  
$EndComp
$Comp
L CONN_6 P1
U 1 1 55B025CD
P 1300 3100
F 0 "P1" V 1250 3100 60  0000 C CNN
F 1 "CONN_6" V 1350 3100 60  0000 C CNN
F 2 "" H 1300 3100 60  0000 C CNN
F 3 "" H 1300 3100 60  0000 C CNN
	1    1300 3100
	-1   0    0    -1  
$EndComp
Text Label 1750 2950 0    60   ~ 0
SCLK
$Comp
L VCC #PWR01
U 1 1 55B02677
P 1800 2650
F 0 "#PWR01" H 1800 2750 30  0001 C CNN
F 1 "VCC" H 1800 2750 30  0000 C CNN
F 2 "" H 1800 2650 60  0000 C CNN
F 3 "" H 1800 2650 60  0000 C CNN
	1    1800 2650
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 55B02686
P 1950 3550
F 0 "#PWR02" H 1950 3550 30  0001 C CNN
F 1 "GND" H 1950 3480 30  0001 C CNN
F 2 "" H 1950 3550 60  0000 C CNN
F 3 "" H 1950 3550 60  0000 C CNN
	1    1950 3550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR03
U 1 1 55B02750
P 2900 3800
F 0 "#PWR03" H 2900 3800 30  0001 C CNN
F 1 "GND" H 2900 3730 30  0001 C CNN
F 2 "" H 2900 3800 60  0000 C CNN
F 3 "" H 2900 3800 60  0000 C CNN
	1    2900 3800
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR04
U 1 1 55B0275F
P 2600 3300
F 0 "#PWR04" H 2600 3400 30  0001 C CNN
F 1 "VCC" H 2600 3400 30  0000 C CNN
F 2 "" H 2600 3300 60  0000 C CNN
F 3 "" H 2600 3300 60  0000 C CNN
	1    2600 3300
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 55B0279D
P 5100 3050
F 0 "R1" V 5180 3050 40  0000 C CNN
F 1 "R" V 5107 3051 40  0000 C CNN
F 2 "~" V 5030 3050 30  0000 C CNN
F 3 "~" H 5100 3050 30  0000 C CNN
	1    5100 3050
	0    -1   -1   0   
$EndComp
$Comp
L LED D1
U 1 1 55B027AC
P 6400 3050
F 0 "D1" H 6400 3150 50  0000 C CNN
F 1 "LED" H 6400 2950 50  0000 C CNN
F 2 "~" H 6400 3050 60  0000 C CNN
F 3 "~" H 6400 3050 60  0000 C CNN
	1    6400 3050
	1    0    0    -1  
$EndComp
$Comp
L R R5
U 1 1 55B0281D
P 5700 3150
F 0 "R5" V 5780 3150 40  0000 C CNN
F 1 "R" V 5707 3151 40  0000 C CNN
F 2 "~" V 5630 3150 30  0000 C CNN
F 3 "~" H 5700 3150 30  0000 C CNN
	1    5700 3150
	0    -1   -1   0   
$EndComp
$Comp
L LED D5
U 1 1 55B02823
P 7000 3150
F 0 "D5" H 7000 3250 50  0000 C CNN
F 1 "LED" H 7000 3050 50  0000 C CNN
F 2 "~" H 7000 3150 60  0000 C CNN
F 3 "~" H 7000 3150 60  0000 C CNN
	1    7000 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	1650 2950 2700 2950
Wire Wire Line
	1650 3050 3050 3050
Wire Wire Line
	1650 3150 2450 3150
Wire Wire Line
	1650 3250 2300 3250
Wire Wire Line
	1650 3350 1950 3350
Wire Wire Line
	1950 3350 1950 3550
Wire Wire Line
	1650 2850 1800 2850
Wire Wire Line
	1800 2850 1800 2650
Wire Wire Line
	2700 2950 2700 3250
Wire Wire Line
	2700 3250 3050 3250
Wire Wire Line
	2300 3250 2300 3550
Wire Wire Line
	2300 3550 3050 3550
Wire Wire Line
	2600 3300 2600 3350
Wire Wire Line
	2600 3350 3050 3350
Wire Wire Line
	2900 3800 2900 3650
Wire Wire Line
	2900 3650 3050 3650
Wire Wire Line
	4450 3950 4450 4450
Wire Wire Line
	4450 4450 2450 4450
Wire Wire Line
	2450 4450 2450 3150
Wire Wire Line
	4450 3050 4850 3050
Wire Wire Line
	5350 3050 6200 3050
Wire Wire Line
	6600 3050 7850 3050
Wire Wire Line
	4450 3150 5450 3150
Wire Wire Line
	5950 3150 6800 3150
Wire Wire Line
	7200 3150 7850 3150
$Comp
L R R2
U 1 1 55B02895
P 5100 3250
F 0 "R2" V 5180 3250 40  0000 C CNN
F 1 "R" V 5107 3251 40  0000 C CNN
F 2 "~" V 5030 3250 30  0000 C CNN
F 3 "~" H 5100 3250 30  0000 C CNN
	1    5100 3250
	0    -1   -1   0   
$EndComp
$Comp
L LED D2
U 1 1 55B0289B
P 6400 3250
F 0 "D2" H 6400 3350 50  0000 C CNN
F 1 "LED" H 6400 3150 50  0000 C CNN
F 2 "~" H 6400 3250 60  0000 C CNN
F 3 "~" H 6400 3250 60  0000 C CNN
	1    6400 3250
	1    0    0    -1  
$EndComp
$Comp
L R R6
U 1 1 55B028A1
P 5700 3350
F 0 "R6" V 5780 3350 40  0000 C CNN
F 1 "R" V 5707 3351 40  0000 C CNN
F 2 "~" V 5630 3350 30  0000 C CNN
F 3 "~" H 5700 3350 30  0000 C CNN
	1    5700 3350
	0    -1   -1   0   
$EndComp
$Comp
L LED D6
U 1 1 55B028A7
P 7000 3350
F 0 "D6" H 7000 3450 50  0000 C CNN
F 1 "LED" H 7000 3250 50  0000 C CNN
F 2 "~" H 7000 3350 60  0000 C CNN
F 3 "~" H 7000 3350 60  0000 C CNN
	1    7000 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 3250 4850 3250
Wire Wire Line
	5350 3250 6200 3250
Wire Wire Line
	6600 3250 7850 3250
Wire Wire Line
	4450 3350 5450 3350
Wire Wire Line
	5950 3350 6800 3350
Wire Wire Line
	7200 3350 7850 3350
$Comp
L R R3
U 1 1 55B028E7
P 5100 3450
F 0 "R3" V 5180 3450 40  0000 C CNN
F 1 "R" V 5107 3451 40  0000 C CNN
F 2 "~" V 5030 3450 30  0000 C CNN
F 3 "~" H 5100 3450 30  0000 C CNN
	1    5100 3450
	0    -1   -1   0   
$EndComp
$Comp
L LED D3
U 1 1 55B028ED
P 6400 3450
F 0 "D3" H 6400 3550 50  0000 C CNN
F 1 "LED" H 6400 3350 50  0000 C CNN
F 2 "~" H 6400 3450 60  0000 C CNN
F 3 "~" H 6400 3450 60  0000 C CNN
	1    6400 3450
	1    0    0    -1  
$EndComp
$Comp
L R R7
U 1 1 55B028F3
P 5700 3550
F 0 "R7" V 5780 3550 40  0000 C CNN
F 1 "R" V 5707 3551 40  0000 C CNN
F 2 "~" V 5630 3550 30  0000 C CNN
F 3 "~" H 5700 3550 30  0000 C CNN
	1    5700 3550
	0    -1   -1   0   
$EndComp
$Comp
L LED D7
U 1 1 55B028F9
P 7000 3550
F 0 "D7" H 7000 3650 50  0000 C CNN
F 1 "LED" H 7000 3450 50  0000 C CNN
F 2 "~" H 7000 3550 60  0000 C CNN
F 3 "~" H 7000 3550 60  0000 C CNN
	1    7000 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 3450 4850 3450
Wire Wire Line
	5350 3450 6200 3450
Wire Wire Line
	6600 3450 7850 3450
Wire Wire Line
	4450 3550 5450 3550
Wire Wire Line
	5950 3550 6800 3550
Wire Wire Line
	7200 3550 7850 3550
$Comp
L R R4
U 1 1 55B02905
P 5100 3650
F 0 "R4" V 5180 3650 40  0000 C CNN
F 1 "R" V 5107 3651 40  0000 C CNN
F 2 "~" V 5030 3650 30  0000 C CNN
F 3 "~" H 5100 3650 30  0000 C CNN
	1    5100 3650
	0    -1   -1   0   
$EndComp
$Comp
L LED D4
U 1 1 55B0290B
P 6400 3650
F 0 "D4" H 6400 3750 50  0000 C CNN
F 1 "LED" H 6400 3550 50  0000 C CNN
F 2 "~" H 6400 3650 60  0000 C CNN
F 3 "~" H 6400 3650 60  0000 C CNN
	1    6400 3650
	1    0    0    -1  
$EndComp
$Comp
L R R8
U 1 1 55B02911
P 5700 3750
F 0 "R8" V 5780 3750 40  0000 C CNN
F 1 "R" V 5707 3751 40  0000 C CNN
F 2 "~" V 5630 3750 30  0000 C CNN
F 3 "~" H 5700 3750 30  0000 C CNN
	1    5700 3750
	0    -1   -1   0   
$EndComp
$Comp
L LED D8
U 1 1 55B02917
P 7000 3750
F 0 "D8" H 7000 3850 50  0000 C CNN
F 1 "LED" H 7000 3650 50  0000 C CNN
F 2 "~" H 7000 3750 60  0000 C CNN
F 3 "~" H 7000 3750 60  0000 C CNN
	1    7000 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 3650 4850 3650
Wire Wire Line
	5350 3650 6200 3650
Wire Wire Line
	6600 3650 7850 3650
Wire Wire Line
	4450 3750 5450 3750
Wire Wire Line
	5950 3750 6800 3750
Wire Wire Line
	7200 3750 7850 3750
$Comp
L GND #PWR05
U 1 1 55B02925
P 7850 4000
F 0 "#PWR05" H 7850 4000 30  0001 C CNN
F 1 "GND" H 7850 3930 30  0001 C CNN
F 2 "" H 7850 4000 60  0000 C CNN
F 3 "" H 7850 4000 60  0000 C CNN
	1    7850 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	7850 3050 7850 4000
Connection ~ 7850 3150
Connection ~ 7850 3250
Connection ~ 7850 3350
Connection ~ 7850 3450
Connection ~ 7850 3550
Connection ~ 7850 3650
Connection ~ 7850 3750
$Comp
L PWR_FLAG #FLG06
U 1 1 55B02960
P 2700 1300
F 0 "#FLG06" H 2700 1395 30  0001 C CNN
F 1 "PWR_FLAG" H 2700 1480 30  0000 C CNN
F 2 "" H 2700 1300 60  0000 C CNN
F 3 "" H 2700 1300 60  0000 C CNN
	1    2700 1300
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG07
U 1 1 55B0296F
P 2950 1300
F 0 "#FLG07" H 2950 1395 30  0001 C CNN
F 1 "PWR_FLAG" H 2950 1480 30  0000 C CNN
F 2 "" H 2950 1300 60  0000 C CNN
F 3 "" H 2950 1300 60  0000 C CNN
	1    2950 1300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR08
U 1 1 55B0297E
P 2700 1450
F 0 "#PWR08" H 2700 1450 30  0001 C CNN
F 1 "GND" H 2700 1380 30  0001 C CNN
F 2 "" H 2700 1450 60  0000 C CNN
F 3 "" H 2700 1450 60  0000 C CNN
	1    2700 1450
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR09
U 1 1 55B0298D
P 2950 1450
F 0 "#PWR09" H 2950 1550 30  0001 C CNN
F 1 "VCC" H 2950 1550 30  0000 C CNN
F 2 "" H 2950 1450 60  0000 C CNN
F 3 "" H 2950 1450 60  0000 C CNN
	1    2950 1450
	-1   0    0    1   
$EndComp
Wire Wire Line
	2700 1300 2700 1450
Wire Wire Line
	2950 1300 2950 1450
$EndSCHEMATC
