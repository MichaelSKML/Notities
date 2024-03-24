Notes maandag - 11 maart 2024

LINUX   
  is een operating system. Veel gebruikt bij servers, overal wel te vinden.
  bestaat uit een kernel en een operating system, gebaseerd op UNIX (OS)
  veel versies linux

  belangrijkste verschil/voordeel tussen andere OS, is dat Linux open-source is.

  voornamelijk op de commandline gebruikt, want niet nodig bij o.a. servers.
  gebruiken dezelfde commando's op commandline in de versies (flavors, zoals debiant)

  ander voordeel: weinig virussen bij linux. er worden weinig virussen geschreven voor linux.
    virussen hebben normaal gesproken geen superuser rechten, dus bij linux heeft het geen rechten tot OS.

  Bij installatie linux maak je een superuser acc aan en een gebruikersaccount. 
    houdt alles goed gescheiden -> stabiliteit

  Om linux te laten draaien heb je een device nodig. 
    zoals raspberry pi of andere apparaten natuurlijk.

  ander verschil tussen windows en linux is hoe schijven zijn ingedeeld.
    linux hebben geen schijven, het ziet alles als als mapjes, veel compartementisatie -> veiliger
      voordeel om linux voor servers te gebruiken

---------------------------------------------------------------------
AZURE 

  Is een hosting system/cloud service 

  Virtual machine createn.
    Ubuntu installeren via Azure 22.04 LTS x64

  porten zijn toegangen tot de server 
    selecteren welke porten we willen gebruiken (HTTP, HTTPS, SSH), anders kunnen we niet in de server komen 

  In directory 
    ~ betekent home directory 
    / is root van server
    / losstaand is naar root gaan 

  in het groen is een shortcut 

  boot map: belangrijkste map, kunnen we niet veel mee 

  media map: als je een usb insteekt, komt ie daar uit 

  Linux silent bash: als ie geen error geeft, dan kan je ervan uitgaan dat een command is uitgevoerd 

  commandos:
  pwd: current/working directory (eerste slash is de root)
  cd: change directory
  cd ~: change directory naar home directory
  cd / : naar root 
  ls: laat zien wat er in map zit 
  touch bestandsnaam.txt : bestand aanmaken
  cd ..: 1 map omhoog 
  clear: clear scherm 
  ls -R : recursive, wat er allemaal in alle mappen onder huidige map zit 
    - is een flag, extra command 
  ctrl C : stoppen van command, cancel knop. 
  ls -al : lijst in kolom 
  nano bestandsnaam.txt: bestand aanpassen inhoud 
    ^ betekent ctrl gebruiken 
  cat bestandsnaam.txt: vertelt inhoud van bestand (als er inhoud is)
  nano zonder bestandsnaam kan ook gebruikt worden om nieuwe txt bestand aan te maken, naast aanpassen
  nano moet altijd met een extensie gebruikt worden (kan alle bestandstypen zijn)
  rm bestandsnaam: remove file 
  mkdir mapnaam: make directory/map 
  mv bestandsnaam mapnaam: file verplaatsen naar map (als beide in zelfde dir zitten)
  mv bestandsnaam helepathnaam: verplaatsen naar map in andere directory
  mv bestandsnaam ~ : verplaatsen naar home dir
  cp bestandsnaam mapsnaam: file kopieren naar map 
  cp bestandsnaam anderbestandsnaam : kopieren met andere bestandsnaam
  ls -a: lijst met alle items (ook onzichtbare dingen)
  rm -r mapsnaam: verwijdert alle items in map en dan verwijdert het map 
  rmdir mapsnaam: verwijdert ook map 
    (maar map moet leeg zijn eerst), rm -r mapsnaam gebruiken is beter daarom
  rm * : verwijdert bestanden, in map waar je in zit 
    * is een wildcard, staat voor all 
  rm *.bestandstypen: verwijdert alles met bestandstypen die je hebt genoemd
  rm test?.*
    ? is ook een wildcard, geeft een karakter aan. 
  rm *test* : verwijdert alles waar test in voorkomt 

  Linux is hoofdlettergevoelig itt windows en mac
    bij commando's en ook bij filenames 
  met pijltje omhoog/omlaag kan je door commando's heen gaan die je hebt gebruikt 
    die je in dezelfde dir hebt gebruikt 
  tab : autocomplete 
  man commando : manual, laat zien wat je met commando kan doen 
  commando --help: laat ook zien wat meest gebruikte flags zijn
  rm -r * : verwijdert files en mappen 
    -r hier als er ook mappen inzitten 


  $ reguliere gebruiker, # superuser 
  sudo apt update : checken voor update 
    sudo zorgt ervoor dat je superuser rechten hebt 
  sudo commando : commando uitvoeren als superuser 

  ping IP adres : kijken of andere server actief 
 
  LAMP stack: om websites of applicaties te maken  
  Linux (OS) 
  apache (apach2): webserver 
  mariaDB/MySQL: database server
  PHP: taal 

  sudo apt update 
  sudo apt install apache2 -y (-y betekent yes op alles)

  sudo service apache2 status : status zien van apache
  "" stop/start/reload 

  sudo apt install mariadb-server

  phpadmin: user interface voor de database 

  sudo mysql_secure_installation (voor securen database)

  sudo apt install phpmyadmin

  sudo apt install php 

  webserver + database installeren, andere groep php 
-----------------------------------
