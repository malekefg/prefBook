# coding: utf-8
#!/usr/bin python3

import datetime
import re
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def main():

        url_B ='http://www.seine-saint-denis.gouv.fr/booking/create/1194/0'

        s='existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        data = {'condition': 'on','nextButton': 'Effectuer une demande de rendez-vous'}
        MSG_1 ='RDV indispobibles  '
        ERR_1 ='Something went wrong in email section  '
        ERR_2 ='ERROR in HTTP request not 200 but -> '
        ERR_3 ='Erreur dans le passage des paramètres de la requête HTTP : Headers ou DATA'
        EMPT ='     '


        #f= open("logPrefReq.txt","a+")
        #f.write("### Fichier Log d'accès web ###\n\n\n")
        #f.close()

        try:
                result_B = requests.post(url_B,headers=headers,data=data)
                Searchresult = re.search(s, result_B.content.decode())
                print(result_B.status_code)
                if result_B.status_code == 200  :
                        if Searchresult : 
                                print (MSG_1)
                                f=open("logPrefReq.txt", "a+")
                                f.write('Time :  '+ str(datetime.datetime.now())+EMPT+MSG_1+'\n')
                                f.close()
                        else :
                                try:
                                        _FROM = 'from@email.com'
                                        _TO = 'to@email.com'
                                        gmail_user=_FROM
                                        gmail_password='passwd'
                                        gmail_smtp='smtp.email.com'
                                        server = smtplib.SMTP_SSL(gmail_smtp, 465)
                                        server.ehlo()
                                        server.login(gmail_user, gmail_password)
                                        msg = MIMEMultipart()
                                        msg['Subject'] = 'Alerte RDV BOBIGNY Disponibles'
                                        server.sendmail(_FROM,_TO,msg.as_string())
                                        server.close()
                                        print (c)
                                        f=open("logPrefReq.txt", "a+")
                                        f.write('Time : '+ str(datetime.datetime.now())+EMPT+'Email sent - OK\n')
                                        f.close()
                                except:
                                        print (ERR_1)
                                        f=open("logPrefReq.txt", "a+")
                                        f.write('Time : '+ str(datetime.datetime.now())+EMPT+ERR_1+'\n')
                                        f.close()
                else :  
                        f=open("logPrefReq.txt", "a+")
                        f.write('Time : '+ str(datetime.datetime.now())+EMPT+ERR_2+str(result_B.status_code)+'\n')
                        f.close()
        except: 
                f=open("logPrefReq.txt", "a+")
                f.write('Time : '+ str(datetime.datetime.now())+EMPT+ERR_3+'\n')
                f.close()
if __name__== "__main__":
  main()