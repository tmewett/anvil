import anvil

error_option = anvil.Option("error")

def get_targets(ctx):
    error = ctx.config[error_option]
    if error is not None:
        raise RuntimeError()
    return []

anvil.generate_ninja(get_targets, options=[error_option])
