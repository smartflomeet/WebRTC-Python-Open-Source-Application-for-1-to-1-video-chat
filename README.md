# Building a 1-to-1 Real-Time Communication Web App with Django (Python Framework) and Web Toolkit

1-to-1 RTC Web App: Python (Django Framework) and Web Toolkit 

Explore a Sample Web App demonstrating the utilization of APIs for crafting fundamental 1to1 RTC (Real Time Communication) Applications. This application is designed to showcase API usage, allowing developers to expedite app development by hosting it on their own devices, eliminating the need for external servers. 

RTC Applications hosted on the platform seamlessly operate on supported web browsers, requiring no additional plugin downloads. 

This basic 1to1 RTC Application is constructed using HTML, CSS, Bootstrap, JavaScript, jQuery, Python, and EnxRtc (Web Toolkit) 

>The details of the supported set of web browsers can be found here:
https://doc.smartflomeet.ttns.in/developer/video/browser-compatibility-video/

## 1. Important!

When developing a Client Application with EnxRtc.js make sure to include the updated EnxRtc.js polyfills from https://doc.smartflomeet.ttns.in/developer/video-api/client-api/web-toolkit/ for RTCPeerConnection and getUserMedia otherwise your application will not work in web browsers.

## 2. Installation

### 2.1 Pre-Requisites

#### 2.1.1 App Id and App Key

* Create your Application
* Get your App ID and App Key delivered to your Email
* Clone or download this Repository [https://github.com/smartflomeet/WebRTC-Python-Open-Source-Application-for-1-to-1-video-chat.git] & follow the steps further 
* You can copy the app into any sub-directory of hosted Website on Python

#### 2.1.2 SSL Certificates

The Application needs to run on https. So, you need to use a valid SSL Certificate for your Domain and point your application to use them.

However you may use self-signed Certificate to run this application locally. There are many Web Sites to get a Self-Signed Certificate generated for you, Google it. Few among them are:
* https://letsencrypt.org/
* https://www.sslchecker.com/csr/self_signed
* https://www.akadia.com/services/ssh_test_certificate.html

As you have Certificate or created a Self-Signed Certificate, create a directory "certs" under your Sample Web App Directory. Copy your Certificate files (.key and .crt files) to this directory.


#### 2.1.3 Configure

Before you you try accessing the /client folder using Browser, configure the API Service by editing main app `settings.py` file to meet your requirement:

```python
API_URL = "https://api.smartflomeet.ttns.in/v1"
APP_ID = "YOUR_APP_ID"
APP_KEY = "YOUR_APP_KEY"
```

### 2.2 Test

* Open a browser and go to [https://yourdomain.com:4443/path-to-sample-app/client/](https://yourdomain.com:4443/path-to-sample-app/client/). The browser should load the App. 
* Allow access to Camera and Mic as and when prompted to start your first RTC Call
* You need to Room ID to join. We have added a "Create Room" link below the login form. Click it to get a Room-Id prefilled in the form. 
* You can share the Room-ID with anyone to join your Conference.



## 3 Server API

Server API is a Rest API service meant to be called from Partners' Application Server to provision video enabled
meeting rooms. API Access is given to each Application through the assigned App ID and App Key. So, the App ID and App Key
are to be used as Username and Password respectively to pass as HTTP Basic Authentication header to access Server API.

For this application, the following Server API calls are used:
* https://doc.smartflomeet.ttns.in/developer/video-api/server-api/rooms-route/#create-room - To create room to carry out a video session
* https://doc.smartflomeet.ttns.in/developer/video-api/server-api/rooms-route/#create-token - To create Token for the given Room to join a session

To know more about Server API, go to:
https://doc.smartflomeet.ttns.in/developer/video-api/server-api/


## 4 Client API

Client End Point Application uses Web Toolkit EnxRtc.js to communicate with Servers to initiate and manage RTC Communications.

To know more about Client API, go to:
https://doc.smartflomeet.ttns.in/developer/video-api/client-api/
