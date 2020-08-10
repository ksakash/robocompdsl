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
#include <rclcpp/rclcpp.hpp>
#include <my_first_comp/msg/short_vector.hpp>
#include <my_first_comp/msg/t_data.hpp>
#include <my_first_comp/msg/laser_conf_data.hpp>
#include <my_first_comp/msg/t_base_state.hpp>
#include <my_first_comp/msg/t_laser_data.hpp>
#include <my_first_comp/srv/get_laser_and_b_state_data.hpp>
#include <my_first_comp/srv/get_laser_data.hpp>
#include <my_first_comp/srv/get_laser_conf_data.hpp>


#define CHECK_PERIOD 5000
#define BASIC_PERIOD 100

using namespace std;
using namespace RoboCompGenericBase;
using namespace std::chrono_literals;
using namespace std::placeholders;

typedef map <string,::IceProxy::Ice::Object*> MapPrx;


class ClientLaser {

public:

	rclcpp::Client<my_first_comp::srv::GetLaserAndBStateData>::SharedPtr client_getLaserAndBStateData;
	rclcpp::Client<my_first_comp::srv::GetLaserConfData>::SharedPtr client_getLaserConfData;
	rclcpp::Client<my_first_comp::srv::GetLaserData>::SharedPtr client_getLaserData;

	rclcpp::Node::SharedPtr node;

	ClientLaser () {

		node = rclcpp::Node::make_shared ("my_client");

		client_getLaserAndBStateData = node->create_client<my_first_comp::srv::GetLaserAndBStateData>("getLaserAndBStateData");
		client_getLaserConfData = node->create_client<my_first_comp::srv::GetLaserConfData>("getLaserConfData");
		client_getLaserData = node->create_client<my_first_comp::srv::GetLaserData>("getLaserData");
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
