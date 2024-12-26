import re

pass_reg =r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

password = "edolour@123D"


print(re.match(pass_reg, password))