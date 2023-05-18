class Environment:
    def __init__(self, env=None):
        self.parent = env
        self.vars = {}
    
    def declare(self, name, value):
        if name in self.vars:
            raise Exception(f"Variable {name} already declared")
        self.vars[name] = value
    
    def assign(self, name, value):
        varEnv = self.resolve(name)
        varEnv.vars[name] = value
        return value
    
    def retrive(self, name):
        varEnv = self.resolve(name)
        return varEnv.vars[name]

    def resolve(self, name):
        if name in self.vars:
            return self
        if self.parent != None:
            return self.parent.resolve(name)
        raise Exception(f"Variable {name} does not exist")

def defineNum(dtype, value):
    return { "type": "number", "value": value, "dtype": dtype}
def defineStr(value):
    return { "type": "string", "value": value}
def defineUndefined():
    return {"type": "undefined", "value": "undefined"}

