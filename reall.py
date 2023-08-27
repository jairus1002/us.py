from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd_callback():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        
        print(request.get_data())  # Print the raw request data for inspection
        
        if content_type == 'application/json':
            data = request.json
            session_id = data['sessionId']
            phone_number = data['phoneNumber']
            user_input = data['text']

            # Implement logic based on user's input
            if user_input == '':
                response = "CON Welcome to our USSD service.\n1. Option A\n2. Option B"
            elif user_input == '1':
                response = "CON You chose Option A.\nReply with:\n1. Confirm\n2. Cancel"
            elif user_input == '1*1':
                response = "END You confirmed Option A. Thank you!"
            elif user_input == '1*2':
                response = "END You canceled Option A. Thank you!"
            elif user_input == '2':
                response = "CON You chose Option B.\nPlease provide your feedback:"
            else:
                response = "CON Invalid input. Please try again."

            return jsonify(
                {
                    "sessionId": session_id,
                    "phoneNumber": phone_number,
                    "text": response
                }
            )
        else:
            return "Unsupported Media Type", 415

if __name__ == '__main__':
    app.run(debug=True)
