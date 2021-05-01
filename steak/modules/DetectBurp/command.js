var img=new Image();
img.onerror=function ()
{
    if (!img) return;
    img=undefined;
    sendDataBack({'burp':true},'<steak>taskid</steak>')
};
img.onload=img.onerror;
img.src='http://burp:8080';
setTimeout(function() {
    if (!img) return;
    img = undefined;
    sendDataBack({'burp':false},'<steak>taskid</steak>')
    },1000);