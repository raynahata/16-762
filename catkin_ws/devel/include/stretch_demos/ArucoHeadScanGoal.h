// Generated by gencpp from file stretch_demos/ArucoHeadScanGoal.msg
// DO NOT EDIT!


#ifndef STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANGOAL_H
#define STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANGOAL_H


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
struct ArucoHeadScanGoal_
{
  typedef ArucoHeadScanGoal_<ContainerAllocator> Type;

  ArucoHeadScanGoal_()
    : aruco_id(0)
    , tilt_angle(0.0)
    , publish_to_map(false)
    , fill_in_blindspot_with_second_scan(false)
    , fast_scan(false)  {
    }
  ArucoHeadScanGoal_(const ContainerAllocator& _alloc)
    : aruco_id(0)
    , tilt_angle(0.0)
    , publish_to_map(false)
    , fill_in_blindspot_with_second_scan(false)
    , fast_scan(false)  {
  (void)_alloc;
    }



   typedef uint32_t _aruco_id_type;
  _aruco_id_type aruco_id;

   typedef float _tilt_angle_type;
  _tilt_angle_type tilt_angle;

   typedef uint8_t _publish_to_map_type;
  _publish_to_map_type publish_to_map;

   typedef uint8_t _fill_in_blindspot_with_second_scan_type;
  _fill_in_blindspot_with_second_scan_type fill_in_blindspot_with_second_scan;

   typedef uint8_t _fast_scan_type;
  _fast_scan_type fast_scan;





  typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> const> ConstPtr;

}; // struct ArucoHeadScanGoal_

typedef ::stretch_demos::ArucoHeadScanGoal_<std::allocator<void> > ArucoHeadScanGoal;

typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanGoal > ArucoHeadScanGoalPtr;
typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanGoal const> ArucoHeadScanGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator1> & lhs, const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator2> & rhs)
{
  return lhs.aruco_id == rhs.aruco_id &&
    lhs.tilt_angle == rhs.tilt_angle &&
    lhs.publish_to_map == rhs.publish_to_map &&
    lhs.fill_in_blindspot_with_second_scan == rhs.fill_in_blindspot_with_second_scan &&
    lhs.fast_scan == rhs.fast_scan;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator1> & lhs, const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace stretch_demos

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7c9f72de60496d5ea3903a808d86da58";
  }

  static const char* value(const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7c9f72de60496d5eULL;
  static const uint64_t static_value2 = 0xa3903a808d86da58ULL;
};

template<class ContainerAllocator>
struct DataType< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "stretch_demos/ArucoHeadScanGoal";
  }

  static const char* value(const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Define the goal\n"
"\n"
"# Specify aruco ID to look for\n"
"uint32 aruco_id\n"
"\n"
"# Specify the camera tilt_angle at which to scan\n"
"float32 tilt_angle\n"
"\n"
"# Publish tf relative to the map frame\n"
"bool publish_to_map\n"
"\n"
"# If robot should rotate to cover the blind spot generated by the mast\n"
"bool fill_in_blindspot_with_second_scan \n"
"\n"
"# If scan should stop as soon as a matching aruco ID is found\n"
"bool fast_scan\n"
"\n"
;
  }

  static const char* value(const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.aruco_id);
      stream.next(m.tilt_angle);
      stream.next(m.publish_to_map);
      stream.next(m.fill_in_blindspot_with_second_scan);
      stream.next(m.fast_scan);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ArucoHeadScanGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator>& v)
  {
    s << indent << "aruco_id: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.aruco_id);
    s << indent << "tilt_angle: ";
    Printer<float>::stream(s, indent + "  ", v.tilt_angle);
    s << indent << "publish_to_map: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.publish_to_map);
    s << indent << "fill_in_blindspot_with_second_scan: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.fill_in_blindspot_with_second_scan);
    s << indent << "fast_scan: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.fast_scan);
  }
};

} // namespace message_operations
} // namespace ros

#endif // STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANGOAL_H