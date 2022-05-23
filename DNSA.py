import dns.resolver
from tqdm import tqdm

myResolver = dns.resolver.Resolver()
myResolver.nameservers = ['8.8.8.8','223.5.5.5']

with open("/root/Workspace/twmeasure/gov.tw.subdomain.A",'w+') as ouf:
    with open("/root/Workspace/twmeasure/gov.tw.subdomain",'r') as inf:
        for line in tqdm(inf.readlines()):
            line = line.strip()
            try:
                result = myResolver.resolve(line, raise_on_no_answer=False, lifetime=3)
            except Exception as e:
                print(e)
                continue
            for ipval in result:
                # print(ipval)
                ouf.write(ipval.to_text()+"," + line + "\n")
