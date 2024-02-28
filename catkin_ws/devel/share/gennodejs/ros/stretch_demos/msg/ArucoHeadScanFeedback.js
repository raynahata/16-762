// Auto-generated. Do not edit!

// (in-package stretch_demos.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ArucoHeadScanFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pan_angle = null;
    }
    else {
      if (initObj.hasOwnProperty('pan_angle')) {
        this.pan_angle = initObj.pan_angle
      }
      else {
        this.pan_angle = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ArucoHeadScanFeedback
    // Serialize message field [pan_angle]
    bufferOffset = _serializer.float32(obj.pan_angle, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ArucoHeadScanFeedback
    let len;
    let data = new ArucoHeadScanFeedback(null);
    // Deserialize message field [pan_angle]
    data.pan_angle = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'stretch_demos/ArucoHeadScanFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f8d06c64a9db7a2a34a365c076b315f6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Define a feedback message
    
    # Pan angle of the camera
    float32 pan_angle
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ArucoHeadScanFeedback(null);
    if (msg.pan_angle !== undefined) {
      resolved.pan_angle = msg.pan_angle;
    }
    else {
      resolved.pan_angle = 0.0
    }

    return resolved;
    }
};

module.exports = ArucoHeadScanFeedback;
