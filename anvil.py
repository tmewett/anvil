from dataclasses import dataclass

@dataclass
class Rule:
    nickname: str
    options: dict

@dataclass
class Target:
    path: str
    rule: Rule
    inputs: list

def _rule_to_ninja(rule):
    return (
        [f"rule {rule.nickname}\n"]
        + [f"  {var} = {value}\n" for var, value in rule.options.items()]
    )

def _target_to_ninja(target):
    return (
        [f"build {target.path}: {target.rule.nickname}"]
        + [f" {input}" for input in target.inputs]
        + ["\n"]
    )

def generate_ninja(get_targets):
    targets = get_targets()
    rules = [t.rule for t in targets]
    fragments = []
    for rule in rules:
        fragments += _rule_to_ninja(rule)
    for target in targets:
        fragments += _target_to_ninja(target)
    with open("build.ninja", 'w') as f:
        for frag in fragments:
            f.write(frag)
