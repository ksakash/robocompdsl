/*
 *    Copyright (C)2020 by YOUR NAME HERE
 *
 *    This file is part of RoboComp
 *
 *    RoboComp is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    RoboComp is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 *    You should have received a copy of the GNU General Public License
 *    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef GENERICWORKER_H
#define GENERICWORKER_H

#include "config.h"
#include <stdint.h>
#include <qlog/qlog.h>

#include <CommonBehavior.h>

#include <GenericBase.h>
#include <ros/ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Int32.h>
#include <std_msgs/Bool.h>
#include <RoboCompLaserROS/TLaserData.h>
#include <RoboCompLaserROS/getLaserDataRequest.h>
#include <RoboCompLaserROS/getLaserConfDataResponse.h>
#include <RoboCompLaserROS/getLaserConfDataRequest.h>
#include <RoboCompLaserROS/getLaserData.h>
#include <RoboCompLaserROS/getLaserAndBStateDataResponse.h>
#include <RoboCompLaserROS/LaserConfData.h>
#include <RoboCompLaserROS/getLaserAndBStateData.h>
#include <RoboCompLaserROS/TData.h>
#include <RoboCompLaserROS/shortVector.h>
#include <RoboCompLaserROS/getLaserConfData.h>
#include <RoboCompLaserROS/getLaserDataResponse.h>
#include <RoboCompLaserROS/getLaserAndBStateDataRequest.h>
#include <RoboCompGenericBaseROS/TBaseState.h>


#define CHECK_PERIOD 5000
#define BASIC_PERIOD 100

using namespace std;
using namespace RoboCompGenericBase;

typedef map <string,::IceProxy::Ice::Object*> MapPrx;


class ClientLaser {

public:

	ros::ServiceClient client_getLaserAndBStateData;
	ros::ServiceClient client_getLaserConfData;
	ros::ServiceClient client_getLaserData;

	std::shared_ptr<ros::NodeHandle> node;

	ClientLaser () {

		client_getLaserAndBStateData = node->serviceClient<RoboCompLaserROS::getLaserAndBStateData>("getLaserAndBStateData");
		client_getLaserConfData = node->serviceClient<RoboCompLaserROS::getLaserConfData>("getLaserConfData");
		client_getLaserData = node->serviceClient<RoboCompLaserROS::getLaserData>("getLaserData");

	}

	~ClientLaser () {}

};


// mix of ROS and ICE
class GenericWorker :
public QObject
{
Q_OBJECT
public:
	GenericWorker(MapPrx& mprx);
	virtual ~GenericWorker();
	virtual void killYourSelf();
	virtual void setPeriod(int p);

	virtual bool setParams(RoboCompCommonBehavior::ParameterList params) = 0;
	QMutex *mutex;

protected:

	QTimer timer;
	int Period;
	ClientLaser* laser_proxy;

public slots:

	virtual void compute() = 0;
    virtual void initialize(int period) = 0;

signals:
	void kill();
};

#endif
