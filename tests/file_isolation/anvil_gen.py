import anvil

def get_targets(ctx):
    cat = anvil.Rule("rule", {
        'command': "cat input1 $in > $out",
    })
    output_file = [anvil.Target("output", cat, inputs=["input2"])]
    return [output_file]

anvil.generate_ninja(get_targets)
