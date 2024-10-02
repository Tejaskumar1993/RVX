def login_form_run_environment(environment_to_run):
    """
    returns "env" which can be used to append to an url for the booking form\n
    ex. https://send + "test" + .ontrackworkflow.com
    :param environment_to_run:
    :return:
    """
    env = ""
    if environment_to_run == "dev":
        env = "dev"
        print("\nRunning scripts in dev")
    if environment_to_run == "testing":
        env = "test"
        print("\nRunning scripts in testing")
    if environment_to_run == "staging":
        env = "stage"
        print("\nRunning scripts in staging")
    if environment_to_run == "prod":
        env = "www"
        print("\nRunning scripts in prod")
    return env
