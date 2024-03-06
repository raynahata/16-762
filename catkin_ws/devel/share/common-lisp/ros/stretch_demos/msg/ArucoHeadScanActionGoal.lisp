; Auto-generated. Do not edit!


(cl:in-package stretch_demos-msg)


;//! \htmlinclude ArucoHeadScanActionGoal.msg.html

(cl:defclass <ArucoHeadScanActionGoal> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (goal_id
    :reader goal_id
    :initarg :goal_id
    :type actionlib_msgs-msg:GoalID
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalID))
   (goal
    :reader goal
    :initarg :goal
    :type stretch_demos-msg:ArucoHeadScanGoal
    :initform (cl:make-instance 'stretch_demos-msg:ArucoHeadScanGoal)))
)

(cl:defclass ArucoHeadScanActionGoal (<ArucoHeadScanActionGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArucoHeadScanActionGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArucoHeadScanActionGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name stretch_demos-msg:<ArucoHeadScanActionGoal> is deprecated: use stretch_demos-msg:ArucoHeadScanActionGoal instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ArucoHeadScanActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stretch_demos-msg:header-val is deprecated.  Use stretch_demos-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'goal_id-val :lambda-list '(m))
(cl:defmethod goal_id-val ((m <ArucoHeadScanActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stretch_demos-msg:goal_id-val is deprecated.  Use stretch_demos-msg:goal_id instead.")
  (goal_id m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <ArucoHeadScanActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader stretch_demos-msg:goal-val is deprecated.  Use stretch_demos-msg:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArucoHeadScanActionGoal>) ostream)
  "Serializes a message object of type '<ArucoHeadScanActionGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal_id) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArucoHeadScanActionGoal>) istream)
  "Deserializes a message object of type '<ArucoHeadScanActionGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal_id) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArucoHeadScanActionGoal>)))
  "Returns string type for a message object of type '<ArucoHeadScanActionGoal>"
  "stretch_demos/ArucoHeadScanActionGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArucoHeadScanActionGoal)))
  "Returns string type for a message object of type 'ArucoHeadScanActionGoal"
  "stretch_demos/ArucoHeadScanActionGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArucoHeadScanActionGoal>)))
  "Returns md5sum for a message object of type '<ArucoHeadScanActionGoal>"
  "ce33614b3cd5a08361338346fe0ff498")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArucoHeadScanActionGoal)))
  "Returns md5sum for a message object of type 'ArucoHeadScanActionGoal"
  "ce33614b3cd5a08361338346fe0ff498")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArucoHeadScanActionGoal>)))
  "Returns full string definition for message of type '<ArucoHeadScanActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%ArucoHeadScanGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: stretch_demos/ArucoHeadScanGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the goal~%~%# Specify aruco ID to look for~%uint32 aruco_id~%~%# Specify the camera tilt_angle at which to scan~%float32 tilt_angle~%~%# Publish tf relative to the map frame~%bool publish_to_map~%~%# If robot should rotate to cover the blind spot generated by the mast~%bool fill_in_blindspot_with_second_scan ~%~%# If scan should stop as soon as a matching aruco ID is found~%bool fast_scan~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArucoHeadScanActionGoal)))
  "Returns full string definition for message of type 'ArucoHeadScanActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%ArucoHeadScanGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: stretch_demos/ArucoHeadScanGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the goal~%~%# Specify aruco ID to look for~%uint32 aruco_id~%~%# Specify the camera tilt_angle at which to scan~%float32 tilt_angle~%~%# Publish tf relative to the map frame~%bool publish_to_map~%~%# If robot should rotate to cover the blind spot generated by the mast~%bool fill_in_blindspot_with_second_scan ~%~%# If scan should stop as soon as a matching aruco ID is found~%bool fast_scan~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArucoHeadScanActionGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArucoHeadScanActionGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'ArucoHeadScanActionGoal
    (cl:cons ':header (header msg))
    (cl:cons ':goal_id (goal_id msg))
    (cl:cons ':goal (goal msg))
))