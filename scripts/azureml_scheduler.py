import azureml.core
from azureml.core import Workspace
from azureml.pipeline.core import Pipeline, PublishedPipeline
from azureml.core.experiment import Experiment
from azureml.pipeline.core.schedule import ScheduleRecurrence, Schedule

ws = Workspace.from_config()

experiments = Experiment.list(ws)
for experiment in experiments:
    print(experiment.name)

# published_pipelines = PublishedPipeline.list(ws)
# for published_pipeline in  published_pipelines:
#     print(f"{published_pipeline.name},'{published_pipeline.id}'")

# experiment_name = "MyExperiment"
# pipeline_id = "aaaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"

# # Create the schedule
# recurrence = ScheduleRecurrence(frequency="Hour", interval=24)
# recurring_schedule = Schedule.create(ws, name="MyRecurringSchedule",
#                             description="Forcast sales at 12.00 each day",
#                             pipeline_id=pipeline_id,
#                             experiment_name=experiment_name,
#                             recurrence=recurrence)

# If you wish to stop the schedulee
ss = Schedule.list(ws)
for s in ss:
    print(s)

schedule_id = '5b505104-14d9-44cf-ab92-b58ecfe3583d'

def stop_by_schedule_id(ws, schedule_id):
    s = next(s for s in Schedule.list(ws) if s.id == schedule_id)
    s.disable()
    return s

stop_by_schedule_id(ws, schedule_id)

# # https://docs.microsoft.com/en-us/azure/machine-learning/how-to-schedule-pipelines
