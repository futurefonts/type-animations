import sys
sys.path.append('../') # this lets us import utils
from utils.hexToRgb import RGBfromHex



fontPath = "../fonts/CheeeVariable.ttf"

exportPath = "./exports/CheeeMood.gif"

docWidth=800
docHeight=int(docWidth * 0.480814)

saveEnabled = True

docColor = RGBfromHex('#ffffff')
defaultTextColor = RGBfromHex('#000000')

numFrames = 50
defaultFrameDuration = 0.08

textSize = 220
leading = textSize * 1.2

textBlocks = []

textBlocks.append({
    "text": 'MOOD', 
    "textSize": textSize, 
    "textColor": defaultTextColor, 
    "lineHeightOffset": 0,
    "keyframes": [
        {
            "pct": 0,
            "axes": {
                "yest": 0,
                "grvt": 0
            }
        },
        {
            "pct": .25,
            "axes": {
                "yest": 0,
                "grvt": 1000
            }
        },
        {
            "pct": .5,
            "axes": {
                "yest": 1000,
                "grvt": 1000
            }
        },
        {
            "pct": .75,
            "axes": {
                "yest": 1000,
                "grvt": 0
            }
        },
        {
            "pct": 1,
            "axes": {
                "yest": 0,
                "grvt": 0
            }
        }
    ]
})

shouldEqualizeKeyframePct = False

spaceBetweenBlocks = leading - textSize 

textBoxVerticalOffset = -15

# Change this for each font. It's used calculate the height of the text line, so it can be spaced evenly vertically. When displayHelpers are visible, the yellow box should extend from the baseline to the top of the main mass of your letterforms.
heightOffsetPct = 0.65

# show this to help set theHeight offset. 
displayHelpers = False

def main():
    setup()
    drawFrames()
    
    if saveEnabled:
        saveImage(exportPath)    

def setup():
    variableFontInfo()
    newDrawing()
    #setCurrentLetter(letter)
    prepKeyframes()
    setBlockHeights()
    setBlockYpositions()
    
def setCurrentLetter(letter):
    for textBlock in textBlocks:
        textBlock['text'] = letter
        
    
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
            
def drawFrame(frameIndex):
    newPage(docWidth, docHeight)

    addBackground()
    frameDuration(defaultFrameDuration)
    
    i = 1
    for textBlock in textBlocks:
        drawHelper(textBlock)
        axesVals = frameAxesVals(frameIndex, textBlock)
        setMainText(textBlock, docWidth/2, textBlock['yPos'], axesVals)
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
        
def variableFontInfo():
    for axis, data in listFontVariations(fontPath).items():
        print((axis, data))
    
def setMainText(textBlock, xPos, yPos, axes):
    c = defaultTextColor
    txt = FormattedString()

    for axis in axes:        
        txt.fontVariations(**axis)

    txt.font(fontPath)


    txt.append(textBlock['text'], 
        fontSize=textBlock['textSize'], 
        lineHeight=textBlock['textSize'], 
        fill=(c))
    text(txt, (xPos,yPos), align="center")      


main()