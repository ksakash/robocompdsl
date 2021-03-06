// Generated by gencpp from file RoboCompLaserROS/getLaserConfData.msg
// DO NOT EDIT!


#ifndef ROBOCOMPLASERROS_MESSAGE_GETLASERCONFDATA_H
#define ROBOCOMPLASERROS_MESSAGE_GETLASERCONFDATA_H

#include <ros/service_traits.h>


#include <RoboCompLaserROS/getLaserConfDataRequest.h>
#include <RoboCompLaserROS/getLaserConfDataResponse.h>


namespace RoboCompLaserROS
{

struct getLaserConfData
{

typedef getLaserConfDataRequest Request;
typedef getLaserConfDataResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct getLaserConfData
} // namespace RoboCompLaserROS


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::RoboCompLaserROS::getLaserConfData > {
  static const char* value()
  {
    return "3961fdd4f8941291375026213e8b0e82";
  }

  static const char* value(const ::RoboCompLaserROS::getLaserConfData&) { return value(); }
};

template<>
struct DataType< ::RoboCompLaserROS::getLaserConfData > {
  static const char* value()
  {
    return "RoboCompLaserROS/getLaserConfData";
  }

  static const char* value(const ::RoboCompLaserROS::getLaserConfData&) { return value(); }
};


// service_traits::MD5Sum< ::RoboCompLaserROS::getLaserConfDataRequest> should match
// service_traits::MD5Sum< ::RoboCompLaserROS::getLaserConfData >
template<>
struct MD5Sum< ::RoboCompLaserROS::getLaserConfDataRequest>
{
  static const char* value()
  {
    return MD5Sum< ::RoboCompLaserROS::getLaserConfData >::value();
  }
  static const char* value(const ::RoboCompLaserROS::getLaserConfDataRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::RoboCompLaserROS::getLaserConfDataRequest> should match
// service_traits::DataType< ::RoboCompLaserROS::getLaserConfData >
template<>
struct DataType< ::RoboCompLaserROS::getLaserConfDataRequest>
{
  static const char* value()
  {
    return DataType< ::RoboCompLaserROS::getLaserConfData >::value();
  }
  static const char* value(const ::RoboCompLaserROS::getLaserConfDataRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::RoboCompLaserROS::getLaserConfDataResponse> should match
// service_traits::MD5Sum< ::RoboCompLaserROS::getLaserConfData >
template<>
struct MD5Sum< ::RoboCompLaserROS::getLaserConfDataResponse>
{
  static const char* value()
  {
    return MD5Sum< ::RoboCompLaserROS::getLaserConfData >::value();
  }
  static const char* value(const ::RoboCompLaserROS::getLaserConfDataResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::RoboCompLaserROS::getLaserConfDataResponse> should match
// service_traits::DataType< ::RoboCompLaserROS::getLaserConfData >
template<>
struct DataType< ::RoboCompLaserROS::getLaserConfDataResponse>
{
  static const char* value()
  {
    return DataType< ::RoboCompLaserROS::getLaserConfData >::value();
  }
  static const char* value(const ::RoboCompLaserROS::getLaserConfDataResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROBOCOMPLASERROS_MESSAGE_GETLASERCONFDATA_H
