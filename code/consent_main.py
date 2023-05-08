#Created By Nathan Rhodes
#Using Python 3.8.3

import rule_exceptions as RuleExceptions
import consent_hierarchy as ConsentHierarchy
import fake_database_sim as DatabaseSimulator
import create_consent_objects as CreateConsentObjects

def getCurrentConsentObject(currentDBConsent, consents):

    currentConsents = {}
    
    for key, value in consents.items():
        if currentDBConsent['pi_em_source'] == value.name:
            currentConsents['PI_EM_Consent'] = value
        if currentDBConsent['pi_ta_source'] == value.name:
            currentConsents['PI_TA_Consent'] = value
        if currentDBConsent['pi_wp_source'] == value.name:
            currentConsents['PI_WP_Consent'] = value    
    return currentConsents

def returnIncomingHierarchy(hierarchy, incomingConsent):
    for key, value in hierarchy.items():
        for x in value:
            #X = each value in hierarchy
            if incomingConsent == x:
                return key
    return -1

def returnCurrentHierarchy(hierarchy, currentConsent):
    for key, value in hierarchy.items():
        for x in value:
            #X = each value in hierarchy
            if currentConsent == x:
                return key
    return -1

def returnConsentValue(hierarchy, incomingConsent, currentConsent, newState):
    incomingHierarchyValue = returnIncomingHierarchy(hierarchy, incomingConsent)
    currentHierarchyValue = returnCurrentHierarchy(hierarchy, currentConsent)     
        
    #Consent hierarchy Indicates incomming consent to override current consent
    if incomingHierarchyValue <= currentHierarchyValue:
        newConsent = {
            'source': incomingConsent.name,
            'state':  newState
        }
    else:
        return  
    return newConsent
        
def determineNewConsent(consentType, hierarchy, incomingConsent, currentConsentObjects, currentConsentState, incomingKey):

    if consentType == "PI_EM":
        consentOptions = incomingConsent.pi_em_options
        exceptionChecker = RuleExceptions.PI_EM_RuleExceptions
        currentConsentObject = currentConsentObjects['PI_EM_Consent']
    elif consentType == "PI_TA":
        consentOptions = incomingConsent.pi_ta_options
        exceptionChecker = RuleExceptions.PI_TA_RuleExceptions
        currentConsentObject = currentConsentObjects['PI_TA_Consent']

    #We care about the incoming key value; which should either be true (1) or false(0)
    if len(consentOptions) > 1:
        if incomingKey == 0 or incomingKey == 1:
            incomingKey = int(incomingKey)
        elif incomingKey.lower() == 'true':
            incomingKey = 1
        elif incomingKey.lower() == 'false':
            incomingKey = 0     
        newState = consentOptions.get(incomingKey)

    else:
        newState = list(consentOptions.values())[0]

    ruleExceptionsProcessedValue = exceptionChecker(hierarchy, incomingConsent, currentConsentObject, currentConsentState, newState)
    #Standard Flow
    if ruleExceptionsProcessedValue[0] == 0:
        hierarchy = ruleExceptionsProcessedValue[1]
        newConsent = returnConsentValue(hierarchy, incomingConsent, currentConsentObject, newState)
    #Removal of certain items from hierarchy (e.g. with whittle)
    elif ruleExceptionsProcessedValue[0] == 1:
        newConsent = ruleExceptionsProcessedValue[1]
   
    return newConsent

def determineConsent(allConsentObjects, incomingConsentName, incomingConsentValue=0):
    #Create Hierarchys
    PI_EM_Hierarchy = ConsentHierarchy.PI_EM_Hierarchy(allConsentObjects)
    PI_TA_Hierarchy = ConsentHierarchy.PI_TA_Hierarchy(allConsentObjects)

    #Get Current Consent
    currentDBConsent = DatabaseSimulator.readConsentFromDB()
    currentConsentObject = getCurrentConsentObject(currentDBConsent, allConsentObjects)

    #Get Incoming Consent
    incomingConsentObject = allConsentObjects.get(incomingConsentName)

    #Determine Any Consent Changes
    #Email Marketing
    EMConsentChange = determineNewConsent('PI_EM', PI_EM_Hierarchy, incomingConsentObject, currentConsentObject, currentDBConsent['pi_em_state'], incomingConsentValue)
    if currentDBConsent['pi_em_source'] == incomingConsentObject.name and currentDBConsent['pi_em_state'] == EMConsentChange['state']:
            EMConsentChange = None
    
    #Targeted Advertising
    TAConsentChange = determineNewConsent('PI_TA', PI_TA_Hierarchy, incomingConsentObject, currentConsentObject, currentDBConsent['pi_ta_state'], incomingConsentValue)
    if currentDBConsent['pi_ta_source'] == incomingConsentObject.name and currentDBConsent['pi_ta_state'] == TAConsentChange['state']:
            TAConsentChange = None


    #TODO: SEND RESULTS TO DATABASE
    print('--------------------------------------------------------------')
    print(EMConsentChange)
    print(TAConsentChange)
    print('--------------------------------------------------------------')

def main():
    simulated_consent_source = 'whittle'

    #Note: simulated_consent_boolean is only used when a consent source has values of true or false attached to the same consent source.
    #Valid values are: True, False, 1, 0 & (Ignoring case) "True", "False"
    simulated_consent_boolean = False

    consents = CreateConsentObjects.createConsents()
    determineConsent(consents, simulated_consent_source, simulated_consent_boolean)

if __name__ == "__main__":
    main()
