# with open("Passports.txt") as f:
#     content = f.read()
#     Passports = content.split("\n\n")

# PassportList = []
# passportDict = {}
# for item in Passports:
#     row = item
#     row = row.replace(" ","\n")
#     row = row.split("\n")
#     PassportList.append(row)
# count = 0

# class Validator:
#     def __init__(self, passport):
#         self.passport = passport

#     def check_field_count(self):
#         return len(self.passport) == 8 or (len(self.passport) == 7 and 'cid' not in self.passport)

#     def check_year(self, key, start, end):
#         return len(self.passport[key]) == 4 and int(self.passport[key]) >= start and int(self.passport[key]) <= end

#     def check_byr(self):
#         return self.check_year('byr', 1920, 2002)

#     def check_iyr(self):
#         return self.check_year('iyr', 2010, 2020)

#     def check_eyr(self):
#         return self.check_year('eyr', 2020, 2030)

#     def check_hcl(self):
#         #return self.passport['hcl'][0] == "#" and (self.passport['hcl'][1:].isalnum() or self.passport["hcl"][1:].isalpha())
#         return self.passport['hcl'][0] == "#" and len(self.passport["hcl"]) == 7 and (self.passport["hcl"][1:].isdecimal() and not (all(c in "abcdef" for c in self.passport["hcl"]) and self.passport["hcl"].isalpha()))

#     def check_ecl(self):
#         return self.passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

#     def check_pid(self):
#         return len(self.passport['pid']) == 9

#     def check_hgt(self):
#         if self.passport.endswith("cm"):
#             return int(self.passport['hgt'][:-2]) >= 150 and int(self.passport['hgt'][:-2]) <= 193
#         elif self.passport.endswith("in"):
#             return int(self.passport['hgt'][:-2]) >= 59 and int(self.passport['hgt'][:-2]) <= 76

#     def is_valid(self):
#         return (self.check_field_count() and self.check_byr() and self.check_iyr() and self.check_eyr() 
#             and self.check_hcl() and self.check_ecl() and self.check_pid() and self.check_hgt())

# # def validate(result):
# #     global count
# #     correct = True
# #     if (int(result["byr"])) <=1920 or (int(result["byr"]) >=2002):
# #         correct = False
# #     if int(result["iyr"]) <= 2010 or int(result["iyr"]) >=2020:
# #         correct = False
# #     if len(result["eyr"]) != 4 or int(result["eyr"]) <= 2020 or int(result["eyr"]) >=2030:
# #         correct = False
# #     if result["hgt"].endswith("cm"):
# #         if int(result["hgt"][:-2]) <=150 or int(result["hgt"][:-2]) >= 193:
# #             correct = False
# #     elif result["hgt"].endswith("in"):        
# #         if int(result["hgt"][:-2]) <=59 or int(result["hgt"][:-2]) >= 76:
# #             correct = False
# #     elif not result["hgt"].endswith("in") or not result["hgt"].endswith("cm"):
# #         correct = False
# #     if not result["hcl"].startswith("#") or len(result["hcl"]) != 7:
# #         correct=False
# #     if not result["hcl"][1:].isdecimal() and not (all(c in "abcdef" for c in result["hcl"]) and result["hcl"].isalpha()):
# #         correct = False
# #     if result["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
# #         correct = False
# #     if len(result["pid"]) != 9:
# #         correct = False
# #     if correct == False:
# #         print("Incorrect")
# #         #print(result)
# #     if correct==True:
# #         print("True")
# #         count +=1
# def check(result):
#     global count
#     check1 = Validator(result)
#     if check1.is_valid:

#         print("True")
#         count +=1
            
        

# for item in PassportList:
#     keys = []
#     values = []
#     for element in item:
#         key, val = element.split(":", 1)
#         keys.append(key)
#         values.append(val)
#     result = dict(zip(keys,values)) 
#     check(result)
# print(count)


from re import match

with open("Passports.txt", "r") as file:
    data = [data.split() for data in file.read().split("\n\n")]
    
    passport_data = []
    for datum in data:
        passport_datum = {}
        for key_value in datum:
            key_value = key_value.split(":")
            key = key_value[0]
            value = key_value[1]

            passport_datum[key] = value
        passport_data.append(passport_datum)

required_fields = {"byr": lambda y: match("\d{4}", y) and 1920 <= int(y) <= 2002,
                   "iyr": lambda y: match("\d{4}", y) and 2010 <= int(y) <= 2020,
                   "eyr": lambda y: match("\d{4}", y) and 2020 <= int(y) <= 2030,
                   "hgt": lambda h: match("\d+(cm|in)", h) and \
                   ((h[-2:] == "cm" and 150 <= int(h[:-2]) <= 193) or \
                    (h[-2:] == "in" and 59 <= int(h[:-2]) <= 76)),
                   "hcl": lambda c: match("#[0-9a-f]{6}", c),
                   "ecl": lambda c: match("amb|blu|brn|gry|grn|hzl|oth", c),
                   "pid": lambda i: match("^\d{9}$", i)}

num_valid_1 = 0
num_valid_2 = 0
for datum in passport_data:
    valid_1 = True
    valid_2 = True
    for field in required_fields:
        validity_check = required_fields[field]
        if field not in datum:
            valid_1 = False
        elif not validity_check(datum[field]):
            valid_2 = False
    
    if valid_1:
        num_valid_1 += 1
        if valid_2:
            num_valid_2 += 1

# Part 1
print("Part 1")
print("Num Valid:", num_valid_1)

print()

# Part 2
print("Part 2")
print("Num Valid:", num_valid_2)