from graphics import*

def main():
    win=GraphWin("Currency Converter",1500,700)
    win.setCoords(0,0,500,500)
    #win.setBackground(color_rgb(218,165,32))
    head=Text(Point(250,490),"YOUR CURRENCY CONVERTER")
    head.setFace("times roman")
    head.setStyle("bold")
    head.draw(win)
    act=Text(Point(250,455),"Enter amount and click on your country")
    act.draw(win)
    act.setStyle("italic")

   

    Rectangle(Point(220,160),Point(270,180)).draw(win)
    cl=Text(Point(245,170),"QUIT")
    cl.setStyle("bold")
    cl.setTextColor("red")
    cl.draw(win)

    Image(Point(110,80),"dollar.gif").draw(win)
    Image(Point(330,80),"golden.gif").draw(win)

    a="bj.gif,ci.gif,et.gif,gh.gif,gm.gif,ke.gif,ly.gif,ng.gif,rw.gif,sa.gif,sz.gif,tg.gif,tz.gif,ug.gif,zimb.gif"
    b=a.split(",")
    count=0
    for i in range(len(b)):
        count+=30
        Image(Point(30+count,470),b[i]).draw(win)
        
        


    amt=Text(Point(180,430),"ENTER AMOUNT")
    amt.draw(win)
    input0=Entry(Point(250,430),10)
    
    input0.draw(win)
    input0.setText("0.0")

    benin=Text(Point(40,410),"BENIN")
    benin.draw(win)
    input1=Entry(Point(150,410),15)
    input1.draw(win)
    input1.setText("0.0")

    ivory=Text(Point(40,390),"COTEDIVOIRE")
    ivory.draw(win)
    input2=Entry(Point(150,390),15)
    input2.draw(win)
    input2.setText("0.0")
    
    eth=Text(Point(40,370),"ETHIOPIA")
    eth.draw(win)
    input3=Entry(Point(150,370),15)
    input3.draw(win)
    input3.setText("0.0")
    
    gh=Text(Point(40,350),"GHANA")
    gh.draw(win)
    input4=Entry(Point(150,350),15)
    input4.draw(win)
    input4.setText("0.0")

    ga=Text(Point(40,330),"GAMBIA")
    ga.draw(win)
    input5=Entry(Point(150,330),15)
    input5.draw(win)
    input5.setText("0.0")

    ke=Text(Point(40,310),"KENYA")
    ke.draw(win)
    input6=Entry(Point(150,310),15)
    input6.draw(win)
    input6.setText("0.0")

    li=Text(Point(40,290),"LIBERIA")
    li.draw(win)
    input7=Entry(Point(150,290),15)
    input7.draw(win)
    input7.setText("0.0")

    ni=Text(Point(40,270),"NIGERIA")
    ni.draw(win)
    input8=Entry(Point(150,270),15)
    input8.draw(win)
    input8.setText("0.0")

    rw=Text(Point(230,410),"RWANDA")
    rw.draw(win)
    input9=Entry(Point(350,410),15)
    input9.draw(win)
    input9.setText("0.0")
    
    sa=Text(Point(230,390),"SOUTH AFRICA") 
    sa.draw(win)
    input10=Entry(Point(350,390),15)
    input10.draw(win)
    input10.setText("0.0")

    tg=Text(Point(230,370),"TOGO")
    tg.draw(win)
    input11=Entry(Point(350,370),15)
    input11.draw(win)
    input11.setText("0.0")

    sw=Text(Point(230,350),"SWAZILAND")
    sw.draw(win)
    input12=Entry(Point(350,350),15)
    input12.draw(win)
    input12.setText("0.0")

    tz=Text(Point(230,330),"TANZANIA")
    tz.draw(win)
    input13=Entry(Point(350,330),15)
    input13.draw(win)
    input13.setText("0.0")

    ug=Text(Point(230,310),"UGANDA")
    ug.draw(win)
    input14=Entry(Point(350,310),15)
    input14.draw(win)
    input14.setText("0.0")

    zim=Text(Point(230,290),"ZIMBABWE")
    zim.draw(win)
    input15=Entry(Point(350,290),15)
    input15.draw(win)
    input15.setText("0.0")

    bp=Text(Point(230,270),"BRITISH POUNDS")
    bp.draw(win)
    input16=Entry(Point(350,270),15)
    input16.draw(win)
    input16.setText("0.0")

    euros=Text(Point(230,250),"EUROS")
    euros.draw(win)
    input17=Entry(Point(350,250),15)
    input17.draw(win)
    input17.setText("0.0")

    usd=Text(Point(40,250),"USDOLLARS")
    usd.draw(win)
    input18=Entry(Point(150,250),15)
    input18.draw(win)
    input18.setText("0.0")
    
    p=win.getMouse()
    amount=eval(input0.getText())
    
    
    while not(220<= p.getX()<=270 and 160<=p.getY()<=180):
    
        if  139.63<=p.getX()<=161.16 and 463.46<= p.getY() <=477.4:
            input1.setText(ghanaconvert(amount)[0])
            input2.setText(ghanaconvert(amount)[1])
            input3.setText(ghanaconvert(amount)[2])
            input4.setText(ghanaconvert(amount)[3])
            input5.setText(ghanaconvert(amount)[4])
            input6.setText(ghanaconvert(amount)[5])
            input7.setText(ghanaconvert(amount)[6])
            input8.setText(ghanaconvert(amount)[7])
            input9.setText(ghanaconvert(amount)[8])
            input10.setText(ghanaconvert(amount)[9])
            input11.setText(ghanaconvert(amount)[10])
            input12.setText(ghanaconvert(amount)[11])
            input13.setText(ghanaconvert(amount)[12])
            input14.setText(ghanaconvert(amount)[13])
            input15.setText(ghanaconvert(amount)[14])
            input16.setText(ghanaconvert(amount)[15])
            input17.setText(ghanaconvert(amount)[16])
            input18.setText(ghanaconvert(amount)[17])
        elif 50<=p.getX()<=71 and 463.46<= p.getY() <=477.4:
            input1.setText(ivorycoast(amount)[0])
            input2.setText(ivorycoast(amount)[1])
            input3.setText(ivorycoast(amount)[2])
            input4.setText(ivorycoast(amount)[3])
            input5.setText(ivorycoast(amount)[4])
            input6.setText(ivorycoast(amount)[5])
            input7.setText(ghanaconvert(amount)[6])
            input8.setText(ivorycoast(amount)[7])
            input9.setText(ivorycoast(amount)[8])
            input10.setText(ivorycoast(amount)[9])
            input11.setText(ivorycoast(amount)[10])
            input12.setText(ivorycoast(amount)[11])
            input13.setText(ivorycoast(amount)[12])
            input14.setText(ivorycoast(amount)[13])
            input15.setText(ivorycoast(amount)[14])
            input16.setText(ivorycoast(amount)[15])
            input17.setText(ivorycoast(amount)[16])
            input18.setText(ivorycoast(amount)[17])
        elif 79.57<=p.getX()<=101.10 and 463.46<= p.getY() <=477.4:
            input1.setText(ivorycoast(amount)[0])
            input2.setText(ivorycoast(amount)[1])
            input3.setText(ivorycoast(amount)[2])
            input4.setText(ivorycoast(amount)[3])
            input5.setText(ivorycoast(amount)[4])
            input6.setText(ivorycoast(amount)[5])
            input7.setText(ghanaconvert(amount)[6])
            input8.setText(ivorycoast(amount)[7])
            input9.setText(ivorycoast(amount)[8])
            input10.setText(ivorycoast(amount)[9])
            input11.setText(ivorycoast(amount)[10])
            input12.setText(ivorycoast(amount)[11])
            input13.setText(ivorycoast(amount)[12])
            input14.setText(ivorycoast(amount)[13])
            input15.setText(ivorycoast(amount)[14])
            input16.setText(ivorycoast(amount)[15])
            input17.setText(ivorycoast(amount)[16])
            input18.setText(ivorycoast(amount)[17])
        elif 105.60<=p.getX()<=134.13 and 463.46<= p.getY() <=477.4:
            input1.setText(ethiopia(amount)[0])
            input2.setText(ethiopia(amount)[1])
            input3.setText(ethiopia(amount)[2])
            input4.setText(ethiopia(amount)[3])
            input5.setText(ethiopia(amount)[4])
            input6.setText(ethiopia(amount)[5])
            input7.setText(ethiopia(amount)[6])
            input8.setText(ethiopia(amount)[7])
            input9.setText(ethiopia(amount)[8])
            input10.setText(ethiopia(amount)[9])
            input11.setText(ethiopia(amount)[10])
            input12.setText(ethiopia(amount)[11])
            input13.setText(ethiopia(amount)[12])
            input14.setText(ethiopia(amount)[13])
            input15.setText(ethiopia(amount)[14])
            input16.setText(ethiopia(amount)[15])
            input17.setText(ethiopia(amount)[16])
            input18.setText(ethiopia(amount)[17])
        elif 169<=p.getX()<=190.6 and 463.46<= p.getY() <=477.4:
            input1.setText(gambia(amount)[0])
            input2.setText(gambia(amount)[1])
            input3.setText(gambia(amount)[2])
            input4.setText(gambia(amount)[3])
            input5.setText(gambia(amount)[4])
            input6.setText(gambia(amount)[5])
            input7.setText(gambia(amount)[6])
            input8.setText(gambia(amount)[7])
            input9.setText(gambia(amount)[8])
            input10.setText(gambia(amount)[9])
            input11.setText(gambia(amount)[10])
            input12.setText(gambia(amount)[11])
            input13.setText(gambia(amount)[12])
            input14.setText(gambia(amount)[13])
            input15.setText(gambia(amount)[14])
            input16.setText(gambia(amount)[15])
            input17.setText(gambia(amount)[16])
            input18.setText(gambia(amount)[17])
        elif 200<=p.getX()<=220.7 and 463.46<= p.getY() <=477.4:
            input1.setText(kenya(amount)[0])
            input2.setText(kenya(amount)[1])
            input3.setText(kenya(amount)[2])
            input4.setText(kenya(amount)[3])
            input5.setText(kenya(amount)[4])
            input6.setText(kenya(amount)[5])
            input7.setText(kenya(amount)[6])
            input8.setText(kenya(amount)[7])
            input9.setText(kenya(amount)[8])
            input10.setText(kenya(amount)[9])
            input11.setText(kenya(amount)[10])
            input12.setText(kenya(amount)[11])
            input13.setText(kenya(amount)[12])
            input14.setText(kenya(amount)[13])
            input15.setText(kenya(amount)[14])
            input16.setText(kenya(amount)[15])
            input17.setText(kenya(amount)[16])
            input18.setText(kenya(amount)[17])
        elif 226<=p.getX()<=254 and 463.46<= p.getY() <=477.4:
            input1.setText(liberia(amount)[0])
            input2.setText(liberia(amount)[1])
            input3.setText(liberia(amount)[2])
            input4.setText(liberia(amount)[3])
            input5.setText(liberia(amount)[4])
            input6.setText(liberia(amount)[5])
            input7.setText(liberia(amount)[6])
            input8.setText(liberia(amount)[7])
            input9.setText(liberia(amount)[8])
            input10.setText(liberia(amount)[9])
            input11.setText(liberia(amount)[10])
            input12.setText(liberia(amount)[11])
            input13.setText(liberia(amount)[12])
            input14.setText(liberia(amount)[13])
            input15.setText(liberia(amount)[14])
            input16.setText(liberia(amount)[15])
            input17.setText(liberia(amount)[16])
            input18.setText(liberia(amount)[17])
        elif  225<=p.getX()<=283 and 463.46<= p.getY() <=477.4:
  
            input1.setText(nija(amount)[0])
            input2.setText(nija(amount)[1])
            input3.setText(nija(amount)[2])
            input4.setText(nija(amount)[3])
            input5.setText(nija(amount)[4])
            input6.setText(nija(amount)[5])
            input7.setText(nija(amount)[6])
            input8.setText(nija(amount)[7])
            input9.setText(nija(amount)[8])
            input10.setText(nija(amount)[9])
            input11.setText(nija(amount)[10])
            input12.setText(nija(amount)[11])
            input13.setText(nija(amount)[12])
            input14.setText(nija(amount)[13])
            input15.setText(nija(amount)[14])
            input16.setText(nija(amount)[15])
            input17.setText(nija(amount)[16])
            input18.setText(nija(amount)[17])
        elif  289.78<=p.getX()<=310 and 463.46<= p.getY() <=477.4:
            input1.setText( rwanda(amount)[0])
            input2.setText(rwanda(amount)[1])
            input3.setText(rwanda(amount)[2])
            input4.setText(rwanda(amount)[3])
            input5.setText(rwanda(amount)[4])
            input6.setText(rwanda(amount)[5])
            input7.setText(rwanda(amount)[6])
            input8.setText(rwanda(amount)[7])
            input9.setText(rwanda(amount)[8])
            input10.setText(rwanda(amount)[9])
            input11.setText(rwanda(amount)[10])
            input12.setText(rwanda(amount)[11])
            input13.setText(rwanda(amount)[12])
            input14.setText(rwanda(amount)[13])
            input15.setText(rwanda(amount)[14])
            input16.setText(rwanda(amount)[15])
            input17.setText(rwanda(amount)[16])
            input18.setText(rwanda(amount)[17])
        elif 318.84<=p.getX()<=340.34 and 463.46<= p.getY() <=477.4:
            input1.setText(saf(amount)[0])
            input2.setText(saf(amount)[1])
            input3.setText(saf(amount)[2])
            input4.setText(saf(amount)[3])
            input5.setText(saf(amount)[4])
            input6.setText(saf(amount)[5])
            input7.setText(saf(amount)[6])
            input8.setText(saf(amount)[7])
            input9.setText(saf(amount)[8])
            input10.setText(saf(amount)[9])
            input11.setText(saf(amount)[10])
            input12.setText(saf(amount)[11])
            input13.setText(saf(amount)[12])
            input14.setText(saf(amount)[13])
            input15.setText(saf(amount)[14])
            input16.setText(saf(amount)[15])
            input17.setText(saf(amount)[16])
            input18.setText(saf(amount)[17])
        elif 384.84<=p.getX()<=370.37 and 463.46<= p.getY() <=477.4:
            input1.setText(swaziland(amount)[0])
            input2.setText(swaziland(amount)[1])
            input3.setText(swaziland(amount)[2])
            input4.setText(swaziland(amount)[3])
            input5.setText(swaziland(amount)[4])
            input6.setText(swaziland(amount)[5])
            input7.setText(swaziland(amount)[6])
            input8.setText(swaziland(amount)[7])
            input9.setText(swaziland(amount)[8])
            input10.setText(swaziland(amount)[9])
            input11.setText(swaziland(amount)[10])
            input12.setText(swaziland(amount)[11])
            input13.setText(swaziland(amount)[12])
            input14.setText(swaziland(amount)[13])
            input15.setText(swaziland(amount)[14])
            input16.setText(swaziland(amount)[15])
            input17.setText(swaziland(amount)[16])
            input18.setText(swaziland(amount)[17])
        elif  377.377<=p.getX()<=400 and 463.46<= p.getY() <=477.4:
            input1.setText(togo(amount)[0])
            input2.setText(togo(amount)[1])
            input3.setText(togo(amount)[2])
            input4.setText(togo(amount)[3])
            input5.setText(togo(amount)[4])
            input6.setText(togo(amount)[5])
            input7.setText(togo(amount)[6])
            input8.setText(togo(amount)[7])
            input9.setText(togo(amount)[8])
            input10.setText(togo(amount)[9])
            input11.setText(togo(amount)[10])
            input12.setText(togo(amount)[11])
            input13.setText(togo(amount)[12])
            input14.setText(togo(amount)[13])
            input15.setText(togo(amount)[14])
            input16.setText(togo(amount)[15])
            input17.setText(togo(amount)[16])
            input18.setText(togo(amount)[17])
        elif 409.409<=p.getX()<=431 and 463.46<= p.getY() <=477.4:
            input1.setText(tanzanian(amount)[0])
            input2.setText(tanzanian(amount)[1])
            input3.setText(tanzanian(amount)[2])
            input4.setText(tanzanian(amount)[3])
            input5.setText(tanzanian(amount)[4])
            input6.setText(tanzanian(amount)[5])
            input7.setText(tanzanian(amount)[6])
            input8.setText(tanzanian(amount)[7])
            input9.setText(tanzanian(amount)[8])
            input10.setText(tanzanian(amount)[9])
            input11.setText(tanzanian(amount)[10])
            input12.setText(tanzanian(amount)[11])
            input13.setText(tanzanian(amount)[12])
            input14.setText(tanzanian(amount)[13])
            input15.setText(tanzanian(amount)[14])
            input16.setText(tanzanian(amount)[15])
            input17.setText(tanzanian(amount)[16])
            input18.setText(tanzanian(amount)[17])
        elif 438<=p.getX()<=460 and 463.46<= p.getY() <=477.4:
            input1.setText(uganda(amount)[0])
            input2.setText(uganda(amount)[1])
            input3.setText(uganda(amount)[2])
            input4.setText(uganda(amount)[3])
            input5.setText(uganda(amount)[4])
            input6.setText(uganda(amount)[5])
            input7.setText(uganda(amount)[6])
            input8.setText(uganda(amount)[7])
            input9.setText(uganda(amount)[8])
            input10.setText(uganda(amount)[9])
            input11.setText(uganda(amount)[10])
            input12.setText(uganda(amount)[11])
            input13.setText(uganda(amount)[12])
            input14.setText(uganda(amount)[13])
            input15.setText(uganda(amount)[14])
            input16.setText(uganda(amount)[15])
            input17.setText(uganda(amount)[16])
            input18.setText(uganda(amount)[17])
            
        elif 464.96<= p.getX()<=270 and 493<=p.getY()<=180:
            input1.setText(zimba(amount)[0])
            input2.setText(zimba(amount)[1])
            input3.setText(zimba(amount)[2])
            input4.setText(zimba(amount)[3])
            input5.setText(zimba(amount)[4])
            input6.setText(zimba(amount)[5])
            input7.setText(zimba(amount)[6])
            input8.setText(zimba(amount)[7])
            input9.setText(zimba(amount)[8])
            input10.setText(zimba(amount)[9])
            input11.setText(zimba(amount)[10])
            input12.setText(zimba(amount)[11])
            input13.setText(zimba(amount)[12])
            input14.setText(zimba(amount)[13])
            input15.setText(zimba(amount)[14])
            input16.setText(zimba(amount)[15])
            input17.setText(zimba(amount)[16])
            input18.setText(zimba(amount)[17])
        
        amount=eval(input0.getText())
        p=win.getMouse()
    else:
        win.close()
        
   
def ghanaconvert(n):
    ben=134.98096*n
    cot=134.98096*n
    eth=5.04*n
    gh=1*n
    gam=9.87406*n
    kenya=22.76243*n
    lib=20.10*n
    nig=68.56351*n 
    rwnda=182.44*n
    sa=2.81019*n
    tg=134.98096*n
    swazi=2.81*n
    tnza=490.51*n
    ug=794.47492*n
    zimb=80.2706*n
    pounds=0.18*n
    euros=0.205777*n
    usd=0.22*n    
    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
    
def ivorycoast(n):
    ben=1*n
    cot=1*n
    eth=0.038*n
    gh=0.0072*n
    gam=0.074*n
    kenya=0.17*n
    lib=0.16*n
    nig=0.50*n
    rwnda=136*n
    sa=0.020*n
    tg=1*n
    swazi=0.020*n
    tnza=3.68*n
    ug=5.911*n
    zimb=16.44*n
    pounds=0.00132*n
    euros=0.00152*n
    usd=0.00165*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
def ethiopia(n):
    ben=26.64*n
    cot=134.98096*n
    eth=1*n
    gh=0.19*n
    gam=2*n
    kenya=4.51*n
    lib=3.68*n
    nig=13.44*n
    rwnda=36.76*n
    sa=0.56*n
    tg=1*n
    swazi=0.543317*n
    tnza=97.98*n
    ug=157.7*n
    zimb=15.7691*n
    pounds=0.035*n
    euros=0.0404173*n
    usd=0.044*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
   
def gambia(n):
    ben=13.30*n
    cot=13.30*n
    eth=0.51*n
    gh=0.10*n
    gam=1*n
    kenya=2.30*n
    lib=2.11*n
    nig=6.88*n
    rwnda=18.04*n
    sa=0.28*n
    tg=13.30*n
    swazi=0.278447*n
    tnza=48.86*n
    ug=80.22*n
    zimb=8.09258*n
    pounds=0.0178735*n
    euros=0.0207409*n
    usd=0.0223614*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
def kenya(n):
    ben=5.87*n
    cot=5.87*n
    eth=0.22*n
    gh=0.042*n
    gam=0.44*n
    kenya=1*n
    lib=0.82*n
    nig=2.99*n
    rwnda=8*n
    sa=0.12*n
    tg=5.87*n
    swazi=0.12*n
    tnza=21.72*n
    ug=34.91*n
    zimb=9.74*n
    pounds=0.0077*n
    euros=0.0089*n
    usd=0.0097*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
def liberia(n):
    ben=7.19*n
    cot=7.19*n
    eth=0.27*n
    gh=0.05*n
    gam=0.54*n
    kenya=1.23*n
    lib=1*n
    nig=3.74*n
    rwnda=8.76720*n
    sa=0.15*n
    tg=7.19*n
    swazi=0.15*n
    tnza=26.57*n
    ug=42.79*n
    zimb=1.19*n
    pounds=0.0085*n
    euros=0.00973411*n
    usd=0.0105820*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)

def nija(n):
    ben=1.96*n
    cot=1.96*n
    eth=0.07*n
    gh=0.014*n
    gam=0.14*n
    kenya=0.33*n
    lib=0.27*n
    nig=1*n
    rwnda=2.63*n
    sa=0.045*n
    tg=1.96*n
    swazi=0.04*n
    tnza=7.10*n
    ug=11.5*n
    zimb=1.14889*n
    pounds=0.0026*n
    euros=0.0031*n
    usd=0.0033*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd) 
def rwanda(n):
    ben=134.98096*n
    cot=134.98096*n
    eth=5.04*n
    gh=1*n
    gam=0.14*n
    kenya=0.33*n
    lib=0.27*n
    nig=68.56351*n
    rwnda=182.44*n
    sa=2.81019*n
    tg=134.98096*n
    swazi=2.81*n
    tnza=490.51*n
    ug=794.47492*n
    zimb=80.2706*n
    pounds=0.18*n
    euros=0.205777*n
    usd=0.22*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
def saf(n):
    ben=44.70*n
    cot=44.70*n
    eth=1.67101*n
    gh=0.30*n
    gam=3.28562*n
    kenya=7.50*n
    lib=6.14*n
    nig=22.26*n
    rwnda=59.9244*n
    sa=1*n
    tg=44.70*n
    swazi=0.98*n
    tnza=162.03*n
    ug=263.42*n
    zimb=7.28*n
    pounds=0.058 *n
    euros=0.068*n
    usd=0.073*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
def swaziland(n):
    ben=44.7362*n
    cot=44.7362*n
    eth=1.67054*n
    gh=0.303999*n
    gam=3.28486*n
    kenya=7.48424*n
    lib=6.82035*n
    nig=68.56351*n
    rwnda=182.44*n
    sa=2.81019*n
    tg=44.7362*n
    swazi=2.81*n
    tnza=490.51*n
    ug=794.47492*n
    zimb=80.2706*n
    pounds=0.18*n
    euros=0.205777*n
    usd=0.0725683*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd) 
   
def togo(n):
    ben=1*n
    cot=1*n
    eth=0.038*n
    gh=0.0072*n
    gam=0.074*n
    kenya=0.17*n
    lib=0.16*n
    nig=0.50*n
    rwnda=136*n
    sa=0.020*n
    tg=1*n
    swazi=0.020*n
    tnza=3.68*n
    ug=5.911*n
    zimb=16.44*n
    pounds=0.00132*n
    euros=0.00152*n
    usd=0.00165*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
def tanzanian(n):
    ben=134.98096*n
    cot=134.98096*n
    eth=5.04*n
    gh=1*n
    gam=9.87406*n
    kenya=22.76243*n
    lib=20.10*n
    nig=68.56351*n
    rwnda=182.44*n
    sa=2.81019*n
    tg=134.98096*n
    swazi=2.81*n
    tnza=490.51*n
    ug=794.47492*n
    zimb=80.2706*n
    pounds=0.18*n
    euros=0.205777*n
    usd=0.22*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
def uganda(n):
    ben=134.98096*n
    cot=134.98096*n
    eth=5.04*n
    gh=1*n
    gam=9.87406*n
    kenya=22.76243*n
    lib=20.10*n
    nig=68.56351*n
    rwnda=182.44*n
    sa=2.81019*n
    tg=134.98096*n
    swazi=2.81*n
    tnza=490.51*n
    ug=794.47492*n
    zimb=80.2706*n
    pounds=0.18*n
    euros=0.205777*n
    usd=0.22*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd)
def zimba(n):
    ben=134.98096*n
    cot=134.98096*n
    eth=5.04*n
    gh=1*n
    gam=9.87406*n
    kenya=22.76243*n
    lib=20.10*n
    nig=68.56351*n
    rwnda=182.44*n
    sa=2.81019*n
    tg=134.98096*n
    swazi=2.81*n
    tnza=490.51*n
    ug=794.47492*n
    zimb=80.2706*n
    pounds=0.18*n
    euros=0.205777*n
    usd=0.22*n    
    return(ben,cot,eth,gh,gam,kenya,lib,nig,rwnda,sa,tg,swazi,tnza,ug,zimb,pounds,euros,usd) 
    
    
    
main()    
    


    
    
