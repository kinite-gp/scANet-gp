from urllib import response
import whois 

def getwhois(domin):
    whoisinfo = whois.whois(domin)
    
    response = f"""
Whois site {domin} 


---------------------------------------"""
