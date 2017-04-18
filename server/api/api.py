from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)
app.debug = True
# app.config['JSON_AS_ASCII']=False

devices = []

cats_data = []


@app.route('/api/device/<device_id>')
def device(device_id):
    for device in devices:
        if(device["device_id"] == device_id):
            data = json.dumps(device,ensure_ascii=False)
            return data
    return jsonify(
        {
            "stsus" : True,
            "error" :"없는 id입니다."
        }
    )

@app.route('/api/devices')
def devicess():
    data = {
        "devices" : devices
    }
    data = json.dumps(data, ensure_ascii=False)
    return data



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
             device["cat_data"].append(data)
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
def register_device():
    data = {
            "device_id" : request.form['device_id'],
            "korean_adress": request.form['korean_adress'],
            "latitude": request.form['latitude'],
            "longtitude": request.form['longtitude'],
            "description": request.form['description'],
            "install_data": request.form['install_data'],
            "cat_data" : []
        }
    devices.append(data)
    return jsonify({
        "status" : True,
        "error" : None
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
