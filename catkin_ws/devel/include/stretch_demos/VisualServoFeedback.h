// Generated by gencpp from file stretch_demos/VisualServoFeedback.msg
// DO NOT EDIT!


#ifndef STRETCH_DEMOS_MESSAGE_VISUALSERVOFEEDBACK_H
#define STRETCH_DEMOS_MESSAGE_VISUALSERVOFEEDBACK_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace stretch_demos
{
template <class ContainerAllocator>
struct VisualServoFeedback_
{
  typedef VisualServoFeedback_<ContainerAllocator> Type;

  VisualServoFeedback_()
    : angle_error(0.0)
    , distance_error(0.0)  {
    }
  VisualServoFeedback_(const ContainerAllocator& _alloc)
    : angle_error(0.0)
    , distance_error(0.0)  {
  (void)_alloc;
    }



   typedef double _angle_error_type;
  _angle_error_type angle_error;

   typedef double _distance_error_type;
  _distance_error_type distance_error;





  typedef boost::shared_ptr< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct VisualServoFeedback_

typedef ::stretch_demos::VisualServoFeedback_<std::allocator<void> > VisualServoFeedback;

typedef boost::shared_ptr< ::stretch_demos::VisualServoFeedback > VisualServoFeedbackPtr;
typedef boost::shared_ptr< ::stretch_demos::VisualServoFeedback const> VisualServoFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::stretch_demos::VisualServoFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::stretch_demos::VisualServoFeedback_<ContainerAllocator1> & lhs, const ::stretch_demos::VisualServoFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.angle_error == rhs.angle_error &&
    lhs.distance_error == rhs.distance_error;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::stretch_demos::VisualServoFeedback_<ContainerAllocator1> & lhs, const ::stretch_demos::VisualServoFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace stretch_demos

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b36919b18c17a48cbd98a249a4c96a61";
  }

  static const char* value(const ::stretch_demos::VisualServoFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb36919b18c17a48cULL;
  static const uint64_t static_value2 = 0xbd98a249a4c96a61ULL;
};

template<class ContainerAllocator>
struct DataType< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "stretch_demos/VisualServoFeedback";
  }

  static const char* value(const ::stretch_demos::VisualServoFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# feedback\n"
"# angle error is the angular error between source and target frames\n"
"float64 angle_error\n"
"\n"
"# distance error is the euclidean error between source and target frames\n"
"float64 distance_error\n"
"\n"
;
  }

  static const char* value(const ::stretch_demos::VisualServoFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.angle_error);
      stream.next(m.distance_error);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VisualServoFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::stretch_demos::VisualServoFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::stretch_demos::VisualServoFeedback_<ContainerAllocator>& v)
  {
    s << indent << "angle_error: ";
    Printer<double>::stream(s, indent + "  ", v.angle_error);
    s << indent << "distance_error: ";
    Printer<double>::stream(s, indent + "  ", v.distance_error);
  }
};

} // namespace message_operations
} // namespace ros

#endif // STRETCH_DEMOS_MESSAGE_VISUALSERVOFEEDBACK_H