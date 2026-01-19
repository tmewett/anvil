import anvil

def get_targets(ctx):
    hello = anvil.Target(
        "hello.txt",
        "anvil.touch",
    )
    return [hello]

anvil.run(get_targets)
