[[[cog

import sys
sys.path.append('../../../python')

import stringcase as sc
import cog
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

ice2rosMap = dict()
ice2rosMap['bool'] = 'bool'
ice2rosMap['byte'] = 'int8'
ice2rosMap['short'] = 'int16'
ice2rosMap['int'] = 'int32'
ice2rosMap['long'] = 'int64'
ice2rosMap['float'] = 'float32'
ice2rosMap['double'] = 'float64'
ice2rosMap['string'] = 'string'

from dsl_parsers.dsl_factory import DSLFactory
idsl = DSLFactory().from_file(theIDSL)

for t in idsl['types']:
    if t['name'] == structName:
        type = t['type']
        if type == 'sequence':
            if t['typeSequence'] in ice2rosMap:
                if rostype == 'ros2':
                    cog.outl (ice2rosMap[t['typeSequence']]+"[] "+sc.snakecase(t['name']))
                else:
                    cog.outl (ice2rosMap[t['typeSequence']]+"[] "+t['name'])
            else:
                if rostype == 'ros2':
                    cog.outl (sc.pascalcase(t['typeSequence'].split('/')[-1])+"[] "+sc.snakecase(t['name']))
                else:
                    cog.outl (t['typeSequence'].replace('/', 'ROS/')+"[] "+t['name'])
        elif type == 'struct':
            for i in t['structIdentifiers']:
                if i['type'] in ice2rosMap:
                    if rostype == 'ros2':
                        cog.outl (ice2rosMap[i['type']]+" "+sc.snakecase(i['identifier']))
                    else:
                        cog.outl (ice2rosMap[i['type']]+" "+i['identifier'])
                elif i['type'] == 'sequence':
                    if i['typeSequence'] in ice2rosMap:
                        if rostype == 'ros2':
                            cog.outl (ice2rosMap[i['typeSequence']]+"[] "+sc.snakecase(i['identifier']))
                        else:
                            cog.outl (ice2rosMap[i['typeSequence']]+"[] "+i['identifier'])
                    else:
                        if rostype == 'ros2':
                            cog.outl (sc.pascalcase(i['typeSequence'].split('/')[-1])+"[] "+sc.snakecase(i['identifier']))
                        else:
                            cog.outl (i['typeSequence'].replace('/', 'ROS/')+"[] "+i['identifier'])
                else:
                    if rostype == 'ros2':
                        cog.outl (sc.pascalcase(i['type'].split('/')[-1])+" "+sc.snakecase(i['identifier']))
                    else:
                        cog.outl (i['type'].replace('/', 'ROS/')+" "+i['identifier'])

]]]
[[[end]]]
