#ifndef ROBOT_H_
#define ROBOT_H_
#include "nodeWifi.h"
#include "motorMovementController.h" 
#include "FacesLed.h"
#include "utils.h"
#include "JointExtra.h"
#define CALIBRATION_SPEED 50
#define MAX_ARGS 4
#define EMOTION_STR "emotions"
#define VERSION "1.0"

class Robot{

  int speeds;
  int currentArgs;
  bool movementCurrentState; 
  String command;
  int timer;
  int movementRobot;
  String arguments[MAX_ARGS];
  String emotion;
  bool shouldAnswer;
  bool isTimedAction;
  int macroStep;
  String lastAction;
  bool motorInactive;
  int lastMotorAck;
  bool macroRunning;
  String macroInExec;
  
  private:
  bool robotForward(); 
  bool robotTurn(int dir); 
  bool robotTimedMove(int dir); 
  bool robotTimedTurn(int dir); 
  bool robotStopMovement();
  void robotForeverMove(int dir);
  void processMsgString(String msg); 
  void calibration();
  void readFaces(String msg);
  
  public:
  String ip;
  String alias;
  long timeElapsed;
  bool inAction;
  bool reverseActive;
  bool forwardActive;
  bool rightActive;
  bool leftActive;
  Robot();
  void setupRobot(int serial, String givenAlias,String ssid, String password);
  void processMsg(String msg,bool checkStatus , WiFiClient client);
  bool robotBasicCommands(String msg, bool checkStatus); 
  void readCustomVariablesMotors(String msg,WiFiClient client); 
  void readCustomVariablesSensors(String msg,WiFiClient client);
  void JointServoMsg(String msg,WiFiClient client); 
  void readFaces(String msg, WiFiClient); 
  bool processCommands(String msg, bool checkStatus);
 
};
#endif
