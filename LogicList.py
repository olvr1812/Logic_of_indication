
def logic_7_6_18(config_path, p_s):
    if p_s[0] == 1:
        im = config_path + "/Images/Indication_7_6_18/Var1.png"
    elif p_s[4] == 1:
        im = config_path + "/Images/Indication_7_6_18/Var5.png"
    elif p_s[1] == 1:
        im = config_path + "/Images/Indication_7_6_18/Var2.png"
    elif p_s[5] == 1:
        im = config_path + "/Images/Indication_7_6_18/Var6.png"
    elif p_s[2] == 1:
        im = config_path + "/Images/Indication_7_6_18/Var3.png"
    elif p_s[3] == 1:
        im = config_path + "/Images/Indication_7_6_18/Var4.png"
    elif p_s[6] == 1:
        im = config_path + "/Images/Indication_7_6_18/Var7.png"
    else:
        im = config_path + "/Images/Indication_7_6_18/Var8.png"