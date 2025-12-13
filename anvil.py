import argparse
from dataclasses import dataclass

@dataclass
class Rule:
    nickname: str
    options: dict
    def __hash__(self):
        return id(self)
    def __eq__(self, other):
        return self is other

@dataclass
class Target:
    path: str
    rule: Rule
    inputs: list = ()

@dataclass
class Option:
    # todo no dups
    name: str
    def __hash__(self):
        return id(self)
    def __eq__(self, other):
        return self is other

@dataclass
class Context:
    config: dict
    def sandboxed_rule(self, nickname, options):
        return Rule(nickname, options | {'command': f"""_anvil_tmp="$$(bash ../../create_sandbox.bash $in)" && _anvil_wd="$$(pwd)" && cd $$_anvil_tmp && {options['command']} && cp --parents -t "$$_anvil_wd" $out; _anvil_status=$$?; rm -rf $$_anvil_tmp; exit $$_anvil_status"""})

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

def generate_ninja(get_targets, *, options=[]):
    parser = argparse.ArgumentParser()
    parser.add_argument("-D", action='append')
    args = parser.parse_args()
    ds = args.D or []
    given_config = dict(arg.split("=", maxsplit=1) for arg in ds)
    config = {opt: given_config.get(opt.name) for opt in options}
    targets = []
    def gather_from(x):
        if isinstance(x, Target):
            targets.append(x)
        else:
            for xx in x:
                gather_from(xx)
    gather_from(get_targets(Context(config)))
    rules = {t.rule for t in targets}
    fragments = []
    for rule in rules:
        fragments += _rule_to_ninja(rule)
    for target in targets:
        fragments += _target_to_ninja(target)
    with open("build.ninja", 'w') as f:
        for frag in fragments:
            f.write(frag)
