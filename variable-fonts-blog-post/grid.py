import sys
sys.path.append('../') # this lets us import utils
from utils.hexToRgb import RGBfromHex
import math


fontPath = "../fonts/rotor-VF.ttf"

exportPath = "./exports/grid.gif"




docWidth=800
#docHeight=int(docWidth * 0.480814)
docHeight=470

numCols = 3.0
numRows = 3.0

colWidth = (docWidth / numCols)
rowHeight = (docHeight / numRows)

saveEnabled = True

docColor = RGBfromHex('#ffffff')
defaultTextColor = RGBfromHex('#000000')

numFrames = 40
defaultFrameDuration = 0.08

textSize = 90
leading = textSize * 1

textBlocks = []

textBlocks.append({
    "fontPath": "../fonts/rotor-VF.ttf",
    "text": 'LOL', 
    "textSize": textSize*1.1, 
    "textColor": RGBfromHex('#2d63e9'), 
    "lineHeightOffset": -10,
    "xOffset": 0,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "rttx": 0
            }
        },
        {
            "pct": 1,
            "axes": {
                "rttx": 360
            }
        }
    ]
})
textBlocks.append({
    "fontPath": "../fonts/SeraphsVAR-V3.ttf",
    "text": '8RO', 
    "textSize": textSize * 1.2, 
    "textColor": RGBfromHex('#1be378'),
    "lineHeightOffset": -10,
    "xOffset": 6,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "SRFS": 3,
                "wght": 200
            }
        },
        {
            "pct": .5,
            "axes": {
                "SRFS": 0,
                "wght": 200
            }
        },
        {
            "pct": 1,
            "axes": {
                "SRFS": 3,
                "wght": 200
            }
        }
    ]
})

textBlocks.append({
    "fontPath": "../fonts/TXT25-VRBL-0.7.ttf",
    "text": 'brb', 
    "textSize": textSize*1.3, 
    "textColor": RGBfromHex("#e59f3b"), 
    "lineHeightOffset": -12,
    "xOffset": 0,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "wght": 1
            }
        },
        {
            "pct": .5,
            "axes": {
                "wght": 1000
            }
        },
        {
            "pct": 1,
            "axes": {
                "wght": 1
            }
        }
    ]
})
textBlocks.append({
    "fontPath": "../fonts/ShrillVariablev0.3.ttf",
    "text": 'yay', 
    "textSize": textSize*1.2, 
    "textColor": RGBfromHex("#964b00"), 
    "lineHeightOffset": 3,
    "xOffset": 0,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "wght": 100
            }
        },
        {
            "pct": .5,
            "axes": {
                "wght": 900
            }
        },
        {
            "pct": 1,
            "axes": {
                "wght": 100
            }
        }
    ]
})
textBlocks.append({
    "fontPath": "../fonts/Dunkelsansv0.63GX.ttf",
    "text": '우주', 
    "textSize": textSize*1.2, 
    "textColor": RGBfromHex("#000000"), 
    "lineHeightOffset": -8,
    "xOffset": 0,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "wdth": 700
            }
        },
        {
            "pct": .5,
            "axes": {
                "wdth": 1000
            }
        },
        {
            "pct": 1,
            "axes": {
                "wdth": 700
            }
        }
    ]
})
textBlocks.append({
    "fontPath": "../fonts/CSTMXprmntl03-VF.ttf",
    "text": 'Oh',
    "textSize": textSize*1.3, 
    "textColor": RGBfromHex("#ff6bb2"), 
    "lineHeightOffset": -20,
    "xOffset": 0,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "wght": 950
            }
        },
        {
            "pct": .5,
            "axes": {
                "wght": 400
            }
        },
        {
            "pct": 1,
            "axes": {
                "wght": 950
            }
        }
    ]
})
textBlocks.append({
    "fontPath": "../fonts/GoitersGX.ttf",
    "text": 'idk', 
    "textSize": textSize * .85, 
    "textColor": RGBfromHex("#ff0000"), 
    "lineHeightOffset": -3,
    "xOffset": 0,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "wght": 900
            }
        },
        {
            "pct": .5,
            "axes": {
                "wght": 100
            }
        },
        {
            "pct": 1,
            "axes": {
                "wght": 900
            }
        }
    ]
})
textBlocks.append({
    "fontPath": "../fonts/ClaretteGX.ttf",
    "text": 'yum', 
    "textSize": textSize*1.1, 
    "textColor": RGBfromHex("#2d3fe9"), 
    "lineHeightOffset": 0,
    "xOffset": 5,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "wdth": 90,
                "ital": 0
            }
        },
        {
            "pct": .5,
            "axes": {
                "wdth": 90,
                "ital": 100
            }
        },
        {
            "pct": 1,
            "axes": {
                "wdth": 90,
                "ital": 0
            }
        }
    ]
})
textBlocks.append({
    "fontPath": "../fonts/CoFoPeshkaV0.4_Variable.ttf",
    "text": 'HAHA', 
    "textSize": textSize*1.1, 
    "textColor": RGBfromHex("#aaaaaa"), 
    "lineHeightOffset": -5,
    "xOffset": 0,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "wdth": 200,
                "wght": 1000
            }
        },
        {
            "pct": .5,
            "axes": {
                "wdth": 400,
                "wght": 0
            }
        },
        {
            "pct": 1,
            "axes": {
                "wdth": 200,
                "wght": 1000
            }
        }
    ]
})

shouldEqualizeKeyframePct = False

spaceBetweenBlocks = leading - textSize 

textBoxVerticalOffset = -25

# Change this for each font. It's used calculate the height of the text line, so it can be spaced evenly vertically. When displayHelpers are visible, the yellow box should extend from the baseline to the top of the main mass of your letterforms.
heightOffsetPct = 0.73

# show this to help set theHeight offset. 
displayHelpers = False

def main():
    variableFontInfo()
    setup()
    drawFrames()
    
    if saveEnabled:
        saveImage(exportPath)    

def setup():
    newDrawing()
    prepKeyframes()
    setBlockHeights()
    setBlockYpositions()
    

def variableFontInfo():
    for textBlock in textBlocks:
        print('---')
        print(textBlock['text'])
        for axis, data in listFontVariations(textBlock['fontPath']).items():
            print((axis, data))
    
def prepKeyframes():
    if shouldEqualizeKeyframePct:
        equalizeKeyframePct()
    addIndexesToTextBlocks()
        
def addIndexesToTextBlocks():
    for textBlock in textBlocks:
        for keyframe in textBlock['keyframes']:
            keyframe['frameIndex'] = int((numFrames-1) * keyframe['pct'])
            
def equalizeKeyframePct():
    for textBlock in textBlocks:
        i = 0
        for keyframe in textBlock['keyframes']:
            keyframe['pct'] = i / (len(textBlock['keyframes']) - 1)
            i += 1
    
def drawFrames():
    for frameIndex in range(numFrames):
        drawFrame(frameIndex)

def addBackground():
    fill(*docColor)
    rect(0,0, docWidth, docHeight)
    drawGrid()
    
def drawGrid():
    stroke(0)
    sWidth = 4
    strokeWidth(sWidth)
    fill(*docColor)
    rect(sWidth * .5, sWidth * .5, docWidth - sWidth, docHeight - sWidth)
    for row in range(int(numRows)):
        if row > 0:  
            y = rowHeight * row
            line((0, y), (docWidth, y))
    
    for col in range(int(numCols)):
        if col > 0:  
            x = colWidth * col
            line((x, 0), (x, docHeight))
    
def getCenterPos(index):
    row = math.ceil((index / numRows))
    col = (((index - 1) % numCols)) 
    x = (colWidth * col) + (colWidth / 2)
    y = docHeight - (rowHeight * row) + (rowHeight / 2)
    
    return(x, y)     
            
def drawFrame(frameIndex):
    newPage(docWidth, docHeight)

    addBackground()
    frameDuration(defaultFrameDuration)
    
    i = 1
    for textBlock in textBlocks:
        drawHelper(textBlock)
        axesVals = frameAxesVals(frameIndex, textBlock)
        x,y = getCenterPos(i)
        setMainText(textBlock, (x + textBlock['xOffset']), (y + textBoxVerticalOffset + textBlock['lineHeightOffset']), axesVals)
        i += 1
       

def frameAxesVals(frameIndex, textBlock):
    keyframes = relevantKeyframes(frameIndex, textBlock)
    pct = pctBetweenKeyframes(frameIndex, keyframes)
    easedPct = easeInOutQuad(pct, 0, 1, 1)
    # t is the current time (or position) of the tween.
    # b is the beginning value of the property.
    # c is the change between the beginning and destination value of the property.
    # d is the total time of the tween.

    axes = axisValsAtPct(easedPct, keyframes)
    return axes
    
def axisValsAtPct(pct, keyframes):
    axes = []
    for axis in keyframes[0]['axes']:
        a = {}
        minVal = keyframes[0]['axes'][axis]
        maxVal = keyframes[1]['axes'][axis]
        axes.append({axis: float((maxVal - minVal) * pct + minVal)
        })
    return axes

def easeInOutQuart(t, b, c, d):
    # t is the current time (or position) of the tween.
    # b is the beginning value of the property.
    # c is the change between the beginning and destination value of the property.
    # d is the total time of the tween.
	t /= d/2
	if t < 1:
		return c/2*t*t*t*t + b
	t -= 2
	return -c/2 * (t*t*t*t - 2) + b
	
def easeInOutQuad(t, b, c, d):
	t /= d/2
	if t < 1:
		return c/2*t*t + b
	t-=1
	return -c/2 * (t*(t-2) - 1) + b

def pctBetweenKeyframes(frameIndex, keyframes):
    frameSpan = keyframes[1]['frameIndex'] - keyframes[0]['frameIndex']
    if frameSpan == 0:
        frameSpan = 1
    framesIntoKeyframe = frameIndex - keyframes[0]['frameIndex']
    pctComplete = framesIntoKeyframe / frameSpan
    return pctComplete

def relevantKeyframes(frameIndex, textBlock):
    minKeyframe = list(filter(lambda x: x['frameIndex'] <= frameIndex, textBlock['keyframes']))
    maxKeyframe = list(filter(lambda x: x['frameIndex'] >= frameIndex, textBlock['keyframes']))
    return minKeyframe[len(minKeyframe)-1], maxKeyframe[0]
    
def setBlockHeights():
    # calculate height of text
    for textBlock in textBlocks:
        tbHeight = (textBlock['textSize'] * heightOffsetPct)
        textBlock['height'] = tbHeight
        
def setBlockYpositions():
    # calculate y position of line
    textBlockHeightTotal = sum(textBlock['height'] for textBlock in textBlocks)
    spacerHeightTotal = len(textBlocks) * spaceBetweenBlocks
    totalHeight = textBlockHeightTotal + spacerHeightTotal
    top = docHeight - ((docHeight - totalHeight) / 2) + textBoxVerticalOffset

    for textBlock in textBlocks:
        textBlock['yPos'] = top - textBlock['height']
        top = top - textBlock['height'] - spaceBetweenBlocks
        
def drawHelper(textBlock):
    # draws helper bg
    if displayHelpers:
        strokeWidth(0)
        fill(255, 255, 0)
        rect(0, textBlock['yPos'], docWidth, textBlock['height'])
        
        strokeWidth(1)
        stroke(255,0,0)
        yMiddle = textBlock['yPos'] + (textBlock['height'] / 2)
        
        line((0, yMiddle), (docWidth, yMiddle))

        strokeWidth(0)    
    
def setMainText(textBlock, xPos, yPos, axes):
    c = textBlock['textColor']
    txt = FormattedString()

    for axis in axes:        
        txt.fontVariations(**axis)

    txt.font(textBlock['fontPath'])


    txt.append(textBlock['text'], 
        fontSize=textBlock['textSize'], 
        lineHeight=textBlock['textSize'], 
        fill=(c))
    text(txt, (xPos,yPos), align="center")      


main()