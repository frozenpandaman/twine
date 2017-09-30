# macros

REPLACE_MACRO_SET = """(function(){version.extensions.replaceMacrosCombined={major:1,minor:1,revision:7};var nullobj={handler:function(){}};function showVer(n,notrans){if(!n){return;}n.innerHTML="";
new Wikifier(n,n.tweecode);n.setAttribute("data-enabled","true");n.style.display="inline";n.classList.remove("revision-span-out");if(!notrans){n.classList.add("revision-span-in");
if(n.timeout){clearTimeout(n.timeout);}n.timeout=setTimeout(function(){n.classList.remove("revision-span-in");n=null;},20);}}function hideVer(n,notrans){if(!n){return;
}n.setAttribute("data-enabled","false");n.classList.remove("revision-span-in");if(n.timeout){clearTimeout(n.timeout);}if(!notrans){n.classList.add("revision-span-out");
n.timeout=setTimeout(function(){if(n.getAttribute("data-enabled")=="false"){n.classList.remove("revision-span-out");n.style.display="none";n.innerHTML="";}n=null;
},1000);}else{n.style.display="none";n.innerHTML="";n=null;}}function tagcontents(b,starttags,desttags,endtags,k){var l=0,c="",tg,a,i;function tagfound(i,e,endtag){for(var j=0;
j<e.length;j++){if(a.indexOf("<<"+e[j]+(endtag?">>":""),i)==i){return e[j];}}}a=b.source.slice(k);for(i=0;i<a.length;i++){if(tg=tagfound(i,starttags)){l++;}else{if((tg=tagfound(i,desttags,true))&&l==0){b.nextMatch=k+i+tg.length+4;
return[c,tg];}else{if(tg=tagfound(i,endtags,true)){l--;if(l<0){return null;}}}}c+=a.charAt(i);}return null;}var begintags=[];var endtags=[];function revisionSpanHandler(g,e,f,b){var k=b.source.indexOf(">>",b.matchStart)+2,vsns=[],vtype=e,flen=f.length,becomes,c,cn,m,h,vsn;
function mkspan(vtype){h=insertElement(m,"span",null,"revision-span "+vtype);h.setAttribute("data-enabled",false);h.style.display="none";h.tweecode="";return h;}if(this.shorthand&&flen){while(f.length>0){vsns.push([f.shift(),(this.flavour=="insert"?"gains":"becomes")]);
}}else{if(this.flavour=="insert"||(this.flavour=="continue"&&this.trigger=="time")){vsns.push(["","becomes"]);}}if(this.flavour=="continue"&&flen){b.nextMatch=k+b.source.slice(k).length;
vsns.push([b.source.slice(k),vtype]);}else{becomes=["becomes","gains"];c=tagcontents(b,begintags,becomes.concat(endtags),endtags,k);if(c&&endtags.indexOf(c[1])==-1){while(c){vsns.push(c);
c=tagcontents(b,begintags,becomes,endtags,b.nextMatch);}c=tagcontents(b,begintags,["end"+e],endtags,b.nextMatch);}if(!c){throwError(g,"can't find matching end"+e);
return;}vsns.push(c);if(this.flavour=="continue"){k=b.nextMatch;b.nextMatch=k+b.source.slice(k).length;vsns.push([b.source.slice(k),""]);}}if(this.flavour=="remove"){vsns.push(["","becomes"]);
}cn=0;m=insertElement(g,"span",null,e);m.setAttribute("data-flavour",this.flavour);h=mkspan("initial");vsn=vsns.shift();h.tweecode=vsn[0];showVer(h,true);while(vsns.length>0){if(vsn){vtype=vsn[1];
}vsn=vsns.shift();h=mkspan(vtype);h.tweecode=vsn[0];}if(typeof this.setup=="function"){this.setup(m,g,f);}}function quantity(m){return(m.children.length-1)+(m.getAttribute("data-flavour")=="remove");
}function revisionSetup(m,g,f){m.className+=" "+f[0].replace(" ","_");}function keySetup(m,g,f){var key=f[0];m.setEventListener("keydown",function l(e){var done=!revise("revise",m);
if(done){m.removeEventListener("keydown",l);}});}function timeSetup(m,g,f){function cssTimeUnit(s){if(typeof s=="string"){if(s.slice(-2).toLowerCase()=="ms"){return Number(s.slice(0,-2))||0;
}else{if(s.slice(-1).toLowerCase()=="s"){return Number(s.slice(0,-1))*1000||0;}}}throwError(g,s+" isn't a CSS time unit");return 0;}var tm=cssTimeUnit(f[0]);var s=state.history[0].passage.title;
setTimeout(function timefn(){if(state.history[0].passage.title==s){var done=!revise("revise",m);if(!done){setTimeout(timefn,tm);}}},tm);}function hoverSetup(m){var fn,noMouseEnter=(document.head.onmouseenter!==null),m1=m.children[0],m2=m.children[1],gains=m2.className.indexOf("gains")>-1;
if(!m1||!m2){return;}m1.onmouseenter=function(e){var efp=document.elementFromPoint(e.clientX,e.clientY);while(efp&&efp!==this){efp=efp.parentNode;}if(!efp){return;
}if(this.getAttribute("data-enabled")!="false"){revise("revise",this.parentNode);}};m2.onmouseleave=function(e){var efp=document.elementFromPoint(e.clientX,e.clientY);
while(efp&&efp!==this){efp=efp.parentNode;}if(efp){return;}if(this.getAttribute("data-enabled")!="false"){revise("revert",this.parentNode);}};if(gains){m1.onmouseleave=m2.onmouseleave;
}if(noMouseEnter){fn=function(n){return function(e){if(!event.relatedTarget||(event.relatedTarget!=this&&!(this.compareDocumentPosition(event.relatedTarget)&Node.DOCUMENT_POSITION_CONTAINED_BY))){this[n]();
}};};m1.onmouseover=fn("onmouseenter");m2.onmouseout=fn("onmouseleave");if(gains){m1.onmouseout=m2.onmouseout;}}m=null;}function mouseSetup(m){var evt=(document.head.onmouseenter===null?"onmouseenter":"onmouseover");
m[evt]=function(){var done=!revise("revise",this);if(done){this[evt]=null;}};m=null;}function linkSetup(m,g,f){var l=Wikifier.createInternalLink(),p=m.parentNode;
l.className="internalLink replaceLink";p.insertBefore(l,m);l.insertBefore(m,null);l.onclick=function(){var p,done=false;if(m&&m.parentNode==this){done=!revise("revise",m);
scrollWindowTo(m);}if(done){this.parentNode.insertBefore(m,this);this.parentNode.removeChild(this);}};l=null;}function visitedSetup(m,g,f){var i,done,shv=state.history[0].variables,os="once seen",d=(m.firstChild&&(this.flavour=="insert"?m.firstChild.nextSibling:m.firstChild).tweecode);
shv[os]=shv[os]||{};if(d&&!shv[os].hasOwnProperty(d)){shv[os][d]=1;}else{for(i=shv[os][d];i>0&&!done;i--){done=!revise("revise",m,true);}if(shv[os].hasOwnProperty(d)){shv[os][d]+=1;
}}}[{name:"insert",flavour:"insert",trigger:"link",setup:linkSetup},{name:"timedinsert",flavour:"insert",trigger:"time",setup:timeSetup},{name:"insertion",flavour:"insert",trigger:"revisemacro",setup:revisionSetup},{name:"later",flavour:"insert",trigger:"visited",setup:visitedSetup},{name:"keyinsert",flavour:"insert",trigger:"key",setup:keySetup},{name:"replace",flavour:"replace",trigger:"link",setup:linkSetup},{name:"timedreplace",flavour:"replace",trigger:"time",setup:timeSetup},{name:"mousereplace",flavour:"replace",trigger:"mouse",setup:mouseSetup},{name:"hoverreplace",flavour:"replace",trigger:"hover",setup:hoverSetup},{name:"revision",flavour:"replace",trigger:"revisemacro",setup:revisionSetup},{name:"keyreplace",flavour:"replace",trigger:"key",setup:keySetup},{name:"timedremove",flavour:"remove",trigger:"time",setup:timeSetup},{name:"mouseremove",flavour:"remove",trigger:"mouse",setup:mouseSetup},{name:"hoverremove",flavour:"remove",trigger:"hover",setup:hoverSetup},{name:"removal",flavour:"remove",trigger:"revisemacro",setup:revisionSetup},{name:"once",flavour:"remove",trigger:"visited",setup:visitedSetup},{name:"keyremove",flavour:"remove",trigger:"key",setup:keySetup},{name:"continue",flavour:"continue",trigger:"link",setup:linkSetup},{name:"timedcontinue",flavour:"continue",trigger:"time",setup:timeSetup},{name:"mousecontinue",flavour:"continue",trigger:"mouse",setup:mouseSetup},{name:"keycontinue",flavour:"continue",trigger:"key",setup:keySetup},{name:"cycle",flavour:"cycle",trigger:"revisemacro",setup:revisionSetup},{name:"mousecycle",flavour:"cycle",trigger:"mouse",setup:mouseSetup},{name:"timedcycle",flavour:"cycle",trigger:"time",setup:timeSetup},{name:"keycycle",flavour:"replace",trigger:"key",setup:keySetup}].forEach(function(e){e.handler=revisionSpanHandler;
e.shorthand=(["link","mouse","hover"].indexOf(e.trigger)>-1);macros[e.name]=e;macros["end"+e.name]=nullobj;begintags.push(e.name);endtags.push("end"+e.name);});function insideDepartingSpan(elem){var r=elem.parentNode;
while(!r.classList.contains("passage")){if(r.classList.contains("revision-span-out")){return true;}r=r.parentNode;}}function reviseAll(rt,rname){var rall=document.querySelectorAll(".passage [data-flavour]."+rname),ret=false;
for(var i=0;i<rall.length;i++){if(!insideDepartingSpan(rall[i])){ret=revise(rt,rall[i])||ret;}}return ret;}function revise(rt,r,notrans){var ind2,curr,next,ind=-1,rev=(rt=="revert"),rnd=(rt.indexOf("random")>-1),fl=r.getAttribute("data-flavour"),rc=r.childNodes,cyc=(fl=="cycle"),rcl=rc.length-1;
function doToGainerSpans(n,fn){for(var k=n-1;k>=0;k--){if(rc[k+1].classList.contains("gains")){fn(rc[k],notrans);}else{break;}}}for(var k=0;k<=rcl;k++){if(rc[k].getAttribute("data-enabled")=="true"){ind=k;
}}if(rev){ind-=1;}curr=(ind>=0?rc[ind]:(cyc?rc[rcl]:null));ind2=ind;if(rnd){ind2=(ind+(Math.floor(Math.random()*rcl)))%rcl;}next=((ind2<rcl)?rc[ind2+1]:(cyc?rc[0]:null));
var docurr=(rev?showVer:hideVer);var donext=(rev?hideVer:showVer);var currfn=function(){if(!(next&&next.classList.contains("gains"))||rnd){docurr(curr,notrans);doToGainerSpans(ind,docurr,notrans);
}};var nextfn=function(){donext(next,notrans);if(rnd){doToGainerSpans(ind2+1,donext,notrans);}};if(!rev){currfn();nextfn();}else{nextfn();currfn();}return(cyc?true:(rev?(ind>0):(ind2<rcl-1)));
}macros.revert=macros.revise=macros.randomise=macros.randomize={handler:function(a,b,c){var l,rev,rname;function disableLink(l){l.style.display="none";}function enableLink(l){l.style.display="inline";
}function updateLink(l){if(l.className.indexOf("random")>-1){enableLink(l);return;}var rall=document.querySelectorAll(".passage [data-flavour]."+rname),cannext,canprev,i,ind,r,fl;
for(i=0;i<rall.length;i++){r=rall[i],fl=r.getAttribute("data-flavour");if(insideDepartingSpan(r)){continue;}if(fl=="cycle"){cannext=canprev=true;}else{if(r.firstChild.getAttribute("data-enabled")==!1+""){canprev=true;
}if(r.lastChild.getAttribute("data-enabled")==!1+""){cannext=true;}}}var can=(l.classList.contains("revert")?canprev:cannext);(can?enableLink:disableLink)(l);}function toggleText(w){w.classList.toggle(rl+"Enabled");
w.classList.toggle(rl+"Disabled");w.style.display=((w.style.display=="none")?"inline":"none");}var rl="reviseLink";if(c.length<2){throwError(a,b+" macro needs 2 parameters");
return;}rname=c.shift().replace(" ","_");l=Wikifier.createInternalLink(a,null);l.className="internalLink "+rl+" "+rl+"_"+rname+" "+b;var v="";var end=false;var out=false;
if(c.length>1&&c[0][0]=="$"){v=c[0].slice(1);c.shift();}switch(c[c.length-1]){case"end":end=true;c.pop();break;case"out":out=true;c.pop();break;}var h=state.history[0].variables;
for(var i=0;i<c.length;i++){var on=(i==Math.max(c.indexOf(h[v]),0));var d=insertElement(null,"span",null,rl+((on)?"En":"Dis")+"abled");if(on){h[v]=c[i];l.setAttribute("data-cycle",i);
}else{d.style.display="none";}insertText(d,c[i]);l.appendChild(d);}l.onclick=function(){reviseAll(b,rname);var t=this.childNodes,u=this.getAttribute("data-cycle")-0,m=t.length,n,lall,i;
if((end||out)&&u>=m-(end?2:1)){if(end){n=this.removeChild(t[u+1]||t[u]);n.className=rl+"End";n.style.display="inline";this.parentNode.replaceChild(n,this);}else{this.parentNode.removeChild(this);
return;}}else{toggleText(t[u]);u=(u+1)%m;if(v){h[v]=c[u];}toggleText(t[u]);this.setAttribute("data-cycle",u);}lall=document.getElementsByClassName(rl+"_"+rname);
for(i=0;i<lall.length;i++){updateLink(lall[i]);}};disableLink(l);setTimeout((function(l){return function(){updateLink(l);};}(l)),1);l=null;}};macros.mouserevise=macros.hoverrevise={handler:function(a,b,c,d){var endtags=["end"+b],evt=(window.onmouseenter===null?"onmouseenter":"onmouseover"),t=tagcontents(d,[b],endtags,endtags,d.source.indexOf(">>",d.matchStart)+2);
if(t){var rname=c[0].replace(" ","_"),h=insertElement(a,"span",null,"hoverrevise hoverrevise_"+rname),f=function(){var done=!reviseAll("revise",rname);if(b!="hoverrevise"&&done){this[evt]=null;
}};new Wikifier(h,t[0]);if(b=="hoverrevise"){h.onmouseover=f;h.onmouseout=function(){reviseAll("revert",rname);};}else{h[evt]=f;}h=null;}}};macros.instantrevise={handler:function(a,b,c,d){reviseAll("revise",c[0].replace(" ","_"));
}};macros.endmouserevise=nullobj;macros.endhoverrevise=nullobj;}());"""

TIMEDGOTO = """version.extensions.timedgotoMacro={major:1,minor:2,revision:0};
macros["goto"]=macros.timedgoto={timer:null,handler:function(a,b,c,d){function cssTimeUnit(s){if(typeof s=="string"){if(s.slice(-2).toLowerCase()=="ms"){return +(s.slice(0,-2))||0
}else{if(s.slice(-1).toLowerCase()=="s"){return +(s.slice(0,-1))*1000||0
}}}throwError(a,s+" isn't a CSS time unit");return 0}var t,d,m,s;
t=c[c.length-1];d=d.fullArgs();m=0;if(b!="goto"){d=d.slice(0,d.lastIndexOf(t));
m=cssTimeUnit(t)}d=eval(Wikifier.parse(d));if(d+""&&state&&state.init){if(macros["goto"].timer){clearTimeout(macros["goto"].timer)
}s=state.history[0].passage.title;macros["goto"].timer=setTimeout(function(){if(state.history[0].passage.title==s){state.display(d,a)
}},m)}}};"""

CYCLINGLINK = """version.extensions.cyclinglinkMacro={major:3,minor:3,revision:0};
macros.cyclinglink={handler:function(a,b,c){var rl="cyclingLink";
function toggleText(w){w.classList.remove("cyclingLinkInit");
w.classList.toggle(rl+"Enabled");w.classList.toggle(rl+"Disabled");
w.style.display=((w.style.display=="none")?"inline":"none")}switch(c[c.length-1]){case"end":var end=true;
c.pop();break;case"out":var out=true;c.pop();break}var v="";if(c.length&&c[0][0]=="$"){v=c[0].slice(1);
c.shift()}var h=state.history[0].variables;if(out&&h[v]===""){return
}var l=Wikifier.createInternalLink(a,null);l.className="internalLink cyclingLink";
l.setAttribute("data-cycle",0);for(var i=0;i<c.length;i++){var on=(i==Math.max(c.indexOf(h[v]),0));
var d=insertElement(null,"span",null,"cyclingLinkInit cyclingLink"+((on)?"En":"Dis")+"abled");
if(on){h[v]=c[i];l.setAttribute("data-cycle",i)}else{d.style.display="none"
}insertText(d,c[i]);if(on&&end&&i==c.length-1){l.parentNode.replaceChild(d,l)
}else{l.appendChild(d)}}l.onclick=function(){var t=this.childNodes;
var u=this.getAttribute("data-cycle")-0;var m=t.length;toggleText(t[u]);
u=(u+1);if(!(out&&u==m)){u%=m;if(v){h[v]=c[u]}}else{h[v]=""}if((end||out)&&u==m-(end?1:0)){if(end){var n=this.removeChild(t[u]);
n.className=rl+"End";n.style.display="inline";this.parentNode.replaceChild(n,this)
}else{this.parentNode.removeChild(this);return}return}toggleText(t[u]);
this.setAttribute("data-cycle",u)}}};"""

REPLACELINK_VARIANT = """/*! <<replacelink>> macro set for SugarCube 2.x */
!function(){"use strict";function showVer(n,notrans){n&&(n.innerHTML="",new Wikifier(n,n.tweecode),n.setAttribute("data-enabled","true"),n.style.display="inline",n.classList.remove("revision-span-out"),notrans||(n.classList.add("revision-span-in"),n.timeout&&clearTimeout(n.timeout),n.timeout=setTimeout(function(){n.classList.remove("revision-span-in"),n=null},20)))}function hideVer(n,notrans){n&&(n.setAttribute("data-enabled","false"),n.classList.remove("revision-span-in"),n.timeout&&clearTimeout(n.timeout),notrans?(n.style.display="none",n.innerHTML="",n=null):(n.classList.add("revision-span-out"),n.timeout=setTimeout(function(){"false"===n.getAttribute("data-enabled")&&(n.classList.remove("revision-span-out"),n.style.display="none",n.innerHTML=""),n=null},1e3)))}function tagcontents(b,starttags,desttags,endtags,k){function tagfound(i,e,endtag){for(var j=0;j<e.length;j++)if(a.indexOf("<<"+e[j]+(endtag?">>":""),i)===i)return e[j]}for(var tg,l=0,c="",a=b.source.slice(k),i=0;i<a.length;i++){if(tg=tagfound(i,starttags))l++;else{if((tg=tagfound(i,desttags,!0))&&0===l)return b.nextMatch=k+i+tg.length+4,[c,tg];if((tg=tagfound(i,endtags,!0))&&(l--,l<0))return null}c+=a.charAt(i)}return null}function revisionSpanHandler(g,e,f,b){function mkspan(vtype){return h=insertElement(m,"span",null,"revision-span "+vtype),h.setAttribute("data-enabled",!1),h.style.display="none",h.tweecode="",h}var becomes,c,cn,m,h,vsn,k=b.source.indexOf(">>",b.matchStart)+2,vsns=[],vtype=e,flen=f.length;if(this.shorthand&&flen)for(;f.length>0;)vsns.push([f.shift(),"insert"===this.flavour?"gains":"becomes"]);else("insert"===this.flavour||"continue"===this.flavour&&"time"===this.trigger)&&vsns.push(["","becomes"]);if("continue"===this.flavour&&flen)b.nextMatch=k+b.source.slice(k).length,vsns.push([b.source.slice(k),vtype]);else{if(becomes=["becomes","gains"],c=tagcontents(b,begintags,becomes.concat(endtags),endtags,k),c&&endtags.indexOf(c[1])===-1){for(;c;)vsns.push(c),c=tagcontents(b,begintags,becomes,endtags,b.nextMatch);c=tagcontents(b,begintags,["/"+e,"end"+e],endtags,b.nextMatch)}if(!c)return void throwError(g,"<<"+e+">>: cannot find a matching close tag");vsns.push(c),"continue"===this.flavour&&(k=b.nextMatch,b.nextMatch=k+b.source.slice(k).length,vsns.push([b.source.slice(k),""]))}for("remove"===this.flavour&&vsns.push(["","becomes"]),cn=0,m=insertElement(g,"span",null,e),m.setAttribute("data-flavour",this.flavour),h=mkspan("initial"),vsn=vsns.shift(),h.tweecode=vsn[0],showVer(h,!0);vsns.length>0;)vsn&&(vtype=vsn[1]),vsn=vsns.shift(),h=mkspan(vtype),h.tweecode=vsn[0];"function"==typeof this.setup&&this.setup(m,g,e,f)}function revisionSetup(m,g,e,f){m.className+=" "+f[0].replace(" ","_")}function keySetup(m,g,e,f){f[0];m.setEventListener("keydown",function l(e){var done=!revise("revise",m);done&&m.removeEventListener("keydown",l)})}function timeSetup(m,g,e,f){function cssTimeUnit(s){if("string"==typeof s){if("ms"===s.slice(-2).toLowerCase())return Number(s.slice(0,-2))||0;if("s"===s.slice(-1).toLowerCase())return 1e3*Number(s.slice(0,-1))||0}return throwError(g,"<<"+e+'>>: "'+s+'" is not a valid CSS time unit'),0}var tm=cssTimeUnit(f[0]),s=passage();setTimeout(function timefn(){if(passage()===s){var done=!revise("revise",m);done||setTimeout(timefn,tm)}},tm)}function hoverSetup(m){var fn,noMouseEnter=null!==document.head.onmouseenter,m1=m.children[0],m2=m.children[1],gains=m2.className.indexOf("gains")>-1;m1&&m2&&(m1.onmouseenter=function(e){for(var efp=document.elementFromPoint(e.clientX,e.clientY);efp&&efp!==this;)efp=efp.parentNode;efp&&"false"!==this.getAttribute("data-enabled")&&revise("revise",this.parentNode)},m2.onmouseleave=function(e){for(var efp=document.elementFromPoint(e.clientX,e.clientY);efp&&efp!==this;)efp=efp.parentNode;efp||"false"!==this.getAttribute("data-enabled")&&revise("revert",this.parentNode)},gains&&(m1.onmouseleave=m2.onmouseleave),noMouseEnter&&(fn=function(n){return function(e){event.relatedTarget&&(event.relatedTarget===this||this.compareDocumentPosition(event.relatedTarget)&Node.DOCUMENT_POSITION_CONTAINED_BY)||this[n]()}},m1.onmouseover=fn("onmouseenter"),m2.onmouseout=fn("onmouseleave"),gains&&(m1.onmouseout=m2.onmouseout)),m=null)}function mouseSetup(m){var evt=null===document.head.onmouseenter?"onmouseenter":"onmouseover";m[evt]=function(){var done=!revise("revise",this);done&&(this[evt]=null)},m=null}function linkSetup(m,g,e,f){var l=document.createElement("a"),p=m.parentNode;l.className="link-internal replaceLink",p.insertBefore(l,m),l.insertBefore(m,null),jQuery(l).ariaClick(function(){var done=!1;m&&m.parentNode===this&&(done=!revise("revise",m),scrollWindowTo(m)),done&&(this.parentNode.insertBefore(m,this),this.parentNode.removeChild(this))}),l=null}function visitedSetup(m,g,e,f){var done,sav=State.variables,os="once seen",d=m.firstChild&&("insert"===this.flavour?m.firstChild.nextSibling:m.firstChild).tweecode;if(sav[os]=sav[os]||{},d&&!sav[os].hasOwnProperty(d))sav[os][d]=1;else{for(var i=sav[os][d];i>0&&!done;i--)done=!revise("revise",m,!0);sav[os].hasOwnProperty(d)&&(sav[os][d]+=1)}}function insideDepartingSpan(elem){for(var r=elem.parentNode;!r.classList.contains("passage");){if(r.classList.contains("revision-span-out"))return!0;r=r.parentNode}}function reviseAll(rt,rname){for(var rall=document.querySelectorAll(".passage [data-flavour]."+rname),ret=!1,i=0;i<rall.length;i++)insideDepartingSpan(rall[i])||(ret=revise(rt,rall[i])||ret);return ret}function revise(rt,r,notrans){function doToGainerSpans(n,fn){for(var k=n-1;k>=0&&rc[k+1].classList.contains("gains");k--)fn(rc[k],notrans)}for(var ind2,curr,next,ind=-1,rev="revert"===rt,rnd=rt.indexOf("random")>-1,fl=r.getAttribute("data-flavour"),rc=r.childNodes,cyc="cycle"===fl,rcl=rc.length-1,k=0;k<=rcl;k++)"true"===rc[k].getAttribute("data-enabled")&&(ind=k);rev&&(ind-=1),curr=ind>=0?rc[ind]:cyc?rc[rcl]:null,ind2=ind,rnd&&(ind2=(ind+Math.floor(Math.random()*rcl))%rcl),next=ind2<rcl?rc[ind2+1]:cyc?rc[0]:null;var docurr=rev?showVer:hideVer,donext=rev?hideVer:showVer,currfn=function(){next&&next.classList.contains("gains")&&!rnd||(docurr(curr,notrans),doToGainerSpans(ind,docurr,notrans))},nextfn=function(){donext(next,notrans),rnd&&doToGainerSpans(ind2+1,donext,notrans)};return rev?(nextfn(),currfn()):(currfn(),nextfn()),!!cyc||(rev?ind>0:ind2<rcl-1)}if("undefined"==typeof version||"undefined"==typeof version.title||"SugarCube"!==version.title||"undefined"==typeof version.major||version.major<2)throw new Error("<<replacelink>> macro set requires SugarCube 2.0.0 or greater, aborting load");version.extensions.replacelinkMacroSet={major:1,minor:1,revision:7};var begintags=[],endtags=[];[{name:"insertlink",flavour:"insert",trigger:"link",setup:linkSetup},{name:"timedinsert",flavour:"insert",trigger:"time",setup:timeSetup},{name:"insertion",flavour:"insert",trigger:"revisemacro",setup:revisionSetup},{name:"later",flavour:"insert",trigger:"visited",setup:visitedSetup},{name:"keyinsert",flavour:"insert",trigger:"key",setup:keySetup},{name:"replacelink",flavour:"replace",trigger:"link",setup:linkSetup},{name:"timedreplace",flavour:"replace",trigger:"time",setup:timeSetup},{name:"mousereplace",flavour:"replace",trigger:"mouse",setup:mouseSetup},{name:"hoverreplace",flavour:"replace",trigger:"hover",setup:hoverSetup},{name:"revision",flavour:"replace",trigger:"revisemacro",setup:revisionSetup},{name:"keyreplace",flavour:"replace",trigger:"key",setup:keySetup},{name:"timedremove",flavour:"remove",trigger:"time",setup:timeSetup},{name:"mouseremove",flavour:"remove",trigger:"mouse",setup:mouseSetup},{name:"hoverremove",flavour:"remove",trigger:"hover",setup:hoverSetup},{name:"removal",flavour:"remove",trigger:"revisemacro",setup:revisionSetup},{name:"once",flavour:"remove",trigger:"visited",setup:visitedSetup},{name:"keyremove",flavour:"remove",trigger:"key",setup:keySetup},{name:"continuelink",flavour:"continue",trigger:"link",setup:linkSetup},{name:"timedcontinue",flavour:"continue",trigger:"time",setup:timeSetup},{name:"mousecontinue",flavour:"continue",trigger:"mouse",setup:mouseSetup},{name:"keycontinue",flavour:"continue",trigger:"key",setup:keySetup},{name:"cycle",flavour:"cycle",trigger:"revisemacro",setup:revisionSetup},{name:"mousecycle",flavour:"cycle",trigger:"mouse",setup:mouseSetup},{name:"timedcycle",flavour:"cycle",trigger:"time",setup:timeSetup},{name:"keycycle",flavour:"replace",trigger:"key",setup:keySetup}].forEach(function(e){e.handler=revisionSpanHandler,e.shorthand=["link","mouse","hover"].indexOf(e.trigger)>-1,macros[e.name]=e,Macro.tags.register(e.name),begintags.push(e.name),endtags.push("/"+e.name,"end"+e.name)}),macros.revertlink=macros.reviselink=macros.randomiselink=macros.randomizelink={handler:function(a,b,c){function disableLink(l){l.style.display="none"}function enableLink(l){l.style.display="inline"}function updateLink(l){if(l.className.indexOf("random")>-1)return void enableLink(l);for(var cannext,canprev,r,fl,rall=document.querySelectorAll(".passage [data-flavour]."+rname),i=0;i<rall.length;i++)r=rall[i],fl=r.getAttribute("data-flavour"),insideDepartingSpan(r)||("cycle"===fl?cannext=canprev=!0:("false"===r.firstChild.getAttribute("data-enabled")&&(canprev=!0),"false"===r.lastChild.getAttribute("data-enabled")&&(cannext=!0)));var can=l.classList.contains("revert")?canprev:cannext;(can?enableLink:disableLink)(l)}function toggleText(w){w.classList.toggle(rl+"Enabled"),w.classList.toggle(rl+"Disabled"),w.style.display="none"===w.style.display?"inline":"none"}if(c.length<2)return void throwError(a,"<<"+b+">>: insufficient arguments (requires at least 2)");var l,rname,actName=b.slice(0,-4),rl="reviseLink",v="",end=!1,out=!1;switch(rname=c.shift().replace(" ","_"),l=insertElement(a,"a"),l.className="link-internal "+rl+" "+rl+"_"+rname+" "+actName,c.length>1&&"$"===c[0][0]&&(v=c[0].slice(1),c.shift()),c[c.length-1]){case"end":end=!0,c.pop();break;case"out":out=!0,c.pop()}for(var h=State.variables,i=0;i<c.length;i++){var on=i===Math.max(c.indexOf(h[v]),0),d=insertElement(null,"span",null,rl+(on?"En":"Dis")+"abled");on?(h[v]=c[i],l.setAttribute("data-cycle",i)):d.style.display="none",insertText(d,c[i]),l.appendChild(d)}jQuery(l).ariaClick(function(){reviseAll(actName,rname);var lall,t=this.childNodes,u=this.getAttribute("data-cycle")-0,m=t.length;if((end||out)&&u>=m-(end?2:1)){if(!end)return void this.parentNode.removeChild(this);var n=this.removeChild(t[u+1]||t[u]);n.className=rl+"End",n.style.display="inline",this.parentNode.replaceChild(n,this)}else toggleText(t[u]),u=(u+1)%m,v&&(h[v]=c[u]),toggleText(t[u]),this.setAttribute("data-cycle",u);lall=document.getElementsByClassName(rl+"_"+rname);for(var i=0;i<lall.length;i++)updateLink(lall[i])}),disableLink(l),setTimeout(function(l){return function(){updateLink(l)}}(l),1),l=null}},macros.mouserevise=macros.hoverrevise={handler:function(a,b,c,d){var endtags=["/"+b,"end"+b],evt=null===window.onmouseenter?"onmouseenter":"onmouseover",t=tagcontents(d,[b],endtags,endtags,d.source.indexOf(">>",d.matchStart)+2);if(t){var rname=c[0].replace(" ","_"),h=insertElement(a,"span",null,"hoverrevise hoverrevise_"+rname),f=function(){var done=!reviseAll("revise",rname);"hoverrevise"!=b&&done&&(this[evt]=null)};new Wikifier(h,t[0]),"hoverrevise"===b?(h.onmouseover=f,h.onmouseout=function(){reviseAll("revert",rname)}):h[evt]=f,h=null}}},Macro.tags.register("mouserevise"),Macro.tags.register("hoverrevise"),macros.instantrevise={handler:function(a,b,c,d){reviseAll("revise",c[0].replace(" ","_"))}}}();"""

REPLACELINK_VARIANT_CSS = """/*! <<replacelink>> macro set for SugarCube 2.x */
.revision-span-in {
	opacity: 0;
}
.revision-span:not(.revision-span-out) {
	-webkit-transition: 1s;
	transition: 1s;
}
.revision-span-out {
	position: absolute;
	opacity: 0;
}
"""

CYCLINGLINK_VARIANT = """/*! <<cyclinglink>> macro for SugarCube 2.x */
!function(){"use strict";if("undefined"==typeof version||"undefined"==typeof version.title||"SugarCube"!==version.title||"undefined"==typeof version.major||version.major<2)throw new Error("<<cyclinglink>> macro requires SugarCube 2.0 or greater, aborting load");version.extensions.cyclinglinkMacro={major:3,minor:3,revision:2},macros.cyclinglink={handler:function(a,b,c){function toggleText(w){w.classList.remove("cyclingLinkInit"),w.classList.toggle(rl+"Enabled"),w.classList.toggle(rl+"Disabled"),w.style.display="none"===w.style.display?"inline":"none"}var rl="cyclingLink";switch(c[c.length-1]){case"end":var end=!0;c.pop();break;case"out":var out=!0;c.pop()}var v=null;c.length&&"$"===c[0][0]&&(v=c[0].slice(1),c.shift());var h=State.variables;if(!out||!v||""!==h[v]){var l=insertElement(a,"a");l.className="link-internal cyclingLink",l.setAttribute("data-cycle",0);for(var i=0;i<c.length;i++){var on=i===(v?Math.max(c.indexOf(h[v]),0):0),d=insertElement(null,"span",null,"cyclingLinkInit cyclingLink"+(on?"En":"Dis")+"abled");on?(v&&(h[v]=c[i]),l.setAttribute("data-cycle",i)):d.style.display="none",insertText(d,c[i]),on&&end&&i===c.length-1?l.parentNode.replaceChild(d,l):l.appendChild(d)}jQuery(l).ariaClick(function(){var t=this.childNodes,u=this.getAttribute("data-cycle")-0,m=t.length;if(toggleText(t[u]),u+=1,out&&u===m?v&&(h[v]=""):(u%=m,v&&(h[v]=c[u])),(end||out)&&u===m-(end?1:0)){if(!end)return void this.parentNode.removeChild(this);var n=this.removeChild(t[u]);return n.className=rl+"End",n.style.display="inline",void this.parentNode.replaceChild(n,this)}toggleText(t[u]),this.setAttribute("data-cycle",u)})}}}}();"""