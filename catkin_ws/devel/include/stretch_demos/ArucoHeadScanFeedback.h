// Generated by gencpp from file stretch_demos/ArucoHeadScanFeedback.msg
// DO NOT EDIT!


#ifndef STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANFEEDBACK_H
#define STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANFEEDBACK_H


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
struct ArucoHeadScanFeedback_
{
  typedef ArucoHeadScanFeedback_<ContainerAllocator> Type;

  ArucoHeadScanFeedback_()
    : pan_angle(0.0)  {
    }
  ArucoHeadScanFeedback_(const ContainerAllocator& _alloc)
    : pan_angle(0.0)  {
  (void)_alloc;
    }



   typedef float _pan_angle_type;
  _pan_angle_type pan_angle;





  typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct ArucoHeadScanFeedback_

typedef ::stretch_demos::ArucoHeadScanFeedback_<std::allocator<void> > ArucoHeadScanFeedback;

typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanFeedback > ArucoHeadScanFeedbackPtr;
typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanFeedback const> ArucoHeadScanFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator1> & lhs, const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.pan_angle == rhs.pan_angle;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator1> & lhs, const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace stretch_demos

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f8d06c64a9db7a2a34a365c076b315f6";
  }

  static const char* value(const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf8d06c64a9db7a2aULL;
  static const uint64_t static_value2 = 0x34a365c076b315f6ULL;
};

template<class ContainerAllocator>
struct DataType< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "stretch_demos/ArucoHeadScanFeedback";
  }

  static const char* value(const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Define a feedback message\n"
"\n"
"# Pan angle of the camera\n"
"float32 pan_angle\n"
"\n"
;
  }

  static const char* value(const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pan_angle);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ArucoHeadScanFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::stretch_demos::ArucoHeadScanFeedback_<ContainerAllocator>& v)
  {
    s << indent << "pan_angle: ";
    Printer<float>::stream(s, indent + "  ", v.pan_angle);
  }
};

} // namespace message_operations
} // namespace ros

#endif // STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANFEEDBACK_H
