from routes import employee

print("Attributes in employee:", dir(employee))
print("Has router?", hasattr(employee, "router"))
print("router object:", getattr(employee, "router", None))
