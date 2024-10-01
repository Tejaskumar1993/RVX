def login_form_run_environment(environment_to_run):
    """
    returns "env" which can be used to append to an url for the booking form\n
    ex. https:// + "pilot" + .tablecheck.com
    :param environment_to_run:
    :return:
    """
    env = ""
    if environment_to_run == "dev":
        env = "dev"
        print("\nRunning scripts in staging-qa")
    if environment_to_run == "testing":
        env = "test"
        print("\nRunning scripts in staging-qa-3")
    if environment_to_run == "staging":
        env = "stage"
        print("\nRunning scripts in pilot-1")
    if environment_to_run == "prod":
        env = "www"
        print("\nRunning scripts in prod")
    return env
