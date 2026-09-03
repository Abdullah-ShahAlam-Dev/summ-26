# Else block mein model ko apened krenge ki bhai ye object aya wo avoid hugaa and wo modle extend hutaa jyega, then wo khd decison le lega ad  hamrein path pr chleega

def agent(data, model):
    if data in model:
        return "avoid obstacles"
    else:
        model.append(data)
        return "avoid obstacles"

# Inputs ki list aur Model (Memory)
inputs = ["chair", "table", "door"]
model = ["chair"]


print(model)
# before hcekck kra hi ki bhai model mie kia tha then ihamrien input se learn huga

for inp in inputs:
    res = agent(inp, model)
    print(res)  # 'yes' ki jagah variable 'res' print hoga

print(model)
# and mein jo modle return  hua, ki ab new model mine kon konse add huoi hi


