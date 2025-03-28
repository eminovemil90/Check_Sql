import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-u","--url",dest="url",help="Buraya saytin url-i daxil edin")
(user_input,args) = parser.parse_args()

url=user_input.url

if not url:
    url=input("Url-i yazin:")



url =user_input.url

command=['sqlmap','-u',url,'--batch','--dbs']
result = subprocess.check_output(command)

if b'available databases' in result:
    print("Sayt sql injectiona qarsi hessasdir")
else:
    print("Sayt sql injectiona qarsi hessas deyil")











