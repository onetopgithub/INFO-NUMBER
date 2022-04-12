# INFO-NUMBER
Info number es para doxxear ah una persona fácil mente
░█████╗░██╗░░██╗░░░░░░████████╗██╗██╗░░██╗
██╔══██╗██║░██╔╝░░░░░░╚══██╔══╝██║██║░██╔╝
███████║█████═╝░█████╗░░░██║░░░██║█████═╝░
██╔══██║██╔═██╗░╚════╝░░░██║░░░██║██╔═██╗░
██║░░██║██║░╚██╗░░░░░░░░░██║░░░██║██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░░░╚═╝░░░╚═╝╚═╝░░╚═╝
------------------------------------------
creador:ak._mxrtxn
tiktok:ak._mxrtxn
instagram:X  Swgayy X
python: dxlswb
-----------------------
ponga un numero y ya lo doxxea ejemplo:+5693663144

api_key = '7e1cadf1fc1587fd37db7ea1e6c29a50'

number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))
