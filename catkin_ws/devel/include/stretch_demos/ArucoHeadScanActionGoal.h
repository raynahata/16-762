// Generated by gencpp from file stretch_demos/ArucoHeadScanActionGoal.msg
// DO NOT EDIT!


#ifndef STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANACTIONGOAL_H
#define STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANACTIONGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <actionlib_msgs/GoalID.h>
#include <stretch_demos/ArucoHeadScanGoal.h>

namespace stretch_demos
{
template <class ContainerAllocator>
struct ArucoHeadScanActionGoal_
{
  typedef ArucoHeadScanActionGoal_<ContainerAllocator> Type;

  ArucoHeadScanActionGoal_()
    : header()
    , goal_id()
    , goal()  {
    }
  ArucoHeadScanActionGoal_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , goal_id(_alloc)
    , goal(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::actionlib_msgs::GoalID_<ContainerAllocator>  _goal_id_type;
  _goal_id_type goal_id;

   typedef  ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator>  _goal_type;
  _goal_type goal;





  typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> const> ConstPtr;

}; // struct ArucoHeadScanActionGoal_

typedef ::stretch_demos::ArucoHeadScanActionGoal_<std::allocator<void> > ArucoHeadScanActionGoal;

typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanActionGoal > ArucoHeadScanActionGoalPtr;
typedef boost::shared_ptr< ::stretch_demos::ArucoHeadScanActionGoal const> ArucoHeadScanActionGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator1> & lhs, const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.goal_id == rhs.goal_id &&
    lhs.goal == rhs.goal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator1> & lhs, const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace stretch_demos

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ce33614b3cd5a08361338346fe0ff498";
  }

  static const char* value(const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xce33614b3cd5a083ULL;
  static const uint64_t static_value2 = 0x61338346fe0ff498ULL;
};

template<class ContainerAllocator>
struct DataType< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "stretch_demos/ArucoHeadScanActionGoal";
  }

  static const char* value(const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
"Header header\n"
"actionlib_msgs/GoalID goal_id\n"
"ArucoHeadScanGoal goal\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: actionlib_msgs/GoalID\n"
"# The stamp should store the time at which this goal was requested.\n"
"# It is used by an action server when it tries to preempt all\n"
"# goals that were requested before a certain time\n"
"time stamp\n"
"\n"
"# The id provides a way to associate feedback and\n"
"# result message with specific goal requests. The id\n"
"# specified must be unique.\n"
"string id\n"
"\n"
"\n"
"================================================================================\n"
"MSG: stretch_demos/ArucoHeadScanGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
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

  static const char* value(const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.goal_id);
      stream.next(m.goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ArucoHeadScanActionGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::stretch_demos::ArucoHeadScanActionGoal_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "goal_id: ";
    s << std::endl;
    Printer< ::actionlib_msgs::GoalID_<ContainerAllocator> >::stream(s, indent + "  ", v.goal_id);
    s << indent << "goal: ";
    s << std::endl;
    Printer< ::stretch_demos::ArucoHeadScanGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // STRETCH_DEMOS_MESSAGE_ARUCOHEADSCANACTIONGOAL_H