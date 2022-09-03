/**
 * @license Licensed under the Apache License, Version 2.0 (the "License"):
 *          http://www.apache.org/licenses/LICENSE-2.0
 *
 * @fileoverview General javaScript for Arduino app with material design.
 */
 'use strict';

 /** Create a namespace for the application. */
 var SmartTown = SmartTown || {};

 SmartTown.setMiddleGenerator = function (generator){
    Blockly.SmartTown.middleGenerator = generator;
 };
 
 SmartTown.getSTRobotSketch= function(){
   return SmartTown.generateRobotSketch(Ardublockly.workspace).join("\n");
 }