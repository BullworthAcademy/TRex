smoke_id = 1000
temp_id = 1001
fire_id = 1100
file_idx = 0
for i in range(10):
    idx = i+1
    assign_line = f"Assign {smoke_id} => Smoke{idx}, {temp_id} => Temp{idx}, {fire_id} => Fire{idx}"
    smoke_id += 1000
    temp_id += 1000
    fire_id += 1000
    for temp_threshold in range(1,101):
        with open(f"trex_rules/trex1_{file_idx}.rule", mode="w", encoding="utf-8") as rule_file:
            rule_file.write(assign_line)
            rule1 = f"""Define  Fire{idx}(area: string, measuredTemp: float)
From    Smoke{idx}(area=>$a) and each Temp{idx}([string]area=$a, value>{temp_threshold}) within 300000 from Smoke{idx}
Where   area:=Smoke{idx}.area, measuredTemp:=Temp{idx}.value;"""
            rule_file.write("\n\n")
            rule_file.write(rule1)
            file_idx += 1

smoke_id = 1000
temp_id = 1001
fire_id = 1100
file_idx = 0
for i in range(10):
    idx = i+1
    assign_line = f"Assign {smoke_id} => Smoke{idx}, {temp_id} => Temp{idx}, {fire_id} => Fire{idx}"
    smoke_id += 1000
    temp_id += 1000
    fire_id += 1000
    for temp_threshold in range(1,101):
        with open(f"trex_rules/trex2_{file_idx}.rule", mode="w", encoding="utf-8") as rule_file:
            rule_file.write(assign_line)
            rule2 = f"""Define  Fire{idx}(area: string, measuredTemp: float)
From    Smoke{idx}(area=>$a) and last Temp{idx}([string]area=$a, value>{temp_threshold}) within 300000 from Smoke{idx}
Where   area:=Smoke{idx}.area, measuredTemp:=Temp{idx}.value;"""
            rule_file.write("\n\n")
            rule_file.write(rule1)
            file_idx += 1
