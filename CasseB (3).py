from pygame import*                                      #Initialisation
init()
fenetre=display.set_mode((1000,1000),RESIZABLE)
fond=image.load("fond.jpg").convert()                   #Chargement des images
brick=image.load("brick.jpg").convert_alpha()
raquette=image.load("raquette.jpg").convert_alpha()
balle=image.load('balle.jpg').convert_alpha()


xr=200
yr=500
xb=250
yb=400
deplax=1
deplay=1
coli=0

dimbrickx=brick.get_size()[0]                           #Dimensions brique
dimbricky=brick.get_size()[1]                 
fenetre.blit(fond,(0,0))
fenetre.blit(balle,(xb,yb))
fenetre.blit(raquette,(xr,yr))
display.flip()

continuer=1
m=[[1,1,0,1,1,1,1,1,1,1],[1,1,1,1,1,0,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]        #Matrice 1

while continuer:
    time.Clock().tick(500)
    for evenements in event.get():
        if evenements.type==QUIT:
            continuer=0
    keyb=key.get_pressed()                                                 # gestion du clavier
    if keyb[K_LEFT]:xr=xr-1
    if keyb[K_RIGHT]:xr=xr+1

    xb+=deplax
    yb+=deplay

    if xb==500 or xb==0: deplax=-deplax
       
    fenetre.blit(fond,(0,0))
    fenetre.blit(raquette,(xr,yr))
    fenetre.blit(balle,(xb,yb))
    
    for i in range(3):                                                       #Affichage briques
        for j in range(10):
            if m[i][j]==1:
                   fenetre.blit(brick,(j*dimbrickx,i*dimbricky))

            if coli>75 and Rect((xr,yr),(raquette.get_size()[0],raquette.get_size()[1])).colliderect(Rect((xb,yb),(balle.get_size()[0],balle.get_size()[1]))):
                coli=0
                deplay=-deplay
            coli+=1


            if xr>300:
              xr=300
            if xr<0:
              xr=0
    
                
               
         
    display.flip()

        
        

quit()
