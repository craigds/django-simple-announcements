
Announcements = {
    // http://www.w3schools.com/JS/js_cookies.asp
    setCookie : function(c_name, value, expiredays) {
        var exdate=new Date();
        exdate.setDate(exdate.getDate()+expiredays);
        document.cookie=c_name+ "=" +escape(value)+
            ((expiredays==null) ? "" : ";expires="+exdate.toUTCString());
    },
    dismiss : function(cookieName, announcementId){
        Announcements.setCookie(cookieName, announcementId, 365);
        document.getElementById('announcements').style.display = 'none';
    }
};
