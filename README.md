# Automation Exercise

## Running Selenium Grid

This with the intention to do not set up any local configuration, all you need to have installed is docker, where we will deploy a Selenium Grid and the automation scripts can consume it to execute the tests in the various browsers (Edge, Chrome, Firefox and Safari)
```
$ cd selenium_grid
$ sudo docker-compose up -d
```
This will start the grid at `http://localhost:4444` which is the one the automation script will consume, in order to stop the grid or restart it, you can run the following commands:
```
$ docker-compose restart
$ docker-compose down
```
You also can check the Selenium grid UI by visiting `http://localhost:4444/ui/index.html#/`

## Configuring the tests

The Automation requires a simple configuration file which can be provided at the root of the repo, its structure is defined in `config.example.json` file, this file must be named as `config.json` and it might look like the following:
```
{
    "config":{
        "useGrid": true,
        "grid":"http://localhost:4444",
        "browser":{
            "name":"chrome"
        },
        "implicitWait": 10,
        "environment":{
            "url":"http://automationpractice.com/"
        }
    }
}
```

## Running the Tests on Selenium Grid
Assuming you already have the grid running, you're ready to actually run the tests by running pytest commands like this:
```
$ pytest -k home_automation --html=./results/report.html
```
By running this command, you will get an html report at `./results/report.html` which will contain the tests results.

## About pixel perfect test
This test will take a screenshot to the home page and will compare it agains the one in `design/home/home.jpg`, if it finds any difference, the test will fail and it will create a new image where you can check the differences, it might look like this:
![alt tag](images/image_analysis.png)
Indicating there are differences when comparing against the design document, here you can see there are minor differences when presenting the prices.