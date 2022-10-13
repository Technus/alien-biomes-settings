from math import inf
from time import sleep
import pyautogui

colors = r"Tile equations:\
deepwater < -1e+78 #101030\
-1e+78 <= water <  -1e+76 #101050\
-1e+76 <= water-shallow <  -1e+74 #101070\
-1e+74 <= water-mud <  -1e+72 #101090\
-1e+72 <= mineral-purple-dirt-1 <  -1e+70 #1010B0\
-1e+70 <= mineral-purple-dirt-2 <  -1e+68 #1010D0\
-1e+68 <= mineral-purple-dirt-3 <  -1e+66 #1010F0\
-1e+66 <= mineral-purple-dirt-4 <  -1e+64 #103010\
-1e+64 <= mineral-purple-dirt-5 <  -1e+62 #103030\
-1e+62 <= mineral-purple-dirt-6 <  -1e+60 #103050\
-1e+60 <= mineral-purple-sand-1 <  -1e+58 #103070\
-1e+58 <= mineral-purple-sand-2 <  -1e+56 #103090\
-1e+56 <= mineral-purple-sand-3 <  -1e+54 #1030B0\
-1e+54 <= mineral-violet-dirt-1 <  -1e+52 #1030D0\
-1e+52 <= mineral-violet-dirt-2 <  -1e+50 #1030F0\
-1e+50 <= mineral-violet-dirt-3 <  -1e+48 #105010\
-1e+48 <= mineral-violet-dirt-4 <  -1e+46 #105030\
-1e+46 <= mineral-violet-dirt-5 <  -1e+44 #105050\
-1e+44 <= mineral-violet-dirt-6 <  -1e+42 #105070\
-1e+42 <= mineral-violet-sand-1 <  -1e+40 #105090\
-1e+40 <= mineral-violet-sand-2 <  -1e+38 #1050B0\
-1e+38 <= mineral-violet-sand-3 <  -1e+36 #1050D0\
-1e+36 <= mineral-red-dirt-1 <  -1e+34 #1050F0\
-1e+34 <= mineral-red-dirt-2 <  -1e+32 #107010\
-1e+32 <= mineral-red-dirt-3 <  -1e+30 #107030\
-1e+30 <= mineral-red-dirt-4 <  -1e+28 #107050\
-1e+28 <= mineral-red-dirt-5 <  -1e+26 #107070\
-1e+26 <= mineral-red-dirt-6 <  -1e+24 #107090\
-1e+24 <= mineral-red-sand-1 <  -1e+22 #1070B0\
-1e+22 <= mineral-red-sand-2 <  -1e+20 #1070D0\
-1e+20 <= mineral-red-sand-3 <  -1e+18 #1070F0\
-1e+18 <= mineral-brown-dirt-1 <  -1e+16 #109010\
-1e+16 <= mineral-brown-dirt-2 <  -1e+14 #109030\
-1e+14 <= mineral-brown-dirt-3 <  -1000000000000 #109050\
-1000000000000 <= mineral-brown-dirt-4 <  -10000000000 #109070\
-10000000000 <= mineral-brown-dirt-5 <  -100000000 #109090\
-100000000 <= mineral-brown-dirt-6 <  -1000000 #1090B0\
-1000000 <= mineral-brown-sand-1 <  -10000 #1090D0\
-10000 <= mineral-brown-sand-2 <  -100 #1090F0\
-100 <= mineral-brown-sand-3 <  -1 #10B010\
-1 <= mineral-tan-dirt-1 <  -0.01 #10B030\
-0.01 <= mineral-tan-dirt-2 <  -0.0001 #10B050\
-0.0001 <= mineral-tan-dirt-3 <  -1e-06 #10B070\
-1e-06 <= mineral-tan-dirt-4 <  -1e-08 #10B090\
-1e-08 <= mineral-tan-dirt-5 <  -1e-10 #10B0B0\
-1e-10 <= mineral-tan-dirt-6 <  -1e-12 #10B0D0\
-1e-12 <= mineral-tan-sand-1 <  -1e-14 #10B0F0\
-1e-14 <= mineral-tan-sand-2 <  -1e-16 #10D010\
-1e-16 <= mineral-tan-sand-3 <  -1e-18 #10D030\
-1e-18 <= mineral-aubergine-dirt-1 <  -1e-20 #10D050\
-1e-20 <= mineral-aubergine-dirt-2 <  -1e-22 #10D070\
-1e-22 <= mineral-aubergine-dirt-3 <  -1e-24 #10D090\
-1e-24 <= mineral-aubergine-dirt-4 <  -1e-26 #10D0B0\
-1e-26 <= mineral-aubergine-dirt-5 <  -1e-28 #10D0D0\
-1e-28 <= mineral-aubergine-dirt-6 <  -1e-30 #10D0F0\
-1e-30 <= mineral-aubergine-sand-1 <  -1e-32 #10F010\
-1e-32 <= mineral-aubergine-sand-2 <  -1e-34 #10F030\
-1e-34 <= mineral-aubergine-sand-3 <  -1e-36 #10F050\
-1e-36 <= mineral-dustyrose-dirt-1 <  -1e-38 #10F070\
-1e-38 <= mineral-dustyrose-dirt-2 <  -1e-40 #10F090\
-1e-40 <= mineral-dustyrose-dirt-3 <  -1e-42 #10F0B0\
-1e-42 <= mineral-dustyrose-dirt-4 <  -1e-44 #10F0D0\
-1e-44 <= mineral-dustyrose-dirt-5 <  -1e-46 #10F0F0\
-1e-46 <= mineral-dustyrose-dirt-6 <  -1e-48 #301010\
-1e-48 <= mineral-dustyrose-sand-1 <  -1e-50 #301030\
-1e-50 <= mineral-dustyrose-sand-2 <  -1e-52 #301050\
-1e-52 <= mineral-dustyrose-sand-3 <  -1e-54 #301070\
-1e-54 <= mineral-beige-dirt-1 <  -1e-56 #301090\
-1e-56 <= mineral-beige-dirt-2 <  -1e-58 #3010B0\
-1e-58 <= mineral-beige-dirt-3 <  -1e-60 #3010D0\
-1e-60 <= mineral-beige-dirt-4 <  -1e-62 #3010F0\
-1e-62 <= mineral-beige-dirt-5 <  -1e-64 #303010\
-1e-64 <= mineral-beige-dirt-6 <  -1e-66 #303030\
-1e-66 <= mineral-beige-sand-1 <  -1e-68 #303050\
-1e-68 <= mineral-beige-sand-2 <  -1e-70 #303070\
-1e-70 <= mineral-beige-sand-3 <  -1e-72 #303090\
-1e-72 <= mineral-cream-dirt-1 <  -1e-74 #3030B0\
-1e-74 <= mineral-cream-dirt-2 <  -1e-76 #3030D0\
-1e-76 <= mineral-cream-dirt-3 <  -1e-78 #3030F0\
-1e-78 <= mineral-cream-dirt-4 <  0 #305010\
mineral-cream-dirt-5 == 0 #305030\
0 <  mineral-cream-dirt-6 <= 1e-80 #305050\
1e-80 <  mineral-cream-sand-1 <= 1e-78 #305070\
1e-78 <  mineral-cream-sand-2 <= 1e-76 #305090\
1e-76 <  mineral-cream-sand-3 <= 1e-74 #3050B0\
1e-74 <  mineral-black-dirt-1 <= 1e-72 #3050D0\
1e-72 <  mineral-black-dirt-2 <= 1e-70 #3050F0\
1e-70 <  mineral-black-dirt-3 <= 1e-68 #307010\
1e-68 <  mineral-black-dirt-4 <= 1e-66 #307030\
1e-66 <  mineral-black-dirt-5 <= 1e-64 #307050\
1e-64 <  mineral-black-dirt-6 <= 1e-62 #307070\
1e-62 <  mineral-black-sand-1 <= 1e-60 #307090\
1e-60 <  mineral-black-sand-2 <= 1e-58 #3070B0\
1e-58 <  mineral-black-sand-3 <= 1e-56 #3070D0\
1e-56 <  mineral-grey-dirt-1 <= 1e-54 #3070F0\
1e-54 <  mineral-grey-dirt-2 <= 1e-52 #309010\
1e-52 <  mineral-grey-dirt-3 <= 1e-50 #309030\
1e-50 <  mineral-grey-dirt-4 <= 1e-48 #309050\
1e-48 <  mineral-grey-dirt-5 <= 1e-46 #309070\
1e-46 <  mineral-grey-dirt-6 <= 1e-44 #309090\
1e-44 <  mineral-grey-sand-1 <= 1e-42 #3090B0\
1e-42 <  mineral-grey-sand-2 <= 1e-40 #3090D0\
1e-40 <  mineral-grey-sand-3 <= 1e-38 #3090F0\
1e-38 <  mineral-white-dirt-1 <= 1e-36 #30B010\
1e-36 <  mineral-white-dirt-2 <= 1e-34 #30B030\
1e-34 <  mineral-white-dirt-3 <= 1e-32 #30B050\
1e-32 <  mineral-white-dirt-4 <= 1e-30 #30B070\
1e-30 <  mineral-white-dirt-5 <= 1e-28 #30B090\
1e-28 <  mineral-white-dirt-6 <= 1e-26 #30B0B0\
1e-26 <  mineral-white-sand-1 <= 1e-24 #30B0D0\
1e-24 <  mineral-white-sand-2 <= 1e-22 #30B0F0\
1e-22 <  mineral-white-sand-3 <= 1e-20 #30D010\
1e-20 <  vegetation-turquoise-grass-1 <= 1e-18 #30D030\
1e-18 <  vegetation-turquoise-grass-2 <= 1e-16 #30D050\
1e-16 <  vegetation-green-grass-1 <= 1e-14 #30D070\
1e-14 <  vegetation-green-grass-2 <= 1e-12 #30D090\
1e-12 <  vegetation-green-grass-3 <= 1e-10 #30D0B0\
1e-10 <  vegetation-green-grass-4 <= 1e-08 #30D0D0\
1e-08 <  vegetation-olive-grass-1 <= 1e-06 #30D0F0\
1e-06 <  vegetation-olive-grass-2 <= 0.0001 #30F010\
0.0001 <  vegetation-yellow-grass-1 <= 0.01 #30F030\
0.01 <  vegetation-yellow-grass-2 <= 1 #30F050\
1 <  vegetation-orange-grass-1 <= 100 #30F070\
100 <  vegetation-orange-grass-2 <= 10000 #30F090\
10000 <  vegetation-red-grass-1 <= 1000000 #30F0B0\
1000000 <  vegetation-red-grass-2 <= 100000000 #30F0D0\
100000000 <  vegetation-violet-grass-1 <= 10000000000 #30F0F0\
10000000000 <  vegetation-violet-grass-2 <= 1000000000000 #501010\
1000000000000 <  vegetation-purple-grass-1 <= 1e+14 #501030\
1e+14 <  vegetation-purple-grass-2 <= 1e+16 #501050\
1e+16 <  vegetation-mauve-grass-1 <= 1e+18 #501070\
1e+18 <  vegetation-mauve-grass-2 <= 1e+20 #501090\
1e+20 <  vegetation-blue-grass-1 <= 1e+22 #5010B0\
1e+22 <  vegetation-blue-grass-2 <= 1e+24 #5010D0\
1e+24 <  volcanic-orange-heat-1 <= 1e+26 #5010F0\
1e+26 <  volcanic-orange-heat-2 <= 1e+28 #503010\
1e+28 <  volcanic-orange-heat-3 <= 1e+30 #503030\
1e+30 <  volcanic-orange-heat-4 <= 1e+32 #503050\
1e+32 <  volcanic-green-heat-1 <= 1e+34 #503070\
1e+34 <  volcanic-green-heat-2 <= 1e+36 #503090\
1e+36 <  volcanic-green-heat-3 <= 1e+38 #5030B0\
1e+38 <  volcanic-green-heat-4 <= 1e+40 #5030D0\
1e+40 <  volcanic-blue-heat-1 <= 1e+42 #5030F0\
1e+42 <  volcanic-blue-heat-2 <= 1e+44 #505010\
1e+44 <  volcanic-blue-heat-3 <= 1e+46 #505030\
1e+46 <  volcanic-blue-heat-4 <= 1e+48 #505050\
1e+48 <  volcanic-purple-heat-1 <= 1e+50 #505070\
1e+50 <  volcanic-purple-heat-2 <= 1e+52 #505090\
1e+52 <  volcanic-purple-heat-3 <= 1e+54 #5050B0\
1e+54 <  volcanic-purple-heat-4 <= 1e+56 #5050D0\
1e+56 <  frozen-snow-0 <= 1e+58 #5050F0\
1e+58 <  frozen-snow-1 <= 1e+60 #507010\
1e+60 <  frozen-snow-2 <= 1e+62 #507030\
1e+62 <  frozen-snow-3 <= 1e+64 #507050\
1e+64 <  frozen-snow-4 <= 1e+66 #507070\
1e+66 <  frozen-snow-5 <= 1e+68 #507090\
1e+68 <  frozen-snow-6 <= 1e+70 #5070B0\
1e+70 <  frozen-snow-7 <= 1e+72 #5070D0\
1e+72 <  frozen-snow-8 <= 1e+74 #5070F0\
1e+74 <  frozen-snow-9 <= 1e+76 #509010"

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