from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)
app.debug = True
app.config['JSON_AS_ASCII']=False

devices = []

cats_data = []


@app.route('/api/devices')
def devicess():
    data = {
        "devices":devices
    }
    print(data)
    # data = json.dumps(data, ensure_ascii=False)
    return jsonify(data)

@app.route('/api/cat_data',methods=['POST'])
def post_cat_data():
    data = {
        "device" : request.form['device'],
        "left_food" : request.form['left_food'],
        "arrive_time" : request.form['arrive_time'],
        "leave_time" : request.form['leave_time']
    }

    for device in devices:
        if(data["device"]==device["device_id"]):
             cats_data.append(data)
             return jsonify(
                    {
                        "status" : True,
                        "error" : None
                    }
            )


    return jsonify(
        {
            "status" : False,
            "error" : "없는 디바이스입니다."
        }
    )

@app.route('/api/register_devices',methods=['POST'])
def device():
    data = {
            "device_id" : request.form['device_id'],
            "korean_adress": request.form['korean_adress'],
            "latitude": request.form['latitude'],
            "longtitude": request.form['longtitude'],
            "description": request.form['description'],
            "install_data": request.form['install_data'],
        }
    devices.append(data)
    return jsonify({
        "status" : True,
        "error" : None
    })


if __name__ == '__main__':
    app.run()
