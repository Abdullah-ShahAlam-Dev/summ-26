
# elevator agent kon konse floor pr user hja raha hi and  reqsu chekc kr ki aata raha hi ki reqyestd floor and current floor ko dkeh bss ye batoo ki upper jana hi yaa neechee jana hi \

# fully observalble huga, socististic and static huga


def agent(current, request):
    if request > current:
        return "Move Up"
    elif request < current:
        return "Move Down"
    else:
        return "Open Doors"

inputs = [
    (2, 6),
    (5, 2),
    (4, 4)
]


for inp in inputs:
    res = agent(inp[0], inp[1])
    print("Current Floor:", inp[0], "Requested Floor:", inp[1])
    print(res)
# Here we applied Simple reflex Agent bcz of enivorments iss fully observalble, socististic and static .