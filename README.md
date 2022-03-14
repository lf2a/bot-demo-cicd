# Bot demo with CI and CD

Python package for a BotCity bot.

## Bot CLI Commands

```shell
# deploy bot
java -jar botCli.jar bot deploy -version 1.0 -botId "botDemoCiCd" -file "<path>" -python

# update bot
java -jar botCli.jar bot update -version 1.0 -botId "botDemoCiCd" -file "<path>" -python

# release bot
java -jar botCli.jar bot release -botId "botDemoCiCd" -version 1.0

# create task activity
java -jar botCli.jar task create -activityLabel "activityCiCd" -test

# restart task
java -jar botCli.jar task restart -taskId "15936"
``` 
