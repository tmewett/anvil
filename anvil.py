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
    function: str

@dataclass
class Option:
    # todo no dups
    name: str
    def configure(self, ctx):
        return ctx.config[self]
    def __hash__(self):
        return id(self)
    def __eq__(self, other):
        return self is other

@dataclass
class Context:
    config: dict

def touch(out):
    with open(out, "w"):
        pass

def run(get_targets, *, options=[]):
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
    # rules = {t.rule for t in targets}
    for t in targets:
        module, var = t.function.rsplit(".", maxsplit=1)
        getattr(__import__(module), var)(os.path.join("anvil_out", t.path))
