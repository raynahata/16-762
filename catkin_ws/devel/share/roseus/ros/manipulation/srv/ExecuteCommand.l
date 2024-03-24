;; Auto-generated. Do not edit!


(when (boundp 'manipulation::ExecuteCommand)
  (if (not (find-package "MANIPULATION"))
    (make-package "MANIPULATION"))
  (shadow 'ExecuteCommand (find-package "MANIPULATION")))
(unless (find-package "MANIPULATION::EXECUTECOMMAND")
  (make-package "MANIPULATION::EXECUTECOMMAND"))
(unless (find-package "MANIPULATION::EXECUTECOMMANDREQUEST")
  (make-package "MANIPULATION::EXECUTECOMMANDREQUEST"))
(unless (find-package "MANIPULATION::EXECUTECOMMANDRESPONSE")
  (make-package "MANIPULATION::EXECUTECOMMANDRESPONSE"))

(in-package "ROS")





(defclass manipulation::ExecuteCommandRequest
  :super ros::object
  :slots (_command ))

(defmethod manipulation::ExecuteCommandRequest
  (:init
   (&key
    ((:command __command) "")
    )
   (send-super :init)
   (setq _command (string __command))
   self)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:serialization-length
   ()
   (+
    ;; string _command
    4 (length _command)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass manipulation::ExecuteCommandResponse
  :super ros::object
  :slots ())

(defmethod manipulation::ExecuteCommandResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass manipulation::ExecuteCommand
  :super ros::object
  :slots ())

(setf (get manipulation::ExecuteCommand :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get manipulation::ExecuteCommand :datatype-) "manipulation/ExecuteCommand")
(setf (get manipulation::ExecuteCommand :request) manipulation::ExecuteCommandRequest)
(setf (get manipulation::ExecuteCommand :response) manipulation::ExecuteCommandResponse)

(defmethod manipulation::ExecuteCommandRequest
  (:response () (instance manipulation::ExecuteCommandResponse :init)))

(setf (get manipulation::ExecuteCommandRequest :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get manipulation::ExecuteCommandRequest :datatype-) "manipulation/ExecuteCommandRequest")
(setf (get manipulation::ExecuteCommandRequest :definition-)
      "# ExecuteCommand.srv
string command
---

")

(setf (get manipulation::ExecuteCommandResponse :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get manipulation::ExecuteCommandResponse :datatype-) "manipulation/ExecuteCommandResponse")
(setf (get manipulation::ExecuteCommandResponse :definition-)
      "# ExecuteCommand.srv
string command
---

")



(provide :manipulation/ExecuteCommand "cba5e21e920a3a2b7b375cb65b64cdea")


