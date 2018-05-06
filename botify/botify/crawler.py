import re
from typing import Any
from logging import getLogger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class Crawler(object):

    def __init__(self, url = 'http://google.com') -> None:
        self.logger = getLogger(__name__)
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = Chrome(chrome_options=options)
        #self.driver = Chrome()
        try:
            self._assert_url(url)

            self.driver.get(url)
            self.driver.maximize_window()

        except Exception as e:
            self.logger.exception(e)
            self.driver.quit()

    def _assert_url(self, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        assert regex.match(url) is not None

    def inject(self):
        # self.driver.execute_script(
        #     "Array.prototype.slice.call(document.getElementsByTagName('*')).forEach(a=> {a.addEventListener('click', function(event){ if (a == document.activeElement){alert(a.tagName);}})})")
        self.driver.execute_script("""function getAllElements(){
  return Array.prototype.slice.call(document.getElementsByTagName('*'));
}
window.events = [];
function registerListener(listenerName, node){
  node.addEventListener(listenerName, function(event){ events.push({'at': new Date(), 'node':node, 'event':event, 
  'isActive': document.activeElement == node});});
}
function getAllPropertyNames(obj){
    var props = Object.getOwnPropertyNames(obj);
    if(obj.__proto__ != null){
        return props.concat(getAllPropertyNames(obj.__proto__))
    }
    else{
    return props;
    }
}

function toDict(obj){
    dict = {}
    getAllPropertyNames(obj).filter(name => name.includes('__') == false).forEach(n => dict[n]=obj[n]);
    return dict;
}

function eventToDict(e){
    var res={}; 
    res['node']=toDict(e.node); 
    res['event']=toDict(e.event); 
    res['at'] = e.at;
    return res;
}
var head = document.getElementsByTagName('head')[0];
var jq = document.createElement('script');
jq.src="https://code.jquery.com/jquery-3.3.1.min.js";
head.appendChild(jq);
window.getAllElements = getAllElements;
window.getAllPropertyNames = getAllPropertyNames;
window.toDict = toDict;
window.eventToDict = eventToDict;
getAllElements().forEach(el=>registerListener('click',el))
getAllElements().forEach(el=>registerListener('change',el))

""")

    def quit(self):
        self.driver.quit()