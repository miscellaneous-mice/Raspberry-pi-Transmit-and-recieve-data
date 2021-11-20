# Raspberry-pi-Transmit-and-recieve-data

TO RECIEVE
-- -------


first install by command:
pip install requests

now to run the command after making a api file which is attached type
sudo python api.py

now to display information first go to thinkspeak.com > thinghttp > newthinghttp 
now inspect the page of any website you want to retrieve data from inspect the page take the xpath of the particular info you are interested in retrieving from that website.
paste it in the parse string then also past the website url link in the link section.

next the website gives you a link, copy that and paste it in the api file in the link space which is what you want to print.





TO TRANSMIT
-- --------

sudo apt-get install apache2 -y    //to install apache forsetting up a website using your dynamic ip address

ifconfig                           //to check your raspberry pi's dynamic ip address 

cd /var/www                        //to navigate to the url

cd html                              
ls                                  // navigating to the html file we get the file name as filename.html

sudo chown pi: filename.html        // to be able to edit the webpage 
sudo rm filename.html               // to clear the file
sudo nano filename.html             // to start editing you own website page


**** as it is dyanmic ip address each time the ip address may change so to maintain static ip address use some tracking software as duck dns or maybe use static ip address
by going to any website that gives you an permanent url ****







