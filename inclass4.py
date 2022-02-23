import requests

url = "http://vcm-7631.vm.duke.edu:5002"
netid = "hb170"
get_patients = "/get_patients/"
get_btype = "/get_blood_type/
match_check = "/match_check"


def get_rec_don(name):
    r = requests.get(url=url+get_patients+name)
    data = r.json()
    recipient = data["Recipient"]
    donor = data["Donor"]
    return recipient, donor


def get_blood_type(pid):
    r = requests.get(url=url+get_btype+pid)
    blood_type = r.text()
    return blood_type


def check_match(recipient, donor):
    match = "No"
    if type1 == "O+":
        if type2 in ["O+", "O-"]:
            match = "Yes"
    elif type2 == "O-":
        if type2 in ["O-"]:
            match = "Yes"
    elif type2 == "A+":
        if type2 in ["O+", "O-", "A+", "A-"]:
            match = "Yes"
    elif type2 == "A-":
        if type2 in ["O-", "A-"]:
            match = "Yes"
    elif type2 == "B+":
        if type2 in ["O+", "O-", "B+", "B-"]:
            match = "Yes"
    elif type2 == "B-":
        if type2 in ["O-", "B-"]:
            match = "Yes"
    elif type2 == "AB+":
            match = "Yes"
    elif type2 == "AB-":
        if "-" in type2:
            match = "Yes"
    return match


def check_answer(name, answer):
    data = {"Name": name, "Match": answer}
    r = requests.post(url=url+match_check, data=data)
    check = r.text()
    print("The answer is", check)
    return check


def main(name=None):
    if name is None:
        name = netid
    recipient, donor = get_rec_don(name)
    recipient_type, donor_type = get_blood_type(pid)
    answer = check_match(recipient, donor)
    check_answer(name, answer)


if __name__ == "__main__":
    main()
