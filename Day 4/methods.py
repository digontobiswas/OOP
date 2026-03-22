#function define e ekta extra perameter dite hobe setar nam hobe self ami chaile onno ta o dite pari

def call():
    print("CALLING SOMEONE")
    return 'CALL DONE'

class Phone:
    price= 1200
    color='blue'
    brand='samsung'
    features=['camera', 'speacker','light']

   # def call():
    def call(self):
        print("CALLING SOMEONE")
    
    def send_sms(self, contact, sms):  #self k ignor korbe baki gula asbe
        text = f'sending SMS to: {contact} and message: {sms}'
        return text  


MY_PHONE =Phone()
print(MY_PHONE.features)
# MY_PHONE.call()   if i acll this function here then output will be Phone.call() takes 0 positional arguments but 1 was given
# Its means ami 1ta perameter pathaichi but am to pathai nai
#so amake ekta perameter diya dite hobe seta k generally self bole ami chaile onno nam dibo. but normally self. self er pore bakigula dite hobe

print(MY_PHONE.send_sms('wife', 'I love you :D')) # finction define e self k ignor korbe baki gula asbe