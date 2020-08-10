cmake_minimum_required( VERSION 3.5 )
PROJECT( my_first_comp )

SET(RC_COMPONENT_PATH ${CMAKE_CURRENT_SOURCE_DIR} CACHE STRING "component base path" FORCE)
SET(RC_COMPONENT_DEVEL_PATH "${CMAKE_CURRENT_SOURCE_DIR}" CACHE STRING "component binary path" FORCE)
#SET(RC_COMPONENT_DEVEL_PATH "${WORKSPACE_PATH}/devel"  CACHE STRING "component binary path")
SET(RC_COMPONENT_INSTALL_PATH "/opt/robocomp" CACHE STRING "component install path")

#commented as now devel is merged into source space
#get_filename_component( COMPONENT_NAME ${CMAKE_CURRENT_SOURCE_DIR} DIRECTORY)
#STRING(REPLACE "${COMPONENT_NAME}/" " " COMPONENT_NAME  ${RC_COMPONENT_PATH})
#STRING(STRIP ${COMPONENT_NAME} COMPONENT_NAME)
#SET(COMPONENT_NAME ${COMPONENT_NAME} CACHE STRING "component name" FORCE)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
	"msg/ShortVector.msg"
	"msg/TData.msg"
	"msg/LaserConfData.msg"
	"msg/TBaseState.msg"
	"msg/TLaserData.msg"
	"srv/GetLaserAndBStateData.srv"
	"srv/GetLaserData.srv"
	"srv/GetLaserConfData.srv"
)

ament_export_dependencies (rosidl_default_runtime)

SUBDIRS( src )

INSTALL(FILES etc/config DESTINATION ${RC_COMPONENT_INSTALL_PATH}/etc-default/ RENAME MyFirstComp.conf )

#ADD_CUSTOM_TARGET(doc doxygen Doxyfile)
#ADD_CUSTOM_TARGET(installdoc mkdir -p ${RC_COMPONENT_INSTALL_PATH}/doc COMMAND cp -R doc/html ${RC_COMPONENT_INSTALL_PATH}/doc/MyFirstComp )

ament_package()
