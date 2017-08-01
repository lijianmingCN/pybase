# -*- coding: UTF-8 -*-
#13.2. ConfigParser — Configuration file parser

import ConfigParser
#An example of writing to a configuration file:
config = ConfigParser.ConfigParser()
config.add_section('db')
config.set('db', 'an_int', '15')
config.set('db', 'a_bool', 'true')
config.set('db', 'a_float', '3.1415')
config.set('db', 'baz', 'fun')
config.set('db', 'bar', 'Python')
with open('example.cfg', 'wb') as configfile:
    config.write(configfile)

#An example of reading the configuration file again:
config = ConfigParser.ConfigParser()
config.read('example.cfg')
print config.sections()
print config.items('db')
print config.get('db', 'an_int')



