sides = ["top", "right", "bottom", "left", "horz", "vert"]
sizes = [5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]
attributes = ["margin", "padding"]

with open('./project-file/util-generator/utilities.txt', 'w') as util_rules:
    for attribute in attributes:
        for side in sides:
            if side == "horz":
                util_rules.write(f"/* {attribute} {side}\n -------------------*/\n")
                for size in sizes:
                    util_rules.write(f".util-{attribute}-{side}-{size} {{ {attribute}: 0 {size}px !important; }} \n")
                util_rules.write(f"\n\n")
            elif side == "vert":
                util_rules.write(f"/* {attribute} {side}\n -------------------*/\n")
                for size in sizes:
                    util_rules.write(f".util-{attribute}-{side}-{size} {{ {attribute}: {size}px 0 !important; }}\n")
                util_rules.write(f"\n\n")
            if side != "horz" and side != "vert":
                util_rules.write(f"/* {attribute} {side}\n -------------------*/\n")
                for size in sizes:
                    util_rules.write(f".util-{attribute}-{side}-{size} {{ {attribute}-{side}: {size}px !important; }}\n")
                util_rules.write(f"\n\n")
