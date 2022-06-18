import whois 
from library import module



def whoisdomin(domin):
    module.log('whois start')
    try:
        doc = whois.whois(domin)
        for key in doc:
            if type(doc.get(key)) == str:
                module.autosave(domin,key)
                module.writeout(domin , "    " + doc[key])
            elif type(doc.get(key)) == list:
                module.autosave(domin,key)
                module.writeout(domin,key)
                for lock in doc[key]:
                    module.autosave(domin,"    " + lock)
                    module.writeout(domin,key)
        module.log('whois end')
    except:
        module.log('whois error')










    

    




# "domain_name": [
#   "GOOGLE.COM",
#    "google.com"D
#  ],
#  "registrar": "MarkMonitor, Inc.",
#  "whois_server": "whois.markmonitor.com",
#  "referral_url": null,
#  "updated_date": "2019-09-09 15:39:04",
#  "creation_date": [
#    "1997-09-15 04:00:00",
#    "1997-09-15 07:00:00"
#  ],
#  "expiration_date": [
#    "2028-09-14 04:00:00",
#    "2028-09-13 07:00:00"
#  ],
#  "name_servers": [
#    "NS1.GOOGLE.COM",
#    "NS2.GOOGLE.COM",
#    "NS3.GOOGLE.COM",
#    "NS4.GOOGLE.COM",
#    "ns4.google.com",
#    "ns3.google.com",
#    "ns1.google.com",
#    "ns2.google.com"
#  ],
#  "status": [
#    "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
#    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
#    "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",
#    "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",
#    "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",
#    "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited",
#    "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
#    "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
#    "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)",
#    "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)",
#    "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)",
#    "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
#  ],
#  "emails": [
#    "abusecomplaints@markmonitor.com",
#    "whoisrequest@markmonitor.com"
#  ],
#  "dnssec": "unsigned",
#  "name": null,
#  "org": "Google LLC",
#  "address": null,
#  "city": null,
#  "state": "CA",
# "zipcode": null,
#  "country": "US"

#{
#"domain_name": null,
#"registrar": null,
#"whois_server": null,
#"referral_url": null,
#"updated_date": null,
#"creation_date": null,
#"expiration_date": null,
#"name_servers": null,
#"status": null,
#"emails": "iri.efc@gmail.com",
#"dnssec": null,
#"name": null,
#"org": null,
#"address": null,
#"city": null,
#"state": null,
#"zipcode": null,
# "country": null
#}
