import anvil

touch = anvil.Rule("touch", {
    'command': "touch $out",
})

def get_targets(config):
    return [
        anvil.Target("file", touch)
    ]

anvil.generate_ninja(get_targets)
