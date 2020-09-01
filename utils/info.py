import drawbot

def variableFontInfo(fontPath):
  for axis, data in listFontVariations(fontPath).items():
    print((axis, data))
  # print('hello')