
(cl:in-package :asdf)

(defsystem "manipulation-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ExecuteCommand" :depends-on ("_package_ExecuteCommand"))
    (:file "_package_ExecuteCommand" :depends-on ("_package"))
  ))