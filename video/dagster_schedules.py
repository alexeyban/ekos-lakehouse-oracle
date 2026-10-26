"""List the generated Dagster schedules and stop the running ones (they start switched on: on a test
machine the first hourly tick would launch the whole extraction before the recorded run).

    python video/dagster_schedules.py http://127.0.0.1:53200 [--stop] [--cancel-runs]

`--cancel-runs` cancels any queued or started run (a tick that fired before the schedules were stopped).
"""
import json, sys, urllib.request


def gql(url, query, variables=None):
    req = urllib.request.Request(url.rstrip("/") + "/graphql", json.dumps({"query": query, "variables": variables or {}}).encode(),
                                 {"Content-Type": "application/json"})
    out = json.load(urllib.request.urlopen(req, timeout=60))
    if out.get("errors"):
        raise SystemExit(json.dumps(out["errors"])[:800])
    return out["data"]


SCHEDULES = """{ workspaceOrError { ... on Workspace { locationEntries { locationOrLoadError {
  ... on RepositoryLocation { repositories { name schedules { name cronSchedule scheduleState { id status } } } }
  ... on PythonError { message } } } } } }"""
STOP = """mutation($id: String!) { stopRunningSchedule(id: $id) { __typename
  ... on ScheduleStateResult { scheduleState { status } } ... on PythonError { message } } }"""


RUNS = """{ runsOrError(filter: {statuses: [QUEUED, NOT_STARTED, STARTING, STARTED]}) {
  ... on Runs { results { runId status jobName } } } }"""
CANCEL = """mutation($id: String!) { terminateRun(runId: $id, terminatePolicy: MARK_AS_CANCELED_IMMEDIATELY) {
  __typename ... on TerminateRunSuccess { run { status } } ... on PythonError { message } } }"""


def main():
    url, stop = sys.argv[1], "--stop" in sys.argv
    data = gql(url, SCHEDULES)
    for entry in data["workspaceOrError"]["locationEntries"]:
        loc = entry["locationOrLoadError"] or {}
        if "message" in loc:
            raise SystemExit(f"code location failed to load: {loc['message'][:500]}")
        for repo in loc.get("repositories", []):
            for s in repo["schedules"]:
                state = s["scheduleState"]
                line = f"{s['name']} ({s['cronSchedule']}): {state['status']}"
                if stop and state["status"] == "RUNNING":
                    r = gql(url, STOP, {"id": state["id"]})["stopRunningSchedule"]
                    line += f" → {r.get('scheduleState', {}).get('status', r)}"
                print(line)
    if "--cancel-runs" in sys.argv:
        for r in gql(url, RUNS)["runsOrError"]["results"]:
            out = gql(url, CANCEL, {"id": r["runId"]})["terminateRun"]
            print(f"cancelled {r['runId']} ({r['jobName']}, was {r['status']}): {out['__typename']}")


if __name__ == "__main__":
    main()
