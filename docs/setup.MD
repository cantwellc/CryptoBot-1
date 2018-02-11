### Building the App
_$ docker build -t cryptobot ._

### Running the App

__Run in the foreground:__<br>
_$ docker run -p 5000:80 cryptobot_

__Run in the background (detached mode):__<br>
_$ docker run -d -p 5000:80 cryptobot_
* This will output an _id_
* To stop the process: _$ docker container stop id_
