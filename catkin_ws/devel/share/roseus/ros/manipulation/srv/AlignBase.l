;; Auto-generated. Do not edit!


(when (boundp 'manipulation::AlignBase)
  (if (not (find-package "MANIPULATION"))
    (make-package "MANIPULATION"))
  (shadow 'AlignBase (find-package "MANIPULATION")))
(unless (find-package "MANIPULATION::ALIGNBASE")
  (make-package "MANIPULATION::ALIGNBASE"))
(unless (find-package "MANIPULATION::ALIGNBASEREQUEST")
  (make-package "MANIPULATION::ALIGNBASEREQUEST"))
(unless (find-package "MANIPULATION::ALIGNBASERESPONSE")
  (make-package "MANIPULATION::ALIGNBASERESPONSE"))

(in-package "ROS")





(defclass manipulation::AlignBaseRequest
  :super ros::object
  :slots (_location ))

(defmethod manipulation::AlignBaseRequest
  (:init
   (&key
    ((:location __location) "")
    )
   (send-super :init)
   (setq _location (string __location))
   self)
  (:location
   (&optional __location)
   (if __location (setq _location __location)) _location)
  (:serialization-length
   ()
   (+
    ;; string _location
    4 (length _location)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _location
       (write-long (length _location) s) (princ _location s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _location
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _location (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass manipulation::AlignBaseResponse
  :super ros::object
  :slots (_success ))

(defmethod manipulation::AlignBaseResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass manipulation::AlignBase
  :super ros::object
  :slots ())

(setf (get manipulation::AlignBase :md5sum-) "210b5d0e3d60fa9dac834d90f73f9337")
(setf (get manipulation::AlignBase :datatype-) "manipulation/AlignBase")
(setf (get manipulation::AlignBase :request) manipulation::AlignBaseRequest)
(setf (get manipulation::AlignBase :response) manipulation::AlignBaseResponse)

(defmethod manipulation::AlignBaseRequest
  (:response () (instance manipulation::AlignBaseResponse :init)))

(setf (get manipulation::AlignBaseRequest :md5sum-) "210b5d0e3d60fa9dac834d90f73f9337")
(setf (get manipulation::AlignBaseRequest :datatype-) "manipulation/AlignBaseRequest")
(setf (get manipulation::AlignBaseRequest :definition-)
      "# AlignBase.srv
string location
---
bool success
")

(setf (get manipulation::AlignBaseResponse :md5sum-) "210b5d0e3d60fa9dac834d90f73f9337")
(setf (get manipulation::AlignBaseResponse :datatype-) "manipulation/AlignBaseResponse")
(setf (get manipulation::AlignBaseResponse :definition-)
      "# AlignBase.srv
string location
---
bool success
")



(provide :manipulation/AlignBase "210b5d0e3d60fa9dac834d90f73f9337")


