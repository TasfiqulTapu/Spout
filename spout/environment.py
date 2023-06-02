class Environment:
    def __init__(self, env=None):
        self.parent = env
        self.vars = {}
        self.consts = {}
        self.declare("print", defineNativeFunction(lambda args,scope: print("".join([str(item["value"]) for item in args]))), False)

    
    def declare(self, name, value, constant):
        if name in self.vars:
            raise Exception(f"Variable {name} already declared")
        self.vars[name] = value
        if constant: self.consts[name] = constant
        return value
    
    def assign(self, name, value):
        varEnv = self.resolve(name)
        if name in varEnv.consts:
            raise Exception(f"Cannot assign value to constant {name}")
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
def defineNativeFunction(call):
    return {"type": "NativeFunction", "call": call}


