#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include <PID_v1.h>

// Connect to the two encoder outputs!
#define ENCODER_A 2
#define ENCODER_B 3

#define J1_ENCODER_A 5
#define J1_ENCODER_B 6

#define J2_ENCODER_A 8
#define J2_ENCODER_B 9

#define J3_ENCODER_A 11
#define J3_ENCODER_B 12

#define J4_ENCODER_A 22
#define J4_ENCODER_B 23

// For the last motor J4
int motorAPin_A = 18;  //Arduino digital 18 is connected to HG7881's A-1A terminal
int motorAPin_B = 19;  //Arduino digital 19 is connected to HG7881's A-1B terminal

// These let us convert ticks-to-RPM
#define ENCODERMULT 7

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *Base1 = AFMS.getMotor(1);
Adafruit_DCMotor *Joint1 = AFMS.getMotor(2);
Adafruit_DCMotor *Joint2 = AFMS.getMotor(3);
Adafruit_DCMotor *Joint3 = AFMS.getMotor(4);

// Derivs_Limiter B1Limiter = Derivs_Limiter(200, 50);  // velocityLimit, accelerationLimit, (decelerationLimit)
// Derivs_Limiter J1Limiter = Derivs_Limiter(250, 70);  // velocityLimit, accelerationLimit, (decelerationLimit)
// Derivs_Limiter J2Limiter = Derivs_Limiter(250, 70);  // velocityLimit, accelerationLimit, (decelerationLimit)
// Derivs_Limiter J3Limiter = Derivs_Limiter(300, 90);  // velocityLimit, accelerationLimit, (decelerationLimit)
// Derivs_Limiter J4Limiter = Derivs_Limiter(300, 90);  // velocityLimit, accelerationLimit, (decelerationLimit)

int gearing[] = { 603, 298, 300, 100, 118 };
volatile float angle[] = { 0, 0, 0, 0, 0 };
volatile uint32_t lastA = 0;
volatile bool motordir[] = { 1, 1, 1, 1, 1 };

double B1Setpoint, B1Input, B1Output;
double B1Kp = 40, B1Ki = 5, B1Kd = 0.5;
PID B1PID(&B1Input, &B1Output, &B1Setpoint, B1Kp, B1Ki, B1Kd, DIRECT);

double J1Setpoint, J1Input, J1Output;
double J1Kp = 30, J1Ki = 5, J1Kd = 0.3;
PID J1PID(&J1Input, &J1Output, &J1Setpoint, J1Kp, J1Ki, J1Kd, DIRECT);

double J2Setpoint, J2Input, J2Output;
double J2Kp = 8, J2Ki = 0.7, J2Kd = 0.3;
PID J2PID(&J2Input, &J2Output, &J2Setpoint, J2Kp, J2Ki, J2Kd, DIRECT);

double J3Setpoint, J3Input, J3Output;
double J3Kp = 12, J3Ki = 2, J3Kd = 0.2;
PID J3PID(&J3Input, &J3Output, &J3Setpoint, J3Kp, J3Ki, J3Kd, DIRECT);

double J4Setpoint, J4Input, J4Output;
double J4Kp = 9, J4Ki = 0.7, J4Kd = 0.3;
PID J4PID(&J4Input, &J4Output, &J4Setpoint, J4Kp, J4Ki, J4Kd, DIRECT);

int i;

String inputString = "";  // for incoming serial data

int Jd[] = { 0, 0, 0, 0, 0 };
float Jc[] = { 0, 0, 0, 0, 0 };
bool stringComplete = 0;

String message;
int count = 0;
int lastCount = 0;

void setup() {
  Serial.begin(115200);  // set up Serial library at 9600 bps

  pinMode(ENCODER_B, INPUT_PULLUP);
  pinMode(ENCODER_A, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENCODER_A), B1_InterruptA, RISING);

  pinMode(J1_ENCODER_B, INPUT_PULLUP);
  pinMode(J1_ENCODER_A, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(J1_ENCODER_A), J1_InterruptA, RISING);

  pinMode(J2_ENCODER_B, INPUT_PULLUP);
  pinMode(J2_ENCODER_A, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(J2_ENCODER_A), J2_InterruptA, RISING);

  pinMode(J3_ENCODER_B, INPUT_PULLUP);
  pinMode(J3_ENCODER_A, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(J3_ENCODER_A), J3_InterruptA, RISING);

  pinMode(J4_ENCODER_B, INPUT_PULLUP);
  pinMode(J4_ENCODER_A, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(J4_ENCODER_A), J4_InterruptA, RISING);

  delay(100);

  while (1) {  // create with the default frequency 1.6KHz
    if (AFMS.begin(1600)) {
      break;
    }
    Serial.println("Could not find Motor Shield. Check wiring.");
  }

  Serial.println("Motor Shield found.");
  Serial.println("MMMMotor party!");


  B1PID.SetOutputLimits(-255.0, 255.0);
  Base1->run(RELEASE);
  B1Setpoint = 0.0;
  B1Input = angle[0];
  B1PID.SetMode(AUTOMATIC);

  J1PID.SetOutputLimits(-255.0, 255.0);
  Joint1->run(RELEASE);
  J1Setpoint = 0.0;
  J1Input = angle[1];
  J1PID.SetMode(AUTOMATIC);

  J2PID.SetOutputLimits(-255.0, 255.0);
  Joint2->run(RELEASE);
  J2Setpoint = 0.0;
  J2Input = angle[2];
  J2PID.SetMode(AUTOMATIC);

  J3PID.SetOutputLimits(-255.0, 255.0);
  Joint3->run(RELEASE);
  J3Setpoint = 0.0;
  J3Input = angle[3];
  J3PID.SetMode(AUTOMATIC);

  J4PID.SetOutputLimits(-255.0, 255.0);
  J4Setpoint = 0.0;
  J4Input = angle[4];
  J4PID.SetMode(AUTOMATIC);

  pinMode(motorAPin_A, OUTPUT);  //direction
  pinMode(motorAPin_B, OUTPUT);  //speed

  digitalWrite(motorAPin_A, LOW);
  digitalWrite(motorAPin_B, LOW);
}

void reset_angles() {
  Jc[0] = 0;
  Jc[1] = 0;
  Jc[2] = 0;
  Jc[3] = 0;
  Jc[4] = 0;

  Jd[0] = 0;
  Jd[1] = 0;
  Jd[2] = 0;
  Jd[3] = 0;
  Jd[4] = 0;

  B1Input = 0;
  J1Input = 0;
  J2Input = 0;
  J3Input = 0;
  J4Input = 0;
}

void print_angles() {
  Serial.print("Desired : ");
  Serial.print(Jd[0]);
  Serial.print(" ");
  Serial.print(Jd[1]);
  Serial.print(" ");
  Serial.print(Jd[2]);
  Serial.print(" ");
  Serial.print(Jd[3]);
  Serial.print(" ");
  Serial.println(Jd[4]);
  Serial.print("Actual : ");
  Serial.print(Jc[0]);
  Serial.print(" ");
  Serial.print(Jc[1]);
  Serial.print(" ");
  Serial.print(Jc[2]);
  Serial.print(" ");
  Serial.print(Jc[3]);
  Serial.print(" ");
  Serial.println(Jc[4]);
}

void B1_InterruptA() {
  motordir[0] = digitalRead(ENCODER_B);

  angle[0] += (2 * motordir[0] - 1) * 360.0 / (gearing[0] * ENCODERMULT);
  B1Input += (2 * motordir[0] - 1) * 360.0 / (gearing[0] * ENCODERMULT);
}

void J1_InterruptA() {
  motordir[1] = digitalRead(J1_ENCODER_B);

  angle[1] += (2 * motordir[1] - 1) * 360.0 / (gearing[1] * ENCODERMULT);
  J1Input += (2 * motordir[1] - 1) * 360.0 / (gearing[1] * ENCODERMULT);
}

void J2_InterruptA() {
  motordir[2] = digitalRead(J2_ENCODER_B);

  angle[2] += (2 * motordir[2] - 1) * 360.0 / (gearing[2] * ENCODERMULT);
  J2Input += (2 * motordir[2] - 1) * 360.0 / (gearing[2] * ENCODERMULT);
}

void J3_InterruptA() {
  motordir[3] = digitalRead(J3_ENCODER_B);

  angle[3] += (2 * motordir[3] - 1) * 360.0 / (gearing[3] * ENCODERMULT);
  J3Input += (2 * motordir[3] - 1) * 360.0 / (gearing[3] * ENCODERMULT);
}

void J4_InterruptA() {
  motordir[4] = digitalRead(J4_ENCODER_B);

  angle[4] += (2 * motordir[4] - 1) * 360.0 / (gearing[4] * ENCODERMULT);
  J4Input += (2 * motordir[4] - 1) * 360.0 / (gearing[4] * ENCODERMULT);
}

void B1_changeSpeed() {
  if (B1Output >= 0) {
    Base1->run(FORWARD);
    Base1->setSpeed(B1Output);
  } else {
    Base1->run(BACKWARD);
    Base1->setSpeed(-B1Output);
  }
}

void J1_changeSpeed() {
  if (J1Output >= 0) {
    Joint1->run(FORWARD);
    Joint1->setSpeed(J1Output);
  } else {
    Joint1->run(BACKWARD);
    Joint1->setSpeed(-J1Output);
  }
}

void J2_changeSpeed() {
  if (J2Output >= 0) {
    Joint2->run(FORWARD);
    Joint2->setSpeed(J2Output);
  } else {
    Joint2->run(BACKWARD);
    Joint2->setSpeed(-J2Output);
  }
}

void J3_changeSpeed() {
  if (J3Output >= 0) {
    Joint3->run(FORWARD);
    Joint3->setSpeed(J3Output);
  } else {
    Joint3->run(BACKWARD);
    Joint3->setSpeed(-J3Output);
  }
}
void J4_changeSpeed() {
  if (J4Output >= 0) {
    analogWrite(motorAPin_A, 0);
    analogWrite(motorAPin_B, J4Output);
  } else {
    analogWrite(motorAPin_A, -J4Output);
    analogWrite(motorAPin_B, 0);
  }
}

int matlabVals[150];
void loop() {
  while (Serial.available()>0)
  {
    message = Serial.readString();
    matlabVals[count] = message.toInt();
    count++;
    Serial.print(message); // just for testing purposes
    Serial.print(count); 
  }
  
  for (int i =0; i < 30; i++)
  {
    Jd[0] = matlabVals[(i * 5)];
    Jd[1] = matlabVals[(i * 5) + 1];
    Jd[2] = matlabVals[(i * 5) + 2];
    Jd[3] = matlabVals[(i * 5) + 3];
    Jd[4] = matlabVals[(i * 5) + 4];

  B1Setpoint = Jd[0];
  B1PID.Compute();
  B1_changeSpeed();

  J1Setpoint = Jd[1];
  J1PID.Compute();
  J1_changeSpeed();

  J2Setpoint = Jd[2];
  J2PID.Compute();
  J2_changeSpeed();

  J3Setpoint = Jd[3];
  J3PID.Compute();
  J3_changeSpeed();

  J4Setpoint = Jd[4];
  J4PID.Compute();
  J4_changeSpeed();

  Jc[0] = B1Input;
  Jc[1] = J1Input;
  Jc[2] = J2Input;
  Jc[3] = J3Input;
  Jc[4] = J4Input;

  print_angles(); // also for testing purposes

  delay(1000);
  }
  
}