'''
test_robots_reader.py

Copyright 2012 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''

from ..helper import PluginTest, PluginConfig

class TestRobots(PluginTest):
    
    target_url = 'http://moth/'
    
    _run_configs = {
        'cfg': {
            'target': target_url,
            'plugins': {'discovery': (PluginConfig('robotsReader'),)}
            }
        }
    
    def test_robots(self):
        cfg = self._run_configs['cfg']
        self._scan(cfg['target'], cfg['plugins'])
        
        urls = self.kb.getData('urls', 'url_objects')
        
        self.assertEqual( len(urls), 5, urls )
        
        hidden_url = 'http://moth/hidden/'
        
        for url in urls:
            if url.url_string == hidden_url:
                self.assertTrue( True )
                break
        else:
            self.assertTrue( False )
