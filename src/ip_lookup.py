from ipwhois import IPWhois

def get_ip_info(ip):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        return res['network']['name'], res['asn_description']
    except:
        return None, "Unknown"
