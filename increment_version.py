import toml

with open("pack.toml", 'r+') as f:
    data = toml.load(f)
    
    data["version"] = str(int(data["version"]) + 1)
    
    f.truncate(0)
    f.seek(0)
    
    toml.dump(data, f)
  