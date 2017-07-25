ns = [1, 2]
ns2 = [1, 2]    # ns & ns2 have

print(ns == ns2)   # ns & ns2 have same value

print(ns is ns2)    # ns & ns2 are different objects --> different memory location

ns3 = ns
print(ns == ns3)   # ns & ns3 have same value
print(ns is ns3)    # ns & ns3 are same objects --> same memory location

print(id(ns))
print(id(ns2))      # ns & ns2 are different objects --> different IDs
print(id(ns3))      # ns & ns3 are same objects --> same ID


# if you change ns, then you also change ns3 because they are the same object in memory
print(ns)
print(ns3)
ns3.append(445)
print(ns)
print(ns3)

ns4 = ns3.copy()