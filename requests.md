## Login
``````
POST /api/service/user/login HTTP/1.1
Host: userdata.link2home.com
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive
Accept: */*
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
Accept-Language: de-DE;q=1, en-DE;q=0.9
Content-Length: 538
Accept-Encoding: gzip, deflate, br

appName=Link2Home&appType=2&appVersion=1.1.1&password=822BC62D4CA47D18608E6FCBB60F39CE&phoneSysVersion=iOS%2017.1.2&phoneType=iPad13%2C8&sign=B0z1xSNsMSJua9tOlmTDc78bsLKzbaVhEyhF2JlTNe7n0mLegaNoSZh3LtP6ehCq0NPfANOEFC%2BorgA%2Bnceidiex/ORnpkm6yklGyTi6lYPYn/BK1%2BFnprGVOOJsbalUJRdAdb9ykVoN/seQjAGlP%2BQ%2B2zF7KuygyRLyEEX7hVt7KVjfKS5O7pxtY8ZMtcYcBMiqR8FOqrkbIwoDXjD0ebcPZkSs3BC/s9HYc0iZhxideft0bpNOXwvrx3mYrheDjTE98751e1ATHBAfzSPs/ZyMCAVYuBIydr/fsHouLshIGC258CgW9alxqRZ1tL12Sx4rKXQK5%2Bevjq4z/yQFZA%3D%3D&username=jengelhardt211%40gmail.com

HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:25 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

7d
{"code":600,"data":{"id":"5fd225c5e4b012e74cacba0e","locale":"EN","token":"811DB9A19B55B0B781DFBA541D88471D"},"success":true}
0
``````
## List Groups
```
GET /api/app/group/list?sign=XZYin8ikKt20Ai8YFXTEd1mgoYhO0G5AHeGVHCMbYKOghcQkfVjBJUu4qynnhgK2BFbKdi%2BAiwtmQJLsiABQLrezS0quW%2BHxcKZeu5wNtLMykCsFN9jhapCmFR1BYPlFN1h4NuPjYiRHdYnRE2M8En1bQPZuMCZ8ixicxKLQVqoPcjHeXKGJyjbhyl0j4nhJwJMnwg6QXaqHRevlq/iKdGjF2flg3FRNEEsAvarTIInsNkyARV7tRnCe/EHzV3H6eYMj0DlVZVdapAzrCKkdIbRoz%2B%2Bu4aMw8Y58SbdugW157Zm7dYXcGHS9qyoX66w3jcpm291W9GqxcuT5p5GUEA%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:25 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

27
{"code":600,"data":null,"success":true}
0

```

## List Device info
```
GET /api/app/device/order/custom/info?sign=XZYin8ikKt20Ai8YFXTEd1mgoYhO0G5AHeGVHCMbYKOghcQkfVjBJUu4qynnhgK2BFbKdi%2BAiwtmQJLsiABQLrezS0quW%2BHxcKZeu5wNtLMykCsFN9jhapCmFR1BYPlFN1h4NuPjYiRHdYnRE2M8En1bQPZuMCZ8ixicxKLQVqoPcjHeXKGJyjbhyl0j4nhJwJMnwg6QXaqHRevlq/iKdGjF2flg3FRNEEsAvarTIInsNkyARV7tRnCe/EHzV3H6eYMj0DlVZVdapAzrCKkdIbRoz%2B%2Bu4aMw8Y58SbdugW157Zm7dYXcGHS9qyoX66w3jcpm291W9GqxcuT5p5GUEA%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:26 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

27
{"data":null,"success":true,"code":600}
0


```

## List Devices
```
GET /api/app/device/list?sign=XZYin8ikKt20Ai8YFXTEd1mgoYhO0G5AHeGVHCMbYKOghcQkfVjBJUu4qynnhgK2BFbKdi%2BAiwtmQJLsiABQLrezS0quW%2BHxcKZeu5wNtLMykCsFN9jhapCmFR1BYPlFN1h4NuPjYiRHdYnRE2M8En1bQPZuMCZ8ixicxKLQVqoPcjHeXKGJyjbhyl0j4nhJwJMnwg6QXaqHRevlq/iKdGjF2flg3FRNEEsAvarTIInsNkyARV7tRnCe/EHzV3H6eYMj0DlVZVdapAzrCKkdIbRoz%2B%2Bu4aMw8Y58SbdugW157Zm7dYXcGHS9qyoX66w3jcpm291W9GqxcuT5p5GUEA%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:26 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

189
{"code":600,"data":[{"macAddress":"98D8638C6142","companyCode":"02","deviceType":"D1","authCode":"0050","deviceName":"Lichterkette","imageName":"","orderNumber":1,"lastOperation":1702824542738,"cityId":"U0WQ3P04RT81","zoneId":"Europe/Berlin","gmtOffset":60,"longtitude":8.849893845712915,"latitude":49.04955111705228,"version":null,"groupId":null,"gColorType":0,"online":true}],"success":true}
0


```

## Get Device Detail
```
GET /api/app/icloud/device/one?macAddress=98D8638C6142&pin=1&sign=DsiRI%2BTaAKwMtbGSqAMnrM6ELw3cyLVQssb%2BhrWbiM/94i3V9UAcEzCU4qQfTl660zKuDkMX3EClKP4wB%2Bv7ZcVKc/DaUJyqghXdXdHNxh94hqMnukMoYt4YpKtQZOWHOQr9RqJpwNwt8v6dDlSd06u4F0q6uwHYUi7KbiaLiR9o9E/EUHKEWNzSL0r5gZ/jdtJ/zy/%2B%2BeNYwgyV3e4Pc42NeL%2BPK%2BFVXSnZF5HgSikBhBkfCtenO/JtrjYjAe8ckSjFnPrjgEGzoa1/K5afwCylTTcXPRdhjmpp9gGpIIhRPLFZVN6D6WA%2BSi2ZGilTuYwKReYqvwbZHOKu6VMHuw%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:26 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

141
{"code":600,"data":{"timer":[{"deleted":false,"enabled":false,"group":false,"hour1":17,"hour2":0,"index":1,"minute1":0,"minute2":0,"pin":0,"repeatDays1":127,"repeatDays2":127,"time":1699113995793,"timestamp":0,"turnOn1":true,"turnOn2":false,"type1":1,"type2":1,"valid1":false,"valid2":false,"version":0}]},"success":true}
0


```

## Get Device Countdown
```
GET /api/app/deivce/countdown?macAddress=98D8638C6142&pin=1&sign=DsiRI%2BTaAKwMtbGSqAMnrM6ELw3cyLVQssb%2BhrWbiM/94i3V9UAcEzCU4qQfTl660zKuDkMX3EClKP4wB%2Bv7ZcVKc/DaUJyqghXdXdHNxh94hqMnukMoYt4YpKtQZOWHOQr9RqJpwNwt8v6dDlSd06u4F0q6uwHYUi7KbiaLiR9o9E/EUHKEWNzSL0r5gZ/jdtJ/zy/%2B%2BeNYwgyV3e4Pc42NeL%2BPK%2BFVXSnZF5HgSikBhBkfCtenO/JtrjYjAe8ckSjFnPrjgEGzoa1/K5afwCylTTcXPRdhjmpp9gGpIIhRPLFZVN6D6WA%2BSi2ZGilTuYwKReYqvwbZHOKu6VMHuw%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:26 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

1b
{"code":600,"success":true}
0


```

## Get Firmware upgrades
```
GET /api/app/version/upgrade/firmware?companyCode=02&deviceType=D1&sign=e3PC4gy2tQKU6MAGBM9UXCqEDJiJTbrD9yQ5fS9xHfjhALb9lBwpvmFbrYjLQZUMNxkRHrPuXb5A7X55//V9wiRmS/YDuEbWKD4Mmu2kQyTMw1eXRv0qZjm551XHUCSqJStzsXSRCogovtSgf2AZjgTLfzmPmdARJ1vWfzOpRMAbAC48oK/E9e8mX65VzoXM5JmaMbPsHHfX/8rsR2Lqt4oLl3zyBlkwmSG6jsL2e25eMyJPi1%2BGIGaJaRNz2uAp/2ljyilqSbnkro4jGHZJ8lWTPi%2BJo4V3GPwzE8cY4dCLRqy5xGbRe09WcKnE2/f4ebvTBZRv1wU5Zrap6Yed%2Bw%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:26 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

a2
{"data":{"downloadPath":"http://userdata.link2home.com/uploadedFile/NW2034_UPGRADE_HSF_HDG_L2H_D1_V1.12_20180912.bin","version":"1.12"},"success":true,"code":600}
0


```

## Get successfull updates
```
GET /api/app/version/upgrade/success?lastOperation=1702825166419&macAddress=98D8638C6142&sign=dLA455UuftevGHJoTlio6ZhKwOhmHxUHic5BbsOMvLKz5PHcQo1pyRET4AMePpm28d5C6Y%2Bwqy9iXBo5RYyqu/1lDmPJ46iCqLa5CU4IGBMq1jO9Kzoqb/BA%2BxOVzTgDMqNKDEK9IPXxb/9EKyhdOaOj/6cFRGl5K836SF0Z/4EGgzT2stUkuLjpwduOBNT0Burda1UMfgqoSfKxznbQD79%2BoEle8ijTV0TNm5PVH%2Ble/2LtHh4LFRrK%2BeWj%2BI/O54JJcwxeto1/j2QlM6XQxNKv6TMAHNbuXaDiEcCCdMIDkOpkjTkh5EjuglSy/mSBGKpT3y9RgRkXSlCfIQKedQ%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D&version=1.12 HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:26 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

1b
{"code":600,"success":true}
0


```

## Get location information
```
GET /api/app/sun/info?cityId=U0WQ3P04RT81&date=2023-12-17&sign=DKUGaSraLQhZ5n9OMk5uexds2J8IC06gC%2Bm/0cM4FQNN/BcAUDuKcj3GjVD5aoJKK%2BHY02ie4mMNke96d1KKDAwXt67uWyMc6XxnmYnNnWCNC6zpkFIqS4Oj0FkbXupyukOt7bR6yGL/YLAU4DhNov%2BnFb5GySIPRC4q1RMXu4bFXexTdc/BYNPrFa7oM28oJoAH5HCMIA14aTBK/oJks0RPwlc/YkPcMb0BgHJpzQYeZ/i7JveJLS1HgVbnfpiGvHBM7LaFIbxhRt8E2bHCn/tpN568JeewbEdr59OOShcMa7iXSDaL/QEG3Bq18qWVxM/M0tOsUEcOoLVcQv9m1Q%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:27 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

4d
{"code":600,"data":{"sunrise":1702797204,"sunset":1702826964},"success":true}
0


```

## Get Device info detail
```
GET /api/app/device/order/custom/info?sign=XZYin8ikKt20Ai8YFXTEd1mgoYhO0G5AHeGVHCMbYKOghcQkfVjBJUu4qynnhgK2BFbKdi%2BAiwtmQJLsiABQLrezS0quW%2BHxcKZeu5wNtLMykCsFN9jhapCmFR1BYPlFN1h4NuPjYiRHdYnRE2M8En1bQPZuMCZ8ixicxKLQVqoPcjHeXKGJyjbhyl0j4nhJwJMnwg6QXaqHRevlq/iKdGjF2flg3FRNEEsAvarTIInsNkyARV7tRnCe/EHzV3H6eYMj0DlVZVdapAzrCKkdIbRoz%2B%2Bu4aMw8Y58SbdugW157Zm7dYXcGHS9qyoX66w3jcpm291W9GqxcuT5p5GUEA%3D%3D&token=811DB9A19B55B0B781DFBA541D88471D HTTP/1.1
Host: userdata.link2home.com
Accept: */*
Accept-Language: de-DE;q=1, en-DE;q=0.9
Connection: keep-alive
Accept-Encoding: gzip, deflate, br
User-Agent: Link2Home/1.1.1 (iPad; iOS 17.1.2; Scale/2.00)
content-length: 0



HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Dec 2023 14:59:37 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive

27
{"data":null,"success":true,"code":600}
0

```