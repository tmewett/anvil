import anvil

error_option = anvil.Option("error")

def get_targets(ctx):
    error = error_option.configure(ctx)
    if error is not None:
        raise RuntimeError()
    return []

anvil.generate_ninja(get_targets, options=[error_option])
