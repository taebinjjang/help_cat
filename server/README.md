# 서버 API document

서버주소 : http://서버주소/

## POST/api/cat_data
설명 : 이 API에서는 디바이스 정보와 음식(사료)의 잔량,
고양이가  다녀온 시간과 떠난 시간을 서버에서 받는다.

Request
```json
{
  "device" : 123456,
  "left_food" : 100,
  "arrive_time" : "YYYY-MM-DD HH:mm:SS",
  "leave_time" : "YYYY-MM-DD HH:mm:SS"
}
```
Responce
```json
{
  "status" : true,
  "error" :  null
}
```


## POST/api/register_device
설명 : 디바이스(우고도)를 초기 설치할때 이것을 설치한 위치(한국 주소, 위도, 경도)를 받고 디바이스 번호 또한 받아서 신규 디바이스를 API에 저장한다.

Request
```json
{
  "device_id" : 12345,
  "korean_adress" : "경기도 고양시 덕양구",
  "latitude" : 9.2739729,
  "longitude" : 83.33929,
  "description" : "비고",
  "install-date" : "2017-04-01"
}
```

Responce
```json
{
  "status" : true,
  "error" : null
}
```


## GET/api/devices
설명 : 만약 사용자가 디바이스들의 정보를 원한다면 서버 내에서 디바이스에 관한 정보를 불러 와서 사용자에게 전달한다.

Responce
```json
{
  "devices" : [
    {
      "device_id" : 12345,
      "korean_adress" : "경기도 고양시 덕양구",
      "latitude" : 9.2739729,
      "longitude" : 83.33929,
      "description" : "비고",
      "install-date" : "2017-04-01",
      "남은_밥량" : "900"
    },
    {
      "device_id" : 12345,
      "korean_adress" : "경기도 고양시 덕양구",
      "latitude" : 9.2739729,
      "longitude" : 83.33929,
      "description" : "비고",
      "install-date" : "2017-04-01",
      "남은_밥량" : "900"
    }
  ]
}
```

## GET/api/device/<device_id>
설명 : 사용자가 한 디바이스에서 정보를 원한다면 서버에서 그 디바이스의 정보를 불러온다.

Responce

```json
{
  "device_id" : 12345,
  "korean_adress" : "경기도 고양시 덕양구",
  "latitude" : 9.2739729,
  "longitude" : 83.33929,
  "description" : "비고",
  "install-date" : "2017-04-01"
}
```
