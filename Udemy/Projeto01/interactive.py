import pygame

listBox = [] # this list used to store all object inside

listBox.append(("text", pos, size, bgColor, textColor, InteractAction)) 
# add dumy object to the list, "text" can be empty if you dont want.

def InteractAction(mousePos):  # sample action used to tie to object
    print("do somehthing")    

def newDrawBox(IableO):
      pygame.draw.rect(gameDisplay, IableO[3],(IableO[1][0], IableO[1][1], IableO[2][0], IableO[2][1]))
      text = basicfont.render(str(IableO[0]), True,IableO[4], None)
      textrect = text.get_rect()
      textrect.centerx = IableO[1][0] + IableO[2][0] / 2
      textrect.centery = IableO[1][1] + IableO[2][1] / 2
      gameDisplay.blit(text, textrect)

while not gameExit:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Mouse[event.button] = 1
            Mouse[0] = (event.pos[0], event.pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            Mouse[event.button] = 0
            Mouse[0] = (event.pos[0], event.pos[1])
#-------- check if mouse is click on any object in the list of Interatable object
  if Mouse[1] == 1:
        for x in listBox:
            if x[1][0] < Mouse[0][0] < x[1][0] + x[2][0] and x[1][1] < Mouse[0][1] < x[1][1] + x[2][1]:
                x[5](Mouse[0])
#---- draw all object -----
  for x in listBox:
        newDrawBox(x)