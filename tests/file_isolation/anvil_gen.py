import anvil

def get_targets(ctx):
    cat = ctx.sandboxed_rule("rule", {
        'command': "cat input1 $in > $out",
    })
    invalid_output = anvil.Target("invalid_output", cat, inputs=["input2"])
    output = anvil.Target("output", cat, inputs=["input1", "input2"])
    return [invalid_output, output]

anvil.generate_ninja(get_targets)
