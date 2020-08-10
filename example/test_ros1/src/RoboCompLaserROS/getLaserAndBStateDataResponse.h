// Generated by gencpp from file RoboCompLaserROS/getLaserAndBStateDataResponse.msg
// DO NOT EDIT!


#ifndef ROBOCOMPLASERROS_MESSAGE_GETLASERANDBSTATEDATARESPONSE_H
#define ROBOCOMPLASERROS_MESSAGE_GETLASERANDBSTATEDATARESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <RoboCompGenericBaseROS/TBaseState.h>
#include <RoboCompLaserROS/TLaserData.h>

namespace RoboCompLaserROS
{
template <class ContainerAllocator>
struct getLaserAndBStateDataResponse_
{
  typedef getLaserAndBStateDataResponse_<ContainerAllocator> Type;

  getLaserAndBStateDataResponse_()
    : bState()
    , response()  {
    }
  getLaserAndBStateDataResponse_(const ContainerAllocator& _alloc)
    : bState(_alloc)
    , response(_alloc)  {
  (void)_alloc;
    }



   typedef  ::RoboCompGenericBaseROS::TBaseState_<ContainerAllocator>  _bState_type;
  _bState_type bState;

   typedef  ::RoboCompLaserROS::TLaserData_<ContainerAllocator>  _response_type;
  _response_type response;





  typedef boost::shared_ptr< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> const> ConstPtr;

}; // struct getLaserAndBStateDataResponse_

typedef ::RoboCompLaserROS::getLaserAndBStateDataResponse_<std::allocator<void> > getLaserAndBStateDataResponse;

typedef boost::shared_ptr< ::RoboCompLaserROS::getLaserAndBStateDataResponse > getLaserAndBStateDataResponsePtr;
typedef boost::shared_ptr< ::RoboCompLaserROS::getLaserAndBStateDataResponse const> getLaserAndBStateDataResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator1> & lhs, const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator2> & rhs)
{
  return lhs.bState == rhs.bState &&
    lhs.response == rhs.response;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator1> & lhs, const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace RoboCompLaserROS

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "439e5adff77032847b0c33145cb20fb2";
  }

  static const char* value(const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x439e5adff7703284ULL;
  static const uint64_t static_value2 = 0x7b0c33145cb20fb2ULL;
};

template<class ContainerAllocator>
struct DataType< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "RoboCompLaserROS/getLaserAndBStateDataResponse";
  }

  static const char* value(const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "RoboCompGenericBaseROS/TBaseState bState\n"
"TLaserData response\n"
"\n"
"\n"
"================================================================================\n"
"MSG: RoboCompGenericBaseROS/TBaseState\n"
"float32 x\n"
"float32 correctedX\n"
"float32 z\n"
"float32 correctedZ\n"
"float32 alpha\n"
"float32 correctedAlpha\n"
"float32 advVx\n"
"float32 advVz\n"
"float32 rotV\n"
"bool isMoving\n"
"\n"
"================================================================================\n"
"MSG: RoboCompLaserROS/TLaserData\n"
"TData[] TLaserData\n"
"\n"
"================================================================================\n"
"MSG: RoboCompLaserROS/TData\n"
"float32 angle\n"
"float32 dist\n"
;
  }

  static const char* value(const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.bState);
      stream.next(m.response);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct getLaserAndBStateDataResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::RoboCompLaserROS::getLaserAndBStateDataResponse_<ContainerAllocator>& v)
  {
    s << indent << "bState: ";
    s << std::endl;
    Printer< ::RoboCompGenericBaseROS::TBaseState_<ContainerAllocator> >::stream(s, indent + "  ", v.bState);
    s << indent << "response: ";
    s << std::endl;
    Printer< ::RoboCompLaserROS::TLaserData_<ContainerAllocator> >::stream(s, indent + "  ", v.response);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOCOMPLASERROS_MESSAGE_GETLASERANDBSTATEDATARESPONSE_H
