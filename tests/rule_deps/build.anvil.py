import anvil

def get_targets(ctx):
    note = anvil.Target(
        "note",
        "my_actions.write_file",
        args=["note", "Hello, world!"],
    )
    return [[note]]

anvil.do(get_targets)
