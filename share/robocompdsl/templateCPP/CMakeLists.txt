[[[cog
import sys
sys.path.append('/home/ksakash/archives/robocomp/python')

import cog
import stringcase as sc

includeDirectories = theIDSLPaths.split('#')


def A():
	cog.out('<@@<')
def Z():
	cog.out('>@@>')
def TAB():
	cog.out('<TABHERE>')
def SPACE(i=0):
	s = ''
	if i>0:
		s = str(i)
	cog.out('<S'+s+'>')

from dsl_parsers.dsl_factory import DSLFactory
from dsl_parsers.parsing_utils import isPub, IDSLPool

includeDirectories = theIDSLPaths.split('#')
component = DSLFactory().from_file(theCDSL, include_directories=includeDirectories)
pool = IDSLPool(theIDSLs, includeDirectories)

]]]
[[[end]]]
cmake_minimum_required( VERSION 3.5 )
PROJECT(
[[[cog
A()
cog.out(' ' + sc.snakecase(component['name']))
Z()
]]]
[[[end]]]
 )

SET(RC_COMPONENT_PATH ${CMAKE_CURRENT_SOURCE_DIR} CACHE STRING "component base path" FORCE)
SET(RC_COMPONENT_DEVEL_PATH "${CMAKE_CURRENT_SOURCE_DIR}" CACHE STRING "component binary path" FORCE)
#SET(RC_COMPONENT_DEVEL_PATH "${WORKSPACE_PATH}/devel"  CACHE STRING "component binary path")
SET(RC_COMPONENT_INSTALL_PATH "/opt/robocomp" CACHE STRING "component install path")

#commented as now devel is merged into source space
#get_filename_component( COMPONENT_NAME ${CMAKE_CURRENT_SOURCE_DIR} DIRECTORY)
#STRING(REPLACE "${COMPONENT_NAME}/" " " COMPONENT_NAME  ${RC_COMPONENT_PATH})
#STRING(STRIP ${COMPONENT_NAME} COMPONENT_NAME)
#SET(COMPONENT_NAME ${COMPONENT_NAME} CACHE STRING "component name" FORCE)

[[[cog

def getMsgList (module):
	msgList = []

	for t in module['types']:
		if t['type'] != 'dictionary':
			msgList.append(sc.pascalcase(t['name'].split('::')[-1]))

	for interface in module['interfaces']:
		for method in interface['methods']:
			m = interface['methods'][method]
			if isPub (m):
				p = m['params'][0]
				if p['type'] in ('float','int'):
					pass
				elif p['type'] in ('uint8','uint16','uint32','uint64'):
					pass
				elif p['type'] in rosTypes:
					pass
				elif '::' in p['type']:
					msgList.append(sc.pascalcase(p['type'].split('::')[-1]))
				else:
					msgList.append(sc.pascalcase(p['type']))

	return msgList

if component['usingROS2']:
	cog.outl("find_package(ament_cmake REQUIRED)")
	cog.outl("find_package(rosidl_default_generators REQUIRED)")
	cog.outl("rosidl_generate_interfaces(${PROJECT_NAME}")
	for interface in component['publishes'] + component['subscribesTo'] + component['implements'] + component['requires']:
		interface = interface[0]
		module = pool.moduleProviding(interface)
		msgList = getMsgList (module)
		# print ("msgList", msgList)
		for msg in msgList:
			cog.outl("<TABHERE>\"msg/"+msg+".msg\"")
	cog.outl(")")

	cog.outl("ament_export_dependencies (rosidl_default_runtime)")

]]]
[[[end]]]

SUBDIRS( src )

INSTALL(FILES etc/config DESTINATION ${RC_COMPONENT_INSTALL_PATH}/etc-default/ RENAME
[[[cog
A()
cog.out(' ' + component['name'])
Z()
]]]
[[[end]]]
.conf )

#ADD_CUSTOM_TARGET(doc doxygen Doxyfile)
#ADD_CUSTOM_TARGET(installdoc mkdir -p ${RC_COMPONENT_INSTALL_PATH}/doc COMMAND cp -R doc/html ${RC_COMPONENT_INSTALL_PATH}/doc/
[[[cog
A()
cog.out( component['name'] + ' ')
Z()
]]]
[[[end]]]
)

[[[cog
if component['usingROS2']:
	cog.outl("ament_package()")
]]]
[[[end]]]
