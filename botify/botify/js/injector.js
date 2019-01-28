function inject(url){
 var head = document.getElementsByTagName('head')[0];
var jq = document.createElement('script');
jq.src = url;
head.appendChild(jq);
}

inject("https://yoavsp.github.io/dad.js/src/domSpy.js");
const spy = new Spy();
