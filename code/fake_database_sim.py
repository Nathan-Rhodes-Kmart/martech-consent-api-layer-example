#TODO: Fake User Consent SetUp
def readConsentFromDB():      #Mock data
    pi_em_consent_source = "email_optout"
    pi_em_consent_state = "Express No"
    pi_ta_consent_source = "whittle"
    pi_ta_consent_state = "Soft No"
    pi_wp_consent_source = "whittle"
    pi_wp_consent_state = "Inferred Yes"

    currentConsent = {
        'pi_em_source': pi_em_consent_source,
        'pi_em_state' : pi_em_consent_state,
        'pi_ta_source': pi_ta_consent_source,
        'pi_ta_state':  pi_ta_consent_state,
        'pi_wp_source': pi_wp_consent_source,
        'pi_wp_state':  pi_wp_consent_state
    }
    return currentConsent
