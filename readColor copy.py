from math import inf
from time import sleep
import pyautogui

colors = r"Tile colors:\
deepwater #264049\
water #33535F\
water-shallow #35616E\
water-mud #36585A\
mineral-purple-dirt-1 #4A4976\
mineral-purple-dirt-2 #383A67\
mineral-purple-dirt-3 #363655\
mineral-purple-dirt-4 #3F3D60\
mineral-purple-dirt-5 #454262\
mineral-purple-dirt-6 #3B3B5B\
mineral-purple-sand-1 #414581\
mineral-purple-sand-2 #414183\
mineral-purple-sand-3 #404079\
mineral-violet-dirt-1 #6C4464\
mineral-violet-dirt-2 #593556\
mineral-violet-dirt-3 #4E3349\
mineral-violet-dirt-4 #53364F\
mineral-violet-dirt-5 #583C53\
mineral-violet-dirt-6 #4C324B\
mineral-violet-sand-1 #6E3D6D\
mineral-violet-sand-2 #733F6D\
mineral-violet-sand-3 #6C3D67\
mineral-red-dirt-1 #7C4033\
mineral-red-dirt-2 #643126\
mineral-red-dirt-3 #5B3229\
mineral-red-dirt-4 #4B261E\
mineral-red-dirt-5 #593229\
mineral-red-dirt-6 #452119\
mineral-red-sand-1 #82362E\
mineral-red-sand-2 #833A2D\
mineral-red-sand-3 #7C3A2E\
mineral-brown-dirt-1 #73513D\
mineral-brown-dirt-2 #5A3F2E\
mineral-brown-dirt-3 #4C372B\
mineral-brown-dirt-4 #443024\
mineral-brown-dirt-5 #463327\
mineral-brown-dirt-6 #3D2B1F\
mineral-brown-sand-1 #7D5640\
mineral-brown-sand-2 #815A42\
mineral-brown-sand-3 #714F3B\
mineral-tan-dirt-1 #8B6944\
mineral-tan-dirt-2 #725431\
mineral-tan-dirt-3 #5D462C\
mineral-tan-dirt-4 #584128\
mineral-tan-dirt-5 #543F27\
mineral-tan-dirt-6 #503B22\
mineral-tan-sand-1 #997849\
mineral-tan-sand-2 #9C7D4E\
mineral-tan-sand-3 #886940\
mineral-aubergine-dirt-1 #3D384A\
mineral-aubergine-dirt-2 #302B3D\
mineral-aubergine-dirt-3 #2D2937\
mineral-aubergine-dirt-4 #312C3B\
mineral-aubergine-dirt-5 #302C3A\
mineral-aubergine-dirt-6 #2C2836\
mineral-aubergine-sand-1 #3B364F\
mineral-aubergine-sand-2 #3C3550\
mineral-aubergine-sand-3 #3B354B\
mineral-dustyrose-dirt-1 #67514A\
mineral-dustyrose-dirt-2 #4F3F3A\
mineral-dustyrose-dirt-3 #4C403F\
mineral-dustyrose-dirt-4 #463C38\
mineral-dustyrose-dirt-5 #473C3A\
mineral-dustyrose-dirt-6 #403633\
mineral-dustyrose-sand-1 #674C49\
mineral-dustyrose-sand-2 #674E49\
mineral-dustyrose-sand-3 #644E47\
mineral-beige-dirt-1 #83765E\
mineral-beige-dirt-2 #6C604B\
mineral-beige-dirt-3 #625A4B\
mineral-beige-dirt-4 #5E5646\
mineral-beige-dirt-5 #5B5345\
mineral-beige-dirt-6 #564E3F\
mineral-beige-sand-1 #8B7C62\
mineral-beige-sand-2 #8D7E64\
mineral-beige-sand-3 #82745B\
mineral-cream-dirt-1 #A3996D\
mineral-cream-dirt-2 #888056\
mineral-cream-dirt-3 #797254\
mineral-cream-dirt-4 #766E50\
mineral-cream-dirt-5 #6F694B\
mineral-cream-dirt-6 #6D6547\
mineral-cream-sand-1 #AFA874\
mineral-cream-sand-2 #B4AD79\
mineral-cream-sand-3 #A09769\
mineral-black-dirt-1 #3B3B37\
mineral-black-dirt-2 #2B2C29\
mineral-black-dirt-3 #2B2D2D\
mineral-black-dirt-4 #2B2D2B\
mineral-black-dirt-5 #272827\
mineral-black-dirt-6 #262726\
mineral-black-sand-1 #383B38\
mineral-black-sand-2 #373A38\
mineral-black-sand-3 #383A37\
mineral-grey-dirt-1 #777873\
mineral-grey-dirt-2 #60635F\
mineral-grey-dirt-3 #606464\
mineral-grey-dirt-4 #606462\
mineral-grey-dirt-5 #5A5E5D\
mineral-grey-dirt-6 #595B59\
mineral-grey-sand-1 #747774\
mineral-grey-sand-2 #737673\
mineral-grey-sand-3 #747673\
mineral-white-dirt-1 #A5A5A1\
mineral-white-dirt-2 #8A8C88\
mineral-white-dirt-3 #8A8D8D\
mineral-white-dirt-4 #8B8D8B\
mineral-white-dirt-5 #828583\
mineral-white-dirt-6 #808280\
mineral-white-sand-1 #B2B2AD\
mineral-white-sand-2 #B5B7B2\
mineral-white-sand-3 #A1A39F\
vegetation-turquoise-grass-1 #37382F\
vegetation-turquoise-grass-2 #3E3928\
vegetation-green-grass-1 #443D15\
vegetation-green-grass-2 #4B3F19\
vegetation-green-grass-3 #453A1E\
vegetation-green-grass-4 #46351A\
vegetation-olive-grass-1 #5B4911\
vegetation-olive-grass-2 #5C4718\
vegetation-yellow-grass-1 #74580E\
vegetation-yellow-grass-2 #6D5015\
vegetation-orange-grass-1 #673810\
vegetation-orange-grass-2 #623414\
vegetation-red-grass-1 #5B1912\
vegetation-red-grass-2 #581915\
vegetation-violet-grass-1 #4E1E31\
vegetation-violet-grass-2 #47192E\
vegetation-purple-grass-1 #422350\
vegetation-purple-grass-2 #371A48\
vegetation-mauve-grass-1 #342D4B\
vegetation-mauve-grass-2 #312841\
vegetation-blue-grass-1 #2C3349\
vegetation-blue-grass-2 #2C313C\
volcanic-orange-heat-1 #24221F\
volcanic-orange-heat-2 #27221F\
volcanic-orange-heat-3 #371C18\
volcanic-orange-heat-4 #7E1810\
volcanic-green-heat-1 #22241F\
volcanic-green-heat-2 #22271F\
volcanic-green-heat-3 #1C3718\
volcanic-green-heat-4 #187E10\
volcanic-blue-heat-1 #1F2424\
volcanic-blue-heat-2 #1F2627\
volcanic-blue-heat-3 #182837\
volcanic-blue-heat-4 #10447E\
volcanic-purple-heat-1 #231F24\
volcanic-purple-heat-2 #241F27\
volcanic-purple-heat-3 #261837\
volcanic-purple-heat-4 #3C107E\
frozen-snow-0 #DADDE6\
frozen-snow-1 #D7DBE4\
frozen-snow-2 #C9CED6\
frozen-snow-3 #D0D3DB\
frozen-snow-4 #C1C7D0\
frozen-snow-5 #99AAB5\
frozen-snow-6 #8093A2\
frozen-snow-7 #8B9FA8\
frozen-snow-8 #A4B2BD\
frozen-snow-9 #9BADB8"

def getHexColor(r,g,b):
    return "#{0:0{1}x}".format((r<<16)|(g<<8)|(b),6)

def colorToRGB(color):
    return (color>>16,(color>>8)%256,color%256)

colorMap = {}

for color in colors.split("\n"):
    color=color.replace("\\","")
    if "#" in color:
        (name,value) = color.split("#")
        color=colorToRGB(int(value,16))
        colorMap[color]=name
        pass

def getClosest(px):
    tile=None
    diff=inf
    for k,v in colorMap.items():
        currDiff=abs(k[0]-px[0])+abs(k[1]-px[1])+abs(k[2]-px[2])
        if currDiff<diff:
            tile=(k,v)
            diff=currDiff
    return tile



while True:
    sleep(0.1)
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    k,v =getClosest(px)
    print(getHexColor(px[0],px[1],px[2])+" -> "+getHexColor(k[0],k[1],k[2])+" "+v)