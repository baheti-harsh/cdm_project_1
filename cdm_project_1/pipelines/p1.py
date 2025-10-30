Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    trade_file_1 = Task(
        task_id = "trade_file_1", 
        component = "Dataset", 
        table = {"name" : "trade_file_1", "sourceType" : "Table", "sourceName" : "trading.raw", "alias" : ""}
    )
    securities = Task(
        task_id = "securities", 
        component = "Dataset", 
        table = {"name" : "securities", "sourceType" : "Table", "sourceName" : "trading.raw", "alias" : ""}
    )
    trade_file_2 = Task(
        task_id = "trade_file_2", 
        component = "Dataset", 
        table = {"name" : "trade_file_2", "sourceType" : "Table", "sourceName" : "trading.raw", "alias" : ""}
    )
