# HoneyPots - Project Code: Nanners


Nginx - 

Setup:
1) Install NGINX: yum install nginx
2) setup the service to start at boot: chkconfig nginx on
3) setup a contab -e to execute the python code every minute:  contab -e

Purpose:  
This will check the nginx access log's to see if anyone has access the device and send off a hipchat alert.  Future revisions will include an alerts.py or something along those lines to setup how the alert should be delivered. 
