from importlib.resources import path
import os
import pathlib
import struct
from zlib import crc32
import imageio.v3 as imageio
import sys
import zipfile
from pathlib import Path


def main():
    modRoot = Path.resolve(Path("."))#should be pointing to factorio mods folder
    print(modRoot)
    outRoot = Path(__file__).parent.resolve()
    print(outRoot)

    base = getFile(modRoot,"**/alien-biomes_*.zip")
    hr = getFile(modRoot,"**/alien-biomes-hr-terrain_*.zip")
    getAssets(outRoot,base)
    getAssets(outRoot,hr)


def getFile(root:str,glob:str):
    base = None
    for path in Path.glob(root,glob):
        if(base is None) or (str(path)>str(base)):
            base = path
    print(base)
    return base

def getAssets(root:str,file:str):
    with zipfile.ZipFile(file,"r") as zip:
        for name in [name for name in zip.namelist() if name.endswith(".png")]:
            with open(zip.extract(name,root),mode="rb+") as img:
                for pix in swap(img,name):
                    #mutate colors...
                    pix[0]=min(pix[0],pix[1],pix[2])
                    pix[1]=min(pix[1],pix[2])
                    pass


def swap(f,name):
    f.seek(0)
    # verify that we have a PNG file
    chunkstr = f.read(8)
    if chunkstr != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError('not a png file!')
    while True:
        chunkstr = f.read(8)
        if len(chunkstr) != 8:
            # end of file
            break
        # decode the chunk header
        length, chtype = struct.unpack('>L4s', chunkstr)
        # we only care about palette chunks
        if chtype == b'PLTE':
            curpos = f.tell()
            paldata = f.read(length)
            outPal = list()
            # change the 3rd palette entry to cyan
            for px in range(0,len(paldata),3):
                pix = list(paldata[px:px+3])
                yield pix
                for channel in range(0,3):
                    outPal.append(pix[channel])
            #paldata = paldata[:6] + '\x00\xff\xde' + paldata[9:]
            # go back and write the modified palette in-place
            paldata=bytes(outPal)
            f.seek(curpos)
            f.write(paldata)
            f.write(struct.pack('>L', crc32(chtype+paldata)&0xffffffff))
        else:
            # skip over non-palette chunks
            f.seek(length+4, os.SEEK_CUR)


if __name__ == "__main__":
    main()