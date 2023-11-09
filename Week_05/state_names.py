"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


#   Version one without functions
# CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
#                 "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
#
# state_code = input("Enter short state:   ").upper()  # added .upper() to make the input uppercase
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state:").upper()  # added .upper() to make the input uppercase

# CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
#                 "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


# Version two with functions
# def main():
#     state_code_to_name = get_state_code_to_name()
#     state_code = input("Enter short state:   ").upper()  # added .upper() to make the input uppercase
#     while state_code != "":
#         if state_code in state_code_to_name:
#             print(state_code, "is", state_code_to_name[state_code])
#         else:
#             print("Invalid short state")
#         state_code = input("Enter short state:").upper()
#
#
# def get_state_code_to_name():
#     """Get state code to name"""
#     CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
#                     "WA": "Western Australia",
#                     "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
#     return CODE_TO_NAME
#
#
# main()


# Version three with exceptions

# def main():
#     state_code_to_name = get_state_code_to_name()
#     state_code = input("Enter short state:   ").upper()  # added .upper() to make the input uppercase
#     while state_code != "":
#         try:
#             print(state_code, "is", state_code_to_name[state_code])
#         except KeyError:
#             print("Invalid short state")
#         state_code = input("Enter short state:").upper()
# def get_state_code_to_name():
#     """Get state code to name"""
#     CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
#                     "WA": "Western Australia",
#                     "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
#     return CODE_TO_NAME
#
#
# main()
