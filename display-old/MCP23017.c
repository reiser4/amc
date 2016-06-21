
#include <stdint.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/types.h>
#include <linux/i2c-dev.h>
#include <stdlib.h>
#include <string.h>


#define ADDR 0x20
#define DIRA 0
#define DIRB 1
#define GPIOA 0x012
#define GPIOB 0x013

static const char *dev = "/dev/i2c-1";

static void exit_on_error (const char *s)
{ 	perror(s);
  	abort();
}


const char *byte_to_binary(int x)
{
    static char b[9];
    b[0] = '\0';

    int z;
    for (z = 128; z > 0; z >>= 1)
    {
        strcat(b, ((x & z) == z) ? "1" : "0");
    }

    return b;
}



char PORTA = 0;
char PORTB = 0;
int fd;

///////////// FUNZIONI MCP

int setup() {
        uint8_t buffer[2];

	if ((fd = open(dev, O_RDWR)) < 0) exit_on_error ("Errore bus i2c");
        if (ioctl(fd, I2C_SLAVE,ADDR) < 0) exit_on_error ("Errore slave");

        buffer[0] = DIRA;
        buffer[1] = 0x00;
        if (write(fd,buffer,2) != 2 ) exit_on_error ("Errore setup direzione A");

        buffer[0] = DIRB;
        buffer[1] = 0x00;
        if (write(fd,buffer,2) != 2 ) exit_on_error ("Errore setup direzione B");
}

void writePortA(int data) {
        uint8_t buffer[2];
        buffer[0] = GPIOA;
        buffer[1] = data;
        //printf("Scrivo su porta A: %s\n",byte_to_binary(data));
        if (write(fd,buffer,2) != 2) exit_on_error ("Errore scrittura porta A");
}

void writePortB(int data) {
        uint8_t buffer[2];
        buffer[0] = GPIOB;
        buffer[1] = data;
        //printf("Scrivo su porta B: %s\n",byte_to_binary(data));
        if (write(fd,buffer,2) != 2) exit_on_error ("Errore scrittura porta A");
}



///////////// FUNZIONI DISPLAY


void displayWriteData() {
    writePortA(PORTA);
    writePortB(PORTB);
}


void displaySetRW(char state) {
    if (state == 1) { 
        PORTA |= 1 << 1;
    } else {
        PORTA &= ~(1 << 1);
    }
}

void displaySetRS(char state) {
    if (state == 1) { 
        PORTA |= 1 << 0;
    } else {
        PORTA &= ~(1 << 0);
    }
}

void displaySetE(char state) {
    if (state == 1) { 
        PORTA |= 1 << 2;
    } else {
        PORTA &= ~(1 << 2);
    }
}

void displaySetDB0(char state) {
    if (state == 1) { 
        PORTB |= 1 << 7;
    } else {
        PORTB &= ~(1 << 7);
    }
}

void displaySetDB1(char state) {
    if (state == 1) { 
        PORTB |= 1 << 6;
    } else {
        PORTB &= ~(1 << 6);
    }
}

void displaySetDB2(char state) {
    if (state == 1) { 
        PORTB |= 1 << 5;
    } else {
        PORTB &= ~(1 << 5);
    }
}

void displaySetDB3(char state) {
    if (state == 1) { 
        PORTB |= 1 << 4;
    } else {
        PORTB &= ~(1 << 4);
    }
}

void displaySetDB4(char state) {
    if (state == 1) { 
        PORTB |= 1 << 3;
    } else {
        PORTB &= ~(1 << 3);
    }
}

void displaySetDB5(char state) {
    if (state == 1) { 
        PORTB |= 1 << 2;
    } else {
        PORTB &= ~(1 << 2);
    }
}

void displaySetDB6(char state) {
    if (state == 1) { 
        PORTB |= 1 << 1;
    } else {
        PORTB &= ~(1 << 1);
    }
}

void displaySetDB7(char state) {
    if (state == 1) { 
        PORTB |= 1 << 0;
    } else {
        PORTB &= ~(1 << 0);
    }
}


void displaySetCS(char state) {
    if (state == 1) { 
        PORTA |= 1 << 3;
    } else {
        PORTA &= ~(1 << 3);
    }
}


void displaySetReset(char state) {
    if (state == 1) { 
        PORTA |= 1 << 4;
    } else {
        PORTA &= ~(1 << 4);
    }
}



void displaySetPins(char rw, char rs, char db7, char db6, char db5, char db4, char db3, char db2, char db1, char db0) {

    displaySetRW(rw);
    displaySetRS(rs);
    displaySetDB7(db7);
    displaySetDB6(db6);
    displaySetDB5(db5);
    displaySetDB4(db4);
    displaySetDB3(db3);
    displaySetDB2(db2);
    displaySetDB1(db1);
    displaySetDB0(db0);
    displaySetE(1);
    displayWriteData();
    displaySetE(0);
    displayWriteData();
    

}

void displayReset() {
    displaySetReset(1);
    displaySetReset(0);
    displayWriteData();
}
    
void displaySetMode(char DB5, char DB4, char DB3, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,0,0,0,0);
    displaySetPins(0,0,0,0,DB5,DB4,DB3,DB2,DB1,DB0);
    displayWriteData();
}

void displaySetChPitch(char DB7, char DB6, char DB5, char DB4, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,0,0,0,1);
    displaySetPins(0,0,DB7,DB6,DB5,DB4,0,DB2,DB1,DB0);
    displayWriteData();
}

void displaySetCharNumber(char DB7, char DB6, char DB5, char DB4, char DB3, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,0,0,1,0);
    displaySetPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0);
    displayWriteData();
}

void displaySetTimeDivision(char DB7, char DB6, char DB5, char DB4, char DB3, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,0,0,1,1);
    displaySetPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0);
    displayWriteData();
}

void displaySetCurPos(char DB3, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,0,1,0,0);
    displaySetPins(0,0,0,0,0,0,DB3,DB2,DB1,DB0);
    displayWriteData();
}

void displaySetStartLower(char DB7, char DB6, char DB5, char DB4, char DB3, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,1,0,0,0);
    displaySetPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0);
    displayWriteData();
}

void displaySetStartUpper(char DB7, char DB6, char DB5, char DB4, char DB3, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,1,0,0,1);
    displaySetPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0);
    displayWriteData();
}

void displaySetCursorLower(char DB7, char DB6, char DB5, char DB4, char DB3, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,1,0,1,0);
    displaySetPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0);
    displayWriteData();
}

void displaySetCursorUpper(char DB7, char DB6, char DB5, char DB4, char DB3, char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,1,0,1,1);
    displaySetPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0);
    displayWriteData();
}

void displayWriteDisplayData(char DB7, char DB6, char DB5, char DB4, char DB3, char DB2, char DB1, char DB0) {
    //printf("Scrivo dati display\n");
    displaySetPins(0,1,0,0,0,0,1,1,0,0);
    //            ### bit invertiti!
    //    ##self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)

    DB0 -= '0';
    DB1 -= '0';
    DB2 -= '0';
    DB3 -= '0';
    DB4 -= '0';
    DB5 -= '0';
    DB6 -= '0';
    DB7 -= '0';
    

    displaySetPins(0,0,DB0,DB1,DB2,DB3,DB4,DB5,DB6,DB7);
    //displayWriteData();
}

void displayWriteBit(char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,1,1,1,0);
    displaySetPins(0,0,0,0,0,0,0,DB2,DB1,DB0);
    displayWriteData();
}

void displayClearBit(char DB2, char DB1, char DB0) {
    displaySetPins(0,1,0,0,0,0,1,1,1,0);
    displaySetPins(0,0,0,0,0,0,0,DB2,DB1,DB0);
    displayWriteData();
}



void setupDisplay() {

    printf("Inizializzo display");

    displaySetReset(0);
    displaySetCS(0);
    displaySetReset(1);

    displaySetMode(1,1,0,0,1,0);

    displaySetChPitch(0,0,0,0,1,1,1);
    displaySetCharNumber(0,0,0,1,0,0,1,1);
    displaySetTimeDivision(1,0,1,0,0,0,0,0);
    displaySetCurPos(0,0,0,0);
    displaySetStartLower(0,0,0,0,0,0,0,0);
    displaySetStartUpper(0,0,0,0,0,0,0,0);
    displaySetCursorLower(0,0,0,0,0,0,0,0);
    displaySetCursorUpper(0,0,0,0,0,0,0,0);
}




void displayWritePixels(char sequence[]) {
    int i,lenoriginale;
    //printf("Stampo sequenza %s\n", sequence);
    displaySetCursorLower(0,0,0,0,0,0,0,0);
    displaySetCursorUpper(0,0,0,0,0,0,0,0);
    //printf("Sequenza: %s\n",sequence);
    lenoriginale = strlen(sequence);
    //for (i = 0; i < strlen(sequence); i++) {
    //    sequence[i] = sequence[i] - '0';
    //}

    //printf("Sequenza: %s\n",sequence); 

    for (i = 0; i < lenoriginale; i+=8) {
        displayWriteDisplayData(sequence[i],sequence[i+1],sequence[i+2],sequence[i+3],sequence[i+4],sequence[i+5],sequence[i+6],sequence[i+7]);
    }
}


int main(int argc, char *argv[])
{
	int fd;
	uint8_t buffer[2];

	fd = setup();

    setupDisplay();
    displayWritePixels(argv[1]);
    //"000000000000000000000000000000000000000000000011111111111111111111111111111100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000");


    close(fd);

	return (0);
}
