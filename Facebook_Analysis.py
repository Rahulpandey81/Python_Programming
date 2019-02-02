import json
import facebook
import requests




def main():
        
    token = "#Paste Token Here"
    mail=input("Enter your Email to Check your Facebook Acount Detail")
    if(mail=='rahulpandey.rp1996@gmail.com'):
        mail=token
        
    graph = facebook.GraphAPI(mail)
	
    profile = graph.get_object('me',fields='name,location,link,email,age_range,languages,hometown,birthday,friends,context')	
        
	
    print(json.dumps(profile, indent=4))


if __name__ == '__main__':
	main()


