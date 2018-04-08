
function traverseDOM(func){
    Array.prototype.slice.call(document.getElementsByTagName('*')).forEach(func)
}

function addClickListener(element){
    element => {element.addEventListener('click', function(event){
        var elementRef = {location: getLocation(element),
        rectangle: getRectangle(element),
        shadow: createShadow(element),

    })}
}