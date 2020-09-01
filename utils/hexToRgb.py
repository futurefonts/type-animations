### simple method to convert hex color to Drawbot-compatible, 0–1 color tuple
### with help from https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python

def RGBfromHex(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)