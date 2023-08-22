firstRow = []
secondRow = []
thirdRow = []
endXofset = 0
import numbers

def Translate(Row):
  global gCode    
  global endXofset

  for item in Row: 
    if item == '1':
      gCode = gCode + 'G0 Z-5;\nG0 Z5;\n'   # "1" --> Press down
    elif item == '2':
      gCode = gCode + 'G0 X2;\n'            # "2" --> Move right 2 mm
      endXofset = endXofset + 2    # Add 2 to line offset
    elif item == '4':
      gCode = gCode + 'G0 X4;\n'            # "4" --> Move right 4 mm
      endXofset = endXofset + 4    # Add 4 to line offset
    elif item == '0':
      gCode = gCode + ''                    # "0" --> Nothing
    else:
      gCode = gCode + ';error\n'

def Append():   # For each row, add the two corresponding digits
  if len(nxt) == 6:
      firstRow.append(nxt[0])   # Two top digits
      firstRow.append('2')
      firstRow.append(nxt[3])
      firstRow.append('4')

      secondRow.append(nxt[1])    # Two middle digits
      secondRow.append('2')
      secondRow.append(nxt[4])
      secondRow.append('4')

      thirdRow.append(nxt[2])   # Two bottom digits
      thirdRow.append('2')
      thirdRow.append(nxt[5])
      thirdRow.append('4')

  else:                         # Here we have double the number of digits so as to take into ccount the CAPITAL letter symbols
     firstRow.append(nxt[0])
     firstRow.append('2')
     firstRow.append(nxt[3])    # Four top digits
     firstRow.append('4')
     firstRow.append(nxt[6])
     firstRow.append('2')
     firstRow.append(nxt[9])
     firstRow.append('4')

     secondRow.append(nxt[1])
     secondRow.append('2')
     secondRow.append(nxt[4])   # Four middle digits
     secondRow.append('4')
     secondRow.append(nxt[7])
     secondRow.append('2')
     secondRow.append(nxt[10])
     secondRow.append('4')

     thirdRow.append(nxt[2])
     thirdRow.append('2')
     thirdRow.append(nxt[5])   # Four bottom digits
     thirdRow.append('4')
     thirdRow.append(nxt[8])
     thirdRow.append('2')
     thirdRow.append(nxt[11])
     thirdRow.append('4')


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


xStart = int(input('Enter X start position under 235\n'))   # Algorithm starts here 
while xStart > 235:
  print('value over 235, chose smaller number')
  xStart = int(input('Enter new X start position.\n'))    # Get start location for X axe 
print('\n')

yStart = int(input('Enter Y start position under 235.\n'))
while yStart > 235:
  print('value over 235, chose smaller number')
  yStart = int(input('Enter new Y start position.\n'))    # Get start location for Y axe
print('\n')


gCode = 'G90;\nG0 Z5;\nG0 X'+ str(xStart) + ' Y' + str(yStart) + ';\n' + 'G91;\n'   # Add start location instructions to G-Code

text = input('Enter what you want to type.\n')

listOfCharacters = []
numbers = []
nbrOn = False

for letter in text:
  listOfCharacters.append(letter)   # Create an array with every character

for i in range(len(listOfCharacters)):    # Create an array with only the digits
  if listOfCharacters[i].isdigit(): 
    numbers.append(i)

for i in range(len(listOfCharacters)):    # For each character

  if i in numbers:    
    if nbrOn == False:    # If it is in the array of numbers and the previous character wasn't, add the number symbol
      nxt = '001111'    
      Append()
      nbrOn = True
  else:
    if nbrOn == True:   # If it isn't in the array of numbers but the previous character was, add the 'back to letters' symbol
      nxt = '000011'
      Append()
      nbrOn = False

  match listOfCharacters[i]:    # Use the dictionnary to find which 6-digit code the character corresponds to
    case " ":
      nxt = '000000'
    case "a":
      nxt = '100000'
    case "b":
      nxt = '110000'
    case "c":
      nxt = '100100'
    case "d":
      nxt = '100110'
    case "e":
      nxt = '100010'
    case "f":
      nxt = '110100'
    case "g":
      nxt = '110110'
    case "h":
      nxt = '110010'
    case "i":
      nxt = '010100'
    case "j":
      nxt = '010110'
    case "k":
      nxt = '101000'
    case "l":
      nxt = '111000'
    case "m":
      nxt = '101100'
    case "n":
      nxt = '101110'
    case "o":
      nxt = '101010'
    case "p":
      nxt = '111100'
    case "q":
      nxt = '111110'
    case "r":
      nxt = '111010'
    case "s":
      nxt = '011100'
    case "t":
      nxt = '011110'
    case "u":
      nxt = '101001'
    case "v":
      nxt = '111001'
    case "w":
      nxt = '010111'
    case "x":
      nxt = '101101'
    case "y":
      nxt = '101111'
    case "z":
      nxt = '101011'  
    case ".":        #SPECIAL CHARACTERS ---------------------
      nxt = '001000'
    case ",":
      nxt = '010000'
    case "?":
      nxt = '010001'
    case ";":
      nxt = '011000'
    case "!":
      nxt = '011010'
    case '"':
      nxt = '011001'
    case "(":
      nxt = '110001'
    case ")":
      nxt = '001110'
    case "-":
      nxt = '001001'
    case "*":
      nxt = '001010'
    case "&":
      nxt = '111101'  
    case "A":        #CAPITAL LETTERS ---------------------
      nxt = '000101100000'
    case "B":
      nxt = '000101110000'
    case "C":
      nxt = '000101100100'
    case "D":
      nxt = '000101100110'
    case "E":
      nxt = '000101100010'
    case "F":
      nxt = '000101110100'
    case "G":
      nxt = '000101110110'
    case "H":
      nxt = '000101110010'
    case "I":
      nxt = '000101010100'
    case "J":
      nxt = '000101010110'
    case "K":
      nxt = '000101101000'
    case "L":
      nxt = '000101111000'
    case "M":
      nxt = '000101101100'
    case "N":
      nxt = '000101101110'
    case "O":
      nxt = '000101101010'
    case "P":
      nxt = '000101111100'
    case "Q":
      nxt = '000101111110'
    case "R":
      nxt = '000101111010'
    case "S":
      nxt = '000101011100'
    case "T":
      nxt = '000101011110'
    case "U":
      nxt = '000101101001'
    case "V":
      nxt = '000101111001'
    case "W":
      nxt = '000101010111'
    case "X":
      nxt = '000101101101'
    case "Y":
      nxt = '000101101111'
    case "Z":
      nxt = '000101101011'
    case "1":               #NUMBERS ---------------------
      nxt = '100000'
    case "2":
      nxt = '110000'
    case "3":
      nxt = '100100'
    case "4":
      nxt = '100110'
    case "5":
      nxt = '100010'
    case "6":
      nxt = '110100'
    case "7":
      nxt = '110110'
    case "8":
      nxt = '110010'
    case "9":
      nxt = '010100'
    case "0":
      nxt = '010110'
    case _:
      print('ERROR ---> I dont know that one yet.')   

  Append()    # See function 'Append()'




gCode = gCode + ';First Row\n'
Translate(reversed(firstRow))   # See function 'Translate()' 
gCode = gCode + 'G0 X-' + str(endXofset) + ' Y-2;\n'    # Tell the 3-D printer to go to the next row, goes down 2 mm and back the length of the previous line
endXofset = 0

gCode = gCode + ';Second Row\n'
Translate(reversed(secondRow))
gCode = gCode + 'G0 X-' + str(endXofset) + ' Y-2;\n'    # Tell the 3-D printer to go to the next row, goes down 2 mm and back the length of the previous line
endXofset = 0

gCode = gCode + ';Third Row\n'
Translate(reversed(thirdRow))
gCode = gCode + 'G0 X-' + str(endXofset) + ' Y-2;\n'    # Tell the 3-D printer to go to the next row, goes down 2 mm and back the length of the previous line
endXofset = 0

print(firstRow)
print(secondRow)
print(thirdRow)
print("G-Code Generated !")   # Just some completion confirmation


text_file = open(r'Export.gcode', 'w')    # Create a text file
text_file.write(gCode)                    # Add the G-Code we generated
text_file.close()                         # Save and close
