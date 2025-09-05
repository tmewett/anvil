from dataclasses import dataclass

@dataclass
class Rule:
    nickname: str
    options: dict

@dataclass
class Target:
    path: str
    rule: Rule

def generate_ninja(get_targets):
    with open("build.ninja", 'w') as f:
        f.write("")
