#Ensures No Misspelling
Express_Yes = "Express Yes"
Express_No = "Express No"
Inferred_Yes = "Inferred Yes"
Soft_No = "Soft No"

class Consent:
  def __init__(self, name, c_ta_options, c_wp_options, pi_em_options, pi_ta_options, pi_wp_options):
    self.name = name
    self.c_ta_options = c_ta_options
    self.c_wp_options = c_wp_options
    self.pi_em_options = pi_em_options
    self.pi_ta_options = pi_ta_options
    self.pi_wp_options = pi_wp_options


#-----------------------------------------------------------------------------
#WARNING - EDIT BELOW THIS LINE ONLY


#When creating consents, values of 1 indicate that the value is a 'Yes' value, where as values of 0 indicate a 'No Value'. The key value pair is then combined to determine thee exact type, while easily being able to refference the necessary values

def createConsents():
    consents = {}


    #Consent Modal
    consent_modal_registered = Consent('consent_modal_registered', {0:Express_No, 1:Express_Yes}, {0:Express_No, 1:Express_Yes}, {0:Express_No, 1:Express_Yes}, {0:Express_No, 1:Express_Yes}, {0:Express_No, 1:Express_Yes})
    consents['consent_modal_registered'] = consent_modal_registered

    #MarComms Sign-Up
    marcomms_signup = Consent('marcomms_signup', {1: Inferred_Yes}, {0:Soft_No}, {1:Express_Yes}, {1:Express_Yes}, {0:Soft_No})
    consents['marcomms_signup'] = marcomms_signup

    #Email Opt-Out
    email_optout = Consent('email_optout', {0:Express_No}, {0:Soft_No}, {0:Express_No}, {0:Express_No}, {0:Soft_No})
    consents['email_optout'] = email_optout

    #Guest Purchase
    guest_purchase = Consent('guest_purchase', {0:Soft_No}, {1:Inferred_Yes}, {0:Soft_No}, {0:Soft_No}, {1:Inferred_Yes})
    consents['guest_purchase'] = guest_purchase
    
    #Whittle
    whittle = Consent('whittle', {0:Soft_No, 1:Inferred_Yes}, {0:Soft_No}, {0:Soft_No, 1:Inferred_Yes}, {0:Soft_No, 1:Inferred_Yes}, {0:Soft_No})
    consents['whittle'] = whittle

    #OnePass Instore Example
    onepass_instore_consent = Consent('onepass_instore_consent', {0:Soft_No}, {0:Soft_No}, {1:Inferred_Yes}, {1:Inferred_Yes}, {0:Soft_No})
    consents['onepass_instore_consent'] = onepass_instore_consent

    #OnePass Account Link Example
    onepass_account_link = Consent('onepass_account_link', {1:Inferred_Yes}, {0:Soft_No}, {1:Inferred_Yes}, {1:Inferred_Yes}, {1:Inferred_Yes})
    consents['onepass_account_link'] = onepass_account_link

    
    return consents
