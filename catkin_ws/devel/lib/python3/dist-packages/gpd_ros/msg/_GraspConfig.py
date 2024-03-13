# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gpd_ros/GraspConfig.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class GraspConfig(genpy.Message):
  _md5sum = "8753a773793263ef11dce97fd6d996d5"
  _type = "gpd_ros/GraspConfig"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# This message describes a 2-finger grasp configuration by its 6-DOF pose,
# consisting of a 3-DOF position and 3-DOF orientation, and the opening
# width of the robot hand.

# Position
geometry_msgs/Point position # grasp position (bottom/base center of robot hand)

# Orientation represented as three axis (R = [approach binormal axis])
geometry_msgs/Vector3 approach # grasp approach direction
geometry_msgs/Vector3 binormal # hand closing direction
geometry_msgs/Vector3 axis # hand axis

std_msgs/Float32 width # Required aperture (opening width) of the robot hand

std_msgs/Float32 score # Score assigned to the grasp by the classifier

geometry_msgs/Point sample # point at which the grasp was found

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: std_msgs/Float32
float32 data"""
  __slots__ = ['position','approach','binormal','axis','width','score','sample']
  _slot_types = ['geometry_msgs/Point','geometry_msgs/Vector3','geometry_msgs/Vector3','geometry_msgs/Vector3','std_msgs/Float32','std_msgs/Float32','geometry_msgs/Point']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       position,approach,binormal,axis,width,score,sample

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GraspConfig, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.approach is None:
        self.approach = geometry_msgs.msg.Vector3()
      if self.binormal is None:
        self.binormal = geometry_msgs.msg.Vector3()
      if self.axis is None:
        self.axis = geometry_msgs.msg.Vector3()
      if self.width is None:
        self.width = std_msgs.msg.Float32()
      if self.score is None:
        self.score = std_msgs.msg.Float32()
      if self.sample is None:
        self.sample = geometry_msgs.msg.Point()
    else:
      self.position = geometry_msgs.msg.Point()
      self.approach = geometry_msgs.msg.Vector3()
      self.binormal = geometry_msgs.msg.Vector3()
      self.axis = geometry_msgs.msg.Vector3()
      self.width = std_msgs.msg.Float32()
      self.score = std_msgs.msg.Float32()
      self.sample = geometry_msgs.msg.Point()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_12d2f3d().pack(_x.position.x, _x.position.y, _x.position.z, _x.approach.x, _x.approach.y, _x.approach.z, _x.binormal.x, _x.binormal.y, _x.binormal.z, _x.axis.x, _x.axis.y, _x.axis.z, _x.width.data, _x.score.data, _x.sample.x, _x.sample.y, _x.sample.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.approach is None:
        self.approach = geometry_msgs.msg.Vector3()
      if self.binormal is None:
        self.binormal = geometry_msgs.msg.Vector3()
      if self.axis is None:
        self.axis = geometry_msgs.msg.Vector3()
      if self.width is None:
        self.width = std_msgs.msg.Float32()
      if self.score is None:
        self.score = std_msgs.msg.Float32()
      if self.sample is None:
        self.sample = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 128
      (_x.position.x, _x.position.y, _x.position.z, _x.approach.x, _x.approach.y, _x.approach.z, _x.binormal.x, _x.binormal.y, _x.binormal.z, _x.axis.x, _x.axis.y, _x.axis.z, _x.width.data, _x.score.data, _x.sample.x, _x.sample.y, _x.sample.z,) = _get_struct_12d2f3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_12d2f3d().pack(_x.position.x, _x.position.y, _x.position.z, _x.approach.x, _x.approach.y, _x.approach.z, _x.binormal.x, _x.binormal.y, _x.binormal.z, _x.axis.x, _x.axis.y, _x.axis.z, _x.width.data, _x.score.data, _x.sample.x, _x.sample.y, _x.sample.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.approach is None:
        self.approach = geometry_msgs.msg.Vector3()
      if self.binormal is None:
        self.binormal = geometry_msgs.msg.Vector3()
      if self.axis is None:
        self.axis = geometry_msgs.msg.Vector3()
      if self.width is None:
        self.width = std_msgs.msg.Float32()
      if self.score is None:
        self.score = std_msgs.msg.Float32()
      if self.sample is None:
        self.sample = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 128
      (_x.position.x, _x.position.y, _x.position.z, _x.approach.x, _x.approach.y, _x.approach.z, _x.binormal.x, _x.binormal.y, _x.binormal.z, _x.axis.x, _x.axis.y, _x.axis.z, _x.width.data, _x.score.data, _x.sample.x, _x.sample.y, _x.sample.z,) = _get_struct_12d2f3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_12d2f3d = None
def _get_struct_12d2f3d():
    global _struct_12d2f3d
    if _struct_12d2f3d is None:
        _struct_12d2f3d = struct.Struct("<12d2f3d")
    return _struct_12d2f3d
