from pygame import*                                      #Initialisation de l'extension pygame pour run le jeu
init()
fenetre=display.set_mode((850,500),RESIZABLE)
fond=image.load("fond.jpg").convert()                   #Chargement des images requis pour le jeu
brick=image.load("brick.jpg").convert_alpha()
raquette=image.load("raquette.jpg").convert_alpha()
balle=image.load('balle.jpg').convert_alpha()


xr=200
yr=480
xb=300
yb=450
dimbrickx=brick.get_size()[0]                           #Dimensions des briques
dimbricky=brick.get_size()[1]                 
fenetre.blit(fond,(0,0))
fenetre.blit(balle,(xb,yb))
fenetre.blit(raquette,(xr,yr))
display.flip()

continuer=1
m=[[1,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]        #Matrice 1

while continuer:
    time.Clock().tick(500)
    for evenements in event.get():
        if evenements.type==QUIT:
            continuer=0
    keyb=key.get_pressed()                                                 # gestion du clavier pour les deplacements
    if keyb[K_LEFT]:xr=xr-1
    if keyb[K_RIGHT]:xr=xr+1

    if xr>200 or xr<200:
        xb=xr
    
       
    fenetre.blit(fond,(0,0))
    fenetre.blit(raquette,(xr,yr))
    fenetre.blit(balle,(xb,yb))
    
    for i in range(3):                                                       #Affichage des briques
        for j in range(10):
            if m[i][j]==1:
                   fenetre.blit(brick,(j*dimbrickx,i*dimbricky))
                
               
         
    display.flip()

        
        

quit()




















