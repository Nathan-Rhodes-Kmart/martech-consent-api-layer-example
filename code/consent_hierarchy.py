def determine_Hierarchy(Hierarchy_list):
    Hierarchy = {}
    item_number = 0
    for x in Hierarchy_list:
        Hierarchy[item_number] = x
        item_number += 1
    return Hierarchy

def PI_EM_Hierarchy(consents):
    PI_EM_Hierarchy = [
        #Express Values (Yes/No)
        [consents['consent_modal_registered'], consents['email_optout'], consents['marcomms_signup']],
        #Inferred Yes
        [],
        #Whittle - Inferred Yes
        [consents['whittle']],

        #Soft No
        [consents['guest_purchase']],

        #Whittle - Soft No
        [consents['whittle']]
    ]
    return determine_Hierarchy(PI_EM_Hierarchy)


def PI_TA_Hierarchy(consents):
    PI_TA_Hierarchy = [
        #Express Values (Yes/No)
        [consents['consent_modal_registered'], consents['email_optout'], consents['marcomms_signup']],
        #Inferred Yes

        #Whittle - Inferred Yes
        [consents['whittle']],

        #Soft No
        [consents['guest_purchase']],

        #Whittle - Soft No
        [consents['whittle']]
    ]
    return determine_Hierarchy(PI_TA_Hierarchy)