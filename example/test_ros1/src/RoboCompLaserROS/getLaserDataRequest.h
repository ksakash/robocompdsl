// Generated by gencpp from file RoboCompLaserROS/getLaserDataRequest.msg
// DO NOT EDIT!


#ifndef ROBOCOMPLASERROS_MESSAGE_GETLASERDATAREQUEST_H
#define ROBOCOMPLASERROS_MESSAGE_GETLASERDATAREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace RoboCompLaserROS
{
template <class ContainerAllocator>
struct getLaserDataRequest_
{
  typedef getLaserDataRequest_<ContainerAllocator> Type;

  getLaserDataRequest_()
    {
    }
  getLaserDataRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> const> ConstPtr;

}; // struct getLaserDataRequest_

typedef ::RoboCompLaserROS::getLaserDataRequest_<std::allocator<void> > getLaserDataRequest;

typedef boost::shared_ptr< ::RoboCompLaserROS::getLaserDataRequest > getLaserDataRequestPtr;
typedef boost::shared_ptr< ::RoboCompLaserROS::getLaserDataRequest const> getLaserDataRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace RoboCompLaserROS

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "RoboCompLaserROS/getLaserDataRequest";
  }

  static const char* value(const ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct getLaserDataRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::RoboCompLaserROS::getLaserDataRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // ROBOCOMPLASERROS_MESSAGE_GETLASERDATAREQUEST_H
