#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/hello-robot/catkin_ws/src/stretch_ros/stretch_demos"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/hello-robot/catkin_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/hello-robot/catkin_ws/install/lib/python3/dist-packages:/home/hello-robot/catkin_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/hello-robot/catkin_ws/build" \
    "/usr/bin/python3" \
    "/home/hello-robot/catkin_ws/src/stretch_ros/stretch_demos/setup.py" \
     \
    build --build-base "/home/hello-robot/catkin_ws/build/stretch_ros/stretch_demos" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/hello-robot/catkin_ws/install" --install-scripts="/home/hello-robot/catkin_ws/install/bin"
