(function(t){function e(e){for(var n,i,r=e[0],l=e[1],c=e[2],d=0,p=[];d<r.length;d++)i=r[d],o[i]&&p.push(o[i][0]),o[i]=0;for(n in l)Object.prototype.hasOwnProperty.call(l,n)&&(t[n]=l[n]);u&&u(e);while(p.length)p.shift()();return s.push.apply(s,c||[]),a()}function a(){for(var t,e=0;e<s.length;e++){for(var a=s[e],n=!0,r=1;r<a.length;r++){var l=a[r];0!==o[l]&&(n=!1)}n&&(s.splice(e--,1),t=i(i.s=a[0]))}return t}var n={},o={app:0},s=[];function i(e){if(n[e])return n[e].exports;var a=n[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,i),a.l=!0,a.exports}i.m=t,i.c=n,i.d=function(t,e,a){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(i.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)i.d(a,n,function(e){return t[e]}.bind(null,n));return a},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var r=window["webpackJsonp"]=window["webpackJsonp"]||[],l=r.push.bind(r);r.push=e,r=r.slice();for(var c=0;c<r.length;c++)e(r[c]);var u=l;s.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"2b56":function(t,e,a){"use strict";var n=a("9906"),o=a.n(n);o.a},"4d30":function(t,e,a){},"56d7":function(t,e,a){"use strict";a.r(e);var n=a("2b0e"),o=a("bb71");a("da64");n["a"].use(o["a"],{iconfont:"md",theme:{primary:"#3cd1c2",success:"#3cd1c2",info:"#ffaa2c",error:"#f83e70"}});var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-app",{staticClass:"grey lighten-4"},[a("Navbar"),a("v-content",{staticClass:"mx-4 mb-4"},[a("router-view")],1)],1)},i=[],r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("nav",[a("v-toolbar",{attrs:{app:""}},[a("v-toolbar-side-icon",{staticClass:"grey--text",on:{click:[function(e){t.drawer=!t.drawer},function(e){t.loadData()}]}}),a("v-toolbar-title",{staticClass:"text-uppercase grey--text"},[a("span",[t._v("SPOTIFY")])]),a("v-spacer"),a("v-menu",{attrs:{"offset-y":""}},[a("v-btn",{attrs:{slot:"activator",flat:"",color:"grey"},slot:"activator"},[a("v-icon",{attrs:{left:""}},[t._v("expand_more")]),a("span",[t._v("Menu")])],1),1==this.$store.state.connected?a("div",[a("v-list",t._l(t.links_connected,function(e){return a("v-list-tile",{key:e.text,attrs:{router:"",to:e.route}},[a("v-list-tile-title",[t._v(t._s(e.text))])],1)}))],1):t._e(),0==this.$store.state.connected?a("div",[a("v-list",t._l(t.links_disconnected,function(e){return a("v-list-tile",{key:e.text,attrs:{router:"",to:e.route}},[a("div",{on:{click:function(a){t.checkToken(),t.logOut(e.text)}}},[a("v-list-tile-title",[t._v(t._s(e.text))])],1)])}))],1):t._e()],1)],1),a("v-navigation-drawer",{staticClass:"primary",attrs:{app:"",color:"grey"},model:{value:t.drawer,callback:function(e){t.drawer=e},expression:"drawer"}},[1==this.$store.state.connected?a("div",[a("v-layout",{attrs:{column:"","align-center":""}},[a("v-flex",{staticClass:"mt-5"},[a("v-avatar",{attrs:{size:"100"}},[a("img",{staticClass:"text-lg-center",attrs:{src:this.$store.state.user_photo}})]),a("p",{staticClass:"white--text subheading mt-1"},[t._v(t._s(this.$store.state.user_name))])],1)],1),a("v-list",t._l(t.links_connected,function(e){return a("v-list-tile",{key:e.text,attrs:{router:"",to:e.route}},[a("div",{on:{click:function(a){t.checkToken(),t.logOut(e.text)}}},[a("v-list-tile-action",[a("v-icon",{staticClass:"white--text"},[t._v(t._s(e.icon))])],1),a("v-list-tile-content",[a("v-list-tile-title",{staticClass:"white--text"},[t._v(t._s(e.text))])],1)],1)])}))],1):t._e(),0==this.$store.state.connected?a("div",[a("v-list",t._l(t.links_disconnected,function(e){return a("v-list-tile",{key:e.text,attrs:{router:"",to:e.route}},[a("v-list-tile-action",[a("v-icon",{staticClass:"white--text"},[t._v(t._s(e.icon))])],1),a("v-list-tile-content",[a("v-list-tile-title",{staticClass:"white--text"},[t._v(t._s(e.text))])],1)],1)}))],1):t._e()])],1)},l=[],c=a("bc3a"),u=a.n(c),d={data(){return{user_name:null,user_photo:null,user_id:null,drawer:!1,links_connected:[{text:"Synchronize",route:"/init"},{text:"Clear Data",route:"/clear"},{text:"Create Playlist",route:"/createplaylist"},{text:"Logout",route:"/connection"}],links_disconnected:[{text:"Login",route:"/connection"}],snackbar:!1}},mounted(){},methods:{loadData(){let t={headers:{jwt_token:this.$store.state.jwt_token}};this.connected=this.$store.state.connected,u.a.get("http://164.90.233.63:5000/#/get-user",t).then(t=>(this.info=t["data"],this.$store.state.user_photo=t["data"][0]["user_photo"],this.$store.state.user_id=t["data"][0]["user_id"],this.$store.state.user_name=t["data"][0]["user_name"]))},logOut(t){"Logout"==t&&(this.$store.state.connected=!1,console.log("logout connected state:::"+this.$store.state.connected))},checkToken(){let t={headers:{jwt_token:this.$store.state.jwt_token}};u.a.get("http://164.90.233.63:5000/#/check-token",t).then(t=>(console.log(this.cathError(t)),this.cathError(t)))},cathError(t){t["data"]["error"]&&(this.$store.state.connected=!1,this.$store.state.message_connection="Token has expired",this.$router.push("/connection"))}}},p=d,h=(a("5dfc"),a("2877")),v=a("6544"),m=a.n(v),f=a("8212"),_=a("8336"),g=a("0e8f"),b=a("132d"),y=a("a722"),x=a("8860"),w=a("ba95"),C=a("40fe"),k=a("5d23"),j=a("e449"),$=a("f774"),V=a("9910"),O=a("71d9"),T=a("706c"),q=a("2a7f"),S=Object(h["a"])(p,r,l,!1,null,null,null);S.options.__file="Navbar.vue";var D=S.exports;m()(S,{VAvatar:f["a"],VBtn:_["a"],VFlex:g["a"],VIcon:b["a"],VLayout:y["a"],VList:x["a"],VListTile:w["a"],VListTileAction:C["a"],VListTileContent:k["a"],VListTileTitle:k["b"],VMenu:j["a"],VNavigationDrawer:$["a"],VSpacer:V["a"],VToolbar:O["a"],VToolbarSideIcon:T["a"],VToolbarTitle:q["a"]});var E={components:{Navbar:D},name:"App",data(){return{}}},L=E,B=a("7496"),M=a("549c"),P=Object(h["a"])(L,s,i,!1,null,null,null);P.options.__file="App.vue";var A=P.exports;m()(P,{VApp:B["a"],VContent:M["a"]});var I=a("8c4f"),J=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-row",{staticClass:"pa-4 text-center"},[a("h1",[t._v("You have to connected first.")])])},N=[],W={data(){return{projects:[{title:"Design a new website",person:"The Net Ninja",due:"1st Jan 2019",status:"ongoing",content:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!"},{title:"Code up the homepage",person:"Chun Li",due:"10th Jan 2019",status:"complete",content:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!"},{title:"Design video thumbnails",person:"Ryu",due:"20th Dec 2018",status:"complete",content:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!"},{title:"Create a community forum",person:"Gouken",due:"20th Oct 2018",status:"overdue",content:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequuntur eos eligendi illum minima adipisci deleniti, dicta mollitia enim explicabo fugiat quidem ducimus praesentium voluptates porro molestias non sequi animi!"}]}},methods:{sortBy(t){this.projects.sort((e,a)=>e[t]<a[t]?-1:1)}}},z=W,H=(a("2b56"),Object(h["a"])(z,J,N,!1,null,null,null));H.options.__file="Dashboard.vue";var Q=H.exports,Y=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[0==this.$store.state.connected?a("v-container",{staticClass:"pa-4 text-center"},[a("h1",[t._v("You have to be login")])]):t._e(),1==this.$store.state.connected?a("div",{staticClass:"projects"},[a("v-container",{staticClass:"my-5"},[a("v-btn",{attrs:{color:"primary",text:"",href:t.info},on:{click:function(e){t.init()}}},[t._v("Synchronize with spotify")])],1)],1):t._e()],1)},F=[],G={data(){return{}},methods:{init(){u()({method:"put",url:"http://164.90.233.63:5000/#/init-db",headers:{jwt_token:this.$store.state.jwt_token}}).then(function(t){console.log(t.data)}).catch(function(t){console.log(t.data)})}}},R=G,K=a("a523"),U=Object(h["a"])(R,Y,F,!1,null,null,null);U.options.__file="Initialise.vue";var X=U.exports;m()(U,{VBtn:_["a"],VContainer:K["a"]});var Z=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[0==this.$store.state.connected?a("v-container",{staticClass:"pa-4 text-center"},[a("h1",[t._v("You have to be login")])]):t._e(),1==this.$store.state.connected?a("div",{staticClass:"projects"},[a("v-container",{staticClass:"my-5"},[a("v-btn",{attrs:{color:"primary",text:"",href:t.info},on:{click:function(e){t.clear()}}},[t._v("Clear DB")])],1)],1):t._e()],1)},tt=[],et={data(){return{}},methods:{clear(){u()({method:"delete",url:"http://164.90.233.63:5000/#/clear-db",headers:{jwt_token:this.$store.state.jwt_token}}).then(function(t){console.log(t.data)}).catch(function(t){console.log(t.data)})}}},at=et,nt=Object(h["a"])(at,Z,tt,!1,null,null,null);nt.options.__file="ClearDb.vue";var ot=nt.exports;m()(nt,{VBtn:_["a"],VContainer:K["a"]});var st=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"team"},[a("h1",{staticClass:"subheading grey--text"},[t._v("Team")]),a("v-container",{staticClass:"my-5"},[a("v-layout",{attrs:{row:"",wrap:""}},t._l(t.team,function(e){return a("v-flex",{key:e.name,attrs:{xs12:"",sm6:"",md4:"",lg3:""}},[a("v-card",{staticClass:"text-xs-center ma-3",attrs:{flat:""}},[a("v-responsive",{staticClass:"pt-4"},[a("v-avatar",{staticClass:"grey lighten-2",attrs:{size:"100"}},[a("img",{attrs:{src:e.avatar}})])],1),a("v-card-text",[a("div",{staticClass:"subheading"},[t._v(t._s(e.name))]),a("div",{staticClass:"grey--text"},[t._v(t._s(e.role))])]),a("v-card-actions",[a("v-btn",{attrs:{flat:"",color:"grey"}},[a("v-icon",{attrs:{small:"",left:""}},[t._v("message")]),a("span",{},[t._v("Message")])],1)],1)],1)],1)}))],1)],1)},it=[],rt={data(){return{team:[{name:"The Net Ninja",role:"Web developer",avatar:"/avatar-1.png"},{name:"Ryu",role:"Graphic designer",avatar:"/avatar-2.png"},{name:"Chun Li",role:"Web developer",avatar:"/avatar-3.png"},{name:"Gouken",role:"Social media maverick",avatar:"/avatar-4.png"},{name:"Yoshi",role:"Sales guru",avatar:"/avatar-5.png"}]}}},lt=rt,ct=a("b0af"),ut=a("99d9"),dt=a("6b53"),pt=Object(h["a"])(lt,st,it,!1,null,null,null);pt.options.__file="Team.vue";var ht=pt.exports;m()(pt,{VAvatar:f["a"],VBtn:_["a"],VCard:ct["a"],VCardActions:ut["a"],VCardText:ut["b"],VContainer:K["a"],VFlex:g["a"],VIcon:b["a"],VLayout:y["a"],VResponsive:dt["a"]});var vt=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[0==this.$store.state.connected?a("v-container",{staticClass:"pa-4 text-center"},[a("h1",[t._v("You have to be login")])]):t._e(),1==this.$store.state.connected?a("v-container",{staticClass:"pa-4 text-center"},[a("h1",{staticClass:"grey--text m-12"},[t._v("Select the playlist you want to create")]),a("v-row",{staticClass:"fill-height",attrs:{align:"center",justify:"center"}},[t._l(t.info,function(e,n){return[t._v("\n                "+t._s(t.test)+"\n                "),a("v-col",{key:n,attrs:{cols:"12",md:"4"}},[a("v-hover",{scopedSlots:t._u([{key:"default",fn:function(n){var o=n.hover;return a("v-card",{class:{"on-hover":o},attrs:{elevation:o?12:2}},[a("v-img",{attrs:{src:e.img,height:"225px"},on:{click:[function(a){t.choose(e.id),t.playlistName(e.name)},function(e){e.stopPropagation(),t.dialog=!0}]}},[a("v-card-title",{staticClass:"title white--text"},[a("v-row",{staticClass:"fill-height flex-column",attrs:{justify:"space-between"}},[a("p",{staticClass:"mt-4 subheading text-left text-uppercase"},[t._v(t._s(e.name))]),a("div",[a("p",{staticClass:"ma-0 body-1 font-weight-bold font-italic text-left"},[t._v("Based on your "+t._s(e.name)+" loved tracks")]),a("p",{staticClass:"caption font-weight-medium font-italic text-left"})])])],1),a("v-btn",{staticClass:"{ 'show-btns': hover }",style:{cursor:t.pointer},attrs:{icon:"",color:"transparent"}},[a("v-icon",{class:{"show-btns":o},attrs:{color:"transparent"}},[t._v("add")])],1)],1)],1)}}])})],1)]})],2),a("div",{staticClass:"dialog"},[a("v-row",{attrs:{justify:"center"}},[a("v-dialog",{attrs:{"content-class":"v-dialog","max-width":"290"},model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[a("div",{staticClass:"dialog"},[a("v-card-title",{staticClass:"headline"},[t._v("Warning")]),a("v-card-text",[t._v("Are you sure to want to create "+t._s(t.playlist_name)+" playlist ?")]),a("v-card-actions",[a("v-spacer"),a("v-btn",{attrs:{color:"primary",text:""},on:{click:function(e){t.dialog=!1}}},[t._v("Disagree")]),a("v-btn",{attrs:{color:"primary",text:""},on:{click:function(e){t.createPlaylist(t.chosen_playlist),t.dialog=!1}}},[t._v("Agree")])],1)],1)])],1)],1)],1):t._e()],1)},mt=[],ft={data:()=>({chosen_playlist:null,playlist_name:null,popup:!1,test:null,name:"CreatePlaylist",icons:["mdi-rewind","mdi-play","mdi-fast-forward"],info:null,dialog:!1,url_img:["https://images.unsplash.com/photo-1578792274110-c407602617da?ixlib=rb-1.2.1&auto=format&fit=crop&w=975&q=80","https://images.unsplash.com/photo-1436262513933-a0b06755c784?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1651&q=80","https://images.unsplash.com/photo-1559761132-5952db82b3e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80","https://images.unsplash.com/photo-1487088678257-3a541e6e3922?ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80","https://images.unsplash.com/photo-1541778956252-6c31bbd0ff64?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2089&q=80","https://images.unsplash.com/photo-1541256942802-7b29531f0df8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1650&q=80","https://images.unsplash.com/photo-1508898578281-774ac4893c0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80","https://images.unsplash.com/photo-1528459584353-5297db1a9c01?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1975&q=80","https://images.unsplash.com/photo-1527239441953-caffd968d952?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80","https://images.unsplash.com/photo-1544306094-e2dcf9479da3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80"],transparent:"rgba(255, 255, 255, 0)"}),mounted(){let t={headers:{jwt_token:this.$store.state.jwt_token}};u.a.get("http://164.90.233.63:5000/#/get-suggest-playlist",t).then(t=>this.info=this.add_url(t["data"]["relevant_category"]))},methods:{add_url(t){for(var e=0;e<t.length;e++)t[e].img=this.url_img[e];return t},choose(t){console.log(t),this.chosen_playlist=t},playlistName(t){this.playlist_name=t},createPlaylist(t){this.$store.state.jwt_token;var e=new FormData;e.set("category_id",t),u()({method:"post",url:"http://164.90.233.63:5000/#/create-playlist",data:e,headers:{jwt_token:this.$store.state.jwt_token}}).then(function(t){console.log(t.data)}).catch(function(t){console.log(t.data)})}}},_t=ft,gt=(a("7c3a"),a("12b2")),bt=a("169a"),yt=a("ce87"),xt=a("adda"),wt=Object(h["a"])(_t,vt,mt,!1,null,"000044bb",null);wt.options.__file="CreatePlaylist.vue";var Ct=wt.exports;m()(wt,{VBtn:_["a"],VCard:ct["a"],VCardActions:ut["a"],VCardText:ut["b"],VCardTitle:gt["a"],VContainer:K["a"],VDialog:bt["a"],VHover:yt["a"],VIcon:b["a"],VImg:xt["a"],VSpacer:V["a"]});var kt=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[null!=this.$store.state.message_connection?a("h1",[t._v(t._s(this.$store.state.message_connection))]):t._e(),a("v-container",{staticClass:"my-5"},[a("v-btn",{staticClass:"ml-5",attrs:{color:"primary",text:"",href:t.info},on:{click:function(e){t.logIn()}}},[t._v("Login")])],1)],1)},jt=[],$t={data(){return{info:null,dialog:!1}},methods:{logIn(){this.$store.state.connected=!0}},mounted(){console.log(this.$store.state.connected=!1),u.a.get("http://164.90.233.635000/#/authent",{headers:{"Access-Control-Allow-Origin":"*"}}).then(t=>(this.info=t["data"],console.log("ICI:::"+t["data"])))}},Vt=$t,Ot=Object(h["a"])(Vt,kt,jt,!1,null,null,null);Ot.options.__file="Connection.vue";var Tt=Ot.exports;m()(Ot,{VBtn:_["a"],VContainer:K["a"]});var qt=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-row",{staticClass:"pa-4 text-center"},[a("h1",[t._v("Now, you can create your favorite playlist")]),a("h2",[t._v('First synchronize you songs by clicking on "Synchronize".')]),a("h2",[t._v('When it\'s done go on "Create Playlist" and select the playlist you want to create.')]),a("h2",[t._v('You can resynchronize your songs by clicking on "Clear DB" then "Synchronize".')])])},St=[],Dt={data(){return{code:null,info:null,dialog:!1}},mounted(){this.get_url(),u.a.get("http://164.90.233.63:5000/#/get-token?code="+this.code.query["code"]).then(t=>(this.info=t["data"],this.$store.state.jwt_token=t["data"]["jwt_token"],this.$store.state.connected=!0)),console.log(this.$store.state.jwt_token)},methods:{get_url(){this.code=this.$route}}},Et=Dt,Lt=Object(h["a"])(Et,qt,St,!1,null,null,null);Lt.options.__file="LoginSuccess.vue";var Bt=Lt.exports,Mt=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",[t._v(t._s(this.$store.state.connected))])])},Pt=[],At={data:()=>({test:null})},It=At,Jt=Object(h["a"])(It,Mt,Pt,!1,null,null,null);Jt.options.__file="Test.vue";var Nt=Jt.exports;n["a"].use(I["a"]);var Wt=new I["a"]({mode:"history",base:"/",routes:[{path:"/",name:"dashboard",component:Q},{path:"/init",name:"init",component:X},{path:"/clear",name:"clear",component:ot},{path:"/connection",name:"connection",component:Tt},{path:"/login-success",name:"loginsuccess",component:Bt},{path:"/team",name:"team",component:ht},{path:"/createplaylist",name:"createplaylist",component:Ct},{path:"/test",name:"test",component:Nt}]}),zt=a("0628"),Ht=a.n(zt),Qt=a("2f62");n["a"].use(Qt["a"]);var Yt=new Qt["a"].Store({state:{connected:!1,jwt_token:null,user_photo:null,user_id:null,user_name:null,message_connection:null},mutations:{},actions:{}});n["a"].use(Ht.a),n["a"].config.productionTip=!1,n["a"].config.silent=!0,new n["a"]({store:Yt,router:Wt,render:t=>t(A)}).$mount("#app")},"5dfc":function(t,e,a){"use strict";var n=a("72ec"),o=a.n(n);o.a},"72ec":function(t,e,a){},"7c3a":function(t,e,a){"use strict";var n=a("4d30"),o=a.n(n);o.a},9906:function(t,e,a){}});
//# sourceMappingURL=app.52ed0e70.js.map