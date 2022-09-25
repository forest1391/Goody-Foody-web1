function myDate(){
document.getElementById('mToday').innerHTML = Today;
    }

Today = new Date();
yy=Today.getFullYear();
mm=Today.getMonth()+1;
dd=Today.getDate();
h=Today.getHours();
m=Today.getMinutes();
s=Today.getSeconds();　
function mToday(){
	document.getElementById("mday").innerHTML = yy+"-"+mm+"-"+dd+'的  '+h+'時'+m+'分'+s+'秒';
    }
