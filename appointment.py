from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

from twilio.rest import Client

account_sid = 'AC5eea7b020cce1f7bad28a590607a95b7'
auth_token = 'b6b3688c57e13bdd2ec20426385835eb'
client = Client(account_sid, auth_token)

user_state = {}

@app.route("/wbot", methods=["POST"])
def bot():
    inmsg=request.values.get("Body","").strip().lower()
    response=MessagingResponse()
    msg=response.message()
    sender_number = request.values.get("From")
   

    if sender_number in user_state and user_state[sender_number] == "awaiting_date":
        msg.body(f"Booking confirmed for {inmsg}.")
        del user_state[sender_number]
       
    elif "hello" in inmsg:
        msg.body("Hello, Welcome to SwasthyaConnect. I am here to help connect you")
        msg.body("with a doctor for your health concerns.")
        msg.body("Please tell me your symptoms or the issues you are facing today")
       
       
    elif "headache" in inmsg and len(inmsg)==8:
        msg.body("Thank you for reaching out, I am here to assist you")
        msg.body("You mentioned you have a headache. ")
        msg.body("How long have you been experiencing the headache?")
        msg.body("Is it mild, moderate or severe?")
        msg.body("Do you have any other symptoms, like nausea or dizziness or fever ?")
        msg.body("This will help us find the right doctor for you")

    elif "mild" in inmsg:
            msg.body("You can contact Dr. R.G. Sharma for an appointment. He is free on Monday, Wednesday, Friday from 12-3pm. Let us know which time is most suitable for you and I will book an appointment with him accordingly.")
    elif "moderate" in inmsg:
            msg.body("You can contact Dr. R.G. Sharma for an appointment.He is free on Tuesday and Wednesday from 11-2pm. Let us know which time is most suitable for you and I will book an appointment with him accordingly.")
    elif "severe" in inmsg:
            msg.body("You can contact Dr. R.G. Sharma for an appointment. He is free on Monday, Thursday, Saturday from 3-5pm. Let us know which time is most suitable for you and I will book an appointment with him accordingly.")
       
    elif "appointment" in inmsg:
        msg.body("Mention the date you are looking for appointment")
        user_state[sender_number] = "awaiting_date"
    elif "bye" in inmsg:
        msg.body("Thanks for connecting, I will book that time for you")
       
   
    else:
        msg.body("I am sorry, I don't understand")
    return str(response)

app.run(port=5000)
