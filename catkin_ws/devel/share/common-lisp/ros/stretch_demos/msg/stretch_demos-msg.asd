
(cl:in-package :asdf)

(defsystem "stretch_demos-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ArucoHeadScanAction" :depends-on ("_package_ArucoHeadScanAction"))
    (:file "_package_ArucoHeadScanAction" :depends-on ("_package"))
    (:file "ArucoHeadScanActionFeedback" :depends-on ("_package_ArucoHeadScanActionFeedback"))
    (:file "_package_ArucoHeadScanActionFeedback" :depends-on ("_package"))
    (:file "ArucoHeadScanActionGoal" :depends-on ("_package_ArucoHeadScanActionGoal"))
    (:file "_package_ArucoHeadScanActionGoal" :depends-on ("_package"))
    (:file "ArucoHeadScanActionResult" :depends-on ("_package_ArucoHeadScanActionResult"))
    (:file "_package_ArucoHeadScanActionResult" :depends-on ("_package"))
    (:file "ArucoHeadScanFeedback" :depends-on ("_package_ArucoHeadScanFeedback"))
    (:file "_package_ArucoHeadScanFeedback" :depends-on ("_package"))
    (:file "ArucoHeadScanGoal" :depends-on ("_package_ArucoHeadScanGoal"))
    (:file "_package_ArucoHeadScanGoal" :depends-on ("_package"))
    (:file "ArucoHeadScanResult" :depends-on ("_package_ArucoHeadScanResult"))
    (:file "_package_ArucoHeadScanResult" :depends-on ("_package"))
    (:file "VisualServoAction" :depends-on ("_package_VisualServoAction"))
    (:file "_package_VisualServoAction" :depends-on ("_package"))
    (:file "VisualServoActionFeedback" :depends-on ("_package_VisualServoActionFeedback"))
    (:file "_package_VisualServoActionFeedback" :depends-on ("_package"))
    (:file "VisualServoActionGoal" :depends-on ("_package_VisualServoActionGoal"))
    (:file "_package_VisualServoActionGoal" :depends-on ("_package"))
    (:file "VisualServoActionResult" :depends-on ("_package_VisualServoActionResult"))
    (:file "_package_VisualServoActionResult" :depends-on ("_package"))
    (:file "VisualServoFeedback" :depends-on ("_package_VisualServoFeedback"))
    (:file "_package_VisualServoFeedback" :depends-on ("_package"))
    (:file "VisualServoGoal" :depends-on ("_package_VisualServoGoal"))
    (:file "_package_VisualServoGoal" :depends-on ("_package"))
    (:file "VisualServoResult" :depends-on ("_package_VisualServoResult"))
    (:file "_package_VisualServoResult" :depends-on ("_package"))
  ))