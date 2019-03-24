function inject(url){
 var head = document.getElementsByTagName('head')[0];
var jq = document.createElement('script');
jq.setAttribute('type', 'module')
jq.src = url;
head.appendChild(jq);

}

inject("https://yoavsp.github.io/dad.js/src/domSpy.js");

class NodeServices{
    getAllPropertyNames(obj) {
        var props = Object.getOwnPropertyNames(obj);
        if (obj.__proto__ != null) {
            return props.concat(this.getAllPropertyNames(obj.__proto__))
        } else {
            return props;
        }
    }

    serialize(obj, exclusions = [], inclusions = []) {
        function notExcluded(n) {
            return !exclusions.filter(v => v.includes(n)).length > 0;
        }

        function included(n) {
            return inclusions.length === 0 || inclusions.includes(n);
        }

        const dict = {}
        this.getAllPropertyNames(obj).filter(included).filter(notExcluded).forEach(n => dict[n] = obj[n]);
        return dict;
    }

    eventToDict(e) {
        var res = {};
        res['nodeUID'] = this.getNodeUniqueId(e.node);
        res['event'] = this.serialize(e.event, ['target']);
        res['at'] = e.at;
        res['isActive'] = document.activeElement == e.node;
        return res;
    }

    getPathTo(element) {
        if (element.tagName == 'HTML')
            return '/HTML[1]';
        if (element === document.body)
            return '/HTML[1]/BODY[1]';

        var ix = 0;
        var siblings = element.parentNode.childNodes;
        for (var i = 0; i < siblings.length; i++) {
            var sibling = siblings[i];
            if (sibling === element)
                return getPathTo(element.parentNode) + '/' + element.tagName + '[' + (ix + 1) + ']';
            if (sibling.nodeType === 1 && sibling.tagName === element.tagName)
                ix++;
        }
    }

}

const nodeServices = new NodeServices();

const handler = mutation => {
    console.log('Yoav Hagevgever!!!! and: ' + nodeServices.serialize(mutation));
};
//import {Crawler} from './domSpy.js';
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}



async function start(){
    await sleep(5000);
    const spy = new Crawler(handler);
}

start();