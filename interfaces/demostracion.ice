//******************************************************************
// 
//  Generated by IDSL to IDL Translator
//  
//  File name: demostracion.idl
//  Source: demostracion.idsl
//  
//******************************************************************   
#ifndef ROBOCOMPDEMOSTRACION_ICE
#define ROBOCOMPDEMOSTRACION_ICE

#include <JointMotor.ice>

#include <CommonHead.ice>

module RoboCompdemostracion{

	interface demostracion{
						RoboCompJointMotor::MotorParamsList getAllMotorParams();
	                void  getAllMotorState(out RoboCompJointMotor::MotorStateMap mstateMap);
	                void  setPosition(RoboCompJointMotor::MotorGoalPosition goal)throws RoboCompJointMotor::UnknownMotorException, RoboCompJointMotor::HardwareFailedException;
	};
};
  
#endif