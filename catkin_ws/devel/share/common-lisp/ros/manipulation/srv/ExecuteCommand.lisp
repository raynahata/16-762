; Auto-generated. Do not edit!


(cl:in-package manipulation-srv)


;//! \htmlinclude ExecuteCommand-request.msg.html

(cl:defclass <ExecuteCommand-request> (roslisp-msg-protocol:ros-message)
  ((command
    :reader command
    :initarg :command
    :type cl:string
    :initform ""))
)

(cl:defclass ExecuteCommand-request (<ExecuteCommand-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExecuteCommand-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExecuteCommand-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name manipulation-srv:<ExecuteCommand-request> is deprecated: use manipulation-srv:ExecuteCommand-request instead.")))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <ExecuteCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader manipulation-srv:command-val is deprecated.  Use manipulation-srv:command instead.")
  (command m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExecuteCommand-request>) ostream)
  "Serializes a message object of type '<ExecuteCommand-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExecuteCommand-request>) istream)
  "Deserializes a message object of type '<ExecuteCommand-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExecuteCommand-request>)))
  "Returns string type for a service object of type '<ExecuteCommand-request>"
  "manipulation/ExecuteCommandRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteCommand-request)))
  "Returns string type for a service object of type 'ExecuteCommand-request"
  "manipulation/ExecuteCommandRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExecuteCommand-request>)))
  "Returns md5sum for a message object of type '<ExecuteCommand-request>"
  "cba5e21e920a3a2b7b375cb65b64cdea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExecuteCommand-request)))
  "Returns md5sum for a message object of type 'ExecuteCommand-request"
  "cba5e21e920a3a2b7b375cb65b64cdea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExecuteCommand-request>)))
  "Returns full string definition for message of type '<ExecuteCommand-request>"
  (cl:format cl:nil "# ExecuteCommand.srv~%string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExecuteCommand-request)))
  "Returns full string definition for message of type 'ExecuteCommand-request"
  (cl:format cl:nil "# ExecuteCommand.srv~%string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExecuteCommand-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'command))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExecuteCommand-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ExecuteCommand-request
    (cl:cons ':command (command msg))
))
;//! \htmlinclude ExecuteCommand-response.msg.html

(cl:defclass <ExecuteCommand-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ExecuteCommand-response (<ExecuteCommand-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExecuteCommand-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExecuteCommand-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name manipulation-srv:<ExecuteCommand-response> is deprecated: use manipulation-srv:ExecuteCommand-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExecuteCommand-response>) ostream)
  "Serializes a message object of type '<ExecuteCommand-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExecuteCommand-response>) istream)
  "Deserializes a message object of type '<ExecuteCommand-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExecuteCommand-response>)))
  "Returns string type for a service object of type '<ExecuteCommand-response>"
  "manipulation/ExecuteCommandResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteCommand-response)))
  "Returns string type for a service object of type 'ExecuteCommand-response"
  "manipulation/ExecuteCommandResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExecuteCommand-response>)))
  "Returns md5sum for a message object of type '<ExecuteCommand-response>"
  "cba5e21e920a3a2b7b375cb65b64cdea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExecuteCommand-response)))
  "Returns md5sum for a message object of type 'ExecuteCommand-response"
  "cba5e21e920a3a2b7b375cb65b64cdea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExecuteCommand-response>)))
  "Returns full string definition for message of type '<ExecuteCommand-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExecuteCommand-response)))
  "Returns full string definition for message of type 'ExecuteCommand-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExecuteCommand-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExecuteCommand-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ExecuteCommand-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ExecuteCommand)))
  'ExecuteCommand-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ExecuteCommand)))
  'ExecuteCommand-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExecuteCommand)))
  "Returns string type for a service object of type '<ExecuteCommand>"
  "manipulation/ExecuteCommand")