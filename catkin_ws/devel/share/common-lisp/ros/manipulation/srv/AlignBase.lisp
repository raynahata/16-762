; Auto-generated. Do not edit!


(cl:in-package manipulation-srv)


;//! \htmlinclude AlignBase-request.msg.html

(cl:defclass <AlignBase-request> (roslisp-msg-protocol:ros-message)
  ((location
    :reader location
    :initarg :location
    :type cl:string
    :initform ""))
)

(cl:defclass AlignBase-request (<AlignBase-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AlignBase-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AlignBase-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name manipulation-srv:<AlignBase-request> is deprecated: use manipulation-srv:AlignBase-request instead.")))

(cl:ensure-generic-function 'location-val :lambda-list '(m))
(cl:defmethod location-val ((m <AlignBase-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader manipulation-srv:location-val is deprecated.  Use manipulation-srv:location instead.")
  (location m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AlignBase-request>) ostream)
  "Serializes a message object of type '<AlignBase-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'location))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'location))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AlignBase-request>) istream)
  "Deserializes a message object of type '<AlignBase-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'location) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'location) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AlignBase-request>)))
  "Returns string type for a service object of type '<AlignBase-request>"
  "manipulation/AlignBaseRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AlignBase-request)))
  "Returns string type for a service object of type 'AlignBase-request"
  "manipulation/AlignBaseRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AlignBase-request>)))
  "Returns md5sum for a message object of type '<AlignBase-request>"
  "210b5d0e3d60fa9dac834d90f73f9337")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AlignBase-request)))
  "Returns md5sum for a message object of type 'AlignBase-request"
  "210b5d0e3d60fa9dac834d90f73f9337")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AlignBase-request>)))
  "Returns full string definition for message of type '<AlignBase-request>"
  (cl:format cl:nil "# AlignBase.srv~%string location~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AlignBase-request)))
  "Returns full string definition for message of type 'AlignBase-request"
  (cl:format cl:nil "# AlignBase.srv~%string location~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AlignBase-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'location))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AlignBase-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AlignBase-request
    (cl:cons ':location (location msg))
))
;//! \htmlinclude AlignBase-response.msg.html

(cl:defclass <AlignBase-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass AlignBase-response (<AlignBase-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AlignBase-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AlignBase-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name manipulation-srv:<AlignBase-response> is deprecated: use manipulation-srv:AlignBase-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <AlignBase-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader manipulation-srv:success-val is deprecated.  Use manipulation-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AlignBase-response>) ostream)
  "Serializes a message object of type '<AlignBase-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AlignBase-response>) istream)
  "Deserializes a message object of type '<AlignBase-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AlignBase-response>)))
  "Returns string type for a service object of type '<AlignBase-response>"
  "manipulation/AlignBaseResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AlignBase-response)))
  "Returns string type for a service object of type 'AlignBase-response"
  "manipulation/AlignBaseResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AlignBase-response>)))
  "Returns md5sum for a message object of type '<AlignBase-response>"
  "210b5d0e3d60fa9dac834d90f73f9337")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AlignBase-response)))
  "Returns md5sum for a message object of type 'AlignBase-response"
  "210b5d0e3d60fa9dac834d90f73f9337")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AlignBase-response>)))
  "Returns full string definition for message of type '<AlignBase-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AlignBase-response)))
  "Returns full string definition for message of type 'AlignBase-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AlignBase-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AlignBase-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AlignBase-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AlignBase)))
  'AlignBase-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AlignBase)))
  'AlignBase-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AlignBase)))
  "Returns string type for a service object of type '<AlignBase>"
  "manipulation/AlignBase")